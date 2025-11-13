import flet as ft

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        page.title = "Калькулятор Статистики"
        self.test()
    
    def test(self):
        self.page.add(ft.Text(value='HelloWorld'))
        self.page.update()

def main(page: ft.Page):
    app = App(page)

if __name__ == "__main__":
    ft.app(target=main)