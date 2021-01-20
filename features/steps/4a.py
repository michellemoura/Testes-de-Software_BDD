from behave import given, when, then, step
from selenium.webdriver.chrome.options import Options
import os
import sys
from features.steps.utils.main_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given('that the user is logged in to the system3')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    login(context)
    time.sleep(1)


@when('the user clicks on the help option in the accessibility bar')
def step_impl(context):
    help_button = context.driver.find_element_by_id('bt-help')
    help_button.click()
    time.sleep(3)


@step('the user enters what he wants to search')
def step_impl(context):
    username = context.driver.find_element_by_id('search')
    username.send_keys('Login')
    time.sleep(2)


@when('the user click the search button')
def step_impl(context):
    search_button = context.driver.find_element_by_xpath("//div[@class='d-flex']/button")
    #buscar_button = context.driver.find_element_by_name_class('btn btn-primary px-4 fontAccessibility')
    #search_button = context.driver.find_element_by_class_name("d-flex")
    search_button.click()
    time.sleep(3)


@then('the system returns the search result')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'faqQuestion')))
    result = context.driver.find_element_by_xpath("//div[@class='faqQuestion']/a").text
    assert result == "Como realizar Login na plataforma?"
    time.sleep(2)
    context.driver.quit()

