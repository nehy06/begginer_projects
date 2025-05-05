import random
import time

# definice seznamu možností, které můžeme využít jako naše volby, stejně tak pc který hraje proti nám
moznosti = ["Kámen", "Nůžky", "Papír"]
# ještě by to chtělo implementovat verzi: Na 3 vítězství, kdo vyhraje 2x, vyhrál všechno :P.

# pravidla + intro
print("Budeme hrát Kámen, Nůžky, Papír do té doby, dokud pc nebo ty nevyhraje 3x. Hodně štěstí.")
time.sleep(1)

print("Jako svou volbu můžeš zvolit klasické:")
for i in range(len(moznosti)):
    print(moznosti[i])
time.sleep(1)

clovek_score = 0
pc_score = 0

while not (clovek_score < 3) or (pc_score < 3):
    time.sleep(1)
    print("Ok, hrajeme!")

    # kontrola vyberu volby cloveka - preklepy atp., implementovat capitalize ať to můžou psát v
    volba_clovek = input("Co dáš? ").capitalize()
    while volba_clovek not in moznosti:
        volba_clovek = input(
            f"špatně, vyber si z {moznosti}! Nezapomeň psát háčky čárky :): ").capitalize()

    volba_pc = random.choice(moznosti)

    # kontrola výběru
    if volba_pc == volba_clovek:
        print(f"{volba_clovek} vs {volba_pc} = remíza.")
    elif volba_pc == "Kámen":
        if volba_clovek == "Nůžky":
            print(f"Kámen tupí nůžky = PC vyhrává. ")
            pc_score += 1
        else:
            print(f"Papír balí kámen  = Vyhráváš ")
            clovek_score += 1
    elif volba_pc == "Nůžky":
        if volba_clovek == "Kámen":
            print("Kámen tupí nůžky = Vyhráváš!")
            clovek_score += 1
        else:
            print("Nůžky stříhají papír = Prohráváš")
            pc_score += 1
    elif volba_pc == "Papír":
        if volba_clovek == "Nůžky":
            print("Nůžky stříhají papír = Vyhráváš!")
            clovek_score += 1
        else:
            print("Papír balí kámen = Prohráváš!")
            pc_score += 1
    print(f"{pc_score} : {clovek_score}")


print(f" Skóre je: {pc_score} : {clovek_score}")
