from selenium import webdriver
import time

driver = webdriver.Chrome("D://workspace_python//MyPublicRepo//Drivers//chromedriver.exe")

class TestLogin:
    def launchBrowser(self):
        url = "https://qa.harness.io/#/login"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(5)

    def validLogin(self):
        driver.find_element_by_xpath("//input[@id='root_login']").send_keys("prathush.indecomm@mailinator.com")
        driver.find_element_by_xpath("//button[text() = 'NEXT']").click()
        driver.find_element_by_xpath("//label[text()='Password']").click()
        #driver.find_element_by_xpath("//input[@id='root_password']").click()
        driver.find_element_by_id("root_password").send_keys("Harness@123")
        driver.find_element_by_xpath("//button[@data-name='SIGN IN']").click()

    def validateElement(self):
        actual = driver.find_element_by_xpath("//span[text()='Main Dashboard']").text
        expected = "Main Dashboard"
        assert actual == expected


obj = TestLogin()
obj.launchBrowser()
obj.validLogin()
obj.validateElement()



