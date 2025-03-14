class calculator:
    """Advanced calculator class"""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {result}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is : {result}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {result}")
