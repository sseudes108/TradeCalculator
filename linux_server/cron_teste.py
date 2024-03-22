import subprocess
import os

def criar_log():
    home_dir = os.path.expanduser("~")
    log_path = os.path.join(home_dir, "logs/")
    log = ler_log(log_path) + 1

    with open("{}log.txt".format(log_path), "w", encoding='utf-8') as log_file:
        log_file.write("{}".format(log, end=""))

    with open("{}log{}.txt".format(log_path, log), "w", encoding='utf-8') as new_log_file:
        new_log_file.write("{}".format(log, end=""))

    processo = ["tail", "-n", "10", "/var/log/syslog"]
    with open("{}log{}.txt".format(log_path, log), "w", encoding='utf-8') as new_log_file:
        subprocess.run(processo, stdout=new_log_file)

def ler_log(log_path):
    log_file = open("{}log.txt".format(log_path), "r")
    log = log_file.read().strip()
    print("current log", log)
    log_file.close()
    return int(log)


criar_log()
