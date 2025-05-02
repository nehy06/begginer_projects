import random
import string


# -----------------------------------
# DEFINICE FUNKCÍ 

def pass_length_check(lenght):
# zjištění délky hesla a ověření, že je délka dostatečná
    try:
        input_lenght = int(lenght)
        print(f"Vase delka hesla je: {lenght}")
        
        if input_lenght <= 5:
            print("Špatná délka hesla - musí být alespoň 5 znaků!")
            return False
        
        return True

    except ValueError:
        print("Neplatný vstup. Vložte celé číslo.")

def generate_password(length):
# funkce pro generování hesla z předem definované množiny znaků

    lowecase = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
    uppercase = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = string.digits  # "0123456789"
    special = string.punctuation # "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    all_chars = lowecase + uppercase + digits + special # sloučení pro náhodný věber dále v kódu

    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# -----------------------------------
# MAIN 
    
def main():
    print(f"Vítej v generátoru hesel!")
    
    while True:
        try:
            # vyžádání délky hesla od uživatele
            password_lenght = input("Zadejte požadovanou délku hesla: \nAnebo uadejte 'konec' pro ukončení generování.").lower()

            if password_lenght == "konec":
                print(f"Děkujeme za použití generátoru hesel, přijďte zas! :-)")
                break
            
            if pass_length_check(password_lenght):
                password = generate_password(int(password_lenght))
                    
                print(f"Vygenerované heslo je: {password}")
                
            pokracovat = input(f"Chcete generovat další heslo? ano/ne: ")
            
            if pokracovat != "ano":
                print(f"Děkujeme za použití generátoru hesel, přijďte zas! :-)")
                break
            
                    
        except ValueError:
            print("Neplatný vstup. Vložte celé číslo.")
            
                    
if __name__ == "__main__":
    main()