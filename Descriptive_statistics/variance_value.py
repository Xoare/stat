import flet as ft
from CheckingTheDataType.TypeFloat import is_float_or_is_int


def VarianceValue(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label="1,2,3,4,5")
    result_text = ft.Text(size=16)
    formula_variance_corrected_sample = ft.Text(size=20, visible=False, weight=ft.FontWeight.BOLD)
    average_value = ft.Text(visible=False, size=16)
    selection = ft.Text(visible=False, size=16)
    result_end = ft.Text(visible=False, size=20, weight=ft.FontWeight.BOLD)
    destroy_button = ft.FilledTonalButton(text = "Очистить", visible=False)
    
    selected_function = None
    
    def Destroy(e):
        hide_elements()
        Average_list.value = ""
        result_text.value = ""
        page.update()
    
    def Variance_corrected_sample(e):
        nonlocal selected_function
        selected_function = Variance_corrected_sample_calc
        result_text.value = "Выбрана исправленная дисперсия"
        hide_elements()
        page.update()
    
    def Variance_biased_sample(e):
        nonlocal selected_function
        selected_function = Variance_biased_sample_calc
        result_text.value = "Выбрана смещенная дисперсия"
        hide_elements()
        page.update()
    
    def Variance_corrected_sample_calc(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(',')
            
            numbers = []
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value = "Ошибка: все значения должны быть числами"
                    hide_elements()
                    page.update()
                    return
                numbers.append(float(item))
                
            sum_of_squares = []
            average = sum(numbers) / len(numbers)
            average_end = round(average, 2)
            for item in numbers:
                sum_of_squares.append((item - average_end)**2)
            result_sum_of_squares = sum(sum_of_squares)
            
            result_text.value = f"X = {{{', '.join(map(str, numbers))}}}"
            formula_variance_corrected_sample.value = f"Формула:\ns² = Σ(xᵢ - x̄)² / (n - 1)"
            average_value.value = f"x̄ = (Σxᵢ) / n\nx̄ = {average:.2f}"
            selection.value = f"n = {len(numbers)}"
            result_end.value = f"s² = {result_sum_of_squares / (len(numbers) - 1):.2f}"
            
            show_element()
            page.update()
                
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            hide_elements() 
            page.update()
    
    def Variance_biased_sample_calc(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(',')
            
            numbers = []
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value = "Ошибка: все значения должны быть числами"
                    hide_elements()
                    page.update()
                    return
                numbers.append(float(item))
                
            sum_of_squares = []
            average = sum(numbers) / len(numbers)
            average_end = round(average, 2)
            for item in numbers:
                sum_of_squares.append((item - average_end)**2)
            result_sum_of_squares = sum(sum_of_squares)
            
            result_text.value = f"X = {{{', '.join(map(str, numbers))}}}"
            formula_variance_corrected_sample.value = f"Формула:\nσ² = Σ(xᵢ - x̄)² / n"
            average_value.value = f"x̄ = (Σxᵢ) / n\nx̄ = {average:.2f}"
            selection.value = f"n = {len(numbers)}"
            result_end.value = f"σ² = {result_sum_of_squares / len(numbers):.2f}"
            
            show_element()
            page.update()
                
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            hide_elements()
            page.update()
    
    def hide_elements():
        formula_variance_corrected_sample.visible = False
        average_value.visible = False
        selection.visible = False
        result_end.visible = False
        destroy_button.visible = False
        
    def show_element():
        formula_variance_corrected_sample.visible = True
        average_value.visible = True
        selection.visible = True
        result_end.visible = True
        destroy_button.visible = True
    
    def calculate_result(e):
        if selected_function:
            selected_function(e)
        else:
            result_text.value = "Сначала выберите тип дисперсии"
            page.update()
    
    corrected_button = ft.FilledButton(
        text="Исправленная Выборочная дисперсия", 
        on_click=Variance_corrected_sample
    )
    
    biased_button = ft.FilledButton(
        text="Смещенная выборочная дисперсия", 
        on_click=Variance_biased_sample
    )
    
    result_button = ft.FilledTonalButton("Результат", on_click=calculate_result)
    destroy_button.on_click = Destroy
    
    page.add(
        ft.Row([corrected_button, biased_button]),
        ft.Divider(thickness=1),
        Average_list,
        ft.Row([result_button, destroy_button]),
        result_text,
        formula_variance_corrected_sample,
        average_value,
        selection,
        result_end
    )
    
    page.update()