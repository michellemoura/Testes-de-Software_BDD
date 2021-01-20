import time

def login(context):
    username = context.driver.find_element_by_id('login')
    username.send_keys('alunoauditivo26')
    time.sleep(1)

    password = context.driver.find_element_by_id('password')
    password.send_keys('abcd1234')
    time.sleep(1)

    login_button = context.driver.find_element_by_id('login-btn')
    login_button.click()
    time.sleep(1)
