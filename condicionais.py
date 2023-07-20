# 
#if idade < 20:
#   print("novinho")
#elif idade < 30:
#   print("Jovem pow")
#elif idade < 40:
#   print("Velho")
#else:
#   print("Múmia dmsss")

distancia = input("Insira uma determinada distância: ")
distancia = int(distancia)
tipo_distancia = input("Agora, insira o tipo de distância: ")

if tipo_distancia == "mm":
    print(str(distancia) + "mm")
    
elif tipo_distancia == "cm":
    centimetros = distancia * 100
    print(str(centimetros) + "mm")
    
elif tipo_distancia == "dm":
    decimetros = distancia * 1000
    print(str(decimetros) + "mm")

elif tipo_distancia == "m":
    metros = distancia * 10000
    print(str(metros) + "mm")

else:
    print("Medida inválida")
    
    
