import json


def analisa_faturamento(faturamento_diario):
    # Remover dias sem faturamento (valores zero)
    dias_com_faturamento = [f for f in faturamento_diario if f > 0]

    # Encontrar o menor e maior valor de faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    # Calcular a média mensal
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Contar os dias em que o faturamento foi superior à média
    dias_acima_da_media = sum(
        1 for f in dias_com_faturamento if f > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media


# Leitura dos dados a partir de um arquivo JSON
def ler_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados['faturamento_diario']


# Caminho do arquivo JSON (exemplo)
caminho_arquivo = 'targetsistemas - 3.json'

# Ler dados de faturamento
faturamento_diario = ler_dados_json(caminho_arquivo)

# Analisar o faturamento
menor, maior, dias_acima_media = analisa_faturamento(faturamento_diario)

# Exibir os resultados
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
