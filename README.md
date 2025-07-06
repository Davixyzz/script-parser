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

---

### 🚀 Como usar

1. **Crie um arquivo chamado `script.py`**


### Exemplo:

├── script.py
├── dados.txt
### 2 Execute o script no terminal:

python3 script.py

---
### 🎯 Resultado
Será gerado um arquivo chamado dados_convertidos.db com a tabela pessoas, contendo todos os dados do .txt.

📜 Estrutura da tabela criada
CREATE TABLE pessoas (
    cpf TEXT,
    nome_completo TEXT,
    sexo TEXT,
    data_nascimento TEXT,
    nome_mae TEXT,
    nome_pai TEXT,
    rg TEXT
);
---
### ⚠️ Aviso importante
Este projeto não contém nem distribui dados pessoais. É uma ferramenta genérica de importação de dados em massa para .db, com fins educacionais ou técnicos.
---
### 👨‍💻 Autor
Davi Sakai
Desenvolvedor fullstack com foco em automação, bots, scraping e manipulação de grandes volumes de dados.



