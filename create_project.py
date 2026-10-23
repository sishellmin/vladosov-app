from pathlib import Path

BASE_DIR = Path("/home/vladislav/Progect/Vlad_Progs_Econom")


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  created: {path.relative_to(BASE_DIR)} ({len(content)} bytes)")


def main():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Project root: {BASE_DIR}\n")

    # ---------- README ----------
    readme = '''# Vlad_Progs_Econom

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
'''
    write_file(BASE_DIR / "README.md", readme)

    # ---------- .vscode/settings.json ----------
    settings = '''{
    "python.defaultInterpreterPath": "${workspaceFolder}/desktop/venv/bin/python",
    "php.validate.executablePath": "/usr/bin/php",
    "files.associations": {
        "*.php": "php"
    }
}
'''
    write_file(BASE_DIR / ".vscode" / "settings.json", settings)

    # ---------- .vscode/tasks.json ----------
    tasks = '''{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Desktop Tutor",
            "type": "shell",
            "command": "${workspaceFolder}/desktop/venv/bin/python",
            "args": ["${workspaceFolder}/desktop/launcher.py"],
            "group": { "kind": "build", "isDefault": true },
            "problemMatcher": []
        }
    ]
}
'''
    write_file(BASE_DIR / ".vscode" / "tasks.json", tasks)

    # ---------- php/index.php ----------
    index_php = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Экономика — Тьютор</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
        .card { background: #f4f4f9; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; }
        h1 { color: #2c3e50; }
        input, button { padding: 0.5rem; font-size: 1rem; margin: 4px; }
        #result { margin-top: 1rem; font-weight: bold; color: #27ae60; }
    </style>
</head>
<body>
    <h1>Тьютор по экономике</h1>
    <div class="card">
        <h2>Калькулятор сложного процента</h2>
        <p>Введите сумму, ставку и количество лет.</p>
        <input type="number" id="principal" placeholder="Сумма" value="1000">
        <input type="number" id="rate" placeholder="Ставка, %" value="5">
        <input type="number" id="years" placeholder="Лет" value="10">
        <button onclick="calculate()">Рассчитать</button>
        <div id="result"></div>
    </div>
    <script>
        function calculate() {
            const p = parseFloat(document.getElementById("principal").value);
            const r = parseFloat(document.getElementById("rate").value) / 100;
            const t = parseFloat(document.getElementById("years").value);
            if (isNaN(p) || isNaN(r) || isNaN(t)) {
                document.getElementById("result").innerText = "Заполните все поля.";
                return;
            }
            const total = p * Math.pow(1 + r, t);
            document.getElementById("result").innerText =
                "Итоговая сумма: " + total.toFixed(2) +
                " (прибыль: " + (total - p).toFixed(2) + ")";
        }
    </script>
</body>
</html>
'''
    write_file(BASE_DIR / "php" / "index.php", index_php)

    # ---------- desktop/launcher.py ----------
    launcher = '''#!/usr/bin/env python3
"""Лаунчер: запускает встроенный PHP-сервер и открывает pywebview."""
import subprocess
import time
import socket
from pathlib import Path

import webview

ROOT = Path(__file__).resolve().parent.parent
PHP_DIR = ROOT / "php"
PHP_HOST = "127.0.0.1"
PHP_PORT = 8000


def is_port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0


def start_php_server():
    cmd = ["php", "-S", f"{PHP_HOST}:{PHP_PORT}", "-t", str(PHP_DIR)]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for _ in range(50):
        if is_port_open(PHP_HOST, PHP_PORT):
            return proc
        time.sleep(0.1)
    proc.terminate()
    raise RuntimeError("PHP-сервер не запустился. Установите PHP: sudo dnf install php-cli")


def main():
    php_proc = start_php_server()
    try:
        webview.create_window(
            "Экономика — Тьютор",
            f"http://{PHP_HOST}:{PHP_PORT}/index.php",
            width=1024,
            height=768,
        )
        webview.start()
    finally:
        php_proc.terminate()
        print("PHP-сервер остановлен.")


if __name__ == "__main__":
    main()
'''
    write_file(BASE_DIR / "desktop" / "launcher.py", launcher)

    # ---------- desktop/requirements.txt ----------
    write_file(BASE_DIR / "desktop" / "requirements.txt", "pywebview>=6.0\n")

    # ---------- android/main.py ----------
    android_main = '''"""Заготовка Android-приложения на Kivy с WebView."""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import platform

if platform == "android":
    from android.webkit import WebView
    from android.runnable import run_on_ui_thread

    class AndroidWebView(Widget):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.webview = WebView()

        @run_on_ui_thread
        def add_to_layout(self, layout):
            layout.add_view(self.webview)

    class EconomApp(App):
        def build(self):
            root = Widget()
            wv = AndroidWebView()
            wv.add_to_layout(root)
            return root

    EconomApp().run()
else:
    print("Этот файл предназначен для запуска на Android через Buildozer.")
'''
    write_file(BASE_DIR / "android" / "main.py", android_main)

    # ---------- android/buildozer.spec ----------
    buildozer = '''[app]
title = Vlad_Progs_Econom
package.name = vladprogseconom
package.domain = org.vlad
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1
requirements = python3,kivy,android
orientation = portrait
fullscreen = 0
'''
    write_file(BASE_DIR / "android" / "buildozer.spec", buildozer)

    print("\nГотово.")
    print("Далее:")
    print("  1) sudo dnf install php-cli")
    print("  2) cd desktop && python -m venv venv && source venv/bin/activate")
    print("  3) pip install -r requirements.txt")
    print("  4) python launcher.py")


if __name__ == "__main__":
    main()