import os
import subprocess

print("Running calling process ...")
subprocess.Popen('echo $PATH', shell=True)
# this runs and replaces the existing process
os.execvp(file="python3", args=["python3", "called_process.py"])
print("Done execution")
