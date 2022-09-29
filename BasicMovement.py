from djitellopy import tello
from time import sleep
import pygame
import cv2

drone = tello.Tello()
drone.connect()
#drone.streamon()

#pygame.init()
#screen = pygame.display.set_mode((400, 400))


if(__name__ == '__main__'):
    print('Hello Mundo '+ str(drone.get_battery()) )
    '''
    while True:
        pygame.event.get()
        print('Hello')
        img = drone.get_frame_read().frame
        screen.blit(img, 0, 0)
        pygame.display.flip()

        pygame.display.update()

        drone.send_rc_control(0, 0, 0, 0)
        #sleep(1)
    '''