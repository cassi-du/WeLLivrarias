import sqlite3
from pathlib import Path

base_dir = Path("meu_sistema_livraria")
data_dir = base_dir / "data"
db_path = data_dir / "livraria.db"

#mkdir para garantir que a pasta existe
data_dir.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER,
    preco REAL
)
''')
conn.commit()

def adicionar_livro(titulo, autor, ano, preco):
    cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                   (titulo, autor, ano, preco))
    conn.commit()

def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)

def atualizar_preco(id_livro, novo_preco):
    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))
    conn.commit()

def remover_livro(id_livro):
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conn.commit()

def buscar_livros_por_autor(autor):
    cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor,))
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)