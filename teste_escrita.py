import subprocess

arquivo = ["services", "passwd"]
palavras = ["ssh", "3389", "22", "80"]

comando = "cat /etc/passwd | grep eudes > file.txt"
subprocess.run(comando, shell=True)

index = 0
for palavra in palavras:
    comando = "cat /etc/{} | grep {} >> file.txt".format(arquivo[index], palavra)
    subprocess.run(comando, shell=True)
    index += 1

print("Arquivo file.txt criado")