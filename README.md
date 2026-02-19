# 🏦 Desafio Técnico: Análise de Câmbio PTAX (Banco do Brasil)

Este repositório contém a solução para o desafio técnico de extração e visualização de dados cambiais. O projeto consiste em um script automatizado em Python para coleta de dados da API do Banco Central e um dashboard interativo no Power BI para análise de mercado.

## 🚀 Funcionalidades

### 🐍 Extração de Dados (Python)
- **Integração com API:** Consumo de dados oficiais via API do Banco Central do Brasil (SGS).
- **Automação:** Coleta automática dos últimos 90 dias de cotações para USD, EUR, GBP e JPY.
- **Tratamento de Erros:** Implementação de blocos `try-except`, timeouts e verificações de status HTTP para garantir a robustez do script.
- **Limpeza de Dados:** Conversão automática de formatos e separadores decimais para compatibilidade imediata com ferramentas de BI.

### 📊 Visualização (Power BI)
- **Análise PTAX:** Dashboard focado na cotação de venda oficial (PTAX).
- **Escalabilidade Visual:** Gráfico de linhas exclusivo para o Iene Japonês (JPY), garantindo clareza na visualização de moedas com diferentes ordens de grandeza.
- **Filtros Dinâmicos:** Segmentação de dados para análise de períodos específicos (7, 30 e 90 dias).
- **Cards de Destaque:** Exibição da cotação mais recente de cada moeda com 4 casas decimais.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Bibliotecas:** `requests`, `csv`, `datetime`
- **BI:** Microsoft Power BI Desktop
- **Dados:** API do Banco Central do Brasil (SGS)

## 📁 Estrutura do Repositório

- `coleta_dados.py`: Script principal de extração.
- `cotacoes_moedas.csv`: Arquivo de dados gerado pelo script.
- `DesafioBB.pbix`: Arquivo do Power BI com os relatórios.
- `README.md`: Documentação do projeto.

## 🔧 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca necessária:
   ```bash
   pip install requests
