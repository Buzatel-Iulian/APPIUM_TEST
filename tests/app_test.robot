*** Settings ***

Documentation    An appium / robotframework exercise

Library    AppiumLibrary
Resource    ../resources/element_ids.resource
Resource    ../resources/components.resource

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
    Open Application    ${APPIUM_SERVER}
    ...    platformName=${PLATFORM_NAME}
    ...    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}
    ...    app=${APP}
    ...    appPackage=${APP_PACKAGE}
    ...    appActivity=${APP_ACTIVITY}
    Sleep    2s

Register New User
    Log Visibility    ${Form.Login.CreateOne.Link}    \nCreate Account Link
    Scroll Down to    ${Form.Login.CreateOne.Link}
    Log Visibility    ${Form.Login.CreateOne.Link}    Create Account Link
    Click Element    ${Form.Login.CreateOne.Link}
    Sleep    2s

    Log Visibility    ${Form.Register.Register.Btn}    Register Button
    Scroll Down to    ${Form.Register.Register.Btn}
    Log Visibility    ${Form.Register.Register.Btn}    Register Button
    Wait Until Element Is Visible    ${Form.Register.Name.Txt}
    Input Text    ${Form.Register.Name.Txt}    Arnold
    Input Text    ${Form.Register.EmailAddress.Txt}    false@gmail.com
    Input Text    ${Form.Register.Password.Txt}    g00dPassword
    Input Text    ${Form.Register.PasswordConfirmation.Txt}    g00dPassword
    Click Element    ${Form.Register.Register.Btn}
    Sleep    2s

    Log Visibility    ${Form.Register.Login.Btn}    Login Link
    Scroll Down to    ${Form.Register.Login.Btn}
    Log Visibility    ${Form.Register.Login.Btn}    Login Link
    Click Element    ${Form.Register.Login.Btn}
    Sleep    2s

Login User
    Input Text    ${Form.Login.EmailAddress.Txt}    false@gmail.com
    Input Text    ${Form.Login.Password.Txt}    g00dPassword
    Click Element    ${Form.Login.Login.Btn}
    Sleep    2s

Verify Account Info
    Element Should Contain Text    ${Form.Account.Name.Txt}    Arnold
    Element Should Contain Text    ${Form.Account.EmailAddress.Txt}    false@gmail.com
    Element Should Contain Text    ${Form.Account.Password.Txt}    g00dPassword

Close App
    Close All Applications

