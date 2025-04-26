import os

def pocitadlo_znaku(text):
    pocet_pismen = 0
    pocet_cislic = 0
    pocet_spec = 0
    
    for znak in text:
        if znak.isalpha():
            pocet_pismen +=1
        if znak.isdigit():
            pocet_cislic +=1
        else:
            pocet_spec +=1
    
    return pocet_pismen, pocet_cislic, pocet_spec

def main():
    # tisk znaků "-" přes celou délku terminálu
    width = os.get_terminal_size().columns  
    print("-"*width)
    
    print("Ahoj, tohle je počítadlo znaků.")
    text = input("Zadej text: ")
    
    pismena, cislice, znaky = pocitadlo_znaku(text)
    
    print(f"Počet písmen: {pismena}")
    print(f"Počet cislic: {cislice}")
    print(f"Počet znaku: {znaky}")
    print(f"Celková délka textu: {len(text)}")
    
    
if __name__ == "__main__":
    main()