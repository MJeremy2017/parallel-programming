import os
import subprocess

print("Running calling process ...")
subprocess.Popen('echo $PATH', shell=True)
os.execvp(file="python3", args=["python3", "called_process.py"])
print("Done execution")
