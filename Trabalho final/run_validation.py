"""Script de validação local usando mocks para testar requisitos principais:
- Criação de objetos CidadeClima a partir do JSON
- Tratamento de HTTPError (cidade inválida)
- Tratamento de payloads malformados

Roda de forma independente e imprime um resumo simples.
"""

from unittest.mock import patch
import requests
import sys

import monitoramento_climatico as mc


class FakeResponse:
    def __init__(self, payload=None, status_code=200):
        self._payload = payload or {}
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload


def teste_sucesso():
    payload = {
        "name": "Paris",
        "main": {"temp": 18.2, "humidity": 55},
        "weather": [{"description": "ceu limpo"}],
    }

    with patch("monitoramento_climatico.requests.get", return_value=FakeResponse(payload)):
        item = mc.consultar_clima("Paris", "fake-key")
        assert item is not None
        assert item.nome == "Paris"
        assert abs(item.temperatura - 18.2) < 1e-6
        assert item.umidade == 55
        assert item.condicao == "Ceu limpo"

    print("teste_sucesso: OK")


def teste_http_error():
    with patch("monitoramento_climatico.requests.get", return_value=FakeResponse({}, status_code=404)):
        item = mc.consultar_clima("CidadeInexistente", "fake-key")
        assert item is None
    print("teste_http_error: OK")


def teste_payload_malformado():
    payload = {"foo": "bar"}  # sem campos esperados
    with patch("monitoramento_climatico.requests.get", return_value=FakeResponse(payload)):
        item = mc.consultar_clima("Paris", "fake-key")
        assert item is None
    print("teste_payload_malformado: OK")


if __name__ == "__main__":
    try:
        teste_sucesso()
        teste_http_error()
        teste_payload_malformado()
        print("\nVALIDACAO: TODOS TESTES PASSARAM")
    except AssertionError as e:
        print("VALIDACAO: FALHA EM ALGUM TESTE", file=sys.stderr)
        raise
