#!/usr/bin/python

import pygame

import pygame.gfxdraw 
#needed to draw pixels

pygame.init()
#to make sure pygame gets set up

screenWidth = 800
screenHeight = 800
#height and width of our screen we'll make next

screen = pygame.display.set_mode((screenWidth,screenHeight))
#create a screen to draw to with screenWidth and Height

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

running = True
#let's make something so we know when to stop

while running:
	screen.fill(black)  #fill screen with black
	#pygame.gfxdraw.pixel(screen,screenWidth//2,screenHeight//2, white)
	for i in range(0, screenWidth):
		pygame.gfxdraw.pixel(screen, i, i, white)
		pygame.gfxdraw.pixel(screen, i, screenWidth - i, white)
		pygame.gfxdraw.pixel(screen, screenWidth//3, i, white)
		pygame.gfxdraw.pixel(screen, (screenWidth-screenWidth//3), i, white)
		pygame.gfxdraw.pixel(screen, i, screenHeight//3, white)
		pygame.gfxdraw.pixel(screen, i, screenHeight-screenHeight//3, white)
		
		
	for event in pygame.event.get():
	#if you try to quit , let's finish this loop
		if event.type == pygame.QUIT:
			running = False
	
	pygame.display.set_caption("Demo")
	pygame.display.flip() #this is how we update the screen we've been drawing on
