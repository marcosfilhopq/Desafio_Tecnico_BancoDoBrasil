import requests
import csv
from datetime import datetime, timedelta

def coletar_dados():
    # Moedas solicitadas no desafio
    moedas = {
        'USD': '10813',
        'EUR': '21619',
        'GBP': '21623',
        'JPY': '21621'
    }
    
    # Período de 90 dias
    data_final = datetime.now().strftime('%d/%m/%Y')
    data_inicial = (datetime.now() - timedelta(days=90)).strftime('%d/%m/%Y')
    
    arquivo_saida = 'cotacoes_moedas.csv'
    
    print("Iniciando coleta via API do Banco Central...")
    
    try:
        with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['data', 'valor', 'moeda'])
            
            for nome, codigo in moedas.items():
                url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
                
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    dados = response.json()
                    for item in dados:

                        #Converte a vírgula da API para ponto 
                        valor_limpo = item['valor'].replace(',', '.')
                        writer.writerow([item['data'], valor_limpo, nome])
                    print(f"Sucesso: {nome}")
                else:
                    print(f"Erro na moeda {nome}: Status {response.status_code}")

        print(f"\nArquivo '{arquivo_saida}' gerado com sucesso na pasta!")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    coletar_dados()