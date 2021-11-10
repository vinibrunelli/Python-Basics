minuto = 60
hora = 60
dia = 24

#function with 2 parameters
def qntminutos(qntDia,frase):
    return (f"{qntDia} dias é igual a {qntDia * dia} horas, em minutos são {qntDia * dia * minuto}  - {frase}")

#calling functions
qntminutos(4, "Chamando direto")


#input calling function with return
userInput = int(input("Entre com a quantidade de dias:\n"))

#chamando como resposta da variavel
user_calculated = qntminutos(userInput,"Dentro da varivável")
print(user_calculated)

#chamando direto do print
print(qntminutos(userInput,"Direto no print"))

check = 1>0
print(check)
#true