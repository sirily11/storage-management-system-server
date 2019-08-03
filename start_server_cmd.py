import subprocess
import threading


def start():
    subprocess.run('yarn prod', shell=True,
                   cwd="./websocket")


def start2():
    subprocess.run("python3 manage.py runserver 0.0.0.0:8080", shell=True
                   , cwd="./serverless")


if __name__ == '__main__':
    t1 = threading.Thread(target=start)
    t2 = threading.Thread(target=start2)
    t1.start()
    t2.start()
