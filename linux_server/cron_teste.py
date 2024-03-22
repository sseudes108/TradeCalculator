import subprocess

def criar_log():
    log = ler_log() + 1

    log_file = open("log.txt", "w", encoding='utf-8')
    log_file.write("{}".format(log, end=""))
    log_file.close()

    new_log_file = open("log{}.txt".format(log), "w", encoding='utf-8')
    new_log_file.write("{}".format(log, end=""))
    new_log_file.close()

    processo = "cat /var/log/syslog | tail -n 10 >> log{}.txt".format(log)
    subprocess.run(processo)

def ler_log():
    log_file = open("log.txt", "r")
    log = log_file.read()
    print("current log", log)
    log_file.close()
    return int(log)

criar_log()

