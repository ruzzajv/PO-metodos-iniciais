def metodo_de_vogel(custos, oferta, demanda):
    oferta_copia = oferta[:]
    demanda_copia = demanda[:]

    num_origens = len(oferta)
    num_destinos = len(demanda)

    alocacao = [[0 for _ in range(num_destinos)] for _ in range(num_origens)]

    while sum(oferta_copia) > 0 and sum(demanda_copia) > 0:
        penalidade_linha = []
        for i in range(num_origens):
            if oferta_copia[i] > 0:
                custos_validos = sorted([custos[i][j] for j in range(num_destinos) if demanda_copia[j] > 0])
                if len(custos_validos) > 1:
                    penalidade_linha.append(custos_validos[1] - custos_validos[0])
                else:
                    penalidade_linha.append(0)
            else:
                penalidade_linha.append(-1)

        penalidade_coluna = []
        for j in range(num_destinos):
            if demanda_copia[j] > 0:
                custos_validos = sorted([custos[i][j] for i in range(num_origens) if oferta_copia[i] > 0])
                if len(custos_validos) > 1:
                    penalidade_coluna.append(custos_validos[1] - custos_validos[0])
                else:
                    penalidade_coluna.append(0)
            else:
                penalidade_coluna.append(-1)

        max_pen_linha = max(penalidade_linha)
        max_pen_coluna = max(penalidade_coluna)

        if max_pen_linha >= max_pen_coluna:
            idx = penalidade_linha.index(max_pen_linha)
            i = idx
            j = min([(custos[idx][j], j) for j in range(num_destinos) if demanda_copia[j] > 0])[1]
        else:
            idx = penalidade_coluna.index(max_pen_coluna)
            j = idx
            i = min([(custos[i][idx], i) for i in range(num_origens) if oferta_copia[i] > 0])[1]

        quantidade = min(oferta_copia[i], demanda_copia[j])
        alocacao[i][j] = quantidade
        oferta_copia[i] -= quantidade
        demanda_copia[j] -= quantidade

    custo_total = sum(alocacao[i][j] * custos[i][j] for i in range(num_origens) for j in range(num_destinos))

    return alocacao, custo_total



