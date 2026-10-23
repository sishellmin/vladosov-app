#!/usr/bin/env python3
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
