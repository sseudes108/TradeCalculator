import subprocess

arquivo = ["services", "passwd"]
palavras = ["ssh", "3389", "22", "80"]

comando = "cat /etc/passwd | grep {} > file.txt".format("eudes")
subprocess.run(comando, shell=True)

for palavra in palavras:
    comando = "cat /etc/{} | grep {} >> file.txt".format(arquivo[0], palavra)
    subprocess.run(comando, shell=True)


print("Arquivo file.txt criado")