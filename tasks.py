import invoke
import resources.launcher as launcher
from time import sleep
import os

@invoke.task()
def emulator_test(c):
    launch = launcher.launcher()
    launch.startEmulator()
    launch.startAppium()
    launch.Execute("robot -d ./output tests/app_test.robot", is_background = False)
    launch.stopAppium()
    launch.stopEmulator()

@invoke.task()
def device_test(c):
    appium_server = launcher.launcher(device="ZH800695RV")
    
    appium_server.start_s()
    launcher.Execute("robot -d ./output -v PLATFORM_VERSION:5.1.1 -v DEVICE_NAME:ZH800695RV tests/app_test.robot", is_background = False)
    sleep(3)
    appium_server.stop_s()
    
@invoke.task()
def launch_test(c):
    appium = launcher.launcher2(command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g appium_log1.txt")
    appium.launch()
    robot = launcher.Execute("robot -d ./output -v PLATFORM_VERSION:5.1.1 -v DEVICE_NAME:ZH800695RV tests/app_test.robot", is_background = False)
    appium.stop()

@invoke.task()
def run_comm(c):
    launcher.Execute("dir", is_background=False)   # worth a shot ..... didn't work