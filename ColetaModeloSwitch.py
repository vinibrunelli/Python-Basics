import netmiko
import csv

usuario = "user"
senha = "pass"

switches = open('devices.txt','r')
index=0

def coleta(conexao):        

        ###   Hostname   ###   
        comando = (conexao.send_command('sh run | i hostname'))
        spliter = comando.split() 
        hostname = spliter[1]

        ###   Modelo   ###
        
        comando = (conexao.send_command('sh ver | i (cisco WS|cisco C)'))
        spliter = comando.split() 
        modelo = spliter[1]
        
        #comando = (conexao.send_command('sh ver |  i of memory'))
        ####modelo = comando[6:18]
        #spliter = comando.split() 
        #modelo = spliter[1]
            
        ###   CTS   ###        
        comando = (conexao.send_command('sh cts environment-data'))
        envData = comando        
        if "Successful" in envData:
            cts = ("ok")
        else:
            cts = ("nok")

        ###   Version   ###

        if modelo == "WS-C3850-48P" or "C9300-48U":
            comando = (conexao.send_command('sh ver | i (BUNDLE|INSTALL)'))
            spliter = comando.split() 
            version = spliter[4]
        else:
            version = "Desconhecido"


        ###   Finalizando a coleta  ###
        print(f"#{index},{ip},{hostname}")  
        return hostname,modelo,version,cts


with open ('consolidado.csv', 'a', newline='') as file:
   wr = csv.writer(file)
   wr.writerow(["INDICE","IP","HOSTNAME","MODELO","Version","TRUSTSEC"])

for ip in switches.read().split('\n'):
        device = {
          'device_type': 'cisco_ios',
          'ip': ip,
          'username': usuario,
          'password': senha,
          'secret': senha,
          'timeout': 15,
        }
        index = index +1
        try:
           conexao = netmiko.ConnectHandler(**device)
        except:
           with open ('consolidado.csv', 'a', newline='') as file:
              wr = csv.writer(file)
              wr.writerow([index,ip,"SEM CONEXAO"])        
        else:
            retorno = coleta(conexao)
            with open ('consolidado.csv', 'a', newline='') as file:
               wr = csv.writer(file)
               wr.writerow([index,ip,retorno[0],retorno[1],retorno[2],retorno[3]])
            conexao.disconnect()