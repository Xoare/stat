import flet as ft
from NavigationDarwer import NavDraw
from AppbarTitle.title import title_appbar
from First_page import start_page

class App:
    def __init__(self, page: ft.Page):
        self.drawer = NavDraw().create_drawer(page)
        self.page = page
        page.title = "Калькулятор Статистики"
        self.button_list = []
        start_page.first_page(page)
        page.scroll = ft.ScrollMode.AUTO
        self.Appbar()

    def Appbar(self, e = None):
        self.page.appbar = ft.AppBar(
            leading= ft.IconButton(
                ft.Icons.MENU, on_click= lambda _ : self.Navigationdrawer(),
                icon_color= ft.Colors.WHITE),
            title = ft.Text(f"{title_appbar.TitleApp(e)}", color = ft.Colors.WHITE),
            actions=[ft.IconButton(icon = ft.Icons.LOGOUT, icon_color = ft.Colors.WHITE, on_click = lambda _: self.page.window.close())],
            leading_width=40, bgcolor ="#36618e", elevation=8)
        self.page.update()

    
    def Navigationdrawer(self):
        self.page.drawer = NavDraw().create_drawer(self.page)
        self.page.drawer.open = True
        self.page.update()

#    def update_appbar_title(self, e: ft.ControlEvent):
#       self.title_appbar.reset_appbar(e)
#        self.Appbar(e)
        
def main(page: ft.Page):
    app = App(page)

if __name__ == "__main__":
    ft.app(target=main)