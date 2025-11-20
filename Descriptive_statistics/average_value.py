import flet as ft
from CheckingTheDataType.TypeFloat import is_float_or_is_int

def AverageValue(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label='1,2,3,4,5')
    result_text = ft.Text(size = 16)
    formula_average = ft.Text("Формула:\nx̄ = (Σxᵢ) / n", visible=False, weight= ft.FontWeight.BOLD, size = 20)
    sum_average = ft.Text(visible=False, size = 16)
    selection = ft.Text(visible=False, size = 16)
    result_average = ft.Text(visible=False, weight= ft.FontWeight.BOLD, size = 20)
    button_destroy = ft.FilledTonalButton(text = "Очистить", visible=False)

    def Destroy(e):
        formula_average.visible = False
        sum_average.visible = False
        selection.visible = False
        result_average.visible = False
        button_destroy.visible = False
        result_text.value = ""
        Average_list.value = ""
        page.update()
    
    def Average(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(',')
            
            numbers = []
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value = "Ошибка: все значения должны быть числами"
                    formula_average.visible = False
                    page.update()
                    return
                numbers.append(float(item))

            average = sum(numbers) / len(numbers)
            result_text.value = f"X = {{{', '.join(map(str, numbers))}}}"
            sum_average.value = f"Σn = {" + ".join(map(str, numbers))} = {sum(numbers)}"
            selection.value = f"n = {len(numbers)}"
            result_average.value = f"x̄ = {average:.2f}"

            formula_average.visible = True
            sum_average.visible = True 
            selection.visible = True   
            result_average.visible = True
            button_destroy.visible = True
            page.update()
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            formula_average.visible = False
            sum_average.visible = False
            selection.visible = False
            result_average.visible = False
            button_destroy.visible = False
            result_text.value = ""
            Average_list.value = ""
            page.update()
    
    button_destroy.on_click = Destroy
    
    Average_list_button =ft.Row([
        ft.FilledTonalButton(
            text="Рассчитать", on_click=Average),
        button_destroy])
    
    page.add(
        ft.Text("Введите числа через запятую:", size=16),
        Average_list,
        Average_list_button,
        result_text,
        formula_average,
        sum_average,
        selection,
        result_average
    )
    page.update()