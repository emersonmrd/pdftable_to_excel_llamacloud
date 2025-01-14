# PDF Table Extractor and Converter to Excel

Este projeto é uma ferramenta que extrai tabelas de documentos PDF e as converte em arquivos Excel. Ele utiliza a API `llama_parse` para processar PDFs e a biblioteca `pandas` para tratar os dados. O objetivo é extrair apenas as tabelas dos documentos, limpar e formatar as informações, e gerar planilhas em Excel de maneira eficiente.

## Arquivos do Projeto

### 1. `main.py`

Este arquivo contém o código principal para processar o arquivo PDF. Ele usa a biblioteca `llama_parse` para extrair as tabelas de um PDF e gerar arquivos Markdown com as tabelas extraídas. As tabelas são extraídas com base em uma instrução personalizada que foca apenas nas tabelas com cabeçalhos e dados bem formatados.

**Fluxo do código:**
- Carrega a chave de API do arquivo `.env`.
- Usa a API `llama_parse` para extrair as tabelas em formato Markdown.
- Salva cada página processada em um arquivo Markdown.

### 2. `transformar_excel.py`

Este arquivo processa os arquivos Markdown gerados no `main.py`. Ele converte as tabelas em arquivos Excel utilizando o `pandas`. As tabelas são tratadas para remover linhas e colunas vazias, garantindo que os dados sejam bem organizados e armazenados corretamente em planilhas.

**Fluxo do código:**
- Lê arquivos Markdown de um diretório.
- Usa expressões regulares para identificar e extrair tabelas.
- Converte as tabelas extraídas em arquivos Excel e os salva em um diretório específico.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado e crie um ambiente virtual para gerenciar as dependências. Você também precisa de uma chave de API para usar o `llama_parse`.

1. **Instalar dependências**

```bash
pip install -r requirements.txt
```

2. **Configurar a chave de API**

Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API do `llama_parse`:

```
LLAMA_CLOUD_API_KEY=your_api_key_here
```

3. **Processar o PDF**

Execute o arquivo `main.py` para processar o PDF e extrair as tabelas:

```bash
python main.py
```

Isso gerará arquivos Markdown para cada página do PDF, contendo as tabelas extraídas.

4. **Converter para Excel**

Após gerar os arquivos Markdown, execute o arquivo `transformar_excel.py` para converter as tabelas extraídas para arquivos Excel:

```bash
python transformar_excel.py
```

As planilhas Excel serão salvas no diretório `tabelas/` com o nome de cada página e tabela.

## Estrutura do Projeto

- **meu_pdf/**: Contém os arquivos PDF e os arquivos Markdown gerados.
- **tabelas/**: Diretório onde os arquivos Excel gerados serão salvos.
- **main.py**: Arquivo principal que processa o PDF e gera arquivos Markdown.
- **transformar_excel.py**: Arquivo que converte os arquivos Markdown para Excel.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Esse projeto foi feito para fins educacionais e para melhorar as habilidades de processamento de documentos e extração de dados.
