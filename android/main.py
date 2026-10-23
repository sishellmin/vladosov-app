"""Заготовка Android-приложения на Kivy с WebView."""
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
