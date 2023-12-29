print("Naučili jsme se psát věci do stringu")
print('Spojení stringu děláme pomocí znaménka "+"')
print("Také jsme používalí print('nějaký text')")
print("První řádek\nDruhý řádek se dělá pomocí lomítka a n")

input("Zadejte své jméno")
# input umožňuje zadávání čehokoliv od uživatele
print("Ahoj, já jsem " + input("Zadejte své jméno\n"))

# proměnné - slouží k uchovávání hodnot
name = input("Jaké je tvé jméno?\n")  # do proměnné uložíme funkci input s
                                      # argumentem 
print("Ahoj, já jsem " + name)   # vytiskneme string společně s proměnnou 

city = input("V jakém městě bydlíte?\n")  # Další příklad input a print funkce
print("Bydlím ve městě " + city )

print(len("Ahoj Debile"))  # funkce len vypíše počet znaků včetně světlých  
name = input("Zadejte své jméno\n")

lenght = len(name)
print(name)
print(lenght)

# Kratší verze

lenght = len(input("Zadejte své jméno\n"))
print(lenght)

# Proměnné - nepovolené znaky

# 3pepa = Martin
# Nam8 = "Martin"
# P = "pepa"
# J = "josef"
# print(P,J)

print("Výtejte v aplikaci na generování vtipných jmen")    # ukol na generovaní vtipných
name = input("Jaké je tvoje křestní jméno?\n")             # jmen
vlastnost = input("Jaká je tvá typická vlastnost? Napiš ji s velkým písmenem\n")
print("Tvoje vtipné jméno je " + name + " " + vlastnost)

# Základní datové typy

# String
print("ahoj"[2])
print("10" + "15")
print("ah" + "oj")

# Integer

print(10+15)  # nepíší se uvozvky
print(123456)
print(123_456)

# FLoat - desetinné číslo
print(3.14)

# Boolean - funkce, která ověří prvadu nebo ne
print(5>2)

age = 40
print(type(age))

weight = 90.7
print(type(weight))

live = True
print(type(live))

name = "Martin"
print(type(name))

str() # převádí na tyo string
int() # převádí na typ integer
bool() # převádí na typ boolean
float() # převádí na typ float

age = 40                   # atribut je typem int
print(type(age))           # vytiskne typ proměnné
age = str(40)              # proměnné převedená na string
print(type(age))           # vytištění typu
print("Ahoj, já jsem Martin a je mi " + str(age) + " let")


number = input("Napište dvoumístné číslo:\n")
sum = int((number)[0]) + int((number)[1]) # proměnná, skládá se z definování čísel a 
print(sum)                                # součtu jejich definicí.
                                          # vytištění  výsledné proměnné


# Matematické operace
print(5 + 2)
print(5 - 3)
print(4 * 3)
print(10 / 2)    # Dělení vždy končí floatem
print(2**3)      # mocnění

#  Priority

# ()
# **
# / *
# + -
 
print(5 * 2 + 6 / 3 -5) # Vrací nám float, kvůli znaménku "/"
print(10 + 2 -5)        #Vrací nám integer



# Vypočítejte BMI, který se počítá jako:
# BMI = váha v kg / (výška v m) na²

height = input("Zadejte svoji výšku v metrech:\n")   # hodnoty jsou zadány jako string
weight = input("Zadejte svoji váhu v kilogramech:\n")

bmi = int(weight) / (float(height)**2)   # musíme převést ze stringu na integer a float
bmi = int(bmi)                           # výsledek bude v int
print("Vaše BMI je: " + str(bmi) +".")   # tisk výstupu plus hodnota ve  



