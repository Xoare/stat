def is_float_or_is_int(value):
    try: 
        float(value)
        return True
    except (ValueError, TypeError):
        return False