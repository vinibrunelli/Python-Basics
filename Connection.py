import netmiko
import time

###########################################
# Conexao ssh 
###########################################

if __name__ == "__main__":
    device = {
        "device_type": 'terminal_server',
        "ip": '163.123.181.60',
        "port": 22,
        "username": 'administrator',
        "password": 'kl8#9!cc',
        "ssh_config_file": '/root/.ssh/config'
    }
    conexao = netmiko.ConnectHandler(**device)
    
 
#print(conexao.send_command("cat /tmp/sh-int-status"))
    saidaComando = (conexao.send_command("cat /tmp/sh-int-status"))

#  conexao.write_channel("\n")
#   time.sleep(1)
#    output = conexao.read_channel()
#    print(saida)

    file = open("saidaConexao.csv","a")
    file.write(saidaComando)
    file.close()
 
    csv = open('output.csv','a')
    csv.write('INDEX,HOSTNAME,INTERFACE')
    csv.close()