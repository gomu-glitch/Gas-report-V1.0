import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong en Python")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Reloj
clock = pygame.time.Clock()

# Paletas
paleta_ancho = 10
paleta_alto = 80

paleta_izq = pygame.Rect(20, ALTO//2 - paleta_alto//2, paleta_ancho, paleta_alto)
paleta_der = pygame.Rect(ANCHO - 30, ALTO//2 - paleta_alto//2, paleta_ancho, paleta_alto)

vel_paleta = 5

# Pelota
pelota = pygame.Rect(ANCHO//2 - 10, ALTO//2 - 10, 20, 20)
vel_pelota_x = 4
vel_pelota_y = 4

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta_izq.top > 0:
        paleta_izq.y -= vel_paleta
    if teclas[pygame.K_s] and paleta_izq.bottom < ALTO:
        paleta_izq.y += vel_paleta

    if teclas[pygame.K_UP] and paleta_der.top > 0:
        paleta_der.y -= vel_paleta
    if teclas[pygame.K_DOWN] and paleta_der.bottom < ALTO:
        paleta_der.y += vel_paleta

    # Movimiento de la pelota
    pelota.x += vel_pelota_x
    pelota.y += vel_pelota_y

    # Rebote arriba/abajo
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        vel_pelota_y *= -1

    # Rebote con paletas
    if pelota.colliderect(paleta_izq) or pelota.colliderect(paleta_der):
        vel_pelota_x *= -1

    # Si sale de la pantalla
    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.center = (ANCHO//2, ALTO//2)
        vel_pelota_x *= -1

    # Dibujar
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, paleta_izq)
    pygame.draw.rect(pantalla, BLANCO, paleta_der)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO//2, 0), (ANCHO//2, ALTO))

    pygame.display.flip()
    clock.tick(60)
