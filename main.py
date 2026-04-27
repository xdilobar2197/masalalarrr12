# masalalarrr12



class Telefon:
    def __init__(self, marka, rang, yil):
        self.marka = marka
        self.rang = rang
        self.yil = yil

    def info(self):
        print(f'marka: {self.marka}')
        print(f'rang: {self.rang}')
        print(f'yil: {self.yil}')

k1 = Telefon("iPhone 13", "qora", 1200)
k2 = Telefon("Samsung S21", "oq", 900)
k1.info()
k2.info()
