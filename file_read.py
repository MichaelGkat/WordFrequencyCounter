

def read_file(filename : str) -> str:
    try:
        with open(filename, 'r') as file:
            return file.read()
    
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return ""