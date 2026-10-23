# Vlad_Progs_Econom

Тьютор по экономике с локальным веб-интерфейсом.

## Структура

- desktop/ — лаунчер для Windows (Python + pywebview + встроенный PHP-сервер)
- php/ — PHP-страницы (бэкенд/логика)
- android/ — заготовка для Android (Kivy WebView)
- .vscode/ — настройки для VSCode

## Быстрый старт (Desktop)

1. Установите PHP:

       sudo dnf install php-cli

2. Создайте venv и установите зависимости:

       cd desktop
       python -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt

3. Запустите:

       python launcher.py
