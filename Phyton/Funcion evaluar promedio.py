def evaluar_promedio(notas):
    promedio = sum(notas) / len(notas)
    estado = "Aprobado" if promedio >= 4.0 else "Reprobado"
    return (promedio, estado)

# Pedir las 4 notas
nota1 = float(input("Nota 1 (1-7): "))
nota2 = float(input("Nota 2 (1-7): "))
nota3 = float(input("Nota 3 (1-7): "))
nota4 = float(input("Nota 4 (1-7): "))

notas = [nota1, nota2, nota3, nota4]

# Resultado
promedio, estado = evaluar_promedio(notas)
print(f"\nPromedio: {promedio:.2f}")
print(f"Estado: {estado}")2