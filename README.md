# Gifts Blog

Данный проект - это мой блог о том, как выбирать и собирать подарки близким людям, чтобы их порадовать


## Начало

Эти инструкции помогут вам запустить копию проекта на вашем локальном компьютере для целей разработки и тестирования.

### Что необходимо для запуска

Какие вещи вам понадобятся для установки программного обеспечения и как их установить:

* [Python 3.11.0](https://www.python.org/downloads/release/python-3110/) 


### Установка

Пошаговая инструкция по установке:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Kxaxtxyxa/DjangoBlog.git
   ```
2. Перейдите в каталог проекта:
   ```bash
   cd gifts
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Настройте базу данных:
   ```bash
   python manage.py migrate
   ```
5. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
6. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

## Запуск

```bash
python manage.py runserver
```


## Authors

* **Kxaxtxyxa** - [Kxaxtxyxa](https://github.com/Kxaxtxyxa)



