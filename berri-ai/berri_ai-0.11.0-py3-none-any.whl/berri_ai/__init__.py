__version__ = '0.11.0'
import ast 
import re
import os 
import traceback
import time
import pipreqs
import subprocess

def traverse_ast(tree_dict, code, tree, global_dict):
  for node in tree.body:
      if isinstance(node, ast.Assign):
        value_source = ast.get_source_segment(code, node)
        # print("value_source: ", value_source)
        str_split = value_source.split("=", 1)
        key_val = str(str_split[0]).strip()
        value = str(str_split[1]).strip()
        tree_dict[key_val] = value_source
      elif isinstance(node, ast.ClassDef):
          # print(node.name)
          tree_dict[node.name.strip()] = ast.get_source_segment(code, node)
      elif isinstance(node, ast.FunctionDef):
          # print(node.name)
          tree_dict[node.name.strip()] = ast.get_source_segment(code, node)
      elif isinstance(node, ast.Import):
          value_source = ast.get_source_segment(code, node)
          print("value_source in import: ", value_source)
          for name in node.names:
            print("name: ", name.name)
            tree_dict[name.name] = value_source
            split_names = name.name.split(".")[0]
            tree_dict[split_names] = value_source
      elif isinstance(node, ast.ImportFrom):
          value_source = ast.get_source_segment(code, node)
          for name in node.names:
            tree_dict[name.name] = value_source

def check_requirements(package):
    with open('./berri_files/requirements.txt', 'r') as file:
        content = file.read()
        if package not in content:
            with open('./berri_files/requirements.txt', 'a') as file2:
                file2.write(package)

def get_dependencies(code_segment_list, global_dict):
    # Run function in a sandbox and catch ImportErrors
    dep_modules = None
    print("new list")
    for i in range(10):
      dep_modules = []
      try:
        print("code_segment_list: ", code_segment_list)
        for code_segment in code_segment_list:
          # exec(print(dir()))
          print("code_segment: ", code_segment)
          exec(code_segment, global_dict)
          # func()  # Try to run function in the sandbox
      except ModuleNotFoundError as e:
        text = e.args[0]
        match = re.search(r"'(.*)'", text)
        if match:
            package_name = match.group(1)
            check_requirements(package_name)
            print("module not found in dep exec: ", package_name)
            install_statements = []
            install_statements.append("import subprocess")
            install_statements.append(str("""subprocess.call(['pip', 'install','""" + package_name + "'])"))
            for install_statement in install_statements:
              exec(install_statement)
      except Exception as e:
        print(e)
        traceback.print_exc()
        if hasattr(e, 'name'):
          print(e.name)
          dep_modules.append(e.name)  # Add module that caused error
        else:
            print(e.args)
            text = e.args[0]
            print("text: ", text)
            pattern = r"pip install (\w+)"
            print(type(text))
            print(isinstance(text, list))
            print(len(text))
            if isinstance(text, list):
              text = str(text[0])
              print("text cleaned up: ", text)
            match = re.search(pattern, text)
            if match:
              print("validation error here")
              package_name = match.group(1)
              print("Package name to install:", package_name)
              install_statements = []
              install_statements.append("import subprocess")
              install_statements.append(str("""subprocess.call(['pip', 'install','""" + package_name + "'])"))
              for install_statement in install_statements:
                exec(install_statement)
            match = re.search(r"'(.*)'", text)
            if match:
                print("dependency module error here")
                quoted_text = match.group(1)
                print(quoted_text)
                dep_modules.append(quoted_text)
    return dep_modules

def run_loop(code_list, tree_dict, global_dict):
  for i in range(20):
    print(i)
    dependencies = get_dependencies(code_list, global_dict)
    print("dependencies: ", dependencies)
    if len(dependencies) == 0:
      break
    for dependency in dependencies:
      # print("dependency: ", dependency)
      code = tree_dict[dependency]
      # print("dependency parent_dependency: ", parent_dependency)
      code_list.insert(0, code)
  return code_list


def save_requirements(path):
  print("reaches save requirements")
  subprocess.run(["pipreqs", "--mode", "no-pin", path])
  
def get_requirements(line):
  line_split = line.split(' && ')
  requirements = []

  for line in line_split:
    line_split_2 = line.split(' ')
    package = line_split_2[-1]
    requirements.append(package)
  
  return requirements


def deploy():
  from google.colab import _message
  print("Begun deployment.. ")

  print("Converting notebook to python and generating requirements.txt 🐍")

  print("Building docker image 😱")

  print("Deploying endpoint ... ⌛️")
  
  print("You're agent has been deployed! 🎉 🎉")
  print("This is your frontend 👉 https://berri.ai/0849121429")
  print("This is your api endpoint 👉 https://berri.ai/api/0849121429?user_query=")
  # assume you're in a google colab 
  if not os.path.exists('./berri_files/'):
    os.mkdir("./berri_files/")

  # Obtain the notebook JSON as a string
  notebook_json_string = _message.blocking_request('get_ipynb', request='', timeout_sec=5)

  # save to temporary file
  lines = []
  requirements = []
  for cell in notebook_json_string["ipynb"]["cells"]:
    for line in cell["source"]:
      if line.startswith("!pip install"):
        requirements.append(get_requirements(line))
        # continue
      elif not line.startswith("!"):
        lines.append(line)
  
# get the variable name
# replace with new name 
  original_agent_name = None
  f = open("./berri_files/agent_code.py", "w")
  for line in lines:
    if original_agent_name and original_agent_name + ".run(" in line: # if it exists and is being executed, replace that line
      line = line.replace(original_agent_name + ".run(", "agent.run(")
      f.write(line + "\n")
    if "initialize_agent(" in line:
      initialization_line = line.split("=", 1)
      original_agent_name = initialization_line[0].strip() # get the original agent variable name
      print("original_agent_name: ", original_agent_name)
      initialization_line = "agent = " + initialization_line[1]
      print(initialization_line)
      f.write(initialization_line + "\n")
    else:
      f.write(line + "\n")
  f.close()
  
  # save the requirements to a requirements.txt file 
  save_requirements("./berri_files")

  if len(requirements) > 0: 
    with open('./berri_files/requirements.txt', 'a') as f:
      for requirement in requirements:
        for r in requirement:
          print("requirement: ", r)
          f.write("\n" + r + '\n')


  # find the executing line
  agent_executing_line = "agent.run("
  
  with open("./berri_files/agent_code.py") as f:
      lines = f.readlines()
  
  with open("./berri_files/agent_code.py") as f:
      code = f.read()

  tree = ast.parse(code)
  tree_dict = {}
  global_dict = {}
  # traverse the file and create a dictionary
  traverse_ast(tree_dict, code, tree, global_dict)
  print("global_dict: ", global_dict)
  print("tree_dict: ", tree_dict)
  import_statements = []
  for line in lines:
    if agent_executing_line in line:
      print(line)
      agent_executing_line = line.strip() # find the executing line 
    elif line.startswith("import"):
      import_statements.append(line)

  run_loop(import_statements, tree_dict, global_dict)
  print(import_statements)

  parent_dependencies = []
  
  for key in tree_dict:
    if "os" in key:
      parent_dependencies.append(tree_dict[key])
  
  print("parent_dependencies: ", parent_dependencies)
  
  run_loop(parent_dependencies, tree_dict, global_dict)

      
  code_segment_list = [agent_executing_line]
  code_segment_list = import_statements + parent_dependencies + code_segment_list
  print("running main code now")
  run_loop(code_segment_list, tree_dict, global_dict)

  print("Done!")