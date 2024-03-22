import subprocess

arquivo = ["services", "passwd"]
palavras = ["ssh", "3398"]

for palavra in palavras:
    comando = "cat /etc/{} | grep {} > file.txt".format(arquivo[0], palavra)
    subprocess.run(comando, shell=True)

comando = "cat /etc/{} | grep {} > file2.txt".format(arquivo[1], "eudes")
subprocess.run(comando, shell=True)

comando = "cat file.txt | grep {} >> file2.txt".format(arquivo[1], "eudes")
subprocess.run(comando, shell=True)

