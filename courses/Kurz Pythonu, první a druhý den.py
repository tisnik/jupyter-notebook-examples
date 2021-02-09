# vim: set fileencoding=utf-8

#
#  (C) Copyright 2020  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# coding: utf-8

# # Kurz Pythonu

# ## První den

# In[145]:


# výrazy se přímo vyhodnotí a vypíše se jejich výsledek
1 + 100


# In[146]:


# funkce print vypíše hodnotu vypočteného výrazu
print(1)
print(1 + 2)

# použití proměnných
x = 5
print(x)


# In[147]:


# složitější aritmetický výraz
y = 2 * x + 3
print(y)


# Nyní se budeme snažit vypočítat Pi

# In[148]:


"""Toto je dokumentační řetězec."""


# In[149]:


# if je klíčové slovo a nejde použít pro jméno proměnné
if = 3


# In[150]:


# vytvoření proměnných různých typů
x = 42
y = "Python"
z = 3e27

print(x)
print(y)
print(z)

x = None
print(x)

x = 10
print(x)

x = "něco jiného"
print(x)


# In[151]:


# vymazání proměnné z paměti
del x


# In[152]:


# vytvoření seznamu se třemi prvky
s = [1, 2, 3]


# In[153]:


# seznam je heterogenní - může obsahovat hodnoty libovolného typu
s2 = [1, "XXX", 3.14, True]


# In[155]:


# číselné hodnoty
print(42000000000000000000000)
print(3.1415)
# 3.5x10^5
print(3.5e5)
print(-3.1e-9)
print(.5)


# In[156]:


# dělení s reálným výsledkem (Python 3)
4/3


# In[157]:


# celočíselné dělení
4//3


# In[158]:


# Hodnota True je definována, hodnota true nikoli
a = True
b = true


# In[159]:


# Logický výraz
True and False or True


# In[160]:


# Proměnné s logickými hodnotami
a = True
b = False
c = True
a and b or c


# In[161]:


# Relační operátor
1 == 2


# In[162]:


# Relační operátor
2 == 2


# In[163]:


# Relační operátor
10 < 20


# In[164]:


# Relační operátor
x = 10
y = 20
podm = x < y
print(podm)


# In[165]:


# Test, zda seznam obsahuje prvek 2
l = [1, 2, 3]
2 in l


# In[166]:


# Test, zda seznam obsahuje prvek 100
100 in l


# In[167]:


# Speciální význam zpětného lomítka
print("test \"test\" test \\test")


# In[168]:


# Tzv. "raw" řetězce
print("c:\\Documents\\xyz")
print(r"c:\Documents\xyz")


# In[169]:


# Víceřádkové řetězce
print("""A
B
C
D
E
F""")


# In[170]:


