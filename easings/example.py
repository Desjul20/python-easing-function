import pygame
from pygame.locals import *
import easings
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

time = 0

while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  
  # Draw.
  
  time += 1/144
  if time < 5:
    pygame.draw.rect(screen, (255,255,255), [round(easings.linear(time,0,1230,5)), 35, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outBack(time,0,1230,5)), 95, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outQuart(time,0,1230,5)), 155, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outQuint(time,0,1230,5)), 215, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outBounce(time,0,1230,5)), 275, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outCubic(time,0,1230,5)), 335, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outCirc(time,0,1230,5)), 395, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outExpo(time,0,1230,5)), 455, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outElastic(time,0,1230,5,1,1)), 515, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outSine(time,0,1230,5)), 575, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outQuad(time,0,1230,5)), 635, 50, 50])
  else:
    pygame.draw.rect(screen, (255,255,255), [round(easings.linear(5,0,1230,5)), 35, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outBack(5,0,1230,5)), 95, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outQuart(5,0,1230,5)), 155, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outQuint(5,0,1230,5)), 215, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outBounce(5,0,1230,5)), 275, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outCubic(5,0,1230,5)), 335, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outCirc(5,0,1230,5)), 395, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outExpo(5,0,1230,5)), 455, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outElastic(5,0,1230,5,1,1)), 515, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outSine(5,0,1230,5)), 575, 50, 50])
    pygame.draw.rect(screen, (255,255,255), [round(easings.outQuad(5,0,1230,5)), 635, 50, 50])
  pygame.display.flip()
  fpsClock.tick(144)
	

	
	
