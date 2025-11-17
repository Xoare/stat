import flet as ft
from Descriptive_statistics.average_value import AverageValue

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
            {"name": "Медиана", "on_click" : AverageValue},
            {"name": "Мода", "on_click" : AverageValue},
            {"name": "Дисперсия", "on_click" : AverageValue},
            {"name": "Стандартное отклонение", "on_click" : AverageValue},
            {"name": "Минимум", "on_click" : AverageValue},
            {"name": "Максимум", "on_click" : AverageValue},
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
    def items_visualization(self, section_name = None):
        items = [ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda e: self.show_main_menu()), ft.Divider(thickness=1)]
        for item in self.Visualization:
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            items.append(ft.Divider(thickness=1))
        return items
    
    """Статистические тесты"""
    def items_statistical_tests(self, section_name = None):
        items = [ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda e: self.show_main_menu()), ft.Divider(thickness=1)]
        for item in self.StatisticalTests:
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            items.append(ft.Divider(thickness=1))
        return items
    
    """Проверка нормальности"""
    def items_checking_for_normality(self, section_name = None):
        items = [ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda e: self.show_main_menu()), ft.Divider(thickness=1)]
        for item in self.ItemCheckingForNormality:
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            items.append(ft.Divider(thickness=1))
        return items
    
    """Корреляционный анализ"""
    def items_correlation_analisis(self, section_name = None):
        items = [ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda e: self.show_main_menu()), ft.Divider(thickness=1)]
        for item in self.ItemСorrelationAnalysis:
            items.append(ft.CupertinoButton(text=item["name"], padding=0))
            items.append(ft.Divider(thickness=1))
        return items
    
    """Описательная статистика"""
    def items_descriptive_statistics(self, section_name=None):
        items = [ft.IconButton(icon = ft.Icons.ARROW_BACK, on_click = lambda e: self.show_main_menu()), ft.Divider(thickness=1)]
        for item in self.ItemDescriptiveStatistics:
            items.append(ft.CupertinoButton(text=item["name"], padding=0, on_click= item["on_click"]))
            items.append(ft.Divider(thickness=1))
        return items
    
    """Начальное меню"""
    def items_statistics_section(self):
        items = []
        for item in self.ItemStatisticsSection:
            items.append(ft.CupertinoButton(
                text=item["name"], 
                padding=0, 
                on_click=lambda e, section=item['name']: self.show_submenu(section)
            ))
            items.append(ft.Divider(thickness=1))
        return items
    
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