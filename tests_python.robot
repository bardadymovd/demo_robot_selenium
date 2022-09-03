*** Settings ***
Documentation   Test suite for demonstration UI tests for amazon
Resource        steps_python.robot
Variables       variables.py
Suite Setup     BasePage.Custom Open Browser
Test Setup      Go To   ${base_url}
Suite Teardown  Close Browser


*** Test Cases ***
Login to Amazon
    Click on sign in button
    Input Login And Proceed    ${username}
    Input Password And Proceed      ${password}
    User should be logged in      ${first_name}

Search and filter items
    Type in search field    laptop
    Title of first item should contain     laptop
    Filter results by price     Under $500
    Price Of Fist Item Should Be Between    0   500
    Filter results by brand     Acer
    Title of first item should contain     Acer
