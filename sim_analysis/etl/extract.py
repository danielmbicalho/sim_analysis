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


# inserir um teste para verificar a existência do arquivo
# os.path.isfile(path) 
# inserir um teste para verificar a disponibilidade do arquivo
# os.path.isdir(path)

# definir uma função que receba apenas um ano para baixar os arquivos
def download_data_files(dst_dir, initial_year, final_year):
    src_url = base_url = "https://diaad.s3.sa-east-1.amazonaws.com/sim/Mortalidade_Geral_"
    date_range = range(initial_year, final_year + 1 )    
   
    for year in date_range:

        data_dir = dst_dir
        data_file= os.path.join(dst_dir, f'Mortalidade_Geral_{year}.csv')

        if not os.path.isdir(data_dir):
            os.mkdir(dst_dir)
        # TODO: comparar os tamanhos do arquivo original com o de destino
        else:
            if os.path.isfile(data_file):
                print(f'The file exists from the year: {year}, download the next file')
        
            else:
                print(f'Getting the file from year {year}')
                url_arquivo = f'{src_url}{year}.csv'
                with open(data_file, 'wb') as f:
                    download(url_arquivo, data_file)

    

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