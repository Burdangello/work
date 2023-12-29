# Destinatio 

# mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
# ceny = (150, 200, 120, 120, 100, 180)
# cara = "=" * 35
# nabidka = """
# 1 - Praha   | 150,- Kč
# 2 - Viden   | 200,- Kč
# 3 - Olomouc | 120,- Kč
# 4 - Svitavy | 100,- Kč
# 5 - Zlin    | 100,- Kč
# 6 - Ostrava | 180,- Kč
# """

# print("VITEJTE U NASI APLIKACE DESTINATIO!")
# print(cara, nabidka, end='') # end nam zkrati print
# print(cara)

# destinace = input("CISLO DESTINACE: ")
# jmeno = input("JMENO: ")
# prijmeni = input("PRIJMENI: ")
# email = input("E-MAIL: ")

# print(cara)

# cilova_stanice = mesta[int(destinace) - 1] # mesta[int(destinace) - 1]
# finalni_cena = ceny[int(destinace) - 1]

# print(cilova_stanice)
# print(finalni_cena, " ,-Kč", sep ='')

# print(cara)
# print("Cestujicí:", jmeno, prijmeni)
# print("Cílová destinace:", destinace)
# print("Cena jízdneho:", finalni_cena)
# print("Jízdenku jsme odeslali na e-mail", email)




# Destinatio 2

# Program bude umět:

# 1. Vybrat pouze z nabídky (1-6),
# 2. přepočítat cenu, pokud bude sleva,
# 3. pracovat pouze s křestním jménem,
# 4. zakázat uživatelům mladším 18 let nakupovat,
# 5. ověřovat emailové adresy.


# mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]

# ceny  = (150, 200, 120, 120, 100, 180)

# slevy = ("Olomouc", "Svitavy", "Ostrava")

# domeny = ("gmail.com", "seznam.cz", "email.cz")

# dvojita_cara = "=" * 35
# cara = "-" * 35

# nabidka = """
# 1 - Praha   | 150
# 2 - Viden   | 200
# 3 - Olomouc | 120
# 4 - Svitavy | 120
# 5 - Zlin    | 100
# 6 - Ostrava | 180
# """
# AKT_ROK = 2023


# print("VITEJTE U NASI APLIKACE DESTINATIO!")
# print(dvojita_cara, nabidka, end='')
# print(dvojita_cara)

# destinace_cislo = int(input("Vyber číslo destinace: "))

# if 1 <= destinace_cislo <= 6:
#     destinace_nazev = mesta[destinace_cislo -1]
#     print("Destinace: " + destinace_nazev.upper())
# else:
#     print("Destinace cislo " + str(destinace_cislo) + " NEEXISTUJE!")    
#     quit()

# print(cara)

# if destinace_nazev in slevy:
#     nova_cena = 0.75 * ceny[destinace_cislo - 1]
#     print("Ziskavate 25% slevu! Nova cena: " + str(nova_cena) + ",-")
# else:
#     nova_cena = ceny[destinace_cislo - 1]
#     print("Jizdenka bez slevy. Cena: " + str(nova_cena) + ",-")

# print(cara)

# cele_jmeno = input("Vaše celé jméno: ")

# krestni_jmeno = cele_jmeno.split()[0]
# if krestni_jmeno.isalpha(): # isalpha - kontroluje, jestli je input alfabeticky
#     print("Křestní jméno:", krestni_jmeno)    # znak.
# else:
#     print("Neplatné jméno!")    
# print(cara)    

# rok_narozeni = int(input("Váš rok narození "))

# if (AKT_ROK - rok_narozeni) >= 18:   # výpočet plnoletosti z roku narození
#     print("Přístup povolen...")
# else:
#     print("jste příliš mladý na nákup jízdenek!")    
#     print("Ukončuji program.")
#     quit()
# print(cara)


# email = input("Zápis vaší e-mailovou adresu: ")

# if "@" in email and email.split("@")[1] in domeny:
#     print("Ověření e-mailu proběhlo v pořádku.")
# else:
#     print("Tento e-mail je neplatný!")    
#     print("Ukončuji program")
#     quit()
# print(dvojita_cara)

# print(
#     "\nDěkuji, " + krestni_jmeno + " za objednavku jizdanky." 
#     "\nCílová destinace: " + destinace_nazev + ", cena jizdneho: " + str(nova_cena) + ",-" 
#     "\nNa Vás e-mail: " + email + " jsme odeslali e-jizdenku.\n"
# )
# print(dvojita_cara * 2)









# Destinatio 3


# 1. Sjednotit všechny 4 slovníky do jednoho,
# 2. přihlásit a uvítat uživatele a vypsat nabídku služeb,
# 3. umožnit výběr ze služeb,
# 4. první služba, vypsat všechny dostupné filmy,
# 5. druhá služba, vypsat deatily jednoho filmu,
# 6, třetí služba, doporučit film,
# 7. Ukončení programu.


