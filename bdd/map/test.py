from csv import reader
import os

def find_project_file(filename):
    current_dir = os.getcwd()
    data_folder = os.path.join(current_dir, 'bdd', 'data')
    if os.path.exists(data_folder):
        return f'{data_folder}/{filename}'
    else:
        raise FileNotFoundError(f"The file '{filename}' does not  not found within the 'bdd/data' folder or not found in the directory structure.")

def ler_csv_cenario(massa:str,cenario:str):
    caminho = find_project_file(f'{massa}.csv')
   
    print("File path:", caminho)  # Print file path for debugging
    try:
        with open(caminho) as csv:
            leitor_csv = reader(csv,delimiter=';')
            next(leitor_csv) # pular o cabeçalho
            for linha in leitor_csv:
                    if linha[1] == cenario:
                        print(linha[2])
                        break
    except FileNotFoundError:
        print(f"File '{caminho}' not found.")    

ler_csv_cenario('test','CENARIO')        