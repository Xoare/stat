import flet as ft
from NavigationDarwer import NavDraw

class App:
    def __init__(self, page: ft.Page):
        self.drawer = NavDraw().create_drawer(page)
        self.page = page
        page.title = "Калькулятор Статистики"
        self.Appbar()

    def Appbar(self):
        self.page.appbar = ft.AppBar(leading= ft.IconButton(ft.Icons.MENU, on_click= lambda _ : self.Navigationdrawer()),title = ft.Text("Калькулятор Статистики"), leading_width=40, bgcolor = ft.Colors.PURPLE_200)
        self.page.update()

    def Navigationdrawer(self):
        self.page.drawer = NavDraw().create_drawer(self.page)
        self.page.drawer.open = True
        self.page.update()

def main(page: ft.Page):
    app = App(page)

if __name__ == "__main__":
    ft.app(target=main)