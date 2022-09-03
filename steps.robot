*** Settings ***
Documentation     Provides keywords for igeneral purpose
Library           SeleniumLibrary
Variables         variables.py


*** Keywords ***
Open Amazon site
    go to  ${base_url}

Perfom login as
    [Arguments]     ${login}    ${password}
    click element    id:nav-link-accountList
    wait until element is visible    id:ap_email
    input text  id:ap_email    ${login}
    click element    id:continue
    sleep    5  # adding wait for bypass amazon captcha
    input text  id:ap_password    ${password}
    click element    id:signInSubmit

User shoud be logged in
    [Arguments]    ${name}
    wait until element contains    css:[data-nav-role=signin]   Hello, ${name}

Type ${item} in search filed
    wait until element is visible   id:twotabsearchtextbox
    input text    id:twotabsearchtextbox    ${item}
    click element    id:nav-search-submit-button
    wait until element is visible    css:.s-result-item .s-card-container

Filter results by price
    [Arguments]    ${text}
    click element   xpath://*[@id='priceRefinements']//*[contains(text(),'${text}')]

Get price of first item
    ${price}    get text    css:.s-result-item .a-price-whole
    [Return]    ${price}

Filter results by brand
    [Arguments]    ${brand}
    click element    css:#brandsRefinements [aria-label="${brand}"] .a-icon-checkbox
    checkbox should be selected    css:#brandsRefinements [aria-label="${brand}"] input

Title of first item should have
    [Arguments]    ${text}
    wait until element contains    css:.s-result-item .s-card-container     ${text}
