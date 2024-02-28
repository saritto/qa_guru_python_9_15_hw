import allure
from allure_commons.types import Severity

from pages.shopping_page import shopping_page


@allure.tag("web")
@allure.description("Проверка сайта Swag Labs")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saritto")
@allure.link("https://www.saucedemo.com/", name="Swag Labs")
@allure.title("Корректные данные пользователя")
def test_swag_labs_valid_user():
    with allure.step("Открытие главной страницы:"):
        shopping_page.open()
    with allure.step("Авторизация пользователя:"):
        shopping_page.auth()
    with allure.step("Открытие экрана магазина в авторизованной зоне:"):
        shopping_page.check_login()


@allure.title("Некорректные данные пользователя")
def test_swag_labs_invalid_user():
    with allure.step("Открытие главной страницы:"):
        shopping_page.open()
    with allure.step("Авторизация пользователя:"):
        shopping_page.auth_error()
    with allure.step("Получение ошибки:"):
        shopping_page.error_auth()


@allure.title("Заблокированный пользователь")
def test_swag_labs_locked_user():
    with allure.step("Открытие главной страницы:"):
        shopping_page.open()
    with allure.step("Авторизация пользователя:"):
        shopping_page.locked_user()
    with allure.step("Получение ошибки:"):
        shopping_page.error_locked_user()


@allure.title("Проверка покупки")
def test_swag_labs_shopping():
    with allure.step("Открытие главной страницы:"):
        shopping_page.open()
    with allure.step("Авторизация пользователя:"):
        shopping_page.auth()
    with allure.step("Сбор корзины:"):
        shopping_page.add_items_to_cart()
    with allure.step("Открытие корзины:"):
        shopping_page.go_to_cart()
    with allure.step("Покупка:"):
        shopping_page.buy()
    with allure.step("Завершение покупки:"):
        shopping_page.finish()


@allure.title("Проверка Logout")
def test_swag_labs_logout():
    with allure.step("Открытие главной страницы:"):
        shopping_page.open()
    with allure.step("Авторизация пользователя:"):
        shopping_page.auth()
    with allure.step("Открытие экрана магазина в авторизованной зоне:"):
        shopping_page.check_login()
    with allure.step("Выход из авторизованной зоны:"):
        shopping_page.logout()


@allure.title("Проверка корзины: добавление, удаление")
def test_swag_labs_cart():
    with allure.step("Открытие главной страницы:"):
        shopping_page.open()
    with allure.step("Авторизация пользователя:"):
        shopping_page.auth()
    with allure.step("Сбор корзины:"):
        shopping_page.add_items_to_cart()
    with allure.step("Проверка добавленных товаров на странице магазине:"):
        shopping_page.check_cart_add()
    with allure.step("Открытие корзины и проверка добавленных товаров:"):
        shopping_page.go_to_cart()
    with allure.step("Удаление товаров из корзины:"):
        shopping_page.check_cart_remove()
