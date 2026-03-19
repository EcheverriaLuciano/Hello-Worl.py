# 1) O Reflorestador / Loop com Acumulador

meta_biomassa = float(input("Digite a meta de biomassa (em unidades): "))

biomassa_total = 0.0
quantidade_arvores = 0

while biomassa_total < meta_biomassa:
    biomassa_arvore = float(input("Digite a biomassa da árvore plantada: "))
    biomassa_total += biomassa_arvore
    quantidade_arvores += 1

print(f"Meta atingida com {quantidade_arvores} árvore(s).")
print(f"Biomassa total: {biomassa_total:.2f} unidades.")
