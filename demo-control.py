
from camera import *
import pygame
from pygame.locals import *

ip = "10.42.0.159"

camera = CAMERA(ip)
pygame.init()
teclado= pygame.key.get_pressed()
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error wil>
        if teclado[K_RIGHT]:
            camera.move_camera(RIGHT_CODE.code,0.05)
        if teclado[K_LEFT]:
            camera.move_camera(LEFT_CODE.code,0.05)
        if teclado[K_UP]:
            camera.move_camera(UP_CODE.code,0.05)
        if teclado[K_DOWN]:
            camera.move_camera(DOWN_CODE.code,0.05)
    except:
        break
