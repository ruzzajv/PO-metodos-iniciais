from aproximacao_de_vogel import metodo_de_vogel
from canto_noroeste import metodo_canto_noroeste

custos = [
    [12, 22, 30],
    [18, 24, 32],
    [22, 15, 34]
]

ofertas = [100, 140, 160]
demandas = [120, 130, 150]

def main():
    matriz_inicial, zmin = metodo_canto_noroeste(custos, ofertas, demandas)
    solucao_v, custo_v = metodo_de_vogel(custos, ofertas, demandas)

    print("Matriz de Alocações Canto Noroeste:")
    for linha in matriz_inicial:
        print(linha)

    print("\nCusto Total de Transporte Canto Noroeste:", zmin)

    print("Matriz de Alocações (Método de Vogel):")
    for linha in solucao_v:
        print(linha)

    print(f"\nCusto Total de Transporte: R$ {custo_v}")

if __name__ == "__main__":
    main()
