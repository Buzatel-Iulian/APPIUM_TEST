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
    