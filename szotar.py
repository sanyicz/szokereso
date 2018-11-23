filein = open('szojegyzek.txt', 'r')            #ebből a fájlból szedjük a szavakat
magy3, magy4, magy5, magy6, magy7, magy8, magy9 = [], [], [], [], [], [], [] #ilyen listákba tároljuk 3,4,...,9 betűs szavakat
while 1:
    sor = filein.readline()     #soronként beolvassuk a fájlt, minden sorban egy szó van
    if sor == '':               #ha elértünk az utolsó, üres sorhoz, leáll
        break
    szo = sor[:(len(sor)-2)]   #leszedjük a végéről a vesszőt, nagybetűssé alakítjuk a szót
##    szo = ''                    #kicseréljük a fura 'ő' és 'ű' betűket jóra
##    for ch in szo0:
##        if ch =='õ':
##            szo = szo + 'ő'
##        elif ch == 'û':
##            szo = szo + 'ű'
##        else:
##            szo = szo + ch
    szo = szo.upper()           #nagybetűssé alakítjuk
    #print(szo)
    if (len(szo)==3):           #a szót hozzáadjuk a megfelelő listához
        magy3.append(szo)
    elif (len(szo)==4):
        magy4.append(szo)
    elif (len(szo)==5):
        magy5.append(szo)
    elif (len(szo)==6):
        magy6.append(szo)
    elif (len(szo)==7):
        magy7.append(szo)
    elif (len(szo)==8):
        magy8.append(szo)
    elif (len(szo)==9):
        magy9.append(szo)
filein.close()                  #fájl bezárása

#itt szedjük ki a szavakból az első 3 betűjüket
magy34 = []
for i in range(len(magy4)):
    magy34.append(magy4[i][:3])
magy35 = []
for i in range(len(magy5)):
    magy35.append(magy5[i][:3])
magy36 = []
for i in range(len(magy6)):
    magy36.append(magy6[i][:3])
magy37 = []
for i in range(len(magy7)):
    magy37.append(magy7[i][:3])
magy38 = []
for i in range(len(magy8)):
    magy38.append(magy8[i][:3])
magy39 = []
for i in range(len(magy9)):
    magy39.append(magy9[i][:3])

#itt szedjük ki a szavakból az első 4 betűjüket
magy45 = []
for i in range(len(magy5)):
    magy45.append(magy5[i][:4])
magy46 = []
for i in range(len(magy6)):
    magy46.append(magy6[i][:4])
magy47 = []
for i in range(len(magy7)):
    magy47.append(magy7[i][:4])
magy48 = []
for i in range(len(magy8)):
    magy48.append(magy8[i][:4])
magy49 = []
for i in range(len(magy9)):
    magy49.append(magy9[i][:4])

#itt szedjük ki a szavakból az első 5 betűjüket
magy56 = []
for i in range(len(magy6)):
    magy56.append(magy6[i][:5])
magy57 = []
for i in range(len(magy7)):
    magy57.append(magy7[i][:5])
magy58 = []
for i in range(len(magy8)):
    magy58.append(magy8[i][:5])
magy59 = []
for i in range(len(magy9)):
    magy58.append(magy9[i][:5])

#itt szedjük ki a szavakból az első 6 betűjüket
magy67 = []
for i in range(len(magy7)):
    magy67.append(magy7[i][:6])
magy68 = []
for i in range(len(magy8)):
    magy68.append(magy8[i][:6])
magy69 = []
for i in range(len(magy9)):
    magy69.append(magy9[i][:6])

#itt szedjük ki a szavakból az első 7 betűjüket
magy78 = []
for i in range(len(magy8)):
    magy78.append(magy8[i][:7])
magy79 = []
for i in range(len(magy9)):
    magy79.append(magy9[i][:7])

#itt szedjük ki a szavakból az első 8 betűjüket - kell ez?
magy89 = []
for i in range(len(magy9)):
    magy89.append(magy9[i][:8])

#a kimeneti lista előállítása
magyar3 = [magy3, magy34, magy35, magy36, magy37, magy38, magy39]
magyar4 = [magy4, magy45, magy46, magy47, magy48, magy49]
magyar5 = [magy5, magy56, magy57, magy58, magy59]
magyar6 = [magy6, magy67, magy68, magy69]
magyar7 = [magy7, magy78, magy79]
magyar8 = [magy8, magy89]
magyar9 = [magy9]
#a végső kimeneti lista
magyar = [magyar3, magyar4, magyar5, magyar6, magyar7, magyar8, magyar9]
