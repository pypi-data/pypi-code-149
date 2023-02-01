__version__ = '0.9.4'
from google.colab import _message
import ast 
import re
import os 
import traceback
import time
import pipreqs
import subprocess
import requests
import shutil

def get_dependencies(path):
    subprocess.run(["pipreqs", path])


def send_files(user_email):
    url = f'https://berriserverv2.krrishdholakia.repl.co/berri_orchestrator?user_email={user_email}'
    agent_code = open('./berri_files/agent_code.py', 'rb')
    requirements = open('./berri_files/requirements.txt', 'rb')
    
    files = {
             'agent_code': agent_code,
             'requirements': requirements
            }

    response = requests.get(url, files=files)
    print(response.json())


def read_file_copy_files_folders(line):
  # Check if the line contains a path to a file or folder
  print("reading file copy")
  path = re.search(r'"([^"]*)"', line)
  if path: 
      # Check if the path exists
      print(path.group(1))
      if os.path.exists(path.group(1)):
        print("path os: ", path.group(1))
        # Copy the file/folder to the berri_files folder
        if os.path.isdir(path.group(1)):
          for file in os.listdir(path.group(1)): 
            new_filepath = shutil.copy(os.path.join(path.group(1), file), 'berri_files')
        else:
            new_filepath = shutil.copy(path.group(1), 'berri_files')
        # Update the line with the new filepath
        if new_filepath:
          line = re.sub(r'"([^"]*)"', '"' + new_filepath + '"', line)     
  return line 


def deploy(user_email: str):
  print("Begun deployment.. If you hit any problems/errors, let us know in the Discord (https://discord.gg/KvG3azf39U) and we'll help you out.")

  print("Converting notebook to python and generating requirements.txt 🐍")
  if not os.path.exists('./berri_files/'):
    os.mkdir("./berri_files/")
  # Obtain the notebook JSON as a string
  notebook_json_string = _message.blocking_request('get_ipynb', request='', timeout_sec=15)

  # save to temporary file
  lines = []
  for cell in notebook_json_string["ipynb"]["cells"]:
    for line in cell["source"]:
      if line.startswith("!pip install"):
        continue
      elif not line.startswith("!"):
        # if it's a local or google drive imported file -> scp it into the berri_files folder
        lines.append(line)
  
  f = open("./berri_files/agent_code.py", "w")
  for line in lines:
    if "initialize_agent(" in line:
      initialization_line = line.split("=", 1)
      initialization_line = "agent = " + initialization_line[1]
      f.write(initialization_line + "\n")
    else: 
      line = read_file_copy_files_folders(line)
      f.write(line + "\n")
  f.close()
  
  get_dependencies("./berri_files")   

  print("Building docker image.. this might take a 1-2 minutes 😱")
  
  send_files(user_email)

  print("Deploying endpoint ... expect an email from us in 5-10 minutes @ " + user_email + " ⌛️")
  
  # assume you're in a google colab 
  print("hello world")
  