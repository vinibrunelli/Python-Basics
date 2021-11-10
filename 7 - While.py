
def checaIdade(userAge):
   try:
        userAgeCast = int(userAge)
        if userAgeCast > 18:
            return ("Você é maior de idade")
        elif (userAgeCast < 18) & (userAgeCast > 0):
            return("Você é menor de idade.")

   except ValueError:
       return("Banhou-se nas aguas do equívoco.")
x="y"
while x == "y":
    userInput = input("Entre com a idade")
    print(checaIdade(userInput))
    x = input("Deseja cotinuar? (Y/N)")