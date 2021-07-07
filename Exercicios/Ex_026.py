frase = str(input("Digite qualquer coisa: ")).strip()
print(f"A letra a apareceu na frase {(frase.lower()).count('a')} vezes")
print(f'A letra a apareceu pela primeira vez na posição {(frase.lower().find("a"))}')
print(f'A letra a apareceu pela ultima vez na posição {(frase.lower().rfind("a"))}')
