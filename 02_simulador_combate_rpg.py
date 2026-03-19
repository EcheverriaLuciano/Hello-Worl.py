# 2) Simulador de Combate: Turnos de RPG
# Fazer que tenha um HP padrão ao invés do usuario definir pra ser mais de boas
hp_heroi = 100
hp_monstro = 100
turno = 1

while hp_heroi > 0 and hp_monstro > 0:
    print(f"\n-      Turno {turno}     -")
    dano_heroi = int(input("Dano do ataque do herói: "))
    dano_monstro = int(input("Dano do ataque do monstro: "))

    hp_monstro -= dano_heroi
    if hp_monstro < 0:
        hp_monstro = 0

    hp_heroi -= dano_monstro
    if hp_heroi < 0:
        hp_heroi = 0

    print(f"HP do Herói: {hp_heroi}")
    print(f"HP do Monstro: {hp_monstro}")

    turno += 1

if hp_heroi == 0 and hp_monstro == 0:
    print("\nEmpate! Ambos foram derrotados. ABSOLUTE CINEMA")
elif hp_monstro == 0:
    print("\nHerói venceu! Louvado Seja o Sol")
else:
    print("\nMonstro venceu! F")
