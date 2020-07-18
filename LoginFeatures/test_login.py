from selenium import webdriver
import time
import pytest
import Utility.Json_Util


driver = webdriver.Chrome("D:/workspace_python/MyStoreApp/Drivers/chromedriver.exe")
path = "D:/workspace_python/MyStoreApp/TestData/login.json"
json_data = Utility.Json_Util.ReadFromJson()


class TestLoginPageClass:
    def launch_browser(self):
        url = "http://automationpractice.com/index.php"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div//a[contains(text(),'Sign in')]").click()
        time.sleep(5)

    def log_out(self):
        driver.find_element_by_xpath("(//div//a[contains(text(),'Sign out')])[1]").click()

    def terminate_browser(self):
        driver.quit()

    def user_name(self, key):
        username = json_data.fetch_json_value(key, path)
        driver.find_element_by_id("email").send_keys(username)

    def pwd(self):
        pwd = json_data.fetch_json_value('password', path)
        driver.find_element_by_id("passwd").send_keys(pwd)

    def pwd_param(self, key):
        pwd = json_data.fetch_json_value(key, path)
        driver.find_element_by_id("passwd").send_keys(pwd)

    def clicklogin(self):
        driver.find_element_by_id("SubmitLogin").click()

    def validate_homescreen(self):
        expUser = json_data.fetch_json_value('expUser', path)
        actual = driver.find_element_by_xpath("(//nav//div//a//span)[1]").text
        assert actual == expUser

    def validate_wrong_emailscreen(self):
        expected = json_data.fetch_json_value('BlankEmailErrMsg', path)
        actual_data = driver.find_element_by_xpath("//li[contains(text(),'An email address required.')]").text
        assert actual_data == expected

    def invalid_Email(self):
        expected = json_data.fetch_json_value('invalidErrMsg', path)
        actual_data = driver.find_element_by_xpath("//li[contains(text(),'Authentication failed.')]").text
        assert actual_data == expected

    def blank_pwd(self):
        expected = json_data.fetch_json_value('blankErrMsg', path)
        actual_data = driver.find_element_by_xpath("//li[contains(text(),'Password is required.')]").text
        assert actual_data == expected

    def err_pwd(self):
        expected = json_data.fetch_json_value('pwdErrMsg', path)
        actual_data = driver.find_element_by_xpath("//li[contains(text(),'Authentication failed.')]").text
        assert actual_data == expected

    #@pytest.mark.xfail(run=False)
    def test_case01(self):
        ref.launch_browser()
        ref.user_name('username')
        ref.pwd()
        ref.clicklogin()
        ref.validate_homescreen()
        ref.log_out()
        #ref.terminate_browser()

    #pytest.mark.xfail(run=False)
    def test_case02(self):
        #ref.launch_browser()
        ref.user_name('invalidUsername')
        ref.pwd()
        ref.clicklogin()
        ref.take_screenshot()
        ref.validate_wrong_emailscreen()
        #ref.terminate_browser()

    #@pytest.mark.xfail(run=False)
    def test_case03(self):
        #ref.launch_browser()
        ref.user_name('non_exist_username')
        ref.pwd()
        ref.clicklogin()
        ref.invalid_Email()
        ref.take_screenshot()
        #ref.terminate_browser()

    #@pytest.mark.xfail(run=False)
    def test_case04(self):
        ref.launch_browser()
        ref.user_name('username')
        ref.pwd_param('blank_password')
        ref.clicklogin()
        ref.blank_pwd()
        ref.take_screenshot()
        #ref.terminate_browser()

    #@pytest.mark.xfail(run=False)
    def test_case05(self):
        ref.launch_browser()
        ref.user_name('username')
        ref.pwd_param('non_exist_pwd')
        ref.clicklogin()
        ref.err_pwd()
        ref.take_screenshot()
        #ref.terminate_browser()



    def take_screenshot(self):
        fileName = str(round(time.time()*1000)) + '.png'
        screenshotDirectory = "D:/workspace_python/MyStoreApp/Screenshots"
        destinationFile = screenshotDirectory + fileName
        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory" + destinationFile)
        except NotADirectoryError:
            print("Not a Directory Issue")


ref = TestLoginPageClass()




