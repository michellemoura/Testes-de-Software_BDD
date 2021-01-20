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


@given('that the user is logged in to the system')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    login(context)


@when('the user clicks on the glossary module')
def step_impl(context):
    glossary_button = context.driver.find_element_by_id('nav-item-6')
    glossary_button.click()
    time.sleep(3)


@step('the user click the search field and enter the BDD name')
def step_impl(context):
    search = context.driver.find_element_by_id('search')
    search.send_keys('BDD')
    time.sleep(1)


@step('the user click the search button1')
def step_impl(context):
    #pesquisa_button = context.driver.find_element_by_css_selector("#glossary-search button")
    get_button = context.driver.find_element_by_xpath("//div[@id='glossary-search']/button")
    get_button.click()
    time.sleep(1)


@then('the system returns the concept of BDD')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'glossaryItem')))
    result = context.driver.find_element_by_xpath("//div[@class='glossaryItem']/h2").text
    assert result == "BDD"
    time.sleep(2)
    context.driver.quit()