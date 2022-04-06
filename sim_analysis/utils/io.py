# testar a existência do diretório e criá-lo
import os

def check_dir(path):
    try:
        os.mkdir(path)
    except FileNotFoundError:
        print(f'Check the parent directories from {path}')
    except FileExistsError:
        print(f'The directory {path} exists')

    print(f'Saving files in {path}')