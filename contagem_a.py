# Função para verificar a existência e contagem da letra 'a'
def verificar_letra_a(string):
    # Converte toda a string para minúscula para facilitar a contagem
    string_lower = string.lower()
    
    # Conta quantas vezes a letra 'a' aparece na string
    contagem = string_lower.count('a')
    
    # Verifica se a letra 'a' aparece
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Entrada da string a ser verificada
texto = input("Informe uma string para verificar a ocorrência da letra 'a': ")

# Chama a função para verificar a letra 'a'
verificar_letra_a(texto)
