import os
import sys
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.steps.utils.main_functions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given('that the user is logged in to the system5')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    login(context)
    time.sleep(1)


@when('user click on Enable video pounds option in accessibility bar')
def step_impl(context):
    videosinPounds_button = context.driver.find_element_by_id('btHabilitaLibras')
    videosinPounds_button.click()
    time.sleep(5)


@then('the system returns the enabled option')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.ID, 'btHabilitaLibras')))
    returnPounds = context.driver.find_element_by_id('btHabilitaLibras').get_attribute("aria-label")
    assert returnPounds == "Desabilitar vídeo libras"
    time.sleep(2)
    context.driver.quit()