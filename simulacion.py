import random

# Clase Especie
class Especie:
    def _init_(self, nombre, nombre_cientifico, tasa_crecimiento, competencia, dispersion):
        self.nombre = nombre
        self.nombre_cientifico = nombre_cientifico
        self.tasa_crecimiento = tasa_crecimiento
        self.competencia = competencia
        self.dispersion = dispersion

# Lista de especies
especies = [
    Especie("Pino chamaite", "Pinus montezumae", 0.25, 0.3, 15),
    Especie("Encino amarillo", "Quercus magnoliifolia", 0.20, 0.4, 10),
    Especie("Modroño", "Arbutus xalapensis", 0.18, 0.35, 12),
    Especie("Pozancle", "Buddleja americana", 0.30, 0.2, 20),
    Especie("Mamojuaxtle", "Clethra mexicana", 0.22, 0.3, 10),
    Especie("Borreguito", "Salix paradoxa", 0.35, 0.1, 25),
    Especie("Roble blanco", "Quercus laeta", 0.21, 0.4, 9),
    Especie("Enebro", "Juniperus deppeana", 0.15, 0.5, 8),
    Especie("Ayarin", "Pseudotsuga menziesii", 0.19, 0.45, 11),
    Especie("Pino hortiguillo", "Pinus lawsonii", 0.23, 0.3, 14),
]

# Función para simular crecimiento
def simular_crecimiento(especie, poblacion_actual):
    crecimiento = poblacion_actual * especie.tasa_crecimiento * (1 - especie.competencia)
    return poblacion_actual + crecimiento

# Función para dispersar semillas
def dispersar_semillas(especie, x, y):
    nuevo_x = x + random.uniform(-especie.dispersion, especie.dispersion)
    nuevo_y = y + random.uniform(-especie.dispersion, especie.dispersion)
    return nuevo_x, nuevo_y

# EJEMPLO DE USO:
if _name_ == "_main_":
    especie = especies[0]  # Pino chamaite
    poblacion = 100
    nueva_poblacion = simular_crecimiento(especie, poblacion)
    print(f"Nueva población de {especie.nombre}: {nueva_poblacion}")

    x, y = 50, 50
    nueva_pos = dispersar_semillas(especie, x, y)
    print(f"Semilla de {especie.nombre} cayó en: {nueva_pos}")
