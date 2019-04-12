from lettuce import step, world
from selenium.webdriver.common.keys import Keys
import time

@step("I'm on Google")
def step_impl(step):
    world.browser.get("https://www.google.com/ncr")
    world.browser.maximize_window()

@step("I search for BrowserStack")
def step_impl(step):
    element = world.browser.find_element_by_name("q")
    element.send_keys("BrowserStack")
    element.send_keys(Keys.RETURN)

@step("the browser title should have BrowserStack - Google Search")
def step_impl(step):

    time.sleep(2)
    assert "BrowserStack - Google Search" == world.browser.title
    print world.browser.title
