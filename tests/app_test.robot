*** Settings ***

Documentation    An appium / robotframework exercise

Library    AppiumLibrary
Resource    ../resources/element_ids.resource

*** Variables ***

${APPIUM_SERVER}    http://127.0.0.1:4723/wb/hub
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    8.1
${DEVICE_NAME}    Pixel_3_API_27
${APP}    C:\\Users\\Iulian\\Documents\\RampUp\\Python\\appium_test\\Sample_Android_App_Login_Test_v4.0_apkpure.com.apk
${APP_PACKAGE}    com.loginmodule.learning
${APP_ACTIVITY}    com.loginmodule.learning.activities.LoginActivity

*** Keywords ***

*** Tasks ***

Launch Aplication
    Log To Console    got to 1
    Open Application    ${APPIUM_SERVER}
    ...    platformName=${PLATFORM_NAME}
    ...    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}
    ...    app=${APP}
    ...    appPackage=${APP_PACKAGE}
    ...    appActivity=${APP_ACTIVITY}
    Log To Console    got to 2

    Close All Applications

