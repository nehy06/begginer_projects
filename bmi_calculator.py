# basic BMI calculator
# vzorec pro výpočet BMI - 

import os

def bmi_formula(vyska, vaha):
    return vaha/(vyska ** 2)

def interpretace_bmi(bmi):
    if bmi <= 18.5:
        return("Podváha")
    elif bmi <= 24.9:
        return("Normální zdravá váha")
    elif bmi <= 29.9:
        return("Nadváha")
    else:
        return("Obezita")

    
def main():
    # tisk znaků "-" přes celou délku terminálu
    width = os.get_terminal_size().columns  
    print("-"*width)  
    
    print("Vítejte v BMI kalkulačce")
    
    while True:
        volba = input("Chcete spočítat BMI? ano/ne ").lower()
    
        if volba == "ano":
            
            try:
                vaha = float(input("Zadejte svou váhu: "))
                vyska = float(input("Zadejte svou výšku v metrech (např. 1.6): "))
                
                if vaha <= 0 or vyska <=0:
                    print("Váha a výška musí být kladné číslo!")
                    break
                
                bmi = bmi_formula(vyska, vaha)
                kategorie = interpretace_bmi(bmi)
                
                print(f"Vaše BMI: {bmi}")
                print(f"Kategorie: {kategorie}")
                
                break
                    
            except ValueError:
                print("Zadejte platné číslo!!")
        else:
            break
                
if __name__ == "__main__":
    main()