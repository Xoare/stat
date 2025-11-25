import flet as ft

class StartPage:
    def __init__(self):
        pass
        
    def first_page(self, page: ft.Page):
        page.add(
            ft.Column([
                ft.Text("Ваш универсальный помощник в мире статистики.", size = 20, weight=ft.FontWeight.BOLD),
                ft.Text("Мощный, точный и невероятно простой калькулятор для анализа данных на вашем телефоне и компьютере.", size = 16, weight=ft.FontWeight.BOLD),
                ft.Text("Ключевые преимущества:"),
                ft.Row([
                    ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT), 
                    ft.Text("Для студентов и ученых:", weight=ft.FontWeight.BOLD), 
                    ft.Text("Все необходимые инструменты от описательной статистики до сложных тестов в одном месте."),
                    ]),
                ft.Row([
                    ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT), 
                    ft.Text("Простота и мощь:", weight=ft.FontWeight.BOLD), 
                    ft.Text("Интуитивный интерфейс скрывает сложные вычисления, даря вам только точный результат.")
                    ]),
                ft.Row([
                    ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT), 
                    ft.Text("Экспорт и визуализация:", weight=ft.FontWeight.BOLD), 
                    ft.Text("выгружайте данные в удобный для вас формат, стройте удобные графики.")
                    ])
                ]),
            ft.Container(
                    content=ft.Column([
                        ft.Text("Поддерживаемые статистические методы:", size=20, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("📊 Описательная статистика", weight=ft.FontWeight.BOLD),
                                    ft.Text("• Среднее, медиана, мода\n• Дисперсия, стандартное отклонение\n• Минимимум, максимум, квартили", size=14)
                                ]),
                                expand=True,
                                padding=10
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("🔬 Проверка нормальности", weight=ft.FontWeight.BOLD),
                                    ft.Text("• Shapiro-Wilk test\n• Гистограмма + Q-Q plot", size=14)
                                ]),
                                expand=True,
                                padding=10
                            ),
                        ]),
                        ft.Row([
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("📈 Корреляционный анализ", weight=ft.FontWeight.BOLD),
                                    ft.Text("• Person correlation\n• Spearman rank correlation\n• Визуализация scatter plot", size=14)
                                ]),
                                expand=True,
                                padding=10
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("📉 Статистические тесты", weight=ft.FontWeight.BOLD),
                                    ft.Text("• t-test\n• ANOVA\n• Chi-square test", size=14)
                                ]),
                                expand=True,
                                padding=10
                            ),
                        ]),
                    ]),
                    padding=20,
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    border_radius=10,
                    margin=ft.margin.only(bottom=20)
                ),
            ft.FilledButton(text = "Начать исследование", icon = ft.Icons.START, width = 200)
            )
        page.update()
    
start_page = StartPage()
