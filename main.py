import time
arquivo = open("letra.txt", "r")
habilitado = arquivo.readable()


if habilitado == True:
    print("Arquivo habilitado para leitura.")
    time.sleep(1)
else:
    print("O arquivo não pôde ser lido.")
    

linha = arquivo.readline()

while linha:
    print(linha)
    linha = arquivo.readline()
    time.sleep(1)

arquivo.close()
