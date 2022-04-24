from web_selenium import Selenium
from pytest import mark

# отчет находится в файле report.html

@mark.auth
@mark.test_1
def test_var_1():

    message = 'Invalid credentials'
    test = Selenium().authorization('test@xtrade.dev', 'Test12345%')
    assert message == test, f'Wrong message'

@mark.auth
@mark.test_2
def test_var_2():


    message = 'Username cannot be empty'
    test = Selenium().authorization('', 'A9aa&')
    assert message == test, f'Wrong message'

@mark.auth
@mark.test_3
def test_var_3():


    message = 'Invalid credentials'
    test = Selenium().authorization('Select * from trade; или id=3', 'Select * from trade; или id=3')
    assert message == test, f'Wrong message'

@mark.auth
@mark.test_4
def test_var_4():

    message = 'Invalid credentials'
    test = Selenium().authorization('<button onclick="myFunction()">Click Me</button><div id="myDIV">Hello</div>', '<button onclick="myFunction()">Click Me</button><div id="myDIV">Hello</div>')
    assert message == test, f'Wrong message'

@mark.auth
@mark.test_5
def test_var_5():

    message = 'Invalid credentials'
    test = Selenium().authorization('日本人@日人日本人.com', '日本人@日人日本人.com')
    assert message == test, f'Wrong message'

@mark.auth
@mark.test_6
def test_var_6():

    message = 'Invalid credentials'
    test = Selenium().authorization('test@google.com', '300 знаков')
    assert message == test, f'Wrong message'

@mark.auth
@mark.test
def test_var_7():

    message = 'Invalid credentials'
    test = Selenium().authorization('test@google.com', 'ЭтоПароль-123')
    assert message == test, f'Wrong message'


