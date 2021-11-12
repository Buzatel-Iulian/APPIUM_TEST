*** Settings ***

Documentation    General keywords for the main tests

Library    AppiumLibrary

*** Variables ***

*** Keywords ***

####### Keep these toghether ##################################################
Scrolling to
    [Arguments]    ${locator}
    Swipe    0    200    0    100
    Element Should Be Visible    ${locator}

Scroll Down to
    [Arguments]    ${locator}
    Wait Until Keyword Succeeds    10s    0.1s    Scrolling to    ${locator}
###############################################################################

Log Visibility
    [Arguments]    ${locator}    ${name}
    ${vizible}    Run Keyword And Return Status    Element Should Be Visible    ${locator}
    Log To Console    ${name} is vizible: ${vizible}
    Log    ${name} is vizible: ${vizible}