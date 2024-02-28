# Проект по тестированию сайта интернет-магазина Swag Labs
> <a target="_blank" href="https://www.saucedemo.com/">Ссылка на Интернет-магазин</a>

#### Список проверок, реализованных в автотестах
- [x] Проверка авторизации с валидными и не валидными данными
- [x] Провека добавления и удаления товаров из корзины
- [x] Проверка покупки
- [x] Проверка выхода из аккаунта

### Структура проекта

### Проект реализован с использованием
- Python 
- Pytest 
- PyCharm 
- Selenoid 
- Selene 
- Jenkins 
- Allure Report 
- Telegram Bot

## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/hw_15_swag_labs/">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/hw_15_swag_labs/">проект</a>

![This is an image](/photos/main_jen.png)

#### 2. Выбрать пункт **Build with Parameters**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Build**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

### Локальный запуск автотестов
1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команду 
  ```bash
  pytest -sv
  ```
5. Для запусков тестов удаленно используйте команду 
  ```bash
  environment='remote' pytest -sv
  ```

Получение отчёта allure:
```bash
allure serve allure-results
```

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/photos/telega.png)
