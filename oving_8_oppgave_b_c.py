spm = []
alt = []
poeng_spiller_1 = 0
poeng_spiller_2 = 0

class Sporsmaal:
    def __init__(self, sporsmaal, alternativer, korrekt_svar):
        self.sporsmaal = sporsmaal
        self.alternativer = alternativer
        self.korrekt_svar = korrekt_svar

    def __str__(self):
        resultat = self.sporsmaal + "\nSvaralternativer:\n"
        for index, verdi in enumerate(self.alternativer):
            resultat += f"{index}: {verdi}\n"
        return resultat
    
    def sjekk_svar(self, svaret):
        if svaret == self.korrekt_svar:
            return True
        else:
            return False

    def korrekt_svar_tekst(self):
            rett = self.korrekt_svar
            string = "Korrekt svar:" + self.alternativer[rett] + "\n\n"
            return string

def lag_spm():
    with open('sporsmaalsfil.txt', 'r', encoding="utf-8") as textfil:
        for line in textfil:
            x = line.split(":")
            alt = x[2].split(",")
            for j in range(len(alt)):
                alt[j] = alt[j].strip()
                alt[j] = alt[j].strip("[]")
            y = Sporsmaal(x[0], alt, int(x[1].strip()))
            spm.append(y)

if __name__ == "__main__":
    lag_spm()
    for i in range(len(spm)):
        sp1 = spm[i]
        print(f"Spørsmål {i + 1}: ")
        print(sp1)
        svar1 = int(input("Spiller 1 sitt svar: "))
        svar2 = int(input("Spiller 2 sitt svar: "))
        print("\n")
        print(sp1.korrekt_svar_tekst())
        if sp1.sjekk_svar(svar1):
            poeng_spiller_1 += 1
            print("Spiller 1 svarte rett!")
        if sp1.sjekk_svar(svar2):
            poeng_spiller_2 += 1
            print("Spiller 2 svarte rett!")
        if sp1.sjekk_svar(svar1) is False:
            print("Spiller 1 svarte feil!")
        if sp1.sjekk_svar(svar2) is False:
            print("Spiller 2 svarte feil!")
        else:
            pass
        print("\n")
    print(f"Spillet er over!")
    print(f"Spiller 1 svarte rett på {poeng_spiller_1} spørrsmål")
    print(f"Spiller 2 svarte rett på {poeng_spiller_2} spørrsmål")
