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
l1 = [1, 2, 3]
2 in l1


# In[166]:


# Test, zda seznam obsahuje prvek 100
100 in l1


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
seznam = [1, 2, 3, 4]
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
s1 = {1, 2, 3, 4}
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
10 % 3


# In[214]:


# 10^3
10**3


# In[215]:


# Původní zápis operátoru pro nerovnost
1 <> 2


# In[216]:


# Nový zápis operátoru pro nerovnost
1 != 2


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
    vysledek = 0
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


# In[130]:


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


# In[144]:


# Plný zápis výpočtu tabulky složených úroků
vysledek = []
for item in seznam:
    vysledek.append(slozeny_urok(item, 10, 10))

vysledek