from pprint import pprint

oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "Martin": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}


## Spojíme všechny slovníky filmů do jednoho slovníku jménem `filmy` ########
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}

## Uvítání a výpis nabídky ##################################################
uzivatel = input("Zadej jmeno: ")

if not uzivatel in uzivatele:
    print("neregistrovany uzivatel!")
    quit()
else:
    print("V poradku", oddelovac, sep="\n")
    print("Vitejte v nasem filmovem slovniku!".upper().center(62),
          oddelovac, sep="\n")
    print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")

## Výběr služby ##############################################################
vyber = input("Vyber sluzbu: ")

## Výpis všech dostupných filmů ##############################
if vyber in sluzby and vyber == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), oddelovac, sep="\n")

## Vyber film a zobraz detaily o něm ########################
elif vyber in sluzby and vyber == "detaily filmu":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), sep="\n")
    film = input("Vyber film:")
    print(oddelovac, f"FILM: {film}", filmy.get(film), oddelovac, sep="\n")

## Vyber všechny režiséry ###################################
elif vyber in sluzby and vyber == 'reziseri':
    reziseri = {
        filmy["Shawshank Redemption"]["REZISER"], 
        filmy["The Godfather"]["REZISER"],
        filmy["The Dark Knight"]["REZISER"], 
        filmy["The Prestige"]["REZISER"]
    }
    print(f" {', ' .join(reziseri)}", oddelovac, sep="\n")

## Doporuč film podle ostatních uživatelů ##################
elif vyber in sluzby and vyber == "doporuc film":
    ## kopie puvodniho slovniku hodnoceni (budeme upravovat pouze kopii!)
    kopie_hodnoceni = uzivatele.copy()

    ## selekce aktivniho uzivatele (vytahnu si uzivatele a jeho oblibene filmy)
    aktivni_uzivatel = kopie_hodnoceni.pop(uzivatel)
    # print(f'{aktivni_uzivatel=}')

    ## zbytek uzivatelu
    zbytek_hodnoceni = kopie_hodnoceni
    # print(f'{zbytek_hodnoceni=}')

    ## ulozim si zbyle uzivatele do oddelenych promennych
    detaily_prvni_uzivatel = zbytek_hodnoceni.popitem()
    detaily_druhy_uzivatel = zbytek_hodnoceni.popitem()
    # print(f'{detaily_prvni_uzivatel=}')
    # print(f'{detaily_druhy_uzivatel=}')


    ## tyto detaily jeste rozdelim do samostatnych promennych
    jmeno_prvni_uz = detaily_prvni_uzivatel[0]
    jmeno_druhy_uz = detaily_druhy_uzivatel[0]
    hodnoceni_prvni_uz = detaily_prvni_uzivatel[1]
    hodnoceni_druhy_uz = detaily_druhy_uzivatel[1]
    # print(f'{jmeno_prvni_uz=}')
    # print(f'{jmeno_druhy_uz=}')
    # print(f'{hodnoceni_prvni_uz=}')
    # print(f'{hodnoceni_druhy_uz=}')

    ## porovnani spolecnych filmu pro aktivniho uzivatele a zbytek uzivatelu
    ## udelam prunik obou uzivatelu s aktivnim uzivatelem abych videl, jake filmy maji spolecne
    spolecni_prvni_uziv = aktivni_uzivatel.intersection(hodnoceni_prvni_uz)
    spolecni_druhy_uziv = aktivni_uzivatel.intersection(hodnoceni_druhy_uz)
    # print(f'{spolecni_prvni_uziv=}')
    # print(f'{spolecni_druhy_uziv=}')

    ## porovnavam, jestli prvni uzivatel ma vetsi pocet spolecnych filmu nez druhy (vuci aktivnimu uzivateli)
    if len(spolecni_prvni_uziv) > len(spolecni_druhy_uziv):
        nejvice_spolecnych = uzivatele[jmeno_prvni_uz]
    
    elif len(spolecni_prvni_uziv) < len(spolecni_druhy_uziv):
        nejvice_spolecnych = uzivatele[jmeno_druhy_uz]
    
    elif len(spolecni_prvni_uziv) == len(spolecni_druhy_uziv):
         nejvice_spolecnych = uzivatele[jmeno_druhy_uz].union(uzivatele[jmeno_prvni_uz])
    # print(f'{nejvice_spolecnych=}')

    ## doporuc film podle rozdilu shlednutych od akt. uzivatele a nejvice shodnych filmu
    print(f"Oblibene filmy akt. uzivatel: {aktivni_uzivatel}")
    print(f"Nejvice spol. oblibenych filmu: {nejvice_spolecnych}")

    navrhy = set(nejvice_spolecnych).difference(aktivni_uzivatel)
    print(f"Navrhuji filmy: {navrhy}" if navrhy else "Nemam pro tebe zadny film")

else:
    print("SLUZBA NENI DOSTUPNA!")