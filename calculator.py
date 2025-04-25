# Základní kalkulačka
# přijímá vstup od uživatele, provádí zvolenou operaci a vrací výsledek

#improt knihoven
import math

# func def
def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mult (a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Dělení nulou není definováno!"
    
def power(a, b):
    return a ** b

def root(a, b):
    if a >= 0 or b % 2 != 0:
        try:
            return a ** (1/b)
        except:
            return "Neplatná operace!"
    return "Nelze vypočítat sudou odmocninu záporného čísla!"

def main ():
    operations = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": divide,
        "^": power,
        "root": root
    } 

    print("-----------")
    print("Vítej v kalkulačce! Je pirmitivní, ale funguje :-D")
    print("Dostupné operace: +, -, *, /, ^(mocnina), root(odmoncnina)")

    while True:
        try:
            # input
            first_number = float(input("Zadejte první číslo: "))
            operation = input("Zadejte operaci: ")
            second_number = float(input("zadejte druhé číslo: "))
        
            if operation in operations:
                result = operations[operation](first_number, second_number)
                print(f"{first_number} {operation} {second_number} = {result}")
            else:
                print("Neplatná operace!")
            
        except ValueError:
            print("Neplatný vstup, prosím zadejte číslo!")
            
        continue_calc = input(f"Chceš pokračovat ve výpočtu? ano/ne: ").lower()
        if continue_calc != "ano":
            print("Děkuji za použití kalkulačky!")
            break
        
# spustí kalkulačku   
if __name__ == "__main__":
    main()




    
