from mavsdk import System
import asyncio


async def print_gps_info(drone):
   async for gps_info in drone.telemetry.gps_info():
       print(f"GPS info: {gps_info}")


async def print_imu_data(drone):
   async for imu in drone.telemetry.imu():
       print(f"IMU: {imu}")


async def run(choice):
   drone = System()
   await drone.connect(system_address="udp://:14540")


   if choice == 1:
       print("Exibindo informações do GPS...")
       await print_gps_info(drone)
   elif choice == 2:
       print("Exibindo dados do IMU...")
       await print_imu_data(drone)
   else:
       print("Escolha inválida! Digite 1 para GPS ou 2 para IMU.")


if __name__ == "__main__":
   # Solicita a entrada do usuário
   try:
       user_choice = int(input("Digite 1 para exibir GPS ou 2 para exibir IMU: "))
       loop = asyncio.get_event_loop()
       loop.run_until_complete(run(user_choice))
   except ValueError:
       print("Entrada inválida! Por favor, digite um número inteiro.")