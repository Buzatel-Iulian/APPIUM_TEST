#   Robotframework Appium Testing

This repository is supposed to serve as a personal note on the setup and use of Appium for mobile application testing. (Only for Android devices, atleast for the moment)

##  Setup
For it to be functional, the test requires the following to be installed:
*   Appium, by installing [node.js](https://nodejs.org/en/) and running the command `npm install appium`
*   [Appium Inspector](https://github.com/appium/appium-inspector/releases) (normal instalation)
*   Java Develompment Kit ([JDK](https://www.oracle.com/java/technologies/java-se-development-kit11-downloads.html))
*   [Android Studio](https://developer.android.com/studio/) (especially if you want to use an emulated android device)
*   [Python](https://www.python.org/downloads/) with the required dependencies from pip_requirements.txt (`pip install -r pip_requirements.txt`)

__Important Note:__ As usual it is recommended that you install the dependencies and run the script in a virtual environment, about which you can find more details [here](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html).

For a more detailed guide on the setup I recommend checking out [Part 1](https://vincereyes.medium.com/mobile-automation-using-appium-robot-framework-part-1-10c4f40d4935) of the tutorial I originally followed, Altough i do not recommend using the code presented in the second part due to some omited test cases.

Depending on the device / emulator configuration you will need to modify the `robot` commands in tasks.py, one of them is already modified so you can get a feeling of how the configuration is done.

##  Running the tests
Once everything is set up, your device is conected (trough USB) / emulator is up and running and your run commands are configured you are ready to run the tests. You can get a list of the avvailable test by running the `invoke --list` command, which should result in the following being printed out:

*   `device-test` (for this you need to enable [developer mode](https://www.youtube.com/watch?v=RT7Nr_Cx-dY&t=63s) on your phone)
*   `emulator-test`
*   `cleanup` (this one is just for convenience)

You can run any of them by typing `invoke [testname]`.

###  Lastly
For the sake of convenience when you want to modify something or there are some unknowns during setup I've left some useful notes in the __Helpful__ folder of the repo, furthermore, here are some links I found useful during the development process:

*   https://vincereyes.medium.com/mobile-automation-using-appium-robot-framework-part-2-5560be591163
*   https://github.com/cloud-vr/mobile-automation-demo
*   https://developer.android.com/studio/run/emulator-commandline
*   https://developer.android.com/studio/command-line/adb#move
*   http://robotframework.org/robotframework/latest/libraries/BuiltIn.html#Wait%20Until%20Keyword%20Succeeds
*   https://pypi.org/project/robotframework-appiumlibrary/
*   https://discuss.appium.io/t/launching-and-stopping-appium-server-programmtically/700/2