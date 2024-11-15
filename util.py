def ler_dados_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = []
            for linha in arquivo:
                partes = linha.strip().split(';')
                if len(partes) == 4: 
                    dados.append(partes)
            return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []
