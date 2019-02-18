import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


dic = {
    "field_search": '#text',
    "first_result": 'div > a > b',
    "pictures": '.navigation__item_name_images',
    "first_picture_site": '#\34 e3ff0acda173b26288e14f23410060d > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)',
    "locator_second": '.polaroid2',
    "back": '.tabs-navigation__content>a',
    "first_result_after_back": 'div.r>a',
    "someid": '#\34 e3ff0acda173b26288e14f23410060d > div > a'
    }

def test_search():
    driver = webdriver.Firefox()
    driver.implicitly_wait(60)
    driver.get("http://yandex.ru/")
    element = wait_and_get_element(driver, dic["field_search"])
    element.click()
    element.send_keys('selenide', Keys.ENTER)
    element = wait_and_get_element(driver, dic["first_result"])
    str = element.text.strip()
    if str == 'ru.selenide.org':
        print(f'Ссылка "{str}" совпадает с ожидаемым результатом "ru.selenide.org"')
    else:
        pytest.fail(f'Ссылка "{str}" не совпадает с ожидаемым результатом "ru.selenide.org"')
    element = wait_and_get_element(driver, dic["pictures"])
    element.click()
    driver.get("https://yandex.ru/images/search?text=selenide")
    element = move_and_click(driver, dic["first_picture_site"], dic["locator_second"], 5)
    str = element.text.strip()
    # element = element.get_attribute('href')
    # if 1:
    #     print('Изображение связано с сайтом selenide.org так как под ним содержится ссылка на сайт selenide.org')
    # else:
    #     print('Изображение не связано с сайтом selenide.org')
    element = wait_and_get_element(driver, dic["back"])
    element.click()
    element = wait_and_get_element(driver, dic["first_result_after_back"])
    con = element.get_attribute('href')
    if con==str:
        print("Ссылки на сайт одинаковы, так как ссылка при первом шаге равна ссылке при третьем шаге")
    else:
        print("Ссылки не одинаковы")


def tearDown(self):
    self.drw.close()

def move_and_click(driver, locator_first, locator_second, time):
    element1 = wait_and_get_element(driver, locator_first)
    element2 = wait_and_get_element(driver, locator_second)
    ActionChains(driver).move_to_element(element1).pause(seconds=time).click(element2).perfom()
    return element2

def wait_and_get_element(driver, locator):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    return element


test_search()

