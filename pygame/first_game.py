#!/usr/bin/python

import pygame,random
from Shiv import shiv



STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS=13

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shiv world")
clock = pygame.time.Clock()


def draw_environment(blob_list):
	game_display.fill(BLACK)

	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			blob.move()
			blob.check_bounds()
	pygame.display.update()

def main():
	blue_blobs = dict(enumerate([shiv(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
	red_blobs = dict(enumerate([shiv(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		draw_environment([blue_blobs,red_blobs])
		clock.tick(60)
		#print(red_blob.x, red_blob.y)

if __name__ == "__main__":
	main()
