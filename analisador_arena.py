import sys
from typing import List, Dict


def ler_arquivo_partida(caminho: str) -> List[Dict]:
    jogadores = []
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = [p.strip() for p in linha.split(";")]
            if len(partes) != 5:
                continue
            jogador = {
                "nome": partes[0],
                "classe": partes[1],
                "kills": int(partes[2]),
                "deaths": int(partes[3]),
                "dano": int(partes[4]),
            }
            jogadores.append(jogador)
    return jogadores


def calcular_kda(kills: int, deaths: int) -> float:
    if deaths == 0:
        return float(kills)
    return kills / deaths


def filtrar_por_classe(jogadores: List[Dict], classe: str) -> List[Dict]:
    classe_lower = classe.strip().lower()
    return [j for j in jogadores if j.get("classe", "").strip().lower() == classe_lower]


def gerar_relatorio(jogadores: List[Dict]) -> Dict:
    if not jogadores:
        return {}
    jogador_maior_dano = max(jogadores, key=lambda j: j["dano"]) 
    media_kills = sum(j["kills"] for j in jogadores) / len(jogadores)
    elite = [j["nome"].upper() for j in jogadores if calcular_kda(j["kills"], j["deaths"]) > 2.0]
    return {
        "maior_dano": jogador_maior_dano,
        "media_kills": media_kills,
        "elite": elite,
    }


def imprimir_relatorio(rel: Dict) -> None:
    if not rel:
        print("Nenhum dado para gerar relatório.")
        return
    md = rel["maior_dano"]
    print("--- Relatório: Arena dos Campeões ---")
    print(f"Jogador que causou o MAIOR DANO: {md['nome']} ({md['classe']}) - {md['dano']}")
    print(f"Média de Kills da partida: {rel['media_kills']:.2f}")
    if rel["elite"]:
        print("Jogadores com KDA > 2.0:")
        for nome in rel["elite"]:
            print(f" - {nome}")
    else:
        print("Nenhum jogador com KDA > 2.0")


def main(caminho: str):
    jogadores = ler_arquivo_partida(caminho)
    rel = gerar_relatorio(jogadores)
    imprimir_relatorio(rel)


if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else "partida.txt"
    try:
        main(caminho)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}. Por favor, crie '{caminho}' na pasta atual.")
