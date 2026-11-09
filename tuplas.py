cores = ('vermelho', 'verde', 'azul', 'amarelo', 'branco', 'preto')

print("=== TUPLA ORIGINAL (IMUTÁVEL) ===")
print("Cores:", cores)
print("Endereço na Memória (ID):", id(cores))
print("-" * 50)

print("\n1. ACESSO POR ÍNDICE:")
print("• Primeira cor (índice 0):", cores[0])
print("• Última cor (índice -1):", cores[-1])

print("\n2. CHECAGEM DE ELEMENTOS:")
cor_busca = "verde"
if cor_busca in cores:
    print(f"• A cor '{cor_busca}' está presente na tupla!")

print("\n3. MÉTODOS PERMITIDOS (Não alteram nada):")
print("• Quantidade total de elementos (len):", len(cores))
print("• Quantas vezes 'azul' aparece (.count):", cores.count('azul'))
print("• Posição da cor 'amarelo' (.index):", cores.index('amarelo'))

print("\n4. TENTATIVA DE ALTERAR O CONTEÚDO:")
try:
    cores[0] = 'rosa'  # O Python impede a alteração!
except TypeError as erro:
    print("❌ ERRO BLOQUEADO PELO PYTHON:")
    print(f"   --> {erro}")

print("\n" + "-" * 50)
print("=== ESTADO FINAL DA TUPLA ===")
print("Cores intactas:", cores)
print("Endereço na Memória (ID):", id(cores)) 