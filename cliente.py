import util

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

def extrair_idades(dados):
    return [int(cliente[2]) for cliente in dados]

def extrair_rendas(dados):
    return [float(cliente[3]) for cliente in dados]

if __name__ == '__main__':
    caminho_arquivo = 'dados.txt'
    dados_clientes = util.ler_dados_arquivo(caminho_arquivo)
    
    if dados_clientes:
        idades = extrair_idades(dados_clientes)
        rendas = extrair_rendas(dados_clientes)
        media_idade = calcular_media(idades)
        media_renda = calcular_media(rendas)

        print(f'Média de idade dos clientes: {media_idade:.2f} anos')
        print(f'Média de renda mensal dos clientes: R$ {media_renda:.2f}')
    else:
        print("Nenhum dado válido foi encontrado no arquivo.")
