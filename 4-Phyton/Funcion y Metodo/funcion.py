def calcular_total(precio: float, impuesto: float) -> float:
    return precio * (1 + impuesto)

#Se llama Directamente
total = calcular_total(100, 0.19)
print(f"Total: {total}")