# Nekorektní použití jednořádkového řetězce
print("A
      B
      C")


# In[48]:


# Použití " a ' pro uvození řetězců
print("ahoj")
print('ahoj')
print('ahoj")


# In[171]:


# Indexování prvků v seznamu
seznam = [1,2,3,4]
print(seznam)

print(seznam[0])
print(seznam[3])


# In[172]:


# Délka seznamu
print(len(seznam))


# In[173]:


# Výběr (indexování) prvků od konce seznamu
print(seznam[-1])


# In[174]:


# Výběr (indexování) prvků od konce seznamu
print(seznam[-2])


# In[175]:


# Přidání prvku na konec seznamu
seznam.append(100)


# In[176]:


seznam


# In[177]:


# Přidání prvku na konec seznamu
seznam.append(10)
seznam


# In[178]:


# Vložení prvku na začátek seznamu
seznam.insert(0, 100)


# In[179]:


seznam


# In[180]:


# Změna prvku uloženého v seznamu
seznam[3] = "ahoj"


# In[60]:


seznam


# In[181]:


# Smazání prvku ze seznamu
del seznam[0]


# In[62]:


seznam


# In[182]:


# Spojení dvou seznamů
seznam1 = [1, 2, 3]
seznam2 = [4, 5, 6]

seznam3 = seznam1 + seznam2

print(seznam3)


# In[183]:


# Spojení dvou seznamů
seznam3 = seznam3 + [3]


# In[66]:


print(seznam3)


# In[184]:


# Spojení většího množství seznamů
seznam3 = seznam1 + seznam2 + seznam3 + seznam1


# In[68]:


print(seznam3)


# In[185]:


# Opakování prvků seznamu 3x za sebou
seznam1 = [1, 2, 3]

seznam2 = seznam1 * 3
print(seznam2)


# In[71]:


seznam4 = [0] * 50


# In[72]:


print(seznam4)


# In[78]:


# Seřazení prvků v seznamu
seznam = [5, 4, 1, 3, 4, 100, -1]
print(seznam)

seznam.sort()
print(seznam)


# In[186]:


# Seřazení prvků v seznamu
firmy = ["Citrix", "IBM", "ABB"]
firmy.sort()
print(firmy)


# In[187]:


# Seřazení prvků DO nového seznamu (původní se nezmění)
seznam = [5, 4, 1, 3, 4, 100, -1]
print(seznam)

seznam2 = sorted(seznam)
print(seznam)
print(seznam2)


# In[188]:


# Získání výseku ze seznamu
seznam = ["a", "b", "c", "d", "e", "f"]

print(seznam[2:4])


# In[189]:


# Získání výseku ze seznamu
print(seznam[4:2])


# In[190]:


# Získání výseku ze seznamu - uvedení kroku
print(seznam[0:6:2])


# In[191]:


# Získání výseku ze seznamu - uvedení kroku
print(seznam[4:2:-1])


# In[192]:


# Získání výseku ze seznamu - uvedení kroku
print(seznam[5:0:-1])


# In[193]:


# Vynechání indexu při tvorbě výseku ze seznamu
print(seznam[4:])
print(seznam[:4])
print(seznam[:])


# In[194]:


# Nový seznam s opačně seřazenými prvky
print(seznam[::-1])


# In[200]:


# S řetězci se do určité míry pracuje stejně jako se seznamy
x = "Test XYZ Test"
print(x)

# Výběr jednoho znaku
print(x[6])
print(x[-1])

# Výber podřetězce
print(x[5:9])
print(x[::2])
print(x[::-1])


# In[201]:


# Vytvoření slovníku a tisk jeho obsahu
d = {"id": 1,
     "name": "Eda",
     "surname": "Wasserfall"}

print(d)


# In[202]:


# Přečtení prvku s využitím klíče
print(d["name"])


# In[203]:


# Chování ve chvíli, kdy klíč neexistuje
print(d["xyzzy"])


# In[204]:


# Přidání nového prvku do slovníku
d["hra"] = "Svestka"


# In[96]:


d


# In[205]:


# Vymazání prvku ze slovníku
del d["hra"]


# In[206]:


d


# In[207]:


# Množiny
s = {1, 2, 3, 4}
print(s)

# Prvky množiny mohou mít různý typ
s2 = {"hello", "world", "!", 0}
print(s2)

# Prázdná množina
s3 = set()
print(s3)

# Další prázdná množina
s4 = {}
print(s4)


# In[208]:


# Přidání jednoho prvku do množiny
s3.add(1)
print(s3)

s3.add(2)
print(s3)

# Přidání více prvků do množiny
s3.update([3, 4, 5])
print(s3)


# In[104]:


s3.add(4)
print(s3)


# In[209]:


# Odebrání prvku z množiny
s1 = {1, 2, 3, 4}
print(s1)

# Nezpůsobí chybu
s1.discard(2)
print(s1)

s1.discard(1000)
print(s1)

# Může způsobit chybu
s1.remove(3)
print(s1)

s1.remove(1000)
print(s1)


# In[210]:


# Test, jestli prvek leží v množině
s1 = {1,2,3,4}
print(s1)

print(2 in s1)
print(1000 in s1)


# In[211]:


# Logická negace operátoru "in"
print(2 not in s1)
print(1000 not in s1)


# In[212]:


# Základní množinové operace
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1)
print(s2)

# Sjednocení, průnik, rozdíl, symetrická diference
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)


# In[1]:


10/3


# In[2]:


10//3


# In[213]:


# Zbytek po dělení
10%3


# In[214]:


# 10^3
10**3


# In[215]:


# Původní zápis operátoru pro nerovnost
1<>2


# In[216]:


# Nový zápis operátoru pro nerovnost
1!=2


# In[7]:


# Spojení více podmínek pomocí logického operátoru and
x = 20
x > 0 and x < 100


# In[217]:


# Spojení více podmínek pomocí logického operátoru or
x == 0 or x == 1


# In[218]:


# Negace podmínky pomocí logického operátoru not
not x == 0 or x == 1


# In[220]:


# Zkrácený zápis operace A = A operator B na A operator= B
x = 10


# In[14]:


x += 1      # x = x + 1


# In[16]:


x


# In[17]:


x /= 2      # x = x / 2


# In[18]:


x


# In[19]:


x *= 100


# In[20]:


x


# In[21]:


print(x)


# In[22]:


x = 10
x / 2


# In[23]:


x = 10
x // 2


# In[24]:


x = x / 2
x = int(x)


# In[25]:


x


# In[221]:


