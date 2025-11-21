import flet as ft

class TitleAppBar:
    def __init__(self):
        self.appbar_title = ["Калькулятор статистики"]
    
    def TitleApp(self, e: ft.ControlEvent):
        return " ".join(self.appbar_title)
    
    def reset_appbar(self, e: ft.ControlEvent):
        self.appbar_title.append(str(e.control.text))
        page = e.page
        page.update()
        print(self.TitleApp)
        
title_appbar = TitleAppBar()