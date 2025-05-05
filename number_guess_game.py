import random

pc_number = random.randrange(1, 10)
guess_number = int(input("Uhádni číslo mezi 1 a 10. "))

while guess_number != pc_number:
    if pc_number > guess_number:
        print("Málo. Hádej znovu.")
        guess_number = int(input("Tvé nové číslo: "))
    elif pc_number < guess_number:
        print("Moc. Hádej znovu.")
        guess_number = int(input("Tvé nové číslo: "))
    else:
        break
print(f"Uhádl jsi {pc_number}!")