# Původní zápis příkazu print v Pythonu 2 (už není dále podporován)
print 1


# In[27]:


x = 10


# In[222]:


# Zjištění typu hodnoty
type(x)


# In[223]:


# Po dělení je výsledek typu float
x = x / 2
type(x)


# In[32]:


x = 9
x /= 2
x


# In[224]:


# Základní použití operátoru is
x is x


# In[225]:


# Naformátování výsledku: 7 znaků, z toho 2 za desetinnou tečkou, číslo doplněno mezerami zleva
"{:7.2f}".format(10.0/3)


# In[226]:


# Naformátování výsledku: 7 znaků, z toho 2 za desetinnou tečkou, číslo doplněno nulami zlevo
"{:07.2f}".format(10.0/3)


# In[227]:


# Priority operátorů + a *
1 + 2 * 3


# In[228]:


# Unární operátor -
-4


# In[229]:


# Priority operátorů
1 + x * 2 > 10 and y < 3 + 2 * x


# In[230]:


# Explicitní zápis priorit
((1+(x*2)) > 10) and (y < (3 + (2*x)))


# In[50]:


x


# In[231]:


# Jednoduché větvení typu if (neúplná větev)
x = 10
if x > 0:
    print("x je kladne cislo")

print("pokračujeme")


# In[232]:


# Úplné větvení typu if
x = -10
if x > 0:
    print("x je kladné číslo")
    print("-----------------")
else:
    print("x je záporné číslo nebo nula")
    print("=================")

print("pokračujeme")


# In[63]:


# Vnořené větve if-else
x = 10
if x > 0:
    print("x je kladné číslo")
    print("-----------------")
else:
    if x == 0:
        print("x je nulové")
    else:
        print("x je záporné číslo")
    print("=================")

print("pokračujeme")


# In[233]:


# Vícenásobné větvení založené na if-elif-elif-elif-else
x = 10
if x > 0:
    print("x je kladné číslo")
    print("-----------------")
elif x == 0:
    print("x je nulové")
    print("=================")
else:
    print("x je záporné číslo")
    print("=================")

print("pokračujeme")


# In[234]:


# Vstup dat z klávesnice
cmd = input()


# In[66]:


# Rozhodovací konstrukce na základě vstupu z klávesnice
if cmd == "quit":
    print("konec")
elif cmd == "new account":
    print("...")
elif cmd == "delete account":
    print("...")
else:
    print("unknown command!")


# In[235]:


# Programová smyčka typu while s testem na začátku
i = 1
while i <= 10:
    print(i)
    i = i + 1


# In[236]:


# Průchod prvky seznamu ve smyčce for
list = ["one", "two", "three", "four"]

for item in list:
    print(item)


# In[237]:


# Vyhledání určitého prvku ze seznamu
list = ["one", "two", "three", "four"]

for item in list:
    if item == "three":
        print("NALEZENO")
    print(item)


# In[73]:


range(10)


# In[238]:


# Počitadlo smyčky vytvořené funkcí range()
for i in range(10):
    print(i)


# In[239]:


# První a poslední hodnota počitadla (kromě)
for i in range(5, 20):
    print(i)


# In[241]:


# Specifikace kroku počitadla
for i in range(0, 30, 5):
    print(i)


# In[242]:


# Záporný krok počitadla
for i in range(10, 0, -2):
    print(i)


# In[243]:


# Výpočet složeného úroku
r = 10
z = 1000
for i in range(0, 10):
    z = z * (1 + r/100.0)
    print(2020+i, z)


# In[244]:


# Výpočet složeného úroku + formátování tabulky s výsledky
r = 10
z = 1000
for i in range(0, 10):
    z = z * (1 + r/100.0)
    print("{:4}  {:6.2f}".format(2020+i, z))


# In[246]:


# Tělo smyčky se nemusí provést ani jednou
for i in range(0, 10, -1):
    print(i)


# In[247]:


# Ukončení smyčky po nalezení prvku
list = ["one", "two", "three", "four"]

for item in list:
    # print(item)
    if item == "three":
        print("NALEZENO")
        break
    else:
        print("toto neni hledana hodnota:", item)


# In[248]:


# Ukončení smyčky po splnění zapsané podmínky
r = 10
z = 1000
for i in range(0, 1000):
    z = z * (1 + r/100.0)
    print("{:4}  {:6.2f}".format(2020+i, z))
    if z > 2000:
        print("to uz je hodne")
        break


# In[249]:


# Konstrukce break a continue
x = 1

while True:
    if x > 1000:
        break
    x *= 2
    if x < 100:
        continue
    print(x)


# In[250]:


# Funkce se dvěma parametry
def soucet(a, b):
    vysledek = a + b
    return vysledek


