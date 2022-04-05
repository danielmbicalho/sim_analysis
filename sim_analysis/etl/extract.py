"""
Script para download e decodificação dos dados relativos ao Sistema de Informação sobre Mortalidade
Fonte de dados
https://dados.gov.br/dataset/sistema-de-informacao-sobre-mortalidade-sim-1979-a-2018/resource/4d858661-073a-485f-8a5d-3c496a8c6354?inner_span=True

"""
import requests
import os
import csv
# import pandas as pd
# from contextlib import closing
from sim_analysis.utils.download_tools import download
from sim_analysis.utils.download_tools import compare_files_size


# Dados de 2020
# https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/sim_preliminar_2020.csv
# Dados de 2021
# https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/DO21OPEN.csv

# definir uma função que receba apenas um ano para baixar os arquivos
def download_data_files(dst_dir, initial_year=1979, final_year=2019):
    src_url = "https://diaad.s3.sa-east-1.amazonaws.com/sim/Mortalidade_Geral_"
    date_range = range(initial_year, final_year + 1 )    
   
    for year in date_range:

        data_dir = dst_dir
        data_file= os.path.join(dst_dir, f'Mortalidade_Geral_{year}.csv')
        url_file = f'{src_url}{year}.csv'

        if not os.path.isdir(data_dir):
            os.mkdir(dst_dir)
        # TODO: comparar os tamanhos do arquivo original com o de destino
        elif os.path.isfile(data_file):
                print(f'The file exists from the year: {year}, download the next file')

        # Tratar a condição de desigualdade de tamanho
        # Ver a ordem das condicionais
        elif compare_files_size(url, data_file):
                print('The size of remote file and local file are differents, download the file?')
        
        else:
                print(f'Getting the file from year {year}')
                with open(data_file, 'wb') as f:
                    download(url_file, data_file)