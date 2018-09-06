import subprocess
import os
import time

files = ['add1.py', 'add2.py']
command = "python"
processes = set()
max_processes = 5

for name in files:
    processes.add(subprocess.Popen([command, name]))
    if len(processes) >= max_processes:
        os.wait()
        processes.difference_update([p for p in processes if p.poll() is not None])
            
