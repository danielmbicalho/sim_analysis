import pandas as pd
import glob
import re

from unicodedata import normalize

def decode_city_data(data_source, city_data, column):
     # decodificação do dataset conforme
     # https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/Estrutura_SIM.pdf
     pass


def define_column_headers(data_source):
     column_names = ['Municipio', 'Acidente Transporte Terrestre: Pedestre',
       'Acidente Transporte Terrestre: Ciclista',
       'Acidente Transporte Terrestre: Motociclista',
       'Acidente Transporte Terrestre: Ocupante triciclo motorizado',
       'Acidente Transporte Terrestre: Ocupante automóvel',
       'Acidente Transporte Terrestre: Ocupante caminhonete',
       'Acidente Transporte Terrestre: Ocupante transporte pesado',
       'Acidente Transporte Terrestre: Ocupante ônibus',
       'Acidente Transporte Terrestre: Outros',
       'Acidente Transporte Aquátivo',
       'Acidente Transporte Aéreo/Espacial',
       'Acidente Transporte: Outros', 'Quedas',
       'Exposição a forças mecânicas inanimadas',
       'Exposição a forças mecânicas animadas',
       'Afogamento e submersão acidentais',
       'Outros riscos acidentais à respiração',
       'Expos Eletricidade, radiação e temp press extrem amb',
       'Exposição à fumaça, ao fogo e às chamas',
       'Contato com fonte de calor ou substâncias quentes',
       'Contato com animais e plantas venenosos',
       'Exposição às forças da natureza',
       'Envenenamento acidental e exposição subst nocivas',
       'Excesso de esforços, viagens e privações',
       'Exposição acidental a fatores não especificados',
       'Lesões autoprovocadas intencionalmente', 'Agressões',
       'Intenção é indeterminada',
       'Intervenções legais e operações de guerra',
       'Ef advers drog, medic e subst biológ finalid terap',
       'Acid ocorr pacientes prest cuid médicos e cirúrg',
       'Incid advers atos diagn terap assoc disposit médic',
       'Reaç anorm compl tard proc cirúrg méd s/menç acid',
       'Seqüelas causas externas de morbidade e mortalidad', 'Total']

     data_source.columns = column_names

     return data_source

# código retirado de
# https://wiki.python.org.br/RemovedorDeAcentos

def clean_text(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
     

def tidy_data(column):
       df1_tidy = pd.melt(frame=df1, id_vars=['Municipio'], var_name=['Motivo da morte'], value_name='Quantidade de vítimas')

# mudar o nome da função
def separar_codigo_do_nome():
     df1_tidy.Municipio = df1_tidy.Municipio.apply(lambda x: re.search('[^0-9]+', x).group(0).upper())
     df1_tidy.head()
