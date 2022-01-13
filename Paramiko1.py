import paramiko
import time

ip='192.168.0.10'
port=22
username='cisco'
password='cisco'


#----------------------------------------------------------#

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, username, password)



def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(65535)
        
        
conexao= ssh.invoke_shell()
#output =clear_buffer(conexao)
#time.sleep(2)
conexao.send("enable \n")
output =conexao.recv(6000)
conexao.send("cisco\n")
output =conexao.recv(6000)
time.sleep(1)
conexao.send("sh version\n")
time.sleep(3)
output =conexao.recv(6000)
#print(output)
saida = ' '.join(map(str, output))
print(saida)

#### VERSION ###
#
#stdin, stdout, stderr = ssh.exec_command("sh version")
#lines2 = stdout.readlines()
##print(' '.join(map(str, lines)))
#output2 = ' '.join(map(str, lines2))
#saida2 = output.split()
#print(saida2[7])





ssh.close()
