import csv
import pandas

file1= input("Arraste aqui o arquivo 1:")

with open(file1, 'r') as t1, open('b.txt', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

#with open('Diff.csv', 'w') as outFile:

#    for line in filetwo:
#        if line not in fileone:
#            outFile.write(line)
#   outFile.write('Interface,Status'+"\n")

    fields = ['INTERFACE','STATUS','VLAN','DUPLEX','SPEED','BASE']
    
    for line in filetwo:
        if line not in fileone:
            saida = line.split('                        ')
            print(saida)
    
 #   csv = open('novaDiff', 'a')
 #   csv.write(saida)
 #   csv.close()

with open('Diff', 'w') as f:
          write = csv.writer(f)
          
          write.writerow(fields)
          write.writerows(line)
                        

    