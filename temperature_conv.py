# převodník z fahrenheitů do normální soustavy :-)

# func def
# z F do C
def f_to_c(f):
    """prevede f° do c°"""
    return (f - 32) * 5/9

# z C do F
def c_to_f(c):
    """prevede c° do f°"""
    return (c * 9/5) + 32

def main():
    # hlavni logika prevodu
    print("---")
    print("Vítejt v převodník z normálních stupňů Celsia do americké blbosti a naopak!")
    
    while True:
        volba = input("Chcete převádět z F° do C°? Ano/Ne ").lower()
        
        if volba == "ano":
            try:
                teplota_f = float(input("Zadejte teplotu ve stupních Fahrenheita: "))
                teplota_c = f_to_c(teplota_f)
                print(f"{teplota_f} F° je {teplota_c} C°.")
            except ValueError:
                print(f"Zadejte platnou hodnotu!")
        else:
            try:
                teplota_c = float(input(f"Zadejte teplotu ve stupních Celsia: "))
                teplota_f = c_to_f(teplota_c)
                print(f"{teplota_f} C° je {teplota_c} F°.")
            except ValueError:
                print(f"Zadejte platnou hodnotu!")
        
        continue_calc = input(f"Chceš pokračovat v převodu? ano/ne: ").lower()
        if continue_calc != "ano":
            print("Děkuji za použití převodníku!")
            break
            
# spustí program
if __name__ == "__main__":
    main()