def sominha(lista):
    soma = 0
    for num in lista :
        soma = soma + num["numeros"]

    return soma

print(sominha([{"numeros" : 3}, {"numeros": 5}]))