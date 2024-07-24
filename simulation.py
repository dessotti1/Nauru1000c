
import asyncio
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
	
	async for position in drone.telemetry.position():
		print(f"Posicao inicial:  Latitude {position.latitude_deg}, Longitude {position.longitude_deg}, Altitude {position.absolute_altitude_m}")
		break
	
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

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(run())