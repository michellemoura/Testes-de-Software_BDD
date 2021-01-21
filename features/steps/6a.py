import os
import sys
import time
from behave import *
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.steps.utils.main_functions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given('that the user is logged in to the system4')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    login(context)


@when('the user click on user information')
def step_impl(context):
    infouser_button = context.driver.find_element_by_id('avatar')
    infouser_button.click()
    time.sleep(2)


@step('the user click the exit button and confirm that he wishes to quit')
def step_impl(context):
    exit_button = context.driver.find_element_by_id('logout')
    exit_button.click()
    time.sleep(2)

    confirm_button = context.driver.find_element_by_class_name('btn-blue')
    confirm_button.click()
    time.sleep(2)


@then('the system returns the login page')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'login-body')))
    vision = context.driver.find_element_by_id('login-body')
    time.sleep(2)
    context.driver.quit()


