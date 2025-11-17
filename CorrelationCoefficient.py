import flet as ft

def is_float(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def StructWindow(page: ft.Page):
    page.clean()
    CorrelationCoefficient_Element_1 = ft.TextField(label="Элемент 1", width=250)
    CorrelationCoefficient_Element_2 = ft.TextField(label="Элемент 2", width=250)
    result_text = ft.Text("", size=16)
    
    def CorreliationCoefficientСalculate(e):
        try:
            value1 = CorrelationCoefficient_Element_1.value
            value2 = CorrelationCoefficient_Element_2.value
            if not is_float(value1) or not is_float(value2):
                result_text.value = "Введите число с запятой"
                page.update()
                return
            
            value1, value2 = float(value1), float(value2)
            
            result = f"Значения: {value1} и {value2}"
            result_text.value = result
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
        
        page.update()
    
    CorrelationCoefficient_Button = ft.FilledTonalButton(
        text="Рассчитать", 
        on_click=CorreliationCoefficientСalculate
    )
    
    page.add(
        CorrelationCoefficient_Element_1, 
        CorrelationCoefficient_Element_2, 
        CorrelationCoefficient_Button,
        result_text
    )
    page.update()