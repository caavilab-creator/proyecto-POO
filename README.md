⚔️ Simulación de Combate POO con Python 🛡️

Este proyecto es una simulación de combate por turnos simple diseñada para ilustrar los cuatro pilares fundamentales de la Programación Orientada a Objetos (POO) en Python: Abstracción, Encapsulación, Herencia y Polimorfismo.

Conceptos de POO Implementados

El código está estructurado en torno a una clase base y dos subclases que demuestran cómo se aplican los principios de POO:

1. Clase Base: `Criatura` (Abstracción y Encapsulación)

Abstracción: Define la estructura esencial de cualquier personaje o enemigo (atributos como `salud`, `fuerza`, `defensa` y comportamientos como `atacar`, `recibir_daño`, `calcular_ataque`), ocultando los detalles internos de cómo se calculan el daño.
Encapsulación:Los métodos como `recibir_daño` y `esta_viva` controlan el acceso y modificación del estado interno de la criatura (`self.salud`), manteniendo la lógica de estado dentro de la clase.

2. Subclases: `Elfo` y `Orco` (Herencia y Polimorfismo)

Herencia: Ambas clases (`Elfo` y `Orco`) heredan todos los atributos y métodos de la clase base `Criatura`, permitiendo la reutilización del código.

Polimorfismo:
    * Ambas subclases modifican (sobrescriben) el método `calcular_ataque` para implementar lógicas de daño específicas de su raza:
      Elfo: Se enfoca en la `sabiduria` como fuente principal de daño (`self.sabiduria * 2 + ...`).
      Orco: Utiliza la `furia` para potenciar su `fuerza` (`self.fuerza * self.furia`).
    * El método `mostrar_stats` también es sobrescrito para mostrar atributos específicos de cada raza (Bonificación de Sabiduría o Furia).



🚀 Estructura del Código

Clase / Función ___Descripción, Conceptos POO.

Criatura : Clase base para todos los personajes. Define el esqueleto y la lógica de combate general. Abstracción, Encapsulación 
Elfo(Criatura): Subclase con bonificación a la Sabiduría y ataque basado en Sabiduría. | Herencia, Polimorfismo |
Orco(Criatura) : Subclase con atributo `furia` y ataque basado en Fuerza potenciada por Furia. | Herencia, Polimorfismo |
iniciar_combate(c1, c2) : Función principal que simula el ciclo de combate por turnos. 

▶️ Ejecución del Ejemplo

El código incluye un bloque de ejemplo al final que demuestra la creación de instancias y la simulación del combate:

1.  Se crea un `Elfo` y un `Orco` con estadísticas diferentes.

    python
    elfo_arquero = Elfo(nombre="Mercurio", fuerza=8, sabiduria=15, defensa=5, salud=120, bonif_sabiduria=3)
    orco_berserker = Orco(nombre="Gronko", fuerza=15, sabiduria=2, defensa=8, salud=150, furia=2)
    
3.  Se llama a la función de combate:
    python
    iniciar_combate(elfo_arquero, orco_berserker)
    
El resultado es un combate por turnos donde las reglas de ataque y daño cambian dinámicamente gracias al Polimorfismo (cada criatura utiliza su propia implementación de `calcular_ataque`).
