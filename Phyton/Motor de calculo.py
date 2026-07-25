def analizar_stock(stock_minimo, *bodegas, **reajustes):
    # Paso 1: Consolidar stock de todas las bodegas
    stock_consolidado = {}
    for bodega in bodegas:
        for producto, cantidad in bodega.items():
            stock_consolidado[producto] = stock_consolidado.get(producto, 0) + cantidad
    
    # Paso 2: Aplicar los reajustes
    for producto, cantidad_reajuste in reajustes.items():
        stock_consolidado[producto] = stock_consolidado.get(producto, 0) + cantidad_reajuste
    
    # Paso 3: Identificar productos bajo stock mínimo
    alertas = [producto for producto, cantidad in stock_consolidado.items() 
               if cantidad <= stock_minimo]
    
    # Paso 4: Retornar resultados
    return {
        "inventario_final": stock_consolidado,
        "alertas_reposicion": alertas
    }

# ============ EJEMPLO DE USO ============
bodega_central = {"teclado": 15, "mouse": 8, "monitor": 5}
bodega_norte = {"teclado": 10, "mouse": 12, "monitor": 3}
bodega_sur = {"teclado": 5, "monitor": 7}
reajustes = {"teclado": -2, "mouse": 5, "laptop": 3}

resultado = analizar_stock(10, bodega_central, bodega_norte, bodega_sur, **reajustes)

print("Inventario Final:", resultado["inventario_final"])
print("Alertas:", resultado["alertas_reposicion"])