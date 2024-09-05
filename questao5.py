print("digite uma frase para ser invertida:")
frase = input()

def inverter_frase (frase):
    inverter = []
    frase = frase.split(" ")
    for word in frase:
        word = word[::-1]
        inverter.append(word)
    resp = " ".join(inverter)
    return resp
print (inverter_frase(frase))

