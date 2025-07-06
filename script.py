import sqlite3
import os

# Configurações
TXT_PATH = '/media/pointsec/databases/SerasaPF.txt'
DB_PATH = 'sua_db'
TABLE_NAME = 'db'
SEPARADOR = '|'

# Criar conexão com SQLite
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)  # remove o antigo se existir
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

# Processar arquivo linha por linha
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

        # Mostra progresso a cada 100.000 linhas
        if i % 100000 == 0:
            print(f'{i} linhas processadas...')
            conn.commit()  # salva em disco regularmente

# Commit final
conn.commit()
conn.close()

print('✅ Processamento finalizado com sucesso!')
