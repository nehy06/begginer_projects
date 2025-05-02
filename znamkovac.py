# ----------------------------
# IMPORTY

 
# ----------------------------
# DEFINICE FUNKCÍ

def znamky(body):
    if body < 0 or body > 100:
        return "Neplatné bodové hodnocení (musí být 0-100)"
    
    if body >= 90:
        return "A (Výborně)"
    elif body >= 80:
        return "B (Velmi dobře)"
    elif body >= 70:
        return "C (Dobře)"
    elif body >= 60:
        return "D (Dostatečně)"
    else:
        return "F (Nedostatečně)"


def main():
    while True:
        try:
        
            body_studenta = int(input("Zadejte počet bodů studenta (0-100): "))

            znamka = znamky(body_studenta)
            print(f"Studentovo znamka je: {znamka}")
            
        except ValueError:
            print("Neplatná hodnota, zadejte počet bodů, který je celé číslo!")
            
        pokracovani = input("Chcete hodnotit další test? ano/ne ").lower() 
        if pokracovani != 'ano':
            break
# ----------------------------
# MAIN
    
if __name__ == "__main__":
    main()