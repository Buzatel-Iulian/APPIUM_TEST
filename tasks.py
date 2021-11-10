import invoke
import resources.launcher as launcher

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
    launch = launcher.launcher(device="ZH800695RV")
    
    launch.startAppium()
    launch.Execute("robot -d ./output -v PLATFORM_VERSION:5.1.1 -v DEVICE_NAME:ZH800695RV tests/app_test.robot", is_background = False)
    launch.stopAppium()
    
@invoke.task()
def launch_test(c):
    appium = launcher.launcher2(command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g appium_log1.txt")
    appium.launch()
    robot = launcher.Execute("robot -d ./output -v PLATFORM_VERSION:5.1.1 -v DEVICE_NAME:ZH800695RV tests/app_test.robot", is_background = False)
    appium.stop()
