*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallez  kalle123123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle124
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle124
    Output Should Contain  Username contains not allowed characers


Register With Valid Username And Too Short Password
    Input Credentials  kalleb  k4
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallej  kallekallekalle
    Output Should Contain  Password has to contain at least one special character


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