# In[92]:


soucet(1, 2)


# In[93]:


vysledek


# In[251]:


# Funkce se třemi povinnými parametry
def slozeny_urok(zaklad, urok, roky):
    r = urok
    z = zaklad
    for i in range(0, roky):
        z = z * (1 + r/100.0)
    return z


# In[95]:


slozeny_urok(1000, 10, 1)


# In[96]:


slozeny_urok(1000, 10, 10)


# In[97]:


for urok in range(1, 10):
    print(slozeny_urok(1000, urok, 5))


# In[252]:


# Rekurzivní funkce
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# In[100]:


factorial(100)


# In[253]:


# Funkce s nepovinným parametrem s implicitní hodnotou
def slozeny_urok(zaklad, urok, roky=10):
    r = urok
    z = zaklad
    for i in range(0, roky):
        z = z * (1 + r/100.0)
    return z


# In[103]:


slozeny_urok(1000, 10)


# In[104]:


print(1, 2)


# In[105]:


print(1, 2, sep=",")


# In[126]:


# Dva povinné parametry následované libovolným počtem nepovinných parametrů
def soucet(a, b, *dalsi):
    vysledek = a + b
    for hodnota in dalsi:
        vysledek += hodnota
    return vysledek


# In[127]:


# Funkce, která akceptuje libovolný počet parametrů
def soucet(*dalsi):
    vysledek = 0     #a + b
    for hodnota in dalsi:
        vysledek += hodnota
    return vysledek


# In[120]:


soucet(2, 3, 4)


# In[254]:


# Funkce akceptující libovolný počet pojmenovaných parametrů
def delej(**parametry):
    print(parametry)


# In[125]:


delej(x=10, y=20, z="ahoj")


# In[129]:


# Lokální a globální proměnné
x = 1

def fn1():
    pass


def fn2():
    x = 2


def fn3():
    global x
    x = 3


print(x)
fn1()
print(x)
fn2()
print(x)
fn3()
print(x)


# In[27]:


# Generátorová notace seznamu - nový seznam, jehož prvky mají oproti původnímu dvojnásobnou hodnotu
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seznam2 = [item*2 for item in seznam]


# In[131]:


seznam


# In[132]:


seznam2


# In[138]:


# Generátorová notace seznamu
[1.0/item for item in seznam]


# In[139]:


(1.0/item for item in seznam)


# In[140]:


# Filtrace prvků splňujících zadanou podmínku
[item for item in seznam if item % 3 == 0]


# In[141]:


# Filtrace prvků splňujících zadanou podmínku
[item for item in seznam if item > 5]


# In[142]:


# Zkrácený zápis tabulky složených úroků
[slozeny_urok(item, 10, 10) for item in seznam]


# In[28]:


# Plný zápis výpočtu tabulky složených úroků
vysledek = []
for item in seznam:
    vysledek.append(slozeny_urok(item, 10, 10))
    
vysledek


# ## Druhý den

# ### Moduly, popis standardní knihovny Pythonu: https://docs.python.org/3.7/library/index.html

# In[2]:


import math


# In[3]:


math.floor(10/3)


# In[4]:


math.ceil(10/3)


# In[8]:


math.sin(math.pi/2)


# In[10]:


from math import floor


# In[11]:


floor(10/3)


# In[12]:


from math import floor, ceil


# In[13]:


from math import *


# In[25]:


sin(pi/2)


# In[15]:


import matplotlib as plt


# ### Zobrazení nápovědy

# In[29]:


help(math)


# In[17]:


help(math.floor)


# In[18]:


help(range)


# In[23]:


# Funkce s nepovinným parametrem s implicitní hodnotou
def slozeny_urok(zaklad, urok, roky=10):
    """Výpočet složeného úroku ze zadaného základu a % p.a.
    
    Očekává tyto paramety:
    - základ ....
    """
    r = urok
    z = zaklad
    for i in range(0, roky):
        z = z * (1 + r/100.0)
    return z


# In[24]:


help(slozeny_urok)


# ## Základní práce se soubory

# ### Open+write+close

# In[30]:


fout = open("hello.txt", "w")
fout.write("Hello World")
fout.close()


# ### Open+read+close

# In[31]:


vstup = open("hello.txt", "r")
data = vstup.read()
vstup.close()
print(data)


# ### Blok with a open+write a open+read

# In[ ]:


with open("hello2.txt", "w") as vystup:
    vystup.write("Hello world #2")


# In[34]:


with open("hello2.txt", "r") as vstup:
    data = vstup.read()
    print(data)


# In[36]:


with open("hello3.txt", "w") as vystup:
    vystup.write("abc\n")
    vystup.write("def\n")
    vystup.write("xyz\n")


