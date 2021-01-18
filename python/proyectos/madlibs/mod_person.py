def madlib():
    persona = input("persona: ")
    nombre = input("nombre: ")
    adjetivo = input("adjetivo: ")
    verbo = input("verbo: ")

    madlib = f"Érase un niño enfermizo. Su madre, opulentísima señora, andaba loca con el afán de\
    darle salud, y el médico, fijándose en la índole del {persona} del niño, decía que,\
    principalmente, {nombre} de una especie de atonía o insensibilidad, efecto de que su sistema\
    nervioso se encontraba como amodorrado o dormido, y no comunicaba al {adjetivo} las reacciones\
    vitales y al espíritu la fuerza necesaria. Es decir, que Fernandito, que así le llamaba vivía\
    a medias, como {verbo}, lo cual es sobrado para una planta, pero insuficiente para un hombre"

    print(madlib)