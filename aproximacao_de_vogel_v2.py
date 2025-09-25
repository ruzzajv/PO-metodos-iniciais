from copy import deepcopy
from typing import Literal

INF = 100_000_000


def _diferenca_dois_menores(valores: list[int]) -> int:
    """Diferença entre os dois menores valores (O(n)); 0 se houver < 2 valores."""
    menor1 = INF
    menor2 = INF
    for valor in valores:
        if valor < menor1:
            menor2 = menor1
            menor1 = valor
        elif valor < menor2:
            menor2 = valor
    if INF in [menor1, menor2]:
        return 0
    return menor2 - menor1


def _calcular_penalidades(
    custos: list[list[int]], oferta_restante: list[int], demanda_restante: list[int],
    eixo: Literal["linha", "coluna"],
) -> list[int]:
    """
    Calcula penalidades de Vogel para linhas ou colunas usando um único loop.
    Retorna -1 para índices inativos (sem oferta/demanda restante).
    """
    qtd_linhas = len(oferta_restante)
    qtd_colunas = len(demanda_restante)

    if eixo == "linha":
        tamanho = qtd_linhas
        ativo_no_eixo = oferta_restante
        custos_disponiveis = lambda k: [
            custos[k][j] for j, demanda
            in enumerate(demanda_restante)
            if demanda > 0
        ]
    else: # == "coluna"
        tamanho = qtd_colunas
        ativo_no_eixo = demanda_restante
        custos_disponiveis = lambda k: [
            custos[i][k] for i, oferta
            in enumerate(oferta_restante)
            if oferta > 0
        ]

    penalidades = []
    for idx in range(tamanho):
        if ativo_no_eixo[idx] > 0:
            custos_validos = custos_disponiveis(idx)
            penalidades.append(_diferenca_dois_menores(custos_validos) if custos_validos else -1)
        else:
            penalidades.append(-1)  # (sem oferta/demanda restante)

    return penalidades


def metodo_de_vogel(
    custos: list[list[int]],
    oferta: list[int],
    demanda: list[int],
) -> tuple[list[list[int]], int]:
    oferta_copia = deepcopy(oferta)
    demanda_copia = deepcopy(demanda)

    num_origens = len(oferta)
    num_destinos = len(demanda)

    alocacoes = [[0 for _ in range(num_destinos)] for _ in range(num_origens)]

    while sum(oferta_copia) > 0 and sum(demanda_copia) > 0:
        penalidades_linha = _calcular_penalidades(custos, oferta_copia, demanda_copia, "linha")
        penalidades_coluna = _calcular_penalidades(custos, oferta_copia, demanda_copia, "coluna")

        maior_pen_linha = max(penalidades_linha)
        maior_pen_coluna = max(penalidades_coluna)

        if maior_pen_linha >= maior_pen_coluna:
            idx_linha = penalidades_linha.index(maior_pen_linha)
            idx_coluna = min([
                (custos[idx_linha][j], j)
                for j in range(num_destinos)
                if demanda_copia[j] > 0
            ])[1]
        else:
            idx_coluna = penalidades_coluna.index(maior_pen_coluna)
            idx_linha = min([
                (custos[i][idx_coluna], i)
                for i in range(num_origens)
                if oferta_copia[i] > 0
            ])[1]

        qtd_alocada = min(oferta_copia[idx_linha], demanda_copia[idx_coluna])
        alocacoes[idx_linha][idx_coluna] = qtd_alocada
        oferta_copia[idx_linha] -= qtd_alocada
        demanda_copia[idx_coluna] -= qtd_alocada

    custo_total = sum(
        alocacoes[i][j] * custos[i][j]
        for i in range(num_origens)
        for j in range(num_destinos)
    )

    return alocacoes, custo_total
