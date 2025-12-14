# Clase Base: Criatura (Abstracción y Encapsulación)
class Criatura:
    """
    Clase base para cualquier criatura o personaje.
    
    Técnicas POO:
    - Abstracción: Define la estructura esencial (atributos y comportamientos) 
      que todas las criaturas deben tener, ocultando los detalles internos de 
      cálculo de daño y manejo de salud.
    - Encapsulación: Los atributos internos (salud, fuerza, etc.) se manejan 
      a través de métodos (recibir_daño, esta_viva), aunque en Python los 
      atributos son por defecto públicos.
    """
    
    # Método Constructor
    def __init__(self, nombre, fuerza, sabiduria, defensa, salud):
        self.nombre = nombre
        self.fuerza = fuerza
        self.sabiduria = sabiduria
        self.defensa = defensa
        self.salud = salud
    # Comportamiento
    def mostrar_stats(self):
        """Muestra los atributos actuales de la criatura."""
        print(f"\n--- {self.nombre} ---")
        print(f"  Fuerza: {self.fuerza}")
        print(f"  Sabiduría: {self.sabiduria}")
        print(f"  Defensa: {self.defensa}")
        print(f"  Salud: {self.salud}")
    # Comportamiento    
    def esta_viva(self):
        """Verifica si la criatura tiene salud positiva."""
        return self.salud > 0
    # Comportamiento (Manejo de estado)
    def recibir_daño(self, cantidad):
        """Reduce la salud de la criatura y verifica si muere."""
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0
        if not self.esta_viva():
            print(f"¡{self.nombre} ha caído!")
    # Comportamiento (Abstracción/Método Base de Cálculo)        
    def calcular_ataque(self, objetivo):
        """Calcula el daño base antes de la defensa del objetivo."""
        # Daño simple: Fuerza más Sabiduría
        return self.fuerza + (self.sabiduria // 2)
    # Comportamiento (Abstracción)
    def atacar(self, objetivo):
        """Realiza un ataque a otra criatura."""
        daño_base = self.calcular_ataque(objetivo)
        daño_final = max(0, daño_base - objetivo.defensa)  # El daño no puede ser negativo

        print(f"\n* {self.nombre} ataca a {objetivo.nombre}!")
        print(f"  Daño base: {daño_base} - Defensa de {objetivo.nombre}: {objetivo.defensa}")
        print(f"  Daño infligido: {daño_final}")

        objetivo.recibir_daño(daño_final)
        if objetivo.esta_viva():
            print(f"  Salud restante de {objetivo.nombre}: {objetivo.salud}")
## Subclase: Elfo (Herencia y Polimorfismo)            
class Elfo(Criatura):
    """Subclase de Criatura, bonificación a la Sabiduría."""
    def __init__(self, nombre, fuerza, sabiduria, defensa, salud, bonif_sabiduria):
        super().__init__(nombre, fuerza, sabiduria, defensa, salud)
        self.bonif_sabiduria = bonif_sabiduria
        # Aumentar la Sabiduría base con la bonificación
        self.sabiduria += bonif_sabiduria
    def mostrar_stats(self):
        """Sobrescribe para mostrar la bonificación de sabiduría."""
        super().mostrar_stats()
        print(f"  Bonificación de Sabiduría: +{self.bonif_sabiduria}")
    def calcular_ataque(self, objetivo):
        """El Elfo usa su Sabiduría multiplicada por un factor."""
        # El Elfo usa la Sabiduría como principal fuente de daño
        return self.sabiduria * 2 + (self.fuerza // 2)
## Subclase: Orco (Herencia y Polimorfismo)    
class Orco(Criatura):
       """Subclase de Criatura, utiliza Furia para un ataque más fuerte."""
       def __init__(self, nombre, fuerza, sabiduria, defensa, salud, furia):
        super().__init__(nombre, fuerza, sabiduria, defensa, salud)
        self.furia = furia

def mostrar_stats(self):
        """Sobrescribe para mostrar el nivel de Furia."""
        super().mostrar_stats()
        print(f"  Furia: {self.furia}")

def calcular_ataque(self, objetivo):
        """El Orco utiliza Furia para potenciar su Fuerza."""
        # El Orco usa su Fuerza multiplicada por su nivel de Furia
        return self.fuerza * self.furia


def iniciar_combate(c_1, c_2):
    """Simula un combate por turnos entre dos criaturas."""
    turno = 1
    print("\n\n################ INICIO DEL COMBATE ################")
    print(f"Luchadores: {c_1.nombre} vs {c_2.nombre}")
    c_1.mostrar_stats()
    c_2.mostrar_stats()

    while c_1.esta_viva() and c_2.esta_viva():
        print(f"\n======== Turno {turno} ========")
        
        # Ataque de la Criatura 1
        if c_1.esta_viva():
            c_1.atacar(c_2)

        # Si el objetivo sigue vivo, la Criatura 2 ataca
        if c_2.esta_viva():
            c_2.atacar(c_1)
        
        turno += 1

    print("\n################ FIN DEL COMBATE ################")
    if c_1.esta_viva():
        print(f"¡El ganador es {c_1.nombre}!")
    elif c_2.esta_viva():
        print(f"¡El ganador es {c_2.nombre}!")
    else:
        print("Ambos han caído. ¡Es un empate!")  
 # ----------------- Ejemplo de Uso -----------------

# Crear instancias de las criaturas
elfo_arquero = Elfo(nombre="Mercurio", fuerza=8, sabiduria=15, defensa=5, salud=120, bonif_sabiduria=3)
orco_berserker = Orco(nombre="Gronko", fuerza=15, sabiduria=2, defensa=8, salud=150, furia=2)

# Iniciar el combate
iniciar_combate(elfo_arquero, orco_berserker)        