# ### Použití funkce print pro zápis dat do souboru

# In[37]:


help(print)


# In[38]:


with open("hello4.txt", "w") as vystup:
    print("abc", file=vystup)
    print("def", file=vystup)
    print("xyz", file=vystup)


# In[39]:


with open("hello4.txt", "r") as vstup:
    data = vstup.read()
    print(data)


# In[40]:


with open("hello4.txt", "r") as vstup:
    for radek in vstup:
        print(radek)


# In[41]:


with open("hello4.txt", "r") as vstup:
    for radek in vstup:
        print(radek.strip())


# ### Formátování výstupu
# https://docs.python.org/3.7/library/string.html#formatspec

# In[42]:


for x in range(1, 11):
    y = 1.0/x
    print(x, y)


# In[43]:


for x in range(1, 11):
    y = 1.0/x
    print("1/{:2d} = {:5.3f}".format(x, y))


# In[44]:


for x in range(1, 11):
    y = 1.0/x
    print("1/{:03d} = {:5.3f}".format(x, y))


# In[45]:


for x in range(1, 11):
    y = 1.0/x
    print("1/{:03d} = {:6.4f}".format(x, y))


# ### Vytvoření souboru s tabulkou s výsledky

# In[47]:


with open("vysledky.txt", "w") as vystup:
    for x in range(1, 11):
        y = 1.0/x
        print("1/{:2d} = {:5.3f}".format(x, y), file=vystup)


# In[48]:


import pandas


# In[52]:


tabulka = pandas.read_csv("data_update_2020.csv", sep=";")


# In[53]:


tabulka


# In[58]:


tabulka.info()


# In[54]:


tabulka.describe()


# In[55]:


tabulka["IC"]


# In[56]:


tabulka["IC"][20]


# In[62]:


s = "1 076.8"


# In[64]:


s.replace(" ", "")


# In[65]:


tabulka


# In[74]:


# Vytvoření nového sloupce, hodnoty jsou získány ze sloupce "avg-exp-pc" a všechny mezery jsou vymazány
tabulka["new-avg-exp-pc"] = tabulka["avg-exp-pc"].transform(lambda s:s.replace(" ", ""))


# In[76]:


tabulka


# In[77]:


tabulka.info()


# In[78]:


# Nový sloupec X, s hodnotami ze sloupce new-avg-exp-pc převedenými na číslo

tabulka['X'] = pandas.to_numeric(tabulka['new-avg-exp-pc'])


# In[71]:


tabulka


# In[72]:


tabulka.describe()


# In[80]:


import matplotlib.pyplot as plt


# In[81]:


plt.plot(tabulka["X"])


# In[82]:


help(pandas.read_excel)


# In[84]:


# Přímé načtení souboru z Excelu
pandas.read_excel(r"c:\dokumenty\test.xlsx")


# ## Obsluha výjimek

# In[87]:


# Přímé načtení souboru z Excelu
try:
    # zde může dojít k výjimce, když soubor neexistuje
    tabulka = pandas.read_excel(r"c:\dokumenty\test.xlsx")
    print("Načtení se podařilo")
    tabulka.describe()
except FileNotFoundError:
    # obsluha výjimky
    print("Chyba při načítání Excelovského sešitu")


# ### Pokus o načtení neexistujícího souboru - výjimka typu `FileNotFoundError`

# In[89]:


# Přímé načtení souboru z Excelu
try:
    # zde může dojít k výjimce, když soubor neexistuje
    tabulka = pandas.read_excel(r"c:\dokumenty\test.xlsx")
    print("Načtení se podařilo")
    print(tabulka.describe())
except FileNotFoundError as e:
    # obsluha výjimky
    print("Chyba při načítání Excelovského sešitu")
    print("Podrobnější informace o chybě:", e)


# ### Pokus o načtení neexistujícího souboru - dojde k výjimce typu `FileNotFoundError`

# In[101]:


try:
    tabulka = pandas.read_csv("neexistujici_soubor.csv", sep=";")
    tabulka['X'] = pandas.to_numeric(tabulka['avg-exp-pc'])
    print("Tabulka byla načtena a zkonvertována!")
    print(tabulka.describe())
except FileNotFoundError as e:
    # obsluha první výjimky
    print("Chyba při načítání CSV souboru")
    print("Podrobnější informace o chybě:", e)
except ValueError as e:
    # obsluha druhé výjimky
    print("Chyba při konverzi dat")
    print("Podrobnější informace o chybě:", e)
except Exception as e:
    # obsluha všech zbývajících typů výjimek
    print("Neznámá chyba: ", e)


