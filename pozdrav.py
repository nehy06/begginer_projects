def pozdrav(jmeno):
    """Funkce pro pozdravení uživatele"""
    return f"Ahoj, {jmeno}!"

def main():
    """Hlavní funkce programu"""
    # Zde začíná běh programu
    jmeno = input("Jak se jmenuješ? ")
    pozdrav_text = pozdrav(jmeno)
    print(pozdrav_text)
    
    vek = int(input("Kolik ti je let? "))
    if vek < 18:
        print("Jsi ještě mladý/á!")
    else:
        print("Už jsi dospělý/á!")

# Toto spustí funkci main(), když je program spuštěn přímo
if __name__ == "__main__":
    main()