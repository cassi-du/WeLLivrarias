import csv
import sqlite3
import shutil
import datetime
from pathlib import Path
from utils import limpar_backups

#Diretorios
base_dir = Path("meu_sistema_livraria")
backup_dir = base_dir / "backups"
export_dir = base_dir / "exports"
data_dir = base_dir / "data"
db_path = data_dir / "livraria.db"

#mkdir para garantir que a pasta existe
export_dir.mkdir(parents=True, exist_ok=True)

#Exportar dados para CSV
def exportar_para_csv(caminho_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, autor, ano_publicacao, preco FROM livros")
    livros = cursor.fetchall()
    
    with open(caminho_csv, 'w', newline='', encoding='utf-8') as csvfile:
        colunas = ['Título', 'Autor', 'Ano', 'Preço']
        writer = csv.writer(csvfile)
        writer.writerow(colunas)

        for livro in livros:
            writer.writerow(livro)
    
    conn.close()
    print(f"Dados exportados com sucesso para {caminho_csv}")

#Importar dados de CSV
def importar_de_csv(caminho_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(caminho_csv, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for linha in reader:
            try:
                titulo = linha[0]
                autor = linha[1]
                ano_publicacao = int(linha[2])
                preco = float(linha[3])
                cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)", 
                               (titulo, autor, ano_publicacao, preco))
            except ValueError as e:
                print(f"Erro ao processar linha: {linha}. Motivo: {e}")
                continue
    conn.commit()
    conn.close()
    print("Dados importados com sucesso.")

# Função backup
def fazer_backup():
    hoje = datetime.date.today().strftime('%Y-%m-%d')
    backup_file = backup_dir / f"backup_livraria_{hoje}.db"
    shutil.copy(db_path, backup_file)
    limpar_backups(backup_dir)
