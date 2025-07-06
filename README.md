# 📦 txt2sqlite – Conversor de TXT para SQLite

Script robusto e direto ao ponto, criado para transformar arquivos `.txt` gigantes (com milhões de linhas) em bancos de dados SQLite `.db`, de forma rápida, segura e com controle de memória.

---

### ✅ Funcionalidades

- Processa arquivos `.txt` com milhões de registros  
- Cria automaticamente a tabela no SQLite (`.db`)  
- Commit a cada 100 mil linhas para não pesar na memória  
- Suporta arquivos com delimitador `|`, `,`, `;` etc.  
- Ignora e trata linhas inválidas automaticamente  
- Ideal para conversão de bases estruturadas para banco  

---

### 🧰 Requisitos

- Python 3.x instalado  
- Biblioteca `sqlite3` (já vem com Python)  

---

### 📁 Exemplo de entrada (`.txt`)

cpf|nome_completo|sexo|data_nascimento|nome_mae|nome_pai|rg
12345678900|João Silva|M|01/01/2000|Maria Silva|José Silva|MG123456
98765432100|Ana Souza|F|15/03/1995|Clara Souza|Carlos Souza|SP987654

python
Copiar
Editar

---

### 🚀 Como usar

1. **Crie um arquivo chamado `processar_txt.py` com o seguinte conteúdo:**

```python
import sqlite3
import os

# CONFIGURAÇÕES DO USUÁRIO
TXT_PATH = './dados.txt'                 # Caminho do arquivo .txt
DB_PATH = './dados_convertidos.db'      # Nome do banco de saída
TABLE_NAME = 'pessoas'                  # Nome da tabela
SEPARADOR = '|'                         # Separador do arquivo

# Se já existir, remove o banco antigo
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# Conecta ao banco
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Cria a tabela
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        cpf TEXT,
        nome_completo TEXT,
        sexo TEXT,
        data_nascimento TEXT,
        nome_mae TEXT,
        nome_pai TEXT,
        rg TEXT
    )
''')
conn.commit()

# Processa o arquivo linha por linha
with open(TXT_PATH, 'r', encoding='utf-8') as file:
    for i, linha in enumerate(file, start=1):
        linha = linha.strip()
        if not linha or SEPARADOR not in linha:
            continue

        campos = linha.split(SEPARADOR)
        if len(campos) < 7:
            continue  # ignora linhas incompletas

        try:
            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} (cpf, nome_completo, sexo, data_nascimento, nome_mae, nome_pai, rg)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', campos[:7])
        except Exception as e:
            print(f"Erro na linha {i}: {e}")
            continue

        if i % 100000 == 0:
            print(f'{i} linhas processadas...')
            conn.commit()

conn.commit()
conn.close()
print('✅ Processamento finalizado com sucesso!')
Coloque seu arquivo .txt no mesmo diretório.

Exemplo:

Copiar
Editar
txt2sqlite/
├── processar_txt.py
├── dados.txt
Execute o script no terminal:

bash
Copiar
Editar
python3 processar_txt.py
🎯 Resultado
Será gerado um arquivo chamado dados_convertidos.db com a tabela pessoas, contendo todos os dados do .txt.

📜 Estrutura da tabela criada
sql
Copiar
Editar
CREATE TABLE pessoas (
    cpf TEXT,
    nome_completo TEXT,
    sexo TEXT,
    data_nascimento TEXT,
    nome_mae TEXT,
    nome_pai TEXT,
    rg TEXT
);
⚠️ Aviso importante
Este projeto não contém nem distribui dados pessoais. É uma ferramenta genérica de importação de dados em massa para .db, com fins educacionais ou técnicos.

👨‍💻 Autor
Davi Sakai
Desenvolvedor fullstack com foco em automação, bots, scraping e manipulação de grandes volumes de dados.

🪪 Licença
MIT License

yaml
Copiar
Editar

---

Assim os passos ficam claros, os códigos e exemplos em blocos próprios, e o README fácil de 
