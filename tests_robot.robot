*** Settings ***
Documentation   Test suite for demonstration UI tests for amazon
Resource        steps.robot
Variables       variables.py
Suite Setup     Open Browser     browser=Chrome
Test Setup      Open Amazon site
Suite Teardown  Close Browser


*** Test Cases ***
Login to Amazon
    Perfom login as     ${username}     ${password}
    User shoud be logged in     ${first_name}

Search and filter items
    Type laptop in search filed
    Filter results by price     Under $500
    ${price}    Get price of first item
    should be true    ${price} < 500
    Filter results by brand     Acer
    Title of first item should have     Acer
