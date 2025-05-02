def main():
    while True:
        try:
            number = int(input("Zadejte číslo: "))
            
            if (number % 2) == 0:
                print("Vaše číslo je sudé.")
                
            else:
                print("vaše číslo je liché.")
            
            pokracovani = input("Chcete vyzkoušet další číslo? ano/ne: ").lower()
            
            if pokracovani != "ano":
                break
            
        except ValueError:
            print("Chybná hodnota, zedejte platné celé číslo!!!")
        
if __name__ == "__main__":
    main()