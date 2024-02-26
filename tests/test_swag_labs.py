import allure
from allure_commons.types import Severity

from pages.shopping_site import ShoppingSite


@allure.tag("web")
@allure.description("Проверка сайта Swag Labs")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saritto")
@allure.link("https://www.saucedemo.com/", name="Swag Labs")
@allure.title("Проверка сайта Swag Labs")
def test_swag_labs():
    shopping_site = ShoppingSite()

    with allure.step("Открытие главной страницы:"):
        shopping_site.open()

    with allure.step("Авторизация пользователя:"):
        shopping_site.auth()

    with allure.step("Сбор корзину:"):
        shopping_site.add_items_to_cart()

    with allure.step("Открытие корзины:"):
        shopping_site.go_to_cart()

    with allure.step("Покупка:"):
        shopping_site.buy()

    with allure.step("Завершение покупки:"):
        shopping_site.finish()
