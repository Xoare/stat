import flet as ft
from CheckingTheDataType.TypeFloat import is_float_or_is_int
from collections import Counter

def SamplingMode(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label = "1,2,3,4,5")
    result_text = ft.Text(visible = False, size = 16)
    button_destroy = ft.FilledTonalButton(visible = False, text = "Очистить")
    result_end = ft.Text(visible = False, size = 20, weight=ft.FontWeight.BOLD)
    
    def Destroy(e):
        result_end.visible = False
        button_destroy.visible = False
        Average_list.value = ""
        result_text.value = ""
        page.update()
    
    def Sample(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(",")
            
            numbers = []
            
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value = "Ошибка: все значения должны быть числми"
                    result_end.visible = False
                    button_destroy.visible = False
                    page.update()
                    return
                numbers.append(float(item))    
            
            counter_mode = Counter(numbers)
            max_number = max(counter_mode.values())
            most_common_items = [item for item, count in counter_mode.items() if count == max_number]
            
            result_text.value = f"X = {{{', '.join(map(str, numbers))}}}"
            result_end.value = f"Mo = {most_common_items}"
            
            result_text.visible = True
            result_end.visible = True
            button_destroy.visible = True
            
            page.update()
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            result_end.visible = False
            button_destroy.visible = False
            page.update()
            
    button_destroy.on_click = Destroy
    
    Sample_mode_list = ft.Row([
        ft.FilledTonalButton(text = "Результат", on_click = Sample),
        button_destroy
    ])
        
    page.add(
        ft.Text("Введите числа через запятую:", size=16),
        Average_list,
        Sample_mode_list,
        result_text,
        result_end)
        
    page.update()