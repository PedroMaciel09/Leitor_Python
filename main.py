import time
arquivo = open("letra.txt", "r")
habilitado = arquivo.readable()


if habilitado == True:
    print("Arquivo habilitado para leitura.")
    time.sleep(2)
else:
    print("O arquivo não pôde ser lido.")
    

print(arquivo.readlines())

arquivo.close()