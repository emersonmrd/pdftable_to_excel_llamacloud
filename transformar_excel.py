import re 
import pandas as pd
from io import StringIO
import os

def tratar_tabelas_texto(texto):
    regra_busca_regex = re.compile(r"((?:\|.+\|(?:\n|\r))+)", re.MULTILINE)
    tabelas = regra_busca_regex.findall(texto)
    return tabelas

def transformar_markdown_excel(texto, num_pagina):
    lista_texto_tabelas = tratar_tabelas_texto(texto)
    if len(lista_texto_tabelas) > 0:
        for i, texto_tabela in enumerate(lista_texto_tabelas):
            tabela = pd.read_csv(StringIO(texto_tabela), sep="|", encoding="utf-8", engine="python")
            tabela = tabela.dropna(axis=0, how="all")
            tabela = tabela.dropna(axis=1, how="all")
            tabela.to_excel(f"tabelas/Pagina{num_pagina}Tabela{i+1}.xlsx", index=False)
        


pasta_paginas = "meu_pdf"
lista_paginas = os.listdir(pasta_paginas)


for i, pagina in enumerate(lista_paginas):
    with open(f"meu_pdf/{pagina}", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    num_pagina = i + 1
    transformar_markdown_excel(texto, num_pagina)