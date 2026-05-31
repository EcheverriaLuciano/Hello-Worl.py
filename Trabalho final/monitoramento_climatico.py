"""
Trabalho: Sistema de Monitoramento Climático

Objetivo

Construir um programa em Python que leia uma lista de cidades, consulte as condições climáticas atuais de cada uma via API, armazene esses dados utilizando conceitos de Orientação a Objetos e exiba um relatório formatado na tela.

Requisitos do Sistema

1. Modelagem de Dados (Orientação a Objetos)

O aluno deve criar uma classe chamada CidadeClima.

Atributos privados/públicos: nome, temperatura, umidade e condicao.
Método Construtor (__init__): Para inicializar as propriedades.
Método de Exibição: Um método (ou sobrescrita do __str__) para retornar os dados formatados da cidade.

2. Consumo de Dados (API e Listas)

O programa deve possuir uma lista inicial com pelo menos 5 cidades pré-definidas (ex: ['São Paulo', 'London', 'Tokyo', 'New York', 'Paris']).
O sistema deve iterar sobre essa lista e fazer uma requisição HTTP (usando a biblioteca requests) para a API do OpenWeatherMap (OU A API TRABALHADA NA ÚLTIMA AULA) para cada cidade.
Os dados JSON retornados devem ser extraídos e instanciados como objetos da classe CidadeClima.
Cada objeto criado deve ser guardado em uma lista principal chamada relatorio_clima.

3. Exibição dos Resultados

O programa deve percorrer a lista relatorio_clima e exibir os dados na tela de forma organizada e legível para o usuário.

====================================
Critérios de Avaliação Sugeridos

Tratamento de Exceções: O aluno tratou possíveis erros de digitação de cidades ?
Uso Correto de OO: Os dados foram de fato transformados em objetos antes de irem para a lista, ou o aluno apenas manipulou dicionários diretamente na exibição?
Clean Code: Legibilidade de variáveis, indentação e comentários explicativos.

Observação: configure a variável de ambiente `OPENWEATHERMAP_API_KEY` com sua chave antes de executar.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Optional

import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def carregar_chave_api() -> Optional[str]:
    """Tenta carregar a chave da API primeiro da variável de ambiente
    `OPENWEATHERMAP_API_KEY` e, se não existir, de um arquivo local
    `openweather_api_key.txt` (opcional). Retorna None se não encontrar.
    """
    chave = os.getenv("OPENWEATHERMAP_API_KEY")
    if chave:
        return chave.strip()

    # fallback para arquivo local (opcional, útil para testes locais)
    caminho_local = os.path.join(os.path.dirname(__file__), "openweather_api_key.txt")
    try:
        if os.path.exists(caminho_local):
            with open(caminho_local, "r", encoding="utf-8") as f:
                conteudo = f.read().strip()
                if conteudo:
                    return conteudo
    except OSError:
        pass

    return None


@dataclass
class CidadeClima:
    """Representa o clima de uma cidade."""

    nome: str
    temperatura: float
    umidade: int
    condicao: str

    def __str__(self) -> str:
        return (
            f"Cidade: {self.nome}\n"
            f"Temperatura: {self.temperatura:.1f} C\n"
            f"Umidade: {self.umidade}%\n"
            f"Condição: {self.condicao}"
        )


def consultar_clima(cidade: str, api_key: str) -> Optional[CidadeClima]:
    """Consulta o clima da cidade na API e transforma o retorno em objeto."""

    cidade = cidade.strip()
    if not cidade:
        print("Aviso: nome de cidade vazio.")
        return None

    parametros = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br",
    }

    try:
        resposta = requests.get(API_URL, params=parametros, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        # Extração com proteção contra chaves ausentes
        nome = dados.get("name", cidade)
        main = dados.get("main", {})
        weather = dados.get("weather", [])

        temperatura = float(main.get("temp"))
        umidade = int(main.get("humidity"))
        condicao = (
            weather[0].get("description", "") if weather and isinstance(weather[0], dict) else ""
        )
        condicao = condicao.capitalize() if condicao else "N/A"

        return CidadeClima(
            nome=nome,
            temperatura=temperatura,
            umidade=umidade,
            condicao=condicao,
        )
    except requests.exceptions.HTTPError:
        print(f"Aviso: cidade nao encontrada ou erro ao consultar '{cidade}'.")
    except requests.exceptions.RequestException as erro:
        print(f"Aviso: falha de rede ao consultar '{cidade}': {erro}")
    except (KeyError, TypeError, ValueError):
        print(f"Aviso: formato de dados inesperado para '{cidade}'.")

    return None


def exibir_relatorio(relatorio_clima: List[CidadeClima]) -> None:
    """Exibe o relatorio final de forma organizada."""

    print("\n" + "=" * 50)
    print("RELATORIO DE MONITORAMENTO CLIMATICO")
    print("=" * 50)

    if not relatorio_clima:
        print("Nenhum dado de clima foi carregado.")
        return

    for indice, cidade_clima in enumerate(relatorio_clima, start=1):
        print(f"\n[{indice}] {cidade_clima.nome}")
        print(f"Temperatura: {cidade_clima.temperatura:.1f} C")
        print(f"Umidade: {cidade_clima.umidade}%")
        print(f"Condição: {cidade_clima.condicao}")
        print("-" * 50)


def main() -> None:
    cidades = ["São Paulo", "London", "Tokyo", "New York", "Paris"]
    api_key = carregar_chave_api()

    if not api_key:
        print(
            "Erro: defina a variavel de ambiente OPENWEATHERMAP_API_KEY "
            "antes de executar o programa, ou coloque a chave em openweather_api_key.txt."
        )
        return

    relatorio_clima: List[CidadeClima] = []

    for cidade in cidades:
        cidade_clima = consultar_clima(cidade, api_key)
        if cidade_clima is not None:
            relatorio_clima.append(cidade_clima)

    exibir_relatorio(relatorio_clima)


if __name__ == "__main__":
    main()
