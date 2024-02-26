import allure
from allure_commons.types import Severity

from pages.shopping_site import shopping_site


@allure.tag("web")
@allure.description("Проверка сайта Swag Labs")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saritto")
@allure.link("https://www.saucedemo.com/", name="Swag Labs")
@allure.title("Корректные данные пользователя")
def test_swag_labs():
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


@allure.title("Некорректные данные пользователя")
def test_swag_labs_invalid_user():
    with allure.step("Открытие главной страницы:"):
        shopping_site.open()
    with allure.step("Авторизация пользователя:"):
        shopping_site.auth_error()
    with allure.step("Получение ошибки:"):
        shopping_site.error_auth()


@allure.title("Заблокированный пользователь")
def test_swag_labs_locked_user():
    with allure.step("Открытие главной страницы:"):
        shopping_site.open()
    with allure.step("Авторизация пользователя:"):
        shopping_site.locked_user()
    with allure.step("Получение ошибки:"):
        shopping_site.error_locked_user()