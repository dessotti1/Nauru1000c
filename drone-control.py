import asyncio
from mavsdk import System
from aioconsole import ainput


async def monitor_keyboard(uav):
   while True:
       command = await ainput("Press 't' to takeoff, 'l' to land: ")
       if command == 't':
           print("Taking Off")
           await uav.action.takeoff()
       elif command == 'l':
           print("Landing")
           await uav.action.land()
       elif command == 'r':
           print("Returning to launch")
           await uav.action.return_to_launch()


       await asyncio.sleep(1)


async def run():
   uav = System()
   await uav.connect(system_address="udp://:14540")  # Connects to the UAV


   print("Establishing Connection...")
   # Check CONNECTION & if there is a positive connection Feedback = CONNECTED
   async for  state in uav.core.connection_state():
       if state.is_connected:
           print("UAV target UUID: {state.uuid}") #Prints the UUID of the UAV to which the system connected
           break


   print("Establishing GPS lock on UAV..")
   # Checks the gps Connection via telemetry health command
   async for health in uav.telemetry.health():
       if health.is_global_position_ok:
           print("Established GPS lock...")  # GPS health approved
           break


   print("Arming UAV")
   await uav.action.arm()


   await monitor_keyboard(uav)


if __name__ == "__main__":
   loop = asyncio.get_event_loop()
   loop.run_until_complete(run())