def izracunaj_podobnostni_rezultat(levo_seznam, desno_seznam):
    # Ustvari slovar za štetje pojavitev števil v desnem seznamu
    stevci_desno = {}
    for stevilo in desno_seznam:
        if stevilo in stevci_desno:
            stevci_desno[stevilo] += 1
        else:
            stevci_desno[stevilo] = 1

    # Izračunaj podobnostni rezultat
    podobnostni_rezultat = 0
    for stevilo in levo_seznam:
        pojavitev = stevci_desno.get(stevilo, 0)  # Število pojavitev v desnem seznamu (privzeto 0)
        podobnostni_rezultat += stevilo * pojavitev

    return podobnostni_rezultat


def preberi_podatke_iz_datoteke(ime_datoteke):
    # Prebere pare števil iz datoteke in vrne dva seznama
    levo_seznam = []
    desno_seznam = []

    with open(ime_datoteke, 'r') as datoteka:
        for vrstica in datoteka:
            # Razdeli vrstico in pretvori številke v cela števila
            stevila = vrstica.split()
            levo_seznam.append(int(stevila[0]))  # Število iz levega stolpca
            desno_seznam.append(int(stevila[1]))  # Število iz desnega stolpca

    return levo_seznam, desno_seznam


# Preberi podatke iz datoteke
ime_datoteke = 'data.txt'
levo_seznam, desno_seznam = preberi_podatke_iz_datoteke(ime_datoteke)

# Izračunaj podobnostni rezultat
podobnostni_rezultat = izracunaj_podobnostni_rezultat(levo_seznam, desno_seznam)

# Izpiši rezultat
print(f"Podobnostni rezultat: {podobnostni_rezultat}")
