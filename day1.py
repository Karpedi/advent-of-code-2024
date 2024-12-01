def izracunaj_skupno_razdaljo(levo_seznam, desno_seznam):
    # Sortiraj oba seznama
    levo_seznam.sort()
    desno_seznam.sort()

    # Inicializiraj skupno razdaljo
    skupna_razdalja = 0

    # Prehodi skozi pare elementov
    for levo, desno in zip(levo_seznam, desno_seznam):
        # Izračunaj absolutno razliko med vsakim parom
        skupna_razdalja += abs(levo - desno)

    return skupna_razdalja


def preberi_podatke_iz_datoteke(ime_datoteke):
    # Prebere pare številk iz datoteke in vrne dva seznama
    levo_seznam = []
    desno_seznam = []

    with open(ime_datoteke, 'r') as datoteka:
        for vrstica in datoteka:
            # Razdeli vrstico in pretvori številke v cele števile
            stevila = vrstica.split()
            levo_seznam.append(int(stevila[0]))  # 5-mestno število za levi seznam
            desno_seznam.append(int(stevila[1]))  # 5-mestno število za desni seznam

    return levo_seznam, desno_seznam


# Preberi podatke iz datoteke
ime_datoteke = 'data.txt'
levo_seznam, desno_seznam = preberi_podatke_iz_datoteke(ime_datoteke)

# Izračunaj skupno razdaljo
skupna_razdalja = izracunaj_skupno_razdaljo(levo_seznam, desno_seznam)

# Izpiši rezultat
print(f"Skupna razdalja: {skupna_razdalja}")
