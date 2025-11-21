import flet as ft
from CheckingTheDataType.TypeFloat import is_float_or_is_int

def MinimumValue(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label='1,2,3,4,5')
    result_text = ft.Text(size=16)
    result_end = ft.Text(size = 20, weight=ft.FontWeight.BOLD, visible = False)
    button_destroy = ft.FilledTonalButton(text = "Очистить", visible = False)
    
    def Destroy(e):
        result_end.visible = False
        button_destroy.visible = False
        Average_list.value = ""
        result_text.value = ""
        page.update()
        
    def Minimum(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(',')
            
            numbers = []
            
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value("Ошибка: все значения должны быть числами")
                    
                    page.update()
                    return
                numbers.append(float(item))
                
            result_text.value = f"X = {{{', '.join(map(str, numbers))}}}"
            result_end.value = f"Min = {float(min(numbers))}"
            
            result_end.visible = True
            button_destroy.visible = True
            
            page.update()
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            result_end.visible = False
            button_destroy.visible = False
            page.update()
            
    button_destroy.on_click = Destroy
    Average_list_button =ft.Row([
        ft.FilledTonalButton(
            text="Рассчитать", on_click=Minimum),
        button_destroy])
    
    page.add(
        ft.Text("Введите числа через запятую:", size=16),
        Average_list,
        Average_list_button,
        result_text,
        result_end
    )