print(8 / 3)  
print(7 // 3)               # znak // taky zaokrouhlí na celé číslo
print(5.0002 / 2)
print(int(8 / 3))           # Číslo vyjde bez desetinné čárky 
print(round(8 / 3))         # zaokrouhlení
print(round(8 / 3 , 2))       # round(* / * , 2) - vypíše nám číslo na dvě des. místa

x = 1
x = x + 1      # x += 1       
x = x - 1      # x -= 1
x = x * 2      # x *= 2

print(x)


# F - string
x = 5
print(f"Proměnná x má hodnotu {x}")

name = "David"
age = 35.5
print(f"Jmenuje se {name} a je mu {age} let. ")



# Pokud vám zadavatel zadá, kolik je mu let, tak tak mu vypíšete:
# Zbývající počet let, měsíců, týdnů, dnů. Všechno za použití jedné f-string věty.





age = int(input("Jaký je tvůj věk?\n"))
remain = 75 - age 
months = 12 * remain
weeks  = 52 * remain
days = 365 * remain

print(f"Zbývá ti: {days} dnů,\n{weeks} týdnů,\n{months} měsíců,\nrespektive {remain} let života.")





# Výpoče na procenta

print("Výtejte v aplikaci na výpočet plateb\n")

bill = float(input("Kolik korun máte celkem zaplatit?\n"))
tip =  float(input("Jaká bude výše Vašeho spropitného v %?\n"))
peoples = int(input("Mezi kolik lidí se má rozdělit částka?\n"))

print(f"Každý člověk musí zaplatit: {round((bill + bill // 100 * tip) // peoples)} Kč\n")

### nebo verze se zaokrouhlovacím formatem na dvě des. čísla

print("Výtejte v aplikaci na výpočet plateb\n")

bill = float(input("Kolik korun máte celkem zaplatit?\n"))
tip =  float(input("Jaká bude výše Vašeho spropitného v %?\n"))
peoples = int(input("Mezi kolik lidí se má rozdělit částka?\n"))
Finally_paymant = "{:.2f}" .format((bill + bill / 100 * tip) / peoples)
print(f"Každý člověk musí zaplatit: {Finally_paymant} Kč\n")

# Zokrouhlený výslede bez des. čísel {round((bill + bill / 100 * tip) / peoples, )}
#                                    {round((bill + bill // 100 * tip) // peoples, )}






# Příklad s horskou dráhou

print("Vítejte na horské dráze")  
height = int(input("Jaká je Vaše výška v cm?\n"))

if height >= 87:                     # podmínka - když větší nebo rovno 87 tak povolí
    print("Můžete jet na horské dráze")   
else:                                 # menší nebo jiné řešení - nepovolí
    print("Omlouváme se, ale na horské dráze jet nemůžete")


########################################################################################



# Příklad dospělosti

# Podmínky - procvičování
age = int(input("Dobrý den, jaký je Váš věk?\n"))

if age >= 18:
    print("Super, už jste dospělý")
else:
    print("Omlouváme se, ale ještě budete muset počkat.")

price = (input("Jste student? odpovězte ano/ne\n"))
if price == "ano":
    print("Vaše cena je 120 Kč.")

else:
    print("Vaše cena je 150 Kč")
    
## využití proměnných ####################################################################################

price = 150
price_student = 120
student_q = input("Jste student?\nOdpovězte ano/ne.")

if student_q == "ano":
    print(f"Cena lístku je {price_student} Kč.")
else: 
    print(f"Cena lístku je {price} Kč.")


########################################################################################



# Podmínky - normal, smart, extrasmart
type = input("Jaký budete chtít typ mobilního telefonu?\nMožnosti jsou: normal, smart, extrasmart\n")

if type == "normal":
    print(f"Cena telefonu typu {type} je 15.000 Kč")
else:
    print(f"Cena telefonu typu {type} je 25.000 Kč")   


########################################################################################



print("Vítejte na horské dráze")  
height = int(input("Jaká je Vaše výška v cm?\n"))

if height >= 87:                     
    print("Můžete jet na horské dráze")      
    age = int(input("Jaký je váš věk?\n"))  
    if age < 18:
        print("cena Vašeho lístku je 100Kč \n")
    else:
        print("Cena Vašeho lístku je 150 Kč\n")    
else:                                
    print("Omlouváme se, ale na horské dráze jet nemůžete") 



########################################################################################



    # Elif spojení funkce else a if, dává se ještě jako dělení další podmínky
print("Vítejte na horské dráze")  
height = int(input("Jaká je Vaše výška v cm?\n"))

if height >= 87:                     
    print("Můžete jet na horské dráze")     
    age = int(input("Jaký je váš věk?\n"))  
    if age < 12:
        print("cena Vašeho lístku je 50 Kč\n")
    elif age < 18:
        print("Cena Vašeho lístku je 100 Kč\n")    
    else:
        print("Cena Vašeho lístku je 150 Kč\n")
    
    
    else:                                
    print("Omlouváme se, ale na horské dráze jet nemůžete") 


  ########################################################################################  ############




    
    # Elif spojení funkce else a if, dává se ještě jako dělení
print("Vítejte na horské dráze")  
height = int(input("Jaká je Vaše výška v cm?\n"))
bill = 0 
if height >= 87:                     
    print("Můžete jet na horské dráze.")     
    age = int(input("Jaký je váš věk?\n"))  
    if age < 12:
        bill = 50 
        print("cena Vašeho lístku je: 50 Kč.")
    elif age < 18:
        bill = 100 
        print("Cena Vašeho lístku je: 100 Kč.")    
    else:
        print("Cena Vašeho lístku je: 150 Kč.")
        bill = 150   
    photo = input("Chcete během jízdy vyfotit? ano nebo ne?\n")       
    if photo == "ano":
       bill = bill + 40    # bill += 40
       print(f"Vaše celková cena lístku je {bill} Kč.")      
    else: 
        photo == "ne"
        print(f"Vaše cena lístku je: {bill} Kč.")   
        
else:                                       
    print("Omlouváme se, ale na horské dráze jet nemůžete.") 







# Výpočet BMI
height = float(input("Vložte svoji výšku v metrech: "))
weight = float(input("Vložte svoji váhu v kilogramech: "))

bmi = weight / height**2
print(f"Vaše BMI je: {round(bmi, 1)}")

if bmi < 18.5:
   print("Máte podvýživu, musíte začít jíst!") 
elif bmi < 24.9:
   print("Gratulujeme! Máte perfektní váhu!")
elif bmi < 29.9:
   print("Bohužel máte mírnou nadváhu.") 
elif bmi < 34.9:
   print("Upozornění, trpíte obezitou!") 
elif bmi > 35:
   print("Nebezpečí zdravotních rizik! hejbej se bečko!")  






 ###  APLIKACE NA ZJIŠTĚNÍ, ZDA JE ROK PŘESTUPNÝ: ###

print("Je tento rok přestupný?")
year = int(input("Zadejte rok:\n"))

if year % 4 == 0 and not year % 100 == 0 :  # pokud je prom. dělitelná 4 a není 100 beze zbytku.
    print("Leap year (přestupný rok.)")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap year (přestupný rok.)")
else:
    print("Not a leap year (není přestupný rok.)")

#### Další řešení ###

year = int(input("Zadejte rok a zjistěte, zda je přestupný:\n"))
if year % 4 == 0:
   if year % 100 == 0:
     if year % 400 == 0:
         print("Váš rok je přestupný.")
   else:
       print("Váš rok je přestupný.")
else:
     print("Váš rok není přestupný.") 







     # pizza = str(input("Dobrý den, jak velkou pizzu byste si přál? S, M, L?:\n"))


# if pizza == "S":
#    bill = 100
   
#    spicy = str(input("Budete si přát na pizzu feferonky?\n"))
   
#    if spicy == "ano":
#       bill += 20
      
#    cheese = str(input("Budete chtít pizzu posypat sýrem?\n"))
      
#    if cheese == "ano":
#       bill += 15

#       print(f"Váš účet za pizzu je: {bill} Kč ")    
#    else:
#        print(f"Váš účet za pizzu je: {bill} Kč.")      

# elif pizza == "M":
#      bill = 150
   
#      spicy = str(input("Budete si přát na pizzu feferonky?\n"))
   
#      if spicy == "ano":
#         bill += 30
      
#      cheese = str(input("Budete chtít pizzu posypat sýrem?\n"))
      
#      if cheese == "ano":
#         bill += 15

#         print(f"Váš účet za pizzu je: {bill} Kč ")    
#      else:
#         print(f"Váš účet za pizzu je: {bill} Kč.") 
      
# elif pizza == "L":   
   #   bill = 200
   
   #   spicy = str(input("Budete si přát na pizzu feferonky?\n"))
   
   #   if spicy == "ano":
   #      bill += 30
      
   #   cheese = str(input("Budete chtít pizzu posypat sýrem?\n"))
      
   #   if cheese == "ano":
   #      bill += 15

   #      print(f"Váš účet za pizzu je: {bill} Kč ")    
   #   else:
   #      print(f"Váš účet za pizzu je: {bill} Kč.") 
      
   #### Další řešení










pizza = str(input("Dobrý den, jak velkou pizzu byste si dal? S, M, L?:\n"))
spicy = str(input("Chcete na tu pizzu chilli? ano nebo ne?\n"))
cheese = str(input("Dáte si na pizzu sýr?\n"))   
wrap = str(input("Chcete pizzu zabalit?\n"))
drink = str(input("Dáte si k tomu něco na pití? Máme kolu, sprite, mirindu.\n"))

bill = 0

if pizza == "S":          # není potřeba psát do pavouku, stačí podmínky pod sebe
    bill += 100
elif pizza == "M":   
      bill += 150
elif pizza == "L":   
      bill += 200

if spicy == "ano":                  #  pálivost
   if pizza != "S":
       bill += 30
   if pizza == "S": 
       bill += 20

if cheese == "ano":                  # sýr
     bill += 15

if wrap == "ano":                    # zabaleni
    if pizza != "S": 
     bill += 20  
    if pizza == "S":
     bill == 10


if drink == "kolu":                  # testování.. pití
    print(f"Celková cena za nákup je {bill} Kč.")
elif drink == "sprite":
   bill += 50 ; print(f"Celková cena za nákup je {bill} Kč.")
elif drink == "mirindu":
   bill += 55 ; print(f"Celková cena za nákup je {bill} Kč.")   

else:   
     print(f"Celková cena za pizzu je {bill} Kč.")     








# logický operátory

a and b   
true and true = True     # pokud platí to a to, je to pravda
true and false = False   # pokud jedno platí ale druhé ne, tak je to nepravda
false and true = False   
false and false = False


a or b
true or true = True     # pokud plati to nebo to, je to true
true or false = True    
false or true = True
false or false = False

negace = not

not true = False
not false = True







#### POUŽITÍ LOGICKÝCH OPERÁTORŮ

print("Vítejte na horské dráze")  
height = int(input("Jaká je Vaše výška v cm?\n"))
bill = 0 

if height >= 87:                     
    print("Můžete jet na horské dráze.")     
    age = int(input("Jaký je váš věk?\n"))  
    if age > 0 and age < 12:
        bill = 50 
    elif age > 12 and age < 18:
        bill = 100 
    elif age > 40 and age < 50:
         bill = 0       
    else:
         bill = 150   
    photo = input("Chcete během jízdy vyfotit? ano nebo ne?\n")       
    if photo == "ano":
       bill = bill + 40    # bill += 40
       print(f"Vaše celková cena lístku je {bill} Kč.")      
    else: 
        photo == "ne"
        print(f"Vaše cena lístku je: {bill} Kč.")   
        
else:                                       
    print("Omlouváme se, ale na horské dráze jet nemůžete.")








print('''
       _
                           /b_,dM\__,_
                         _/MMMMMMMMMMMm,
                        _YMMMMMMMMMMMM(                   
                       `MMMMMM/   /   \   _   ,    
                        MMM|  __  / __/  ( |_|
                        YMM/_/# \__/# \    | |_)arry
                        (.   \__/  \__/     ___  
                          )       _,  |    '_|_)
                     _____/\     _   /       | otter
                         \  `._____,'
                          `..___(__
                                   ``-.
                                       \
                                   gnv  )
''')                                                                                 #. lower() nám převede text z inputu na mala písmena
print("Výtejte v Bradavicích milí studenti,\nNyní se vypravíte do svých kolejí.")
  
follow = str(input("Následovat spolužáky do sve nebelvírské koleje? Ano nebo Ne.\n")).lower()

if follow == "ne":
    way = str(input("Odpojili jste se od svých spolužáků a stojíte sami na chodbě.\nChcete se vydat doprava nebo doleva?\n")).lower()
    if way == "doleva":
       print("Narazili jste na flinche, ten vás poslal do komnaty spát.") 
    if way == "doprava":
       print("Došli jste k dolů až ke dveřím ke sklepení.") 
if follow == "ano":
   stairs = str(input('''Jdete po samohybných schodech se spolužáky nahorou do komnat. Došli jste do nebelvírské společenské místnosti.
Chcete tu zůstat nebo jít po schodech do své ložnice? Napiště zůstat nebo jít.\n''')).lower() 
   if stairs == "zůstat":
      stay = print("Zůstáváte v místnosti a jíte s kamarády Jelly Belly, Ron se málem pozvracel a Hermiona se smála ja pominutá.")   
   if stairs == "jít":
      print("dostali jste se do své ložnice, jdete spát společně se svými kamarády.")   



##########################################################################################################################################
#          ############################################## Import čísel  #########################################################



# modul - slouží na importování z modulu 
import new_modul

import random
 
#  # Generování náhodného celého čísla z rozmezi
print(random.randint(10,20))  
 
# # Generování náhodného desetiného čísla + zaokrouhlení na 2 des čísla
print(round(random.random(),2)),

# # Generování náhodného číslo z rozmezí + krok
print(random.randrange(15, 20, 2))

print(random.randint(1, 20))            #  20                              / náhodné číslo mezi 1 a 20 inclusive                \
print(random.randrange(20))             #  18                              \ náhodné číslo mezi 1 a 20 / bere index 0 až do 19  /

print(random.randrange(1, 21, 2))       #  4                                 náhodné číslo mezi 1 a 21, ale po dvou krocích   

print(random.uniform(1, 10))            #  9.411010847849195                 náhodné desetinné číslo v intervalu 1 - 9,999999999999999999

print(random.random())                  #  0.6356792428014956                náhodné desetinné číslo v intervalu 0 - 1

print(round(random.random(), 2))        #  0.29                              náhodné desetinné číslo v intervalu 0 - 1, zaokrouhléné na dvě desetiná čísla.

print(round(random.uniform(1, 10), 3))  # 1.429                              náhodné desetinné číslo v intervalu 1 - 9,99.... zaokr. na 3 des. čís.

print(random.sample([10, 20, 30, 40, 50], k=2))      # [50, 40]              náhodně vybere ,,k" prvků z listu


import math 
print(math.ceil(5.1))  # zaokrouhlí celé číslo nahoru - 6
print(math.floor(5.1)) # zaokrouhlí celé číslo dolu - 5


import random
import math

print(math.ceil(random.random() * 6))                                        print(random.randint(1, 6))
print(math.ceil(random.random() * 6))                                        print(random.randint(1, 6))
print(math.ceil(random.random() * 6))            kratší verze:               print(random.randint(1, 6))
print(math.ceil(random.random() * 6))                                        print(random.randint(1, 6))
print(math.ceil(random.random() * 6))                                        print(random.randint(1, 6)) 
print(math.ceil(random.random() * 6))                                        print(random.randint(1, 6))




 ######################################## HLAVA NEBO OREL ######################################################

import random
coin = ((random.randint(1,2))) 
if coin == 1:
  print("Hlava")
else:
  print("Orel")   
# simpler option:
import random   
print(random.choice(['win', 'lose', 'draw']))      # Single random element from a sequence


##################################################################################################################################################



                                                                # list  []
#  - neboli seznam, který nám umožňuje uložit do proměnné více hodnot, čísel nebo funkcí:

Using a pair of square brackets to denote the empty list: []
Using square brackets, separating items with commas: [a], [a, b, c]
Using a list comprehension: [x for x in iterable]
Using the type constructor: list() or list(iterable)

print(list('abc'))          ->         #    ['a', 'b', 'c']
print(list( (1, 2, 3) ))    ->         #    [ 1, 2, 3]


employees = ["David" , "Harry",  "Ron"]
print(employees[0])
print(employees[1])
print(employees[2])

# mění položku
employees[1] = "Hermiona"
print(employees)

# přidáváme obsah # . append - přidá položku na konec o jednu navíc
 
employees.append("Harry")
print(employees)

# přidáváme více položek
employees.extend(["Crabbe, Goyle"])

# Odstraňujeme položku 
employees.remove("Ron")
print(employees)









import random

names = input("Napiš mi všechna jména oddělena čárkou.\n") # proměná s inputem

list_peopple = names.split(", ")  # list obshající proměnou, která prvky oddělí čárkou.

random_number = random.randint(0, len(list_peopple)-1) #  Další proměná, která má funkci random, která ze seznamu vybere prvek díky jejímu indexu,
                                                       #  od nuly až na konec len
                                                       # .Musí být minus jedna, protože se index počítá od jedné

print(f"{list_peopple[random_number]} bude dnes platit účet.")


 ######################################################   lepší verze: ##################################x

import random

names = input("Napiš mi všechna jména oddělena čárkou.\n") #    proměná s inputem

list_peopple = names.split(", ")                       #   list obshající proměnou, která prvky oddělí čárkou.
                                                        #     list obsahující proměnou, která prvky oddělí čárkou. Musí to tak být, jinak by funkce random.choice vybírala pouze
                                                        #        písmenka
random_people = (random.choice(list_peopple))        #           Další proměná, která má funkci random.choice, vybere náhodně prvek ze seznamu list_people
                                                      
print(f"{random_people} dnes bude platit účet.")




##########################################################################################################################


Index Erorr
gryffindor = ["David", "Harry", "Ron", "Hermiona"]
slytherin = ["Draco", "Crabe", "Goyle"]

number = len(gryffindor)   # uložení do proměnné délku, počet prvků, Funkce len nám vrátí počet položek, délku objektu.
                            # print(gryffindor[1])  # 


# Nasted list # vnoření, spojí nám dva objekty, např. listy

students = [gryffindor, slytherin]
print(students[0][0])     # vypíše nám z prvního seznamu s indexem 0, prvek č. 0 - David
print(students[1][2])     # vypíše nám z druhého seznamu s indexem 1, prvek s indexem 2 - Goyle
print(students)           # vypíše oba seznamy v proměnné students







set1 =["🤡", "🤡", "🤡"]  
set2 =["🤡", "🤡", "🤡"]                                 # tři různé seznamy - listy
set3 =["🤡", "🤡", "🤡"]  

all_sets = [set1, set2, set3]                              # proměnná, co obsahuje více listů

print(f"{set1}\n{set2}\n{set3}")                             # tisk seznamů

position = input("Zadejte souřednice oddělené čárkou:\n")   # zadejte souřednice
position_con = position.split(",")                           # proměnná která obsahuje dva oddělené prvky

all_sets[int(position_con[0])][int(position_con[1])]=("👾") # proměnná all_sets, která obsahuje již seznam listů,
                                                             # ještě nově obsahuje na vložených pozicích nového panáčka

print(f"{set1}\n{set2}\n{set3}")



   


             
              ####           KÁMEN, NŮŽKY, PAPÍR     ###


choice =int(input("Výtejte ve hře na kámen, nůžky papír.\nNa začátek si vyberte: 1 - kámen, 2 - nůžky, 3 - papír.\n"))
 
if choice == 1:  
   print("Vybral/a jste si kámen.\n"
      '''
        _____
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___)
   ''')
if choice == 2:
     print("Vybral/a jste si nůžky.\n"
     '''
        _____
   ---'   ___)_____
             ______)
          __________)
         (____)
   ---.__(___)
   
   ''')
if choice == 3:
     print("Vybral/a jste si papír.\n"   
          '''
     ______
 ---'   ___)_____
         ________)
         _________)
         _______)
 ---.__________)
 ''') 
     
import random
coin = ((random.randint(1,3))) 
if coin == 1:
  print("Počítač si vybral: Kámen\n"
        '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
        )
elif coin == 2:
  print("Počítač si vybral: Nůžky\n"
         '''
    _____
---'   ___)____
          ______)
       __________)
      (____)
---.__(___)
'''
)  
else:
     print("Počítač si vybral: Papír\n"
           
           '''
    _____
---'   ___)____
          ______)
          _______)
         _______)
---.__________)
'''
)  


if choice == 1 and coin == 1:
    print("Remíza, hrajte znovu.")
elif choice == 1 and coin == 2:
    print("Kámen tupí nůžky, Vyhrál jste.")
elif choice == 1 and coin == 3:
    print("Papír balí kámen, prohrál jste!")

if choice == 2 and coin == 1:
    print("Prohrál jste, nůžky tupí kámen!")
elif choice == 2 and coin == 2:
    print("Remíza, hrajte znovu.")    
elif choice == 2 and coin == 3:
    print("Vyhrál jste, nůžky stříhají papír")


if choice == 3 and coin == 1:
    print("Vyhrál jste, papír balí kámen!")
elif choice == 3 and coin == 2:
    print("Prohrál jste, nůžky stříhají papír.")    
elif choice == 3 and coin == 3:
    print("Remíza, hrajte znovu.")
 



 #########                 Druhá verze za použití listu + import pro hru znova ######

import random
 
rock = ('''
Kámen:\n
        _____
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___)
   ''')
scissors = ('''
Nůžky:\n
        _____
   ---'   ___)_____
             ______)
          __________)
         (____)
   ---.__(___)
   
   ''')
paper = ( '''
Papír:\n
     ______
 ---'   ___)_____
         ________)
         _________)
         _______)
 ---.__________)
 ''') 
     
all_list = [rock, scissors, paper]

user_choice = int(input("Vítejte ve hře na kámen, nůžky papír.\nNa začátek si vyberte: 0 - kámen, 1 - nůžky, 2 - papír.\n"))
user_picture = all_list[user_choice]   # zadavatel nám vybere ze seznamu listů danný list. 0, 1, 2
 
computer_choice = random.randint(0,2)    # vložení modulu na generování náhodných čísel.
computer_picture = all_list[computer_choice]  # počítačem vybrané číslo nám vybere prvek ze seznamu listů 

print(f"Uživatel si vybral:\n {user_picture}")      # tisk vybraných hodnot
print(f"Počítač si vybral:\n {computer_picture}")
                                                        # Zadání podmínek
if user_choice == computer_choice:    
    print("Remíza, hrajte znovu")
    import Kamen_nuzky_papir                                             # Zadání podmínek
elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 0 and computer_choice == 2:            
   print("Vyhrál jste!")
                                                   # Zadání podmínek
elif user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 0:
   print("Prohrál jste!")

 
next = input("Chceš pokračovat? Y/N\n")       # otázka, jestli chci hrát znovu.
if next == "Y" or "y":
   import Kamen_nuzky_papir     #Kamen_nuzky_papir je název souboru, v kterém je hra napsaná :)
else:
    print("Konec hry.")







###############################               Cyklus For            ##################################################################


fruits = ["Apple", "Pear", "Orange", "Strawbbery"]

for one_fruit in fruits:  # postupně projíždí proměnnou fruits, vezme první prvek, jelikož
                          # jsme zadali tisk, tak ho vytiskne. A znova další prvek až na 
    print(one_fruit)       # konec  
    print(f"Nezapomeň koupit: {one_fruit}.")    # další funkce na print
    print(F"Znova říkám: {one_fruit}!")






#########                     CYKLUS FOR PODRUHÉ       ############


heights = input("Vložte výšky lidí v cm, oddělené čárkou a mezerou\n")  
height_people = heights.split(",")  # zadané čísla patří do nového seznamu, oddělený čárkou,
                                     
total = 0                           # proměnná, která nám bude operovat, přičítat atd..

for one_height in height_people:        # projíždí proměnnou heigt_people, najde číslo, přidá ho
    total += int(one_height)             # k totalu dokola je přičteno káždé číslo  
    avarage = total / len(height_people) # do avarage je každou smyčkou přiřazeno číslo lomeno počtem číslic

print(f"Průměrná výška je: {round(avarage, 2)} cm .")   





############### největší max, nejmenší min. funkce for, převedení str na int a zalistování do seznamu########

# # Nejvyšší skóre v testu
score = [98, 50, 25, 78, 92]
print(max(score))
print(min(score))

###############################################################################################
score = input("Zadejte score studentů oddělené čárkou a mezerou\n")  # Zadání atributů
score_list = score.split(", ")                                      # oddělení hodnot a zadání do proměnné
score_list_number = []                                              # vytvoření listu

for index in range(0, len(score_list)):                             #vytváření něčeho u rozsahu - range- od nuly 
    score_list_number.append(int(score_list[index]))          # do len (počet atributu v proměnné score_list)
                                                               # postupně přidává vstupní str ze score_list do
print(score_list_number)                                           # seznamu score_list_number                                                                    





########################## range - funkce for funguje i bez listu###################################xx

for one_number in range(1, 5):   # vypíše hodnoty postupně mimo poslední hodnotu: konkrétně u tohoto příkladu - 5
    print(one_number)

# ###########################range s kroky#################################xx
 
for one_number in range(1, 11, 2):   # Vybírá kroky po dvou / dá se použít pro vyjmenování lichých čísel
    print(one_number)


################################################ suma čísel #############################################################################################
 
1 + 2 + 3 .... + 99 + 100     
100 + 99 + 98 .... 2 + 1 

100 * 101 / 2 = 5050    



suma = 0


for one_number in range(1, 101):
    suma += one_number

print(suma)

#####################################################################################################

##                  Sečtěte včechna sudá a lichá čísla od 1 do 100                ######################
#### lichá čísla: ####
                                     
suma = 0

for one_number in range(1, 100, 2):          #  součet čísel  1 - 99 
    suma += one_number

print(suma)

## suda Čísla:  

suma_suda = 0

for one_number in range(0, 101, 2):
    suma_suda += one_number

print(suma_suda)


####################################################################################################################


                                        # HRA FIZZ - BUZZ

####################################################################################################################

#   když je číslo dělitelné 3 a 5, piš fizzbuzz
#   když je číslo dělitelné 3 = Fizz
#   když je číslo dělitelné 5 = Buzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


####################################################################################################################



#Dodatek k funkci for

# postupně nám vypíše všechny hodnoty, není třeba indexovat

my_name = "Martin" 
myList = [1, 2, 4334, True]

for one_letter in my_name:
    print(one_letter)
            #X#
for one_atribut in myList:
    print(one_atribut)
    



####################################################################################################################


##############           Generátor náhodných hesel 1          ###

import random
print("------------GENERÁTOR HESLA----------------")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_char = [ '%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

number_of_letters = int(input("Kolik písmen chcete mít ve svém heslu:\n"))
number_of_numbers = int(input("Kolik čísel chcete mít ve svém heslu:\n"))
number_of_special_chars = int(input("Kolik speciálních znaků chcete mít ve svém heslu:\n"))

password = []

for index in range(number_of_letters):       # počet písmen je dán range
    password.append(random.choice(letters))  # do listu password přiřadí random vybraný prvek z listu letters

for index in range(number_of_numbers):       # počet čísel je dán range     
    password.append(random.choice(numbers))  # do listu password přiřadí random vybraný prvek z listu numbers

for index in range(number_of_special_chars):     # počet speciálních znaků je dán range
    password.append(random.choice(special_char)) # password přiřadí random vybraný prvek z listu special char

    ## funkce choice, která bere náhodnou proměnnou z rozsahu

def List2strings(): #  převod listu na string 
    str1 = " " 
    return (str1.join(password))



print(f"Vaše vygenerované heslo: - {List2strings()} -")

# nebo jinačí konec: převod listu na string.

result_password = " "

for one_piece in password:
    result_password += one_piece

print(f"Vaše výsledné heslo:{result_password}")


  


 ##################################################### CYKLUS WHILE ############################################################

# příkaz while se vykonává tak, že se nejprve vyhodnotí vstupní podmínka, a je-li pravdivá, provede se tělo cyklu a běh programu se vrací na test vtupní
# podmínky. Tělo příkazu se opakovaně provádí tak dlouho, dokud je vstupní podmínka pravdivá.

x = 0

while x <= 10:                         # takto je cyklus nekonečný, podmínka stále platí a nic se nemění.
    print(f"Já jsem cyklus {x}.")


while x <= 10:
    print(f"Já jsem cyklus {x}.")     # k příčítáním hodnoty se už počet cyklů omezí.
    x += 1




### Hádací hra: ###

character = "Harry"
guess = "" # prvně se píše prázdý string, aby se první cyklus vykonal

while character != guess:  
    guess = input("Uhádněte postavu z filmu Harry Potter.\n")   # pokud je odpověď false, tak podmínka je true a vykoná se cyklus

print("Uhádli jste, výborně!")                                  # pokud je odpověď true, tak podmínka je false a vyprintuje se konec hry



#### Další verze hry:
# character nyní nebude předem dán, ale bude záviset na nádném výběru.

import random 

characters = ["Ron", "Hermiona", "Harry", "Draco", "Snape", "Voldemort", "Albus"]
character = random.choice(characters)      # náhodný generátor
guess = ""

while character != guess:
    guess = input("Uhádněte postavu u Harryho Pottera.\n")

print("Uhádli jste, výborně!\n")
  

#### Další verze hry:
  
import random 

print("Vítejte ve hře na uhodutí postavy,")

characters = ["Ron", "Hermiona", "Harry", "Draco", "Snape", "Voldemort", "Albus"]
character = random.choice(characters)      # náhodný generátor
guess = ""
guess_count = 5    # počítadlo na počet pokusů

while character != guess:
    if guess_count != 0:
       guess = input("Uhádněte postavu u Harryho Pottera.\n")
       guess_count -= 1
    else:
        print("Vyčerpali jste počet pokusů.\n")      # když se počítadlo dostane na nulu.
        break 
    
    if character == guess: 
        print(f"Uhádli jste!! Hádané slovo bylo {character}!")    # když uhádneme. 

########################################################################################################################################

# Hangman
     














        ######################## FUNKCE   #########################
 #     

  # Funkce
 

# Předpřipravená funkce:    
 #y = x + 1 
print("Ahoj")
number_character = len("Ahoj")
print(number_character)

# vlastní funkce:
def my_function():
    if 5 == 5:
        print("Je to číslo pět")
    else:
        print("Není to číslo pět")     



my_function()



        ######################## FUNKCE S PARAMETREM   #########################


def greet_name(name):             # (name) - argument
    print(f"Já jsem {name}")

greet_name("Martin")              # (martin) - parametr 
greet_name("Harry")  
greet_name("Hermiona")  

# funkce s více parametry:

def greet(name, location):
    print(f"Ahoj, já jsem {name} a pocházím z vescnice {location}.")

# positional arguments - závisí na pořadí
greet("Martin", "Rácov")

# keyword arugumens - nezávísí na pořadí
greet(location="Tábor", name="Martin")



###############################################################################################
   #              Příklad na výpočet  kusů barvy plechovky

import math
wall_h = int(input("Výška stěny v m: "))
wall_w = int(input("Šířka stěny v m: "))
coverage = 5

def paint_calculator(width, height, cover):
    area = width * height
    number_can = math.ceil(area / 5)
    print(f"je potřeba koupit: {number_can} kusů.")
    
paint_calculator(width=wall_w, height=wall_h, cover=coverage)




###############################################################################################

# prvočíslo

def prime_number_checker(number):
    result = "je to prvočíslo"
    for one_number in range(2, number):
        if number % one_number == 0:
            result = "Není to prvočíslo"
    print(result)         




n = int(input("Zadejte prosím číslo: "))
prime_number_checker(n)

################################################################################################################################
######################################################################################################################################

# Dictonary - slovník 
#        key :  Value

it_dictionary = {
    "String": "Text",
    "Integer": "Celé číslo",
    "Float": "Desetinné číslo",
    "Boolean": "Pravda" "Neprava"

}

print(it_dictionary["String"])
print(it_dictionary["Float"])


it_dictionary_two = {
     1 : "Text",
     2 : "Celé číslo",
     0 : "Desetinné číslo",
     3  : "Pravda" "Neprava"
}    

print(it_dictionary_two[0])    
print(it_dictionary_two[1])
print(it_dictionary_two[2])
                                                    
it_dictionary_two[4] = "Uložení více hodnot"    # Přidání hodnot do dictionary  

print(it_dictionary_two[0])    
print(it_dictionary_two[1])
print(it_dictionary_two[2])
print(it_dictionary_two[4])

# nastavení prázdného dictionary
empty_dictionary = {} 

# Vyprázdnit dictionary
it_dictionary_two = {}

# Měnínm hodoty v dictionary
it_dictionary_two[1] = "Textová hodnota"
print(it_dictionary_two)


# Dictionary a cyklus

it_dictionary = {
     "String": "Text",
     "Integer" : "Celé číslo",
     "Float" : "Desetinné číslo",
     "Boolean"  : "Pravda" "Neprava"

}

for key in it_dictionary:          
   print(key)                            # vypíše key - levou část slovníku
   print(it_dictionary[key])             # vypíše - vylue



