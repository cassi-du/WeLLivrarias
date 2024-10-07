import sqlite3
import os
import shutil
import pandas as pd
from pathlib import Path
from utils import limpar_backups
from datetime import datetime

#Diretorios
base_dir = Path("meu_sistema_livraria")
backup_dir = base_dir / "backups"
export_dir = base_dir / "exports"
data_dir = base_dir / "data"
db_path = data_dir / "livraria.db"

#mkdir para garantir que a pasta existe
export_dir.mkdir(parents=True, exist_ok=True)

#Exportar dados para CSV
import pandas as pd
import sqlite3

def exportar_para_csv(caminho_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, autor, ano_publicacao, preco FROM livros")
    livros = cursor.fetchall()

    df = pd.DataFrame(livros, columns=['Título', 'Autor', 'Ano', 'Preço'])

    df.to_csv(caminho_csv, index=False, encoding='utf-8', sep=',')
    
    conn.close()
    print(f"Dados exportados com sucesso para {caminho_csv}")

def importar_de_csv(caminho_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        df = pd.read_csv(caminho_csv, encoding='utf-8').dropna(how='all')
        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO livros (titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?)
            """, (row['Título'], row['Autor'], int(row['Ano']), float(row['Preço'])))
        
    except ValueError as e:
        print(f"Erro ao processar o CSV. Motivo: {e}")
    
    conn.commit()
    conn.close()
    print("Dados importados com sucesso.")

def fazer_backup():
    backups_dir = 'meu_sistema_livraria/backups'
    
    #mkdir
    if not os.path.exists(backups_dir):
        os.makedirs(backups_dir)
        print(f"Diretório de backups criado: {backups_dir}")

    db_path = 'meu_sistema_livraria/data/livraria.db'
    backup_filename = f"backup_livraria_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.db"
    backup_path = os.path.join(backups_dir, backup_filename)

    shutil.copy(db_path, backup_path)
    print(f"Backup do banco de dados realizado com sucesso: {backup_path}")

    limpar_backups(backups_dir)