# ### V tomto příkladu dojde k výjimce při konverzi dat - `ValueError`

# In[98]:


try:
    tabulka = pandas.read_csv("data_update_2020.csv", sep=";")
    tabulka['X'] = pandas.to_numeric(tabulka['avg-exp-pc'])
    print("Tabulka byla načtena a zkonvertována!")
    print(tabulka.describe())
except FileNotFoundError as e:
    # obsluha první výjimky
    print("Chyba při načítání CSV souboru")
    print("Podrobnější informace o chybě:", e)
except ValueError as e:
    # obsluha druhé výjimky
    print("Chyba při konverzi dat")
    print("Podrobnější informace o chybě:", e)
except Exception as e:
    # obsluha všech zbývajících typů výjimek
    print("Neznámá chyba: ", e)


# ### V tomto příkladu k výjimce nedojde

# In[100]:


try:
    tabulka = pandas.read_csv("data_update_2020.csv", sep=";")
    # Vytvoření nového sloupce, hodnoty jsou získány ze sloupce "avg-exp-pc" a všechny mezery jsou vymazány
    tabulka["new-avg-exp-pc"] = tabulka["avg-exp-pc"].transform(lambda s:s.replace(" ", ""))
    tabulka['X'] = pandas.to_numeric(tabulka['new-avg-exp-pc'])
    print("Tabulka byla načtena a zkonvertována!")
    print(tabulka.describe())
except FileNotFoundError as e:
    # obsluha první výjimky
    print("Chyba při načítání CSV souboru")
    print("Podrobnější informace o chybě:", e)
except ValueError as e:
    # obsluha druhé výjimky
    print("Chyba při konverzi dat")
    print("Podrobnější informace o chybě:", e)
except Exception as e:
    # obsluha všech zbývajících typů výjimek
    print("Neznámá chyba: ", e)


# ### Vyhození vlastní výjimky po splnění nějaké podmínky

# In[106]:


try:
    tabulka = pandas.read_csv("data_update_2020.csv", sep=";")
    # test, jestli má sloupec avg-exp-pc správný typ
    if tabulka['avg-exp-pc'].dtypes == "object":
        raise ValueError("Sloupec avg-exp-pc obsahuje špatné hodnoty")
    print(tabulka.describe())
    print(tabulka['avg-exp-pc'].mean())
except FileNotFoundError as e:
    # obsluha první výjimky
    print("Chyba při načítání CSV souboru")
    print("Podrobnější informace o chybě:", e)
except ValueError as e:
    # obsluha druhé výjimky
    print("Chyba při konverzi dat")
    print("Podrobnější informace o chybě:", e)
except Exception as e:
    # obsluha všech zbývajících typů výjimek
    print("Neznámá chyba: ", e)


# ### Použití bloku `finally`

# In[107]:


try:
    tabulka = pandas.read_csv("data_update_2020.csv", sep=";")
    # test, jestli má sloupec avg-exp-pc správný typ
    if tabulka['avg-exp-pc'].dtypes == "object":
        raise ValueError("Sloupec avg-exp-pc obsahuje špatné hodnoty")
    print(tabulka.describe())
    print(tabulka['avg-exp-pc'].mean())
except FileNotFoundError as e:
    # obsluha první výjimky
    print("Chyba při načítání CSV souboru")
    print("Podrobnější informace o chybě:", e)
except ValueError as e:
    # obsluha druhé výjimky
    print("Chyba při konverzi dat")
    print("Podrobnější informace o chybě:", e)
except Exception as e:
    # obsluha všech zbývajících typů výjimek
    print("Neznámá chyba: ", e)
finally:
    print("Blok finally")


# ### Deklarace třídy

# In[111]:


class Employee:
    pass

# vytvoření objektu typu Employee
# neboli vytvoření instance třídy Employee
e = Employee()


# In[112]:


e


# ### Více instancí třídy

# In[113]:


e1 = Employee()
e2 = Employee()
print(e1)
print(e2)


# In[125]:


class Employee:

    # konstruktor - první parametr musí být self
    def __init__(self, first_name, surname, salary):
        print("Konstruktor", first_name, surname, salary)
        # vytvoření a inicializace atributů objektu
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._test = 1000

    # metoda -- funkce deklarovaná uvnitř třídy, má přístup k atributům objektu
    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)


# Vytvoříme dvě instance třídy Employee
e1 = Employee("Pepa", "Vyskoč", 15000)
e2 = Employee("Petr", "Pavel", 20000)


# In[128]:


# Zavoláme metodu display_employee()
e1.display_employee()


# In[129]:


# Zavoláme metodu display_employee()
e2.display_employee()


# In[131]:


