class Atom:

    def __init__(self,symbol, atomic, mass, isotope=12):
        self.symbol = symbol
        self.atomic = atomic
        self.mass = mass
        self.isotope = isotope
    
    def neutrons(self):
        number = self.isotope - self.atomic
        print(f"neutrons",self.symbol, number)
        return number
    def grams_to_moles(self,grams):
        moles = grams/self.mass
        print(f"moles",moles)
        return moles


if __name__=="__main__":
    oxygen = Atom("O", 8, 15.999, 16)

    carbon = Atom("C", 6, 12.001, )
    
    oxygen.neutrons()
    oxygen.grams_to_moles(24)
    carbon.grams_to_moles(24)
