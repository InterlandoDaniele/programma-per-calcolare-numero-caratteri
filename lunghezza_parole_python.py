def lunghezza_parole(lista_parole):
    lunghezza = []
    for parola in lista_parole:
        lunghezza.append(len(parola))
    return lunghezza
lista_parole_input = ["buongiorno", "buonanotte", "caffè", "andiamo"]
lista_lunghezza_output = lunghezza_parole(lista_parole_input)
print(lista_lunghezza_output)
