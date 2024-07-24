import asyncio
import matplotlib.pyplot as plt
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")
    
    print("Esperando drone conectar...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone conectado")
            break

    await asyncio.sleep(2)
    await drone.action.arm()
    print("Drone arming...")
    await asyncio.sleep(2)

    await drone.action.takeoff()
    print("Decolando...")
    await asyncio.sleep(20)
    
    velocity_data = []
    time_data = []

    
    async def capture_velocity():
        start_time = asyncio.get_event_loop().time()
        async for velocity_ned in drone.telemetry.velocity_ned():
            velocity_data.append({
                'north': velocity_ned.north_m_s,
                'east': velocity_ned.east_m_s,
                'down': velocity_ned.down_m_s
            })
            current_time = asyncio.get_event_loop().time() - start_time
            time_data.append(current_time)

    # Iniciar a captura da velocidade
    capture_task = asyncio.ensure_future(capture_velocity())

    await drone.action.transition_to_fixedwing()
    print("Mudando para asa fixa...")
    await asyncio.sleep(5)

    await drone.action.goto_location(47.3977505, 8.55, 500, 90.0)
    print("Voando ate a localizacao...")
    await asyncio.sleep(10)

    print("Chegou na poiscao de destino. Retornando para a base...")
    await drone.action.return_to_launch()
    await asyncio.sleep(50)

    await drone.action.transition_to_multicopter()
    print("Mudando para helices...")
    await asyncio.sleep(5)

    await drone.action.land()
    print("Pousando...")
    await asyncio.sleep(30)

    await drone.action.disarm()
    print("Missao concluida")

    await drone.action.shutdown()

    capture_task.cancel()
    try:
        await capture_task
    except asyncio.CancelledError:
        pass

    
    plt.figure(figsize=(10, 6))

    
    north_velocities = [entry['north'] for entry in velocity_data]
    east_velocities = [entry['east'] for entry in velocity_data]
    down_velocities = [entry['down'] for entry in velocity_data]

    
    plt.plot(time_data, north_velocities, marker='o', linestyle='-', color='b', label='Velocidade Norte')
    plt.plot(time_data, east_velocities, marker='o', linestyle='-', color='g', label='Velocidade Leste')
    plt.plot(time_data, down_velocities, marker='o', linestyle='-', color='r', label='Velocidade para Baixo')

    plt.title('Velocidades do drone durante o voo')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
