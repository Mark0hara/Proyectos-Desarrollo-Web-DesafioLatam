from membresia import (
    Gratis,
    Basica,
    Familiar,
    SinConexion,
    Pro,
    Membresia
)


def probar():
    print("Probando el desafío de membresías...\n")
    print("1) Membresía abstracta no debe poder instanciarse")
    try:
        Membresia("correo@correo.cl", "123456")
        raise AssertionError("ERROR: se pudo instanciar Membresia")
    except TypeError:
        print("OK: no se puede crear una instancia directa de Membresia\n")

    correo = "usuario@correo.cl"
    tarjeta = "123456789"
    print("2) Creando membresía Gratis")
    gratis = Gratis(correo, tarjeta)

    assert gratis.costo == 0
    assert gratis.cantidad_dispositivos == 1
    print("OK: Gratis creada correctamente\n")
    print("3) Cambiando Gratis a Básica")
    basica = gratis.cambiar_suscripcion(1)

    assert isinstance(basica, Basica)
    assert basica.costo == 3000
    assert basica.cantidad_dispositivos == 2
    assert basica.correo_suscriptor == correo
    assert basica.numero_tarjeta == tarjeta
    print("OK: Gratis cambió a Básica correctamente\n")
    print("4) Probando cambio no válido en Básica")
    misma_basica = basica.cambiar_suscripcion(1)
    assert misma_basica is basica
    print("OK: Básica no puede cambiar a Básica; retorna la misma membresía\n")
    print("5) Cambiando Básica a Familiar")
    familiar = basica.cambiar_suscripcion(2)

    assert isinstance(familiar, Familiar)
    assert familiar.costo == 5000
    assert familiar.cantidad_dispositivos == 5
    assert familiar.dias_regalo == 7
    assert familiar.correo_suscriptor == correo
    assert familiar.numero_tarjeta == tarjeta
    print("OK: Básica cambió a Familiar correctamente\n")
    print("6) Probando cambio no válido en Familiar")
    mismo_familiar = familiar.cambiar_suscripcion(2)

    assert mismo_familiar is familiar
    print("OK: Familiar no puede cambiar a Familiar; retorna la misma membresía\n")
    print("7) Cambiando Familiar a Sin Conexión")
    sin_conexion = familiar.cambiar_suscripcion(3)

    assert isinstance(sin_conexion, SinConexion)
    assert sin_conexion.costo == 3500
    assert sin_conexion.cantidad_dispositivos == 2
    assert sin_conexion.dias_regalo == 7
    print("OK: Familiar cambió a Sin Conexión correctamente\n")
    print("8) Probando cambio no válido en Sin Conexión")
    misma_sin_conexion = sin_conexion.cambiar_suscripcion(3)

    assert misma_sin_conexion is sin_conexion
    print("OK: Sin Conexión no puede cambiar a Sin Conexión\n")
    print("9) Cambiando Sin Conexión a Pro")
    pro = sin_conexion.cambiar_suscripcion(4)

    assert isinstance(pro, Pro)
    assert pro.costo == 7000
    assert pro.cantidad_dispositivos == 6
    assert pro.dias_regalo == 15
    print("OK: Sin Conexión cambió a Pro correctamente\n")
    print("10) Probando cambio no válido en Pro")
    mismo_pro = pro.cambiar_suscripcion(4)

    assert mismo_pro is pro
    print("OK: Pro no puede cambiar a Pro\n")
    print("11) Probando métodos heredados en Pro")

    assert hasattr(pro, "modificar_control_parental")
    assert hasattr(pro, "incrementar_contenido_sin_conexion")

    pro.modificar_control_parental()
    pro.incrementar_contenido_sin_conexion()

    print("OK: Pro tiene los métodos de Familiar y Sin Conexión\n")
    print("12) Cancelando suscripción desde Pro")
    gratis_cancelada = pro.cancelar_suscripcion()

    assert isinstance(gratis_cancelada, Gratis)
    assert gratis_cancelada.correo_suscriptor == correo
    assert gratis_cancelada.numero_tarjeta == tarjeta
    print("OK: Pro canceló y volvió a Gratis\n")

    print("Todo correcto ✅")


if __name__ == "__main__":
    probar()