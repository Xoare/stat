import flet as ft
from Descriptive_statistics.average_value import AverageValue
from Descriptive_statistics.median import MedianValue
from Descriptive_statistics.sampling_mode import SamplingMode
from Descriptive_statistics.minimum_value import MinimumValue
from Descriptive_statistics.maximum_value import MaximumValue
from Descriptive_statistics.variance_value import VarianceValue

"""Создание Navigation Drawer"""

class NavDraw:
    def __init__(self):
        self.drawer = None
        self.page = None
        
        self.ItemStatisticsSection = [
            {"name": 'Описательная статистика', "on_click": self.items_descriptive_statistics},
            {"name": "Корреляционный анализ", "on_click": self.items_correlation_analisis},
            {"name": "Проверка нормальности", "on_click": self.items_checking_for_normality},
            {"name": "Статистические тесты", "on_click": self.items_statistical_tests},
            {"name": "Визуализация", "on_click": self.items_visualization}
]
        
        self.ItemDescriptiveStatistics = [
            {"name": "Среднее", "on_click" : AverageValue},
            {"name": "Медиана", "on_click" : MedianValue},
            {"name": "Мода", "on_click" : SamplingMode},
            {"name": "Дисперсия", "on_click" : VarianceValue},
            {"name": "Стандартное отклонение", "on_click" : AverageValue},
            {"name": "Минимум", "on_click" : MinimumValue},
            {"name": "Максимум", "on_click" : MaximumValue},
            {"name": "Квартили", "on_click" : AverageValue}
        ]
        
        self.ItemСorrelationAnalysis = [
            {"name": "Person correlation"},
            {"name": "Spearman rank correlation"},
            {"name": "Визуализация scatter plot"},
        ]
        
        self.ItemCheckingForNormality = [
            {"name": "Shapiro-Wilk test"},
            {"name": "Гистограмма + Q-Q plot"},
        ]

        self.StatisticalTests = [
            {"name": "t-test"},
            {"name": "ANOVA"},
            {"name": "Chi-square test"},
        ]
        
        self.Visualization = [
            {"name": "Графики (гистограммы, box plots)"},
            {"name": "Экспорт результатов"},
            {"name": "Сохранение сессий"},
        ]
    
    """Визуализация"""
    def items_visualization(self, e: ft.ControlEvent, section_name = None):
        items = [ft.CupertinoFilledButton(
            content=ft.Row([
                ft.Text("Визуализация"),
                ft.Icon(ft.Icons.ARROW_DROP_DOWN, color = ft.Colors.WHITE)
                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            )
            )]
        for index, item in enumerate(self.Visualization):
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            if self.Visualization[index] == self.Visualization[-1]:
                continue
            else:
                items.append(ft.Divider(thickness=1))


        self.page.update()
        items.append(ft.CupertinoFilledButton(text = "Назад", on_click = lambda e: self.show_main_menu()))
        return items
    
    """Статистические тесты"""
    def items_statistical_tests(self, section_name = None):
        items = [ft.CupertinoFilledButton(
            content=ft.Row([
                ft.Text("Статистические тесты"),
                ft.Icon(ft.Icons.ARROW_DROP_DOWN, color = ft.Colors.WHITE)
                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            )
            )]
        for index, item in enumerate(self.StatisticalTests):
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            if self.StatisticalTests[index] == self.StatisticalTests[-1]:
                continue
            else:
                items.append(ft.Divider(thickness=1))
        items.append(ft.CupertinoFilledButton(text = "Назад", on_click = lambda e: self.show_main_menu()))
        return items
    
    """Проверка нормальности"""
    def items_checking_for_normality(self, section_name = None):
        items = [ft.CupertinoFilledButton(
            content=ft.Row([
                ft.Text("Проверка нормальности"),
                ft.Icon(ft.Icons.ARROW_DROP_DOWN, color = ft.Colors.WHITE)
                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            )
            )]
        for index, item in enumerate(self.ItemCheckingForNormality):
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            if self.ItemCheckingForNormality[index] == self.ItemCheckingForNormality[-1]:
                continue
            else:
                items.append(ft.Divider(thickness=1))
        items.append(ft.CupertinoFilledButton(text = "Назад", on_click = lambda e: self.show_main_menu()))
        return items
    
    """Корреляционный анализ"""
    def items_correlation_analisis(self, section_name = None):
        items = [ft.CupertinoFilledButton(
            content=ft.Row([
                ft.Text("Корреляционный анализ"),
                ft.Icon(ft.Icons.ARROW_DROP_DOWN, color = ft.Colors.WHITE)
                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            )
            )]
        for index, item in enumerate(self.ItemСorrelationAnalysis):
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            if self.ItemСorrelationAnalysis[index] == self.ItemСorrelationAnalysis[-1]:
                continue
            else:
                items.append(ft.Divider(thickness=1))
        items.append(ft.CupertinoFilledButton(text = "Назад", on_click = lambda e: self.show_main_menu()))
        return items
    
    """Описательная статистика"""
    def items_descriptive_statistics(self, section_name=None):
        items = [ft.CupertinoFilledButton(
            content=ft.Row([
                ft.Text("Описательная статистика"),
                ft.Icon(ft.Icons.ARROW_DROP_DOWN, color = ft.Colors.WHITE)
                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            )
            )]
        for index, item in enumerate(self.ItemDescriptiveStatistics):
            items.append(ft.CupertinoButton(text=item["name"], padding=0, on_click=lambda e, item=item: item["on_click"](e)
                                            or setattr(self.page.drawer, "open", False)
                                            or self.page.update()))
            if self.ItemDescriptiveStatistics[index] == self.ItemDescriptiveStatistics[-1]:
                continue
            else:
                items.append(ft.Divider(thickness=1))
        items.append(ft.CupertinoFilledButton(text = "Назад", on_click = lambda e: self.show_main_menu()))
        return items
    
    """Начальное меню"""
    def items_statistics_section(self):
        items = [
    ft.Container(
        content=ft.Row([
            ft.IconButton(
                icon=ft.Icons.MENU, 
                icon_color=ft.Colors.WHITE,
                on_click = lambda e: setattr(self.page.drawer, "open", False) or self.page.update()
            ),
            ft.CupertinoFilledButton(
                content=ft.Row([
                    ft.Text("Калькулятор Статистики"),
                    ft.Icon(ft.Icons.INFO_OUTLINE_ROUNDED, color=ft.Colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#36618e",
    )
]
        
        for item in self.ItemStatisticsSection:
            items.append(ft.CupertinoButton(
                content =ft.Row([
                    ft.Text(item["name"]),
                    ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT)
                ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                on_click=lambda e, section=item['name']: self.show_submenu(section)
            ))
            items.append(ft.Divider(thickness=1))
        return items
    
    """Создание NavigationDrawer"""
    def create_drawer(self, page):
        self.page = page
        self.drawer = ft.NavigationDrawer()
        self.show_main_menu()
        return self.drawer
    
    def controls_edit(self, controls):
        self.drawer.controls = controls
        self.page.update()
    
    def show_main_menu(self):
        self.controls_edit(self.items_statistics_section())
    
    def show_submenu(self, section_name):
        for item in self.ItemStatisticsSection:
            if item['name'] == section_name:
                self.controls_edit(item['on_click'](section_name))