import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
script_absolute_path = os.path.join(script_dir, "shell.sh")

print(f"Attempting to run script at: {script_absolute_path}")

subprocess.call(["sh", script_absolute_path])
