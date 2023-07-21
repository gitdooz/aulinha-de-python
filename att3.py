def funcaonzi(entradinha):
    total = 0
    for x in entradinha:
        total = total + x["pontos"]

    return total 

funcaonzi([{"pontos" : 3}, {"pontos": 5}])   