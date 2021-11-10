#função com print
def checaIdade(userAge):
    userAgeCast = int(userAge)
    if userAgeCast > 18:
        print("Você é maior de idade")
    elif (userAgeCast < 18) & (userAgeCast > 0):
        print("Você é menor de idade.")
    else:
        print("Digitou errado amigão")

y = checaIdade(32)
print(y)

#Função com return
def checaIdadeReturn(userAge):
    userAgeCast = int(userAge)
    if userAgeCast > 18:
        return ("Você é maior de idade")
    elif (userAgeCast < 18) & (userAgeCast > 0):
        return("Você é menor de idade.")
    else:
        return("Digitou errado amigão")
x = 12
resposta = checaIdadeReturn(x)
print(resposta)
#ou direto
print(checaIdade(13))

