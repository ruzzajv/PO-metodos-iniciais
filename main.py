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
    MatrizInicial, Zmin = metodo_canto_noroeste(custos, ofertas, demandas)
    solucaoV, custoV = metodo_de_vogel(custos, ofertas, demandas)

    print("Matriz de Alocações Canto Noroeste:")
    for linha in MatrizInicial:
        print(linha)

    print("\nCusto Total de Transporte Canto Noroeste:", Zmin)

    print("Matriz de Alocações (Método de Vogel):")
    for linha in solucaoV:
        print(linha)

    print(f"\nCusto Total de Transporte: R$ {custoV}")

if __name__ == "__main__":
    main()
