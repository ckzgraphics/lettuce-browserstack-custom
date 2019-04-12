from lettuce import before, world,after
from selenium import webdriver

import os

@before.all
def setup_browser():

  BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
  BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']

  desired_capabilities = {}
  desired_capabilities['os'] = 'Windows'
  desired_capabilities['os_version'] = '10'
  desired_capabilities['browser'] = 'Chrome'
  desired_capabilities['browser_version'] = '70'
  desired_capabilities['project'] = 'Test Run'
  desired_capabilities['build'] = 'Support Automate'
  desired_capabilities['name'] = 'Testing Selenium with Lettuce'

  world.browser = webdriver.Remote(desired_capabilities=desired_capabilities,
  command_executor="https://%s:%s@hub-cloud.browserstack.com/wd/hub"  % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY))

@after.all
def tear_down(total):
      print "Total %d of %d scenarios passed!" % ( total.scenarios_ran, total.scenarios_passed)
      world.browser.quit()
