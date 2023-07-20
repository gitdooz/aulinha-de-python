#idade = 15
#pode_entrar_no_cinema = (idade >= 15 and idade <= 40)
#pode_entrar_no_cinema = (idade < 15 or idade > 40)
#pode_entrar_no_cinema = (idade < 15 or (idade > 40 and idade <50))

preco_medio = input("Qual é o preço de um PS5? ")
preco_medio = int(preco_medio)
preco_maior_e_menor = preco_medio > 3500 and preco_medio <= 4500
print(preco_maior_e_menor)

#Airtonzi fez assim:
#preco = input("Valor que tu acha: ")
#preco = int(preco)
#print(preco > 3500 and preco <= 4500)
