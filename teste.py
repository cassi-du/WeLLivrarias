import pandas as pd

# Testando a leitura do arquivo CSV gerado
df = pd.read_csv(r'C:\Users\cassi\OneDrive\Documentos\1-Programas\WeLLivrarias\meu_sistema_livraria\exports\livros_exportados.csv', encoding='utf-8')
print(df.head())  # Isso deve exibir os dados corretamente
