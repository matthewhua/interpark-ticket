import time

import undetected_chromedriver as uc
from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # 禁用自动化栏
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 屏蔽保存密码提示框
    prefs = {'credentials_enable_service': False, 'profile.password_manager_enable': False}
    options.add_experimental_option('prefs', prefs)
    # 反爬虫特征处理
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = uc.Chrome()

    driver.get("https://www.globalinterpark.com/en/login")

    title = driver.title
    driver.implicitly_wait(10)
    while True:
        time.sleep(1)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text
# driver.quit()
