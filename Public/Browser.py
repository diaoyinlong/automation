import platform
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Module import Config, Uri


class Browser:
    def __init__(self):
        # instance a Browser for test case
        if Config.browser == 'Chrome':
            chrome_options = webdriver.ChromeOptions()
            if Config.emulateMobile == 'True':
                mobile_emulation = {'deviceName': 'Apple iPhone 6 Plus'}
                chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
            if 'Ubuntu' in platform.version():
                self.browser = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
            else:
                self.browser = webdriver.Chrome(Config.rootPath + '/Driver/ChromeDriver.exe',
                                                desired_capabilities=chrome_options.to_capabilities())
        elif Config.browser == 'IE':
            self.browser = webdriver.Ie(Config.rootPath + '/Driver/IEDriverServer.exe')

        # implicitly wait for global driver
        self.browser.implicitly_wait(10)

        # explicit wait for special control
        self.wait = WebDriverWait(self.browser, 10)

        # make the browser window max
        self.browser.maximize_window()

    def quit(self):
        self.browser.quit()

    def go_to(self, url, token=''):
        if token == '':
            self.browser.get(url)
        else:
            self.browser.get(Uri.LoginPage + '/Interface/Sign/dispatch?url=' + url + '&accessToken=' + token)

    # we have to switch to a window for find control when there are many windows appear
    def switch_window(self, index):
        time.sleep(1)
        self.browser.switch_to.window(self.browser.window_handles[index])

    # switch to the latest opened window
    def switch_to_new_window(self):
        time.sleep(1)
        self.browser.switch_to.window(self.browser.window_handles[len(self.browser.window_handles) - 1])

    def wait_until_clickable(self, css):
        self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css)))

    def wait_until_not_clickable(self, css):
        self.wait.until_not(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css)))

    def move_mouse_to(self, element):
        webdriver.ActionChains(self.browser).move_to_element(element).perform()
