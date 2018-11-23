class Cella:                                        #az egyes cellák osztálya
    def __init__(self, i=1, j=1, b = 'A'):          #jellemzők: két koordináta és egy betű
        self.x = i
        self.y = j
        self.betu = b
    def kiir(self):                                 #függvény minden jellemző kiírására
        print(str(self.x) + ', ' + str(self.y) + ': ' + str(self.betu), sep='')
    def kiir_betu(self):                            #függvény csak a betű kiírására
        print(str(self.betu))
    def kiir_koord(self):                           #függvény a koordináták kiírására
        print('x = ' + str(self.x) + ', y = ' + str(self.y), sep='')