e1.display_employee()
Employee.display_employee(e1)


# In[134]:


class Employee:

    # konstruktor - první parametr musí být self
    def __init__(self, first_name, surname, salary):
        print("Konstruktor", first_name, surname, salary)
        # vytvoření a inicializace atributů objektu
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._test = 1000

    # metoda -- funkce deklarovaná uvnitř třídy, má přístup k atributům objektu
    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)

    # metoda, která mění jeden atribut objektu
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
    
    def increase_salary(self, ratio):
        self._salary = self._salary * (1 + ratio/100.0)
        

# Vytvoříme dvě instance třídy Employee
e1 = Employee("Pepa", "Vyskoč", 15000)
e2 = Employee("Petr", "Pavel", 20000)

e1.display_employee()
e1.set_first_name("***")
e1.display_employee()
e1.increase_salary(10)
e1.display_employee()


# In[137]:


employes = [
    Employee("Pepa", "Vyskoč", 15000),
    Employee("Petr", "Pavel", 20000),
    Employee("Kamil", "Vedoucí", 60000),
]


# In[138]:


employes


# In[140]:


for e in employes:
    e.display_employee()


# In[141]:


for e in employes:
    e.increase_salary(10)


# In[143]:


for e in employes:
    print(e)


# ### Použití speciální metody `__str__`

# In[144]:


class Employee:

    # konstruktor - první parametr musí být self
    def __init__(self, first_name, surname, salary):
        print("Konstruktor", first_name, surname, salary)
        # vytvoření a inicializace atributů objektu
        self._first_name = first_name
        self._surname = surname
        self._salary = salary
        self._test = 1000

    # metoda -- funkce deklarovaná uvnitř třídy, má přístup k atributům objektu
    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)

    # metoda, která mění jeden atribut objektu
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
    
    def increase_salary(self, ratio):
        self._salary = self._salary * (1 + ratio/100.0)
        
    # speciální metoda __str__
    def __str__(self):
        return "Full name: " + self._first_name + " " + self._surname + "   Salary: " + str(self._salary)


# In[147]:


employes = [
    Employee("Pepa", "Vyskoč", 15000),
    Employee("Petr", "Pavel", 20000),
    Employee("Kamil", "Vedoucí", 60000),
]
print()

for e in employes:
    print(e)


# In[152]:


class Person:
    # konstruktor - první parametr musí být self
    def __init__(self, first_name, surname):
        print("Konstruktor", first_name, surname)
        # vytvoření a inicializace atributů objektu
        self._first_name = first_name
        self._surname = surname

    # metoda, která mění jeden atribut objektu
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
    
    # speciální metoda __str__
    def __str__(self):
        return "Full name: " + self._first_name + " " + self._surname


# Třída Employee je odvozena od třídy Person
# Employee je předek Person
# Person je potom Employee
class Employee(Person):

    # konstruktor - první parametr musí být self
    def __init__(self, first_name, surname, salary):
        print("Konstruktor", first_name, surname, salary)
        # vytvoření a inicializace atributů objektu
        self._first_name = first_name
        self._surname = surname
        self._salary = salary

    # metoda -- funkce deklarovaná uvnitř třídy, má přístup k atributům objektu
    def display_employee(self):
        print("Full name: ", self._first_name, self._surname, "   Salary: ", self._salary)

    def increase_salary(self, ratio):
        self._salary = self._salary * (1 + ratio/100.0)
        
    # speciální metoda __str__
    def __str__(self):
        return "Full name: " + self._first_name + " " + self._surname + "   Salary: " + str(self._salary)


# In[150]:


e = Employee("first", "surname", 10000)


# In[151]:


e.set_first_name("new first name")


# ## Klíčové slovo `assert`

# In[153]:


assert 1==1


# In[154]:


assert 1!=1


# In[169]:


# Funkce se třemi povinnými parametry
def slozeny_urok(zaklad, urok, roky):
    assert zaklad >= 0, "Základ musí být nezáporný"
    assert urok >= 0, "Úrok by měl být kladný"
    
    r = urok
    z = zaklad
    for i in range(0, roky):
        z = z * (1 + r/100.0)
        assert z > 0, "Mezivýpočet..."
    return z


# In[168]:


slozeny_urok(10000, 500, 50)


# In[213]:


