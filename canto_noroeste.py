def metodo_canto_noroeste(custos, ofertas, demandas):
    num_fontes = len(ofertas)
    num_destinos = len(demandas)
    i, j = 0, 0

    ofertas_restantes = list(ofertas)
    demandas_restantes = list(demandas)

    alocacoes = [
        [0] * num_destinos
        for _ in range(num_fontes)
    ]

    while i < num_fontes and j < num_destinos:
        alocacao_atual = min(ofertas_restantes[i], demandas_restantes[j])
        alocacoes[i][j] = alocacao_atual

        ofertas_restantes[i] -= alocacao_atual
        demandas_restantes[j] -= alocacao_atual

        if ofertas_restantes[i] == 0:
            i += 1
        if demandas_restantes[j] == 0:
            j += 1

    custo_total = sum(
        alocacoes[i][j] * custos[i][j]
        for i in range(num_fontes)
        for j in range(num_destinos)
    )

    return alocacoes, custo_total
