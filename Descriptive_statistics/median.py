import flet as ft
from CheckingTheDataType.TypeFloat import is_float_or_is_int

def MedianValue(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label='1,2,3,4,5')
    result_text = ft.Text(size=16)
    formula_median = ft.Text("Формулы:\nMe = x₍ₙ₊₁₎/₂\nMe = (xₙ/₂ + xₙ/₂ ₊ ₁) / 2", weight=ft.FontWeight.BOLD, size=20, visible=False)
    soreted_number = ft.Text(visible=False, size=16)
    selection = ft.Text(visible=False, size=16)
    parity = ft.Text(visible=False, size=16)
    result_end = ft.Text(visible=False, weight=ft.FontWeight.BOLD, size=20)
    button_destroy = ft.FilledTonalButton(text="Очистить", visible=False)

    def Destroy(e):
        formula_median.visible = False
        soreted_number.visible = False
        parity.visible = False
        selection.visible = False
        result_end.visible = False
        button_destroy.visible = False
        Average_list.value = ""
        result_text.value = ""
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
                    formula_median.visible = False
                    soreted_number.visible = False
                    parity.visible = False
                    selection.visible = False
                    result_end.visible = False
                    button_destroy.visible = False
                    page.update()
                    return
                numbers.append(float(item))

            result_text.value = f"X = {{{', '.join(map(str, numbers))}}}"
            soreted_number.value = f"X = {{{', '.join(map(str, sorted(numbers)))}}}"
            selection.value = f"n = {len(numbers)}"
            parity.value = f"n: {'Четное' if len(numbers) % 2 == 0 else 'Нечетное'}"
            numbers.sort()

            if len(numbers) % 2 == 0:
                median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
            else:
                median = numbers[len(numbers)//2]
            result_end.value = f"Me = {median}"

            formula_median.visible = True
            soreted_number.visible = True
            parity.visible = True
            button_destroy.visible = True
            selection.visible = True
            result_end.visible = True
            page.update()
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            formula_median.visible = False
            soreted_number.visible = False
            parity.visible = False
            selection.visible = False
            result_end.visible = False
            button_destroy.visible = False
            page.update()
    
    button_destroy.on_click = Destroy
    
    Average_list_button = ft.Row([
        ft.FilledTonalButton(text="Рассчитать", on_click=Average),
        button_destroy
    ])
    
    page.add(
        ft.Text("Введите числа через запятую:", size=16),
        Average_list,
        Average_list_button,
        result_text,
        formula_median,
        soreted_number,
        selection,
        parity,
        result_end
    )
    page.update()