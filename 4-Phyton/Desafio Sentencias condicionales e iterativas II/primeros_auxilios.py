def preguntar_si_no(pregunta):
    """Valida la respuesta del usuario usando un ciclo while."""
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta in ("s", "si", "sí", "n", "no"):
            return respuesta.startswith("s")
        print("Respuesta inválida. Responde 's' (sí) o 'n' (no).")

print("=" * 50)
print("        PROTOCOLO DE PRIMEROS AUXILIOS")
print("=" * 50)
print("\nPaso 1: Asegúrate de que la escena sea segura para ti y la víctima.")
input("Presiona ENTER para continuar...")
consciente = preguntar_si_no(
    "\nPaso 2: Toca sus hombros y pregúntale en voz alta: '¿Estás bien?'\n"
    "¿La persona está consciente? (s/n): "
)

if consciente:
    print("\nLa persona está consciente:")
    print("- Pregúntale qué ocurrió y si siente dolor.")
    print("- Revisa si tiene heridas visibles.")
    herida_grave = preguntar_si_no(
        "¿Presenta una herida grave o sangrado abundante? (s/n): "
    )
    if herida_grave:
        print("- Llama de inmediato a emergencias (SAMU: 131 / 911).")
        print("- Aplica presión directa sobre la herida con un paño limpio.")
    else:
        print("- Bríndale tranquilidad y acompáñala.")
    print("- Monitorea su estado hasta que llegue ayuda.")
else:
    print("\nLa persona NO está consciente:")
    print("- Llama de inmediato a emergencias (SAMU: 131 / 911).")
    respira = preguntar_si_no(
        "Paso 3: Acerca tu oído a su boca/nariz y observa su pecho "
        "(máx. 10 segundos). ¿Respira? (s/n): "
    )
    if respira:
        print("\nLa persona respira:")
        print("- Colócala en posición lateral de seguridad (de lado).")
        print("- Verifica su respiración constantemente.")
    else:
        print("\nLa persona NO respira:")
        print("- Inicia RCP: 30 compresiones torácicas y 2 ventilaciones.")
        print("- Continúa la RCP hasta que llegue ayuda profesional.")

print("\n" + "=" * 50)
print("Recuerda: nunca dejes sola a la víctima.")
print("=" * 50)