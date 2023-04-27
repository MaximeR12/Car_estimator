def correct_brands(name : str) -> str:
    if "v" in name and "w" in name :
        return "volkswagen"
    elif 'p' in name and "o" in name and "r" in name and "h" in name:
        return 'porsche'
    elif 't' in name and "o" in name and "y" in name and "a" in name:
        return 'toyota'
    elif "m" in name  and "d" in name  and "a" in name:
        return 'mazda'
    elif 'alfa' in name:
        return 'alfa-romeo'
    else:
        return name.lower()
    
def nb_str_to_int (number : str) -> int:
    if number == 'two':
        return 2
    elif number == "three":
        return 3
    elif number == "four":
        return 4
    elif number == "five":
        return 5
    elif number == "six":
        return 6
    elif number == "eight":
        return 8
    elif number == "twelve":
        return 12

def convert_to_centimeters(value):
    return value * 2.54

def convert_pounds_to_kilograms(value):
    return value * 0.453592

def convert_cubic_inches_to_liters(value):
    """Convert cubic inches to liters and round to 1 deciimal place"""
    return round(value * 0.0163871, 1)

def convert_mpg_to_l_100km(value):
    """Convert miles per gallon to liters per 100 kilometers"""
    return round(235.215 / value, 1)

def clean_price_str(price : float) -> str:
    price = str(round(price))
    return "This car can be estimated at : " + price[:-3] + " " + price[-3:] + " $"
