import flet as ft
from CheckingTheDataType.TypeFloat import is_float_or_is_int

def SamplingMode(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label = "1,2,3,4,5")
    result_text = ft.Text()
    
    
    def Sample(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(",")
            
            numbers = []
            
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value = "Ошибка: все значения должны быть числми"
                numbers.append(float(item))
                
                page.update()
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            
            page.update()
            
        
    Sample_mode_list = ft.Row([
        ft.FilledTonalButton(text = "Результат", on_click = Sample),
        ft.FilledTonalButton(text = "Очистить", on_click = None)
    ])
        
    page.add(
        ft.Text("Введите числа через запятую:", size=16),
        Average_list,
        Sample_mode_list,
        result_text)
        
    page.update()