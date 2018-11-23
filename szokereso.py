from tkinter import *           #importáljuk a grafikus modult
from random import *            #importáljuk a randomizáló modult
from class_cella import *       #importáljuk a cellák osztályát tartalmazó fájlt
from szotar import *            #importáljuk az ismert szavak szótárát
from time import *              #importáljuk az időt

class Szokereso:
    cim = 'SZÓKERESŐ'
    mezorajz = [(0,0),(0,2),(0,4),(2,0),(2,2),(2,4),(4,0),(4,2),(4,4)] #cellakoordináták a rajzoláshoz (mivel 2x2-esek a cellák)
    mezocella = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)] #cellakoordináták a számoláshoz
    file = open('jomezok_14k.txt', 'r')
    adatbazis = []
    while 1: #a jó mezőket tartalmazó txt-ből csinál adatbazis nevű tömböt
        sor1 = file.readline()
        if sor1=='':
            break
        sor2 = sor1[:9]
        adatbazis.append(sor2)
    def __init__(self, boss=None): #létrehozza a grafikus felületet, egyebeket
        self.ablak = Tk()
        self.ablak.title(Szokereso.cim) #ablak címe
        self.gombok = [] #a betűs gombokat tartalmazó lista
        for i in range(9): #gombok létrehozása
            self.gombok.append(Button(text = Szokereso.cim[i], font = ('Times', '30')))
            self.gombok[i].grid(row = Szokereso.mezorajz[i][0], column = Szokereso.mezorajz[i][1], rowspan = 2, columnspan = 2)
        self.lehet = [] #a lehetséges kirakható szavakat tartalmazó lista
        for i in range(7):
            Label(self.ablak, text = str(i+3) + ' betűsek').grid(row = 0, column = 6+i)
            lehetdb = IntVar()
            self.lehet.append((Label(self.ablak, textvariable = lehetdb), lehetdb))
            self.lehet[i][0].grid(row = 1, column = 6+i)
        self.beirt = StringVar() #a beírt szót tartalmazó sztringváltozó
        self.beiro = Entry(self.ablak, textvariable = self.beirt) #ebbe a mezőbe írjuk a tippelt szót
        self.beiro.grid(row = 2, column = 6, columnspan = 3) #elhelyezés
        self.beiro.bind("<Return>", self.szotipp) #a tippmezőben ütött <Enter>-hez kötjük a szotipp metódust
        Button(self.ablak, text = 'Új játék', command = self.jatszma).grid(row = 3, column = 6, columnspan = 3) #új játékot indító gomb
        Button(self.ablak, text = 'Szavak listája', command = self.szolista).grid(row = 4, column = 6, columnspan = 3) #segítséget adó gomb
        self.kesz = Label(self.ablak) #'Kész!' üzenet kiírására való, később hivatkozunk rá
        self.kesz.grid(row = 3, column = 9) #elhelyezés
        Button(self.ablak, text = 'Játék vége', command = self.ablak.destroy).grid(row = 5, column = 6, columnspan = 3) #a játékot befejező gomb
        Label(self.ablak, text = 'Megtalált szavak:').grid(row = 6, column = 0, columnspan = 3, sticky = W) #az adott pontig megtalált szavakat írjuk ki
        self.megtalaltdb = Label(self.ablak) #megtalált szavak számának kiírása
        self.megtalaltdb.grid(row = 6, column = 3) #elhelyezés
        self.megtalaltlista = Label(self.ablak) #megtalált szavak listájának kiírása
        self.megtalaltlista.grid(row = 7, column = 0, columnspan = 12, sticky = W) #elhelyezés
        self.megtalalt = [] #megtalált szavak listája
        Label(self.ablak, text='Max pontszám').grid(row = 2, column = 10) #max pontszám
        self.max = IntVar() #max pontszám változója
        self.max.set(0)
        self.maxpont = Label(self.ablak, textvariable=self.max)
        self.maxpont.grid(row = 3, column = 10)
        Label(self.ablak, text='Pontszám').grid(row = 2, column = 11) #pontszám
        self.pont = IntVar() #elért pontok számának változója
        self.pont.set(0)
        self.pontszam = Label(self.ablak, textvariable=self.pont)
        self.pontszam.grid(row = 3, column = 11)
        Label(self.ablak, text='Százalék (%)').grid(row = 2, column = 12)
        self.szaz = StringVar() #elért százalék változója
        self.szaz.set('0')
        self.szazalek = Label(self.ablak, textvariable=self.szaz)
        self.szazalek.grid(row = 3, column = 12)
        #self.ablak.mainloop() #eseményfigyelő indítása, elvileg nem szabad a konstruktorba rakni, a főprogramban van

    def szotipp(self, event): #a beírt tipp helyességét kezelő metódus
        tipp = self.beirt.get().upper() #kiszedi a beírt szót
        tipp = tipp.replace('Ő','Õ') #a karakterkódolási bajokat nem tudom máshogy megoldani
        tipp = tipp.replace('Ű','Û') #a karakterkódolási bajokat nem tudom máshogy megoldani
        for i in range(len(self.lehetszavak)):
            if tipp in self.lehetszavak[i]: #megnézi, hogy ismert szó-e
                if not tipp in self.megtalalt: #megnézi, hogy megtaláltuk-e már, ha nem, tovább
                    self.megtalalt.append(tipp) #hozzáadja a megtalált szavak listájához
                    self.megtalaltlista.configure(text = self.megtalalt) #kiírja
                    self.megtalaltdb.configure(text = str(len(self.megtalalt)))
                    self.beirt.set('') #kiüríti a beírómezőt
                    if len(self.megtalalt) == self.osszesszo: #ha minden lehetséges szó megvan
                        self.kesz.configure(text = 'Kész!')
                    for j in range(3,10): #találat esetén állítja a még bennlévő szavak számának kijelzését
                        if len(tipp) == j:
                            self.lehet[j-3][1].set(self.lehet[j-3][1].get() - 1) #találat esetén csökkenti a még bennlévő szavak számát
                            self.pont.set(self.pont.get() + j) #pontozás: minden szó annyi pontot ér, ahány betűs (kell majd egy százalékszámláló)
                            self.szaz.set('%0.2f' % (100*self.pont.get()/self.max.get()))

    def szolista(self): #segítségként/ellenőrzésként kiírja a lehetséges kirakható szavakat
        try:
            print(self.osszesszo, ':', self.lehetszavak)
        except:
            print('Nincs elkezdett játék.')

    def jatszma(self): #maga a játék
        self.kesz.configure(text = '') #nullázza a 'Kész!' feliratot
        self.megtalalt = [] #nullázza a megtalált szavakat
        self.megtalaltlista.configure(text = self.megtalalt)
        self.megtalaltdb.configure(text = str(len(self.megtalalt)))
        self.mezo = []
        self.mezohasz = randrange(len(Szokereso.adatbazis))
        for i in range(9): #betűk létrehozása az egyes cellákba
            self.mezo.append(Cella(Szokereso.mezocella[i][0],Szokereso.mezocella[i][1],Szokereso.adatbazis[self.mezohasz][i])) #a jomezok txt fájlból szedi a mezőket random
            self.gombok[i].configure(text = self.mezo[i].betu) #kiírja a betűket a gombokra
        szav3, szav4, szav5, szav6, szav7, szav8, szav9 = [], [], [], [], [], [], [] #a megtalált 3,4,...,9 betűs szavakat eltároló listák
        t0 = time() #innentől mennyi idő alatt fut le?
        for i1 in range(9): #ez a rész keresi meg a kirakható szavakat
            for i2 in range(9):
                if i1!=i2:
                    if abs(self.mezo[i2].x - self.mezo[i1].x)<=1 and abs(self.mezo[i2].y - self.mezo[i1].y)<=1:
                        for i3 in range(9):
                            if i1!=i3 and i2!=i3:
                                if abs(self.mezo[i3].x - self.mezo[i2].x)<=1 and abs(self.mezo[i3].y - self.mezo[i2].y)<=1:
                                    szo3 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu
                                    if not szo3 in szav3: #ha a 3 betűs szó létezik, hozzáadjuk a megtaláltakhoz
                                        if (szo3 in magyar[0][0]):
                                            szav3.append(szo3)
                                    if (szo3 in magyar[0][1]) or (szo3 in magyar[0][2]) or (szo3 in magyar[0][3]) or (szo3 in magyar[0][4]) or (szo3 in magyar[0][5]) or (szo3 in magyar[0][6]):    #ha a 3 betűs szó egyezik a 4,5,...,9 betűs szavak első 3 betűjével, folytatjuk a keresést
                                        for i4 in range(9):
                                            if i1!=i4 and i2!=i4 and i3!=i4:
                                                if abs(self.mezo[i4].x - self.mezo[i3].x)<=1 and abs(self.mezo[i4].y - self.mezo[i3].y)<=1:
                                                    szo4 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu + self.mezo[i4].betu
                                                    if not szo4 in szav4:
                                                        if (szo4 in magyar[1][0]):
                                                            szav4.append(szo4)
                                                    if (szo4 in magyar[1][1]) or (szo4 in magyar[1][2]) or (szo4 in magyar[1][3]) or (szo4 in magyar[1][4]) or (szo4 in magyar[1][5]):
                                                        for i5 in range(9):
                                                            if i1!=i5 and i2!=i5 and i3!=i5 and i4!=i5:
                                                                if abs(self.mezo[i5].x - self.mezo[i4].x)<=1 and abs(self.mezo[i5].y - self.mezo[i4].y)<=1:
                                                                    szo5 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu + self.mezo[i4].betu + self.mezo[i5].betu
                                                                    if not szo5 in szav5:
                                                                        if (szo5 in magyar[2][0]):
                                                                            szav5.append(szo5)
                                                                    if (szo5 in magyar[2][1]) or (szo5 in magyar[2][2]) or (szo5 in magyar[2][3]) or (szo5 in magyar[2][4]):
                                                                        for i6 in range(9):
                                                                            if i1!=i6 and i2!=i6 and i3!= i6 and i4!=i6 and i5!=i6:
                                                                                if abs(self.mezo[i6].x - self.mezo[i5].x)<=1 and abs(self.mezo[i6].y - self.mezo[i5].y)<=1:
                                                                                    szo6 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu + self.mezo[i4].betu + self.mezo[i5].betu + self.mezo[i6].betu
                                                                                    if not szo6 in szav6:
                                                                                        if (szo6 in magyar[3][0]):
                                                                                            szav6.append(szo6)
                                                                                    if (szo6 in magyar[3][1]) or (szo6 in magyar[3][2]) or (szo6 in magyar[3][3]):
                                                                                        for i7 in range(9):
                                                                                            if i1!=i7 and i2!=i7 and i3!= i7 and i4!=i7 and i5!=i7 and i6!=i7:
                                                                                                if abs(self.mezo[i7].x - self.mezo[i6].x)<=1 and abs(self.mezo[i7].y - self.mezo[i6].y)<=1:
                                                                                                    szo7 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu + self.mezo[i4].betu + self.mezo[i5].betu + self.mezo[i6].betu + self.mezo[i7].betu
                                                                                                    if not szo7 in szav7:
                                                                                                        if (szo7 in magyar[4][0]):
                                                                                                            szav7.append(szo7)
                                                                                                    if (szo7 in magyar[4][1]) or (szo7 in magyar[4][2]):
                                                                                                        for i8 in range(9):
                                                                                                            if i1!=i8 and i2!=i8 and i3!=i8 and i4!=i8 and i5!=i8 and i6!=i8 and i7!=i8:
                                                                                                                if abs(self.mezo[i8].x - self.mezo[i7].x)<=1 and abs(self.mezo[i8].y - self.mezo[i7].y)<=1:
                                                                                                                    szo8 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu + self.mezo[i4].betu + self.mezo[i5].betu + self.mezo[i6].betu + self.mezo[i7].betu + self.mezo[i8].betu
                                                                                                                    if not szo8 in szav8:
                                                                                                                        if (szo8 in magyar[5][0]):
                                                                                                                            szav8.append(szo8)
                                                                                                                    if (szo8 in magyar[5][1]):
                                                                                                                        for i9 in range(9):
                                                                                                                            if i1!=i9 and i2!=i9 and i3!=i9 and i4!=i9 and i5!=i9 and i6!=i9 and i7!=i9 and i8!=i9:
                                                                                                                                if abs(self.mezo[i9].x - self.mezo[i8].x)<=1 and abs(self.mezo[i9].y - self.mezo[i8].y)<=1:
                                                                                                                                    szo9 = self.mezo[i1].betu + self.mezo[i2].betu + self.mezo[i3].betu + self.mezo[i4].betu + self.mezo[i5].betu + self.mezo[i6].betu + self.mezo[i7].betu + self.mezo[i8].betu + self.mezo[i9].betu
                                                                                                                                    if not szo9 in szav9:
                                                                                                                                        if (szo9 in magyar[6][0]):
                                                                                                                                            szav9.append(szo9)
        self.lehetszavak = [szav3, szav4, szav5, szav6, szav7, szav8, szav9] #visszaadja a megtalált szavak listáit
        for i in range(7):
            self.max.set(self.max.get() + len(self.lehetszavak[i])*(i+3))
        self.osszesszo = 0
        for i in range(len(self.lehetszavak)):
            self.osszesszo = self.osszesszo + len(self.lehetszavak[i])
            self.lehet[i][1].set(len(self.lehetszavak[i]))
        t1 = time() #eddig mennyi idő alatt fut le?
        print(t1-t0, 's') #a futási idő mérése, kiíratása

if __name__ == '__main__':
    jatek = Szokereso()
    jatek.ablak.mainloop() #eseményfigyelő indítása
