import os
from dotenv import load_dotenv
from llama_parse import LlamaParse  

# Carregar variáveis de ambiente
load_dotenv()
chave_api = os.getenv("LLAMA_CLOUD_API_KEY")

# Processar o PDF
documentos = LlamaParse(
    result_type="markdown", 
    parsing_instruction='''
        This file contains both text and tables. Please extract only the tables with a clear header row and data rows. Ensure that the extracted tables have consistent column formatting, where each row has the same number of columns as the header. If any table has irregular formatting, clean the data by:

        Removing any unnecessary text, footnotes, or additional rows that do not belong to the table.
        Standardizing columns that may be misaligned (e.g., if a table has extra columns like 'Variação' or 'Produto' in additional columns, remove them if they do not match the context of the other rows).
        If columns are incorrectly merged or split, correct the structure to ensure that each data entry aligns properly under its respective column.
        Ignore all other content outside the tables, such as general text or non-relevant sections. Focus on extracting the data rows and headers only, formatted as a standard table.
    ''').load_data("resultado.pdf")

for i, pagina in enumerate(documentos):
    with open(f"meu_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)
