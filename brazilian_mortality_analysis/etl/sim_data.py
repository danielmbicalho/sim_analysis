"""
Script para download e decodificação dos dados relativos ao Sistema de Informação sobre Mortalidade
Fonte de dados
https://dados.gov.br/dataset/sistema-de-informacao-sobre-mortalidade-sim-1979-a-2018/resource/4d858661-073a-485f-8a5d-3c496a8c6354?inner_span=True

"""
import requests
import os
import csv
import wget 

import pandas as pd

from contextlib import closing



# inserir um teste para verificar a existência do arquivo
# os.path.isfile(path) 
# inserir um teste para verificar a disponibilidade do arquivo
# os.path.isdir(path)

def download_data_files(src_url, dst_dir, initial_year, final_year):
    date_range = range(initial_year, final_year + 1 )    
   
    for year in date_range:   
        print(f'Getting the file from year {year}')
        url_arquivo = f'{src_url}{year}.csv'
        with open(f'./dados/Mortalidade_Geral_{year}.csv', 'wb') as f:
                requests.get(url_arquivo, stream=True) as r:
                wget(url_file)
            for line in r.iter_lines():
                f.write(line+'\n'.encode())

def decode_city_data(data_source, city_data, column):
     # decodificação do dataset conforme
     # https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/Estrutura_SIM.pdf
     pass


def main():

    dst_data = "./data"
    base_url = "https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/Mortalidade_Geral_"

    download_data_files(base_url, dst_data, 1979, 2018)

if __name__ == "__main__":
    main()