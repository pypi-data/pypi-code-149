import os

def CreateDirectory(directory_path: str):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)