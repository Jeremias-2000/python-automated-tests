from csv import reader


def ler_csv_cenario(massa:str,cenario:str):
    caminho = '/home/jeremias/Documentos/workspace/test-python-integration2/bdd/data/' + massa + '.csv'
    caminho = caminho.replace('"', '')
    print("File path:", caminho)  # Print file path for debugging
    try:
        with open(caminho) as csv:
            leitor_csv = reader(csv)
            next(leitor_csv) # pular o cabeçalho
            for linha in leitor_csv:
                    if linha[1] == cenario:
                        print(linha)
                        break
    except FileNotFoundError:
        print(f"File '{caminho}' not found.")
    

ler_csv_cenario('test','test')        