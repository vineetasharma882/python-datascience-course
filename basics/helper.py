import os 

def read(file):
    if os.path.exists(file):
        with open(file, errors="ignore") as f:
            return f.read()
    return 'File Not Found'