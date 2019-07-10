import subprocess

print("Starting websocket server")
subprocess.run(["yarn"], cwd="./websocket")
subprocess.Popen(["yarn", "prod"], cwd="./websocket")
print("Starting django server")
subprocess.run(["python3.7", "manage.py", "runserver", "0.0.0.0:8080"], cwd="./serverless")
