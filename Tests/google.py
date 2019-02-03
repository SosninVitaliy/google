import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_and_get_element(xpath, driver) -> WebElement:
    locator = (By.XPATH, xpath)
    WebDriverWait(driver=driver, timeout=20) \
    .until(expected_conditions.
    presence_of_element_located(locator=locator))
    element = driver.find_element_by_xpath(xpath=xpath)
    return element


def test_search():
    drw = webdriver.WebDriver('/Users/sosninvitaliy/Desktop/google/webdriver/chromedriver')
    drw.get('http://www.google.ru')
    drw.maximize_window()
    element = WebDriverWait(drw, 20)\
    .until(expected_conditions.
    presence_of_element_located((By.XPATH, '//div[@aria-label="Голосовой поиск"]/../..//input')))

    element.send_keys('selenide', Keys.ENTER)

    element = wait_and_get_element('(//h3)[1]/..', driver=drw)
    str = element.get_attribute('href')

    if str == 'https://ru.selenide.org/':
        print(f'Ссылка "{str}" совпадает с ожидаемым результатом "https://ru.selenide.org/" ')
    else:
        pytest.fail(f'Ссылка "{str}" не совпадает с ожидаемым результатом "https://ru.selenide.org/"')

    element = drw.find_element_by_xpath('//a[text() = "Ещё"]/ancestor::g-header-menu')
    element.click()

    element = drw.find_element_by_xpath('//a[text() = "Картинки"]')
    element.click()

    element = wait_and_get_element('//*[@id="rg_s"]/div[1]/a[2]/div[2]', driver=drw)
    pic = element.text.strip()

    i = "selenide.org" in pic

    if i:
        print('Изображение связано с сайтом selenide.org так как под ним содержится ссылка на сайт selenide.org')
    else:
        print('Изображение не связано с сайтом selenide.org')

    element = drw.find_element_by_xpath('//a[text() = "Все"]')
    element.click()

    element = wait_and_get_element('(//h3)[1]/..', driver=drw)
    con = element.get_attribute('href')

    if con==str:
        print("Ссылки на сайт одинаковы, так как ссылка при первом шаге равна ссылке при третьем шаге")
    else:
        print("Ссылки не одинаковы")


def tearDown(self):
    self.drw.close()