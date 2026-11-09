pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Joinville"
}

print("=== 1. ESTADO INICIAL DO DICIONÁRIO ===")
print("• Conteúdo:", pessoa)
print("• Tipo da estrutura:", type(pessoa))
print("• Endereço de Memória (ID):", id(pessoa))

print("\n" + "="*50 + "\n")

print("2. ALTERANDO E ADICIONANDO ELEMENTOS:")

pessoa["idade"] = 29

pessoa["profissao"] = "Engenheira"

print("• Dicionário modificado:", pessoa)
print("• NOVO Endereço de Memória (ID):", id(pessoa))
print("👉 O ID PERMANECE O MESMO! Isso comprova que o dicionário é MUTÁVEL.")

print("\n" + "="*50 + "\n")

print("3. MÉTODOS DE LEITURA NATIVOS:")
print("• Chaves (.keys()):", list(pessoa.keys()))
print("• Valores (.values()):", list(pessoa.values()))
print("• Par Chave-Valor (.items()):", list(pessoa.items()))

print("\n" + "="*50 + "\n")

print("4. REMOVENDO UM ELEMENTO (.pop()):")
cidade_removida = pessoa.pop("cidade")

print(f"• Elemento removido: '{cidade_removida}'")
print("• Dicionário após a remoção:", pessoa)

print("\n" + "="*50 + "\n")

print("5. TESTE DE ERRO: Tentar usar um objeto MUTÁVEL (Lista) como Chave")
try:
    pessoa[[1, 2, 3]] = "Lista de números"

except TypeError as erro:
    print("❌ ERRO BLOQUEADO PELO PYTHON:")
    print(f"   --> {erro}")
    print("   [Explicação]: As chaves devem ser IMUTÁVEIS (ex: str, int, tupla).")

print("\n" + "="*50 + "\n")
print("=== ESTADO FINAL DO DICIONÁRIO ===")
print("Resultado final:", pessoa)
print("Endereço de Memória final (ID):", id(pessoa))