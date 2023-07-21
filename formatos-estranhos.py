# None
avaliacao = None
print(avaliacao) # None : quando nn temos o valor para colocar numa variável
avaliacao = 10.0
print(avaliacao) # 10.0
 
# Strings formatadas 
# 
nome = "Airton"
sobrenome = "Sampaio de Sobral"
idade = 32
dados = f"Nome Completo: {nome} {sobrenome}, Idade: {idade}"
print(dados) # Nome Completo: Airton Sampaio de Sobral, Idade: 32
 
# Dicionários
#ex abaixo: 
compras_china = {
    "blusa": 3,
    "meia": 5,
    "bolsa": 1
}
print(compras_china)
compras_china["blusa"] = 4
print(compras_china["blusa"])
# print(compras_china["sapato"]) # KeyError: 'sapato'
print(compras_china.get("sapato", None)) # me entregue o valor da chave sapato e me retorne o valor None
print(compras_china.get("sapato", 0)) 
# ".get" é 
 
# Função 
# ex abaixo:
def somar(num, outro_num):
    return num + outro_num
# acima, eu estou criando duas funçoes e definindo ela a uma outra funçao, e me retorna a soma delas 
print(somar(3, 5))
print(somar(0.7, 3.5))
 
# Classes
class ContaBancaria:
    def __init__(self, num_conta, dono_conta, saldo=0.0):
        self.num_conta = num_conta
        self.dono_conta = dono_conta
        self.saldo = saldo
 
    def depositar(self, valor):
        self.saldo += valor
 
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente!")
 
    def __str__(self):
        return f"Número conta: {self.num_conta}, Dono conta: {self.dono_conta}, Saldo: {self.saldo}"
 
 
conta_airton = ContaBancaria(230, "Airton Sampaio de Sobral", 10.0)
print(conta_airton)
conta_airton.depositar(50000)
print(conta_airton)
conta_airton.sacar(55000)
print(conta_airton)
conta_airton.sacar(5000)
print(conta_airton)
 
# Módulos
 
import utils
 
print(utils.subtrair(5, 3))
 
from utils import subtrair
 
print(subtrair(3, 5))
 
# Exceções
 
#num = 20/0 # ZeroDivisionError: division by zero
#int("bola") # ValueError: invalid literal for int() with base 10: 'bola'
 
try:
    num = 20/0
    #int("bola")
except ZeroDivisionError as exc:
    print(f"Erro, não dá para dividir por zero! {exc}")
except ValueError as exc:
    print(f"Erro, valor inválido! {exc}")
 
 
# Servidor web
# $ pip install flask
# Criar arquivo servidor.py
'''
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
'''
# $ flask --app servidor run
# Comandos úteis:
# CTRL + C para matar o programa
# Seta para cima no terminal para repetir o último comando digitado