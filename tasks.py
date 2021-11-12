import invoke
import resources.launcher as lutil

    
@invoke.task()
def launch_test(c):
    appium = lutil.launcher(command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g appiumlog1.txt", task_name = "node")
    appium.launch()
    lutil.Execute("robot -d ./output -v PLATFORM_VERSION:5.1.1 -v DEVICE_NAME:ZH800695RV tests/app_test.robot", is_background = False)
    appium.stop()
