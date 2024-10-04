import database as dt
import file_manager as fm

def menu():
    while True:
        print('''
        1- Adicionar novo livro
        2- Exibir todos os livros
        3- Atualizar preço de um livro
        4- Remover um livro
        5- Buscar livros por autor
        6- Exportar dados para CSV
        7- Importar dados de CSV
        8- Fazer backup do banco de dados
        9- Sair
        ''')
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            preco = float(input("Preço: "))
            dt.adicionar_livro(titulo, autor, ano, preco)
        
        elif escolha == '2':
            dt.listar_livros()
        
        elif escolha == '3':
            id_livro = int(input("ID do livro: "))
            novo_preco = float(input("Novo preço: "))
            dt.atualizar_preco(id_livro, novo_preco)
        
        elif escolha == '4':
            id_livro = int(input("ID do livro a remover: "))
            dt.remover_livro(id_livro)
        
        elif escolha == '5':
            autor = input("Autor: ")
            dt.buscar_livros_por_autor(autor)
        
        elif escolha == '6':
            caminho_csv = "meu_sistema_livraria/exports/livros_exportados.csv"
            fm.exportar_para_csv(caminho_csv)
            
        elif escolha == '7':
            caminho_csv = input("Digite o caminho do arquivo CSV para importação: ")
            fm.importar_de_csv(caminho_csv)

        elif escolha == '8':
            fm.fazer_backup()
        
        elif escolha == '9':
            print("Saindo...")
            break

menu()
