class Conto:
    def __init__(self, soldi,codice):
        self.soldi = soldi
        self.codice = codice

    def getSoldi(self):
        return self.soldi
    def getCodice(self):
        return self.codice
    def transfer(self):
        if int (input("PIN: ")) == self.codice:
            s = input(" Quantità di soldi da trasferire: ")
            if int(s) > self.soldi:
                print("Impossibile trasferire, importo sul conto insufficiente.")
            else:
                print("Denaro Trasferito")
                self.soldi= self.soldi - int(s)
                print("Importo restante: $ " + str(self.soldi))
        else:
            print("Pin Errato")



if __name__ == "__main__":
    cliente = Conto(1000000, 1111)
    cliente.transfer()



