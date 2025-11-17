import flet as ft

def is_float_or_is_int(value):
    try: 
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def AverageValue(e: ft.ControlEvent):
    page = e.page
    page.clean()
    
    Average_list = ft.TextField(label='1,2,3,4,5')

    def Average(e):
        try:
            value1 = Average_list.value
            value1 = str(value1).split(',')
            
            numbers = []
            for item in value1:
                item = item.strip()
                if not is_float_or_is_int(item):
                    result_text.value = "Ошибка: все значения должны быть числами"
                    page.update()
                    return
                numbers.append(float(item))

            average = sum(numbers) / len(numbers)
            result_text.value = f"Среднее значение: {average:.2f}"
            page.update()
            
        except Exception as ex:
            result_text.value = f"Ошибка: {ex}"
            page.update()
    
    Average_list_button = ft.FilledTonalButton(
        text="Расчитать", 
        on_click=Average
    )
    
    result_text = ft.Text()
    
    page.add(
        ft.Text("Введите числа через запятую:", size=16),
        Average_list,
        Average_list_button,
        result_text
    )
    page.update()