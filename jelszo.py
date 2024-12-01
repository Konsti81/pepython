import random
import string
szotar=["alma", "kereszt", "fal","kő", "kapu", "elem", "lista", "ragasztó"]
felhasznalonev=input("Adj meg egy felhasználó nevet!: ")
def jelszogeneralas():
    szavak=random.choices(szotar, k=2)
    szam=random.randint(100,999)
    speckaraterter=random.choice(string.punctuation)
    return f"{szavak[0]}{szavak[1]}{szam}{speckaraterter}"
jelszo=jelszogeneralas()
print("1. Új felhasználónév-jelszó pár létrehozás")
print("2. Meglévő felhasznűlónév-jelszó pár módositása")
print("3. Meglévő felhasználónév-jelszó pár törlése")
menupont_szama=int(input("Kérem a kiválasztott menüpont számát:"))
if menupont_szama==1:
    print(f"A felhasználóneved:{felhasznalonev} És az ehhez tartozó jelszavad:{jelszo}")
    #szavak imprtálása txt fáljból.
    #szavak=[2 random szó a szótárból]szavak.append()random.choices(szotar,2)
    
    #szam=random.randit(100,999)
    #speckaraterter=random.choice(string.puntuation)
if menupont_szama==2:
    print("1. Meglévő felhasználónév-jelszó pár újragenerálása")
    print("2. Meglévő felhasználónév módosítása")
    print("Meglévő jelszó módosítása")
    almenu2_szama=int(input(print("Kérem a kiválasztott menüpont számát:")))
    if almenu2_szama==1:
        print("")
    if almenu2_szama==2:
        print("")
    if almenu2_szama==3:
        print("")
if menupont_szama==3:
    print("")

