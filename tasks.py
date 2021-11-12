import invoke
import resources.launcher as lutil
from time import sleep

def confirmation(tested):
    print("You made sure that the {} is conected/turned on ? ( y/n ) ".format(tested))
    confirm = input()
    if confirm == 'y':
        return True
    return False

@invoke.task()
def device_test(c):
    if confirmation("Android Device") :
        appium = lutil.launcher(command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g output/appiumlog1.txt", task_name = "node")
        appium.launch()
        # Here you write any device specific information that the robot needs in a similar format to that below
        robot_var="-v PLATFORM_VERSION:5.1.1 -v DEVICE_NAME:ZH800695RV -v Form.Account.Name.Txt:xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]"
        lutil.Execute("robot -d ./output {} tests/app_test.robot".format(robot_var), is_background = False)
        appium.stop()

@invoke.task()
def emulator_test(c):
    if confirmation("Emulator") :
        appium = lutil.launcher(command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g output/appiumlog1.txt", task_name = "node")
        appium.launch()
        lutil.Execute("robot -d ./output tests/app_test.robot", is_background = False)
        appium.stop()

@invoke.task()
def cleanup(c):                    #  log     report  output      =    NONE
    lutil.Execute("robot -d ./output -l NONE -r NONE -o NONE tests/cleanup.robot")