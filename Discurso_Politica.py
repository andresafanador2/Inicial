import random
Lambetazo = [ "Queridos", "Apreciados", "Distinguidos", "Honorables", "Estimados", "Respetados"]
PotencialesMarranos = [ "compatriotas", "conciudadanos", "amigos", "coterraneos", "copartidarios", "electores"]
Condicion = ["en mi gobierno", "con su apoyo", "siendo elegido", "con su ayuda", "si me siguien", "durante mi mandato"]
Compromiso = ["voy a derrotar", "vencere", "eliminare", "acabare", "luchare contra", "combatire"]
IlusionGuerrerista = ["la violencia y", "la delincuencia y", "la corrupcion y", "la inflacion y", "la pobreza y", "el desplazamiento y"]
Promesa = ["trabajare por", "garantizare", "protegere", "velare por", "promovere", "defendere"]
BeneficioPopulista = ["la educacion", "el empleo", "la seguridad", "la paz", "la idualdad", "la salud"]
DependiendodelaCantidaddeVotos = ["del pais", "de la ciudad", "de la comunidad", "de la poblacion", "para toda la gente", "de cada colombiano"]

Lambetazo_seleccionado = random.choice(Lambetazo) 
PotencialesMarranos_seleccionada = random.choice(PotencialesMarranos)
Condicion_seleccionado = random.choice(Condicion)
compromiso_seleccionado = random.choice(Compromiso)
IlusionGuerrera_seleccionado = random.choice(IlusionGuerrerista)
Promesa_seleccionado = random.choice(Promesa)
BeneficioPopulista_seleccionado = random.choice(BeneficioPopulista)
DependiendodelaCantidaddeVotos_seleccionado = random.choice(DependiendodelaCantidaddeVotos)

print("Discurso generado: " + Lambetazo_seleccionado + " " + PotencialesMarranos_seleccionada + " " + Condicion_seleccionado + " " 
      + compromiso_seleccionado + " " + IlusionGuerrera_seleccionado + " " + Promesa_seleccionado + " " + BeneficioPopulista_seleccionado + " " + DependiendodelaCantidaddeVotos_seleccionado)
