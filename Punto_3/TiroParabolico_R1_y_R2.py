import pygame
import math

#parametros iniciales
posx = 15
posy = 900
radio = 10
valid = True

dimension = input("Ingrese la dimension deseada (R1/R2): ")

if dimension == "R1":
    grados = 90
    posx=765
    velocidad = input("Ingrese la velocidad inicial: ")
elif dimension == "R2":
    grados = input("Ingrese los grados: ")
    velocidad = input("Ingrese la velocidad inicial: ")
else:
    print("Ingrese una dimension valida")
    valid = False

# Inicializar pygame
if valid:
    pygame.init()

    # Definir constantes
    WIDTH = 1500 # Ancho de la ventana
    HEIGHT = 1000 # Alto de la ventana
    FPS = 30 # Fotogramas por segundo
    G = 9.8 # Aceleración de la gravedad

    # Definir colores
    BLACK = (0, 0, 0) # Negro
    WHITE = (255, 255, 255) # Blanco
    RED = (255, 0, 0) # Rojo
    GREEN = (0, 255, 0) # Verde
    BLUE = (0, 0, 255) # Azul

    # Crear la ventana
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de proyectil")

    # Reloj para controlar el tiempo
    clock = pygame.time.Clock()

    # Lista para almacenar los proyectiles
    projectiles = []

    # Clase projectile
    class projectile(object):
        def __init__(self, x, y, radius, facing, vel):
            self.x = x # Posición x del proyectil
            self.y = y # Posición y del proyectil
            self.radius = radius # Radio del proyectil
            self.color = WHITE # Color del proyectil
            self.facing = int(facing) * math.pi/180 # Dirección del proyectil
            self.vel = int(vel) # Velocidad del proyectil (en m/s)
            self.t = 0 # Tiempo del proyectil (en s)

        def draw(self, screen):
            # Dibujar el proyectil como un círculo en la pantalla
            pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)

    # Variable para controlar el bucle principal
    running = True


    #creacion del proyectil
    projectiles.append(projectile(posx , posy, radio, grados, velocidad))

    # Bucle principal
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        #Detener el programa cuando se alcanza la posy inicial
        for projectile in projectiles:
            if  projectile.y > posy:
                running = False
                break

            # Obtener el tiempo transcurrido en segundos
            dt = clock.get_time() / 1000
            # Actualizar el tiempo del proyectil
            projectile.t += dt

            # Calcular las nuevas coordenadas del proyectil
            projectile.x = projectile.x + projectile.vel * math.cos(projectile.facing) * projectile.t
            projectile.y = projectile.y - (projectile.vel * math.sin(projectile.facing) * projectile.t - 0.5 * G * projectile.t**2)
        
        # Rellenar la pantalla con color negro
        screen.fill(BLACK)
        # Pintar una linea roja
        pygame.draw.lines(screen, RED, False, [(0,posy), (1500,posy)], 1)
        # Dibujar todos los proyectiles en la pantalla
        for projectile in projectiles:
            projectile.draw(screen)
            
        # Actualizar la pantalla
        pygame.display.update()
    # Salir de pygame
    pygame.quit()