try:
    tabulka = pandas.read_csv("data_update_2020.csv", sep=";")
    # Vytvoření nového sloupce, hodnoty jsou získány ze sloupce "avg-exp-pc" a všechny mezery jsou vymazány
    tabulka["new-avg-exp-pc"] = tabulka["avg-exp-pc"].transform(lambda s:s.replace(" ", ""))
    tabulka['X'] = pandas.to_numeric(tabulka['new-avg-exp-pc'])
    del tabulka["avg-exp-pc"]
    del tabulka["new-avg-exp-pc"]
    tabulka["avg-exp-pc"] = tabulka["X"]
    print("Tabulka byla načtena a zkonvertována!")
    
    # průchod přes řádky tabulky
    #for i, zaznam in tabulka.iterrows():
    #    if zaznam["avg-exp-pc"] > 1000:
    #        print(i, zaznam["OBEC"], zaznam["avg-exp-pc"])

    vyber2 = tabulka[tabulka["avg-exp-pc"] > 1000]
    print(vyber2["avg-exp-pc"].max())
    print(vyber2["avg-exp-pc"].min())
    print(vyber2["avg-exp-pc"].mean())
    print(vyber2["avg-exp-pc"].sum())
    
    # ruční výpočet sumy
    avg = vyber2["avg-exp-pc"]
    suma = 0
    for i, a in avg.items():
        suma += a
    print("Suma:", suma)
    
    #plt.plot(vyber2["avg-exp-pc"])
    #plt.plot(vyber2["avg-exp-pc"])
    #vyber2["avg-exp-pc"].plot.bar()
    vyber2["avg-exp-pc"].plot.hist()
        
except FileNotFoundError as e:
    # obsluha první výjimky
    print("Chyba při načítání CSV souboru")
    print("Podrobnější informace o chybě:", e)
except ValueError as e:
    # obsluha druhé výjimky
    print("Chyba při konverzi dat")
    print("Podrobnější informace o chybě:", e)
except Exception as e:
    # obsluha všech zbývajících typů výjimek
    print("Neznámá chyba: ", e)


# In[199]:


# Dokumentace Pandas: https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api


# # Numpy a Matplotlib

# https://github.com/tisnik/python-programming-courses/blob/master/Matplotlib/matplotlib_in_action.py

# In[214]:


# Pro potřeby prezentace naimportujeme všechny funkce a konstanty z knihovny `matplotlib.pyplot`
import matplotlib.pyplot as plt

# Taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np


# In[215]:


# hodnoty na x-ové ose
x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)


# In[216]:


x


# In[217]:


# hodnoty na x-ové ose
x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
plt.plot(x, y1, x, y2)


# In[220]:


# hodnoty na x-ové ose
x = np.linspace(0.01, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# hodnoty na y-ové ose: třetí funkce
y3 = np.sin(x)/x

# vykreslit průběh všech tří funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r.", label="cos")
plt.plot(x, y3, "g--", label="sinc")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x), cos(x) a sinc(x)")


# In[221]:


# historické ceny ropy
cena_ropy = [
    46.68, 44.68, 46.90, 47.15, 44.59, 44.00, 44.63, 45.92, 44.15, 45.94,
    46.05, 46.75, 46.25, 45.41, 49.20, 45.22, 42.56, 38.60, 39.31, 38.24,
    40.45, 41.32, 40.80, 42.62, 41.87, 42.50, 42.23, 43.30, 43.08, 44.96,
    43.87, 44.66, 45.15, 47.12, 48.52, 48.79, 47.98, 47.39, 48.14, 48.45]

# počet prvků
N = len(cena_ropy)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 1.00

# sloupcový graf
plt.bar(indexes, cena_ropy, width, color='yellow', edgecolor='black',
        label='Cena ropy')

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")


# In[228]:


# první pole hodnot
vals1 = [10, 15, 20, 12, 14, 8]

# druhé pole hodnot
vals2 = [19, 18,  6, 11,  6, 14]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color='gray', edgecolor='black', label='CPU#1')
# posunuté sloupce
plt.bar(indexes+width, vals2, width, color='red', edgecolor='black',
        label='CPU#2')

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")


# In[231]:


# náhodné hodnoty
y = np.random.normal(0, 0.1, 100000)

plt.hist(y, bins=50, range=None, density=True)


# In[232]:


# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18,  6, 11,  6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color='gray', edgecolor='black', label='CPU#1',
        yerr=delta1)

# posunuté sloupce
plt.bar(indexes+width, vals2, width, color='red', edgecolor='black',
        label='CPU#2', yerr=delta2)

# povolení zobrazení mřížky
plt.grid(True)


# In[233]:


# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18,  6, 11,  6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color='gray', edgecolor='black', label='CPU#1',
        yerr=delta1, error_kw=dict(elinewidth=2, ecolor='red'))

# posunuté sloupce
plt.bar(indexes+width, vals2, width, color='red', edgecolor='black',
        label='CPU#2',
        yerr=delta2, error_kw=dict(elinewidth=2, ecolor='black'))

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

