#!/usr/bin/python
import operator
import pygame
from pygame.locals import *
from sys import exit

from tile import Tile

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

windowSurface = pygame.display.set_mode((980, 640), 0, 32)
pygame.display.set_caption('Hive')

playAreaSurface = pygame.image.load('assets/playarea.png')
basicFont = pygame.font.SysFont(None, 48)


sideBoardSurface = pygame.image.load('assets/sideboard.png')

blackQueenTile = pygame.image.load('assets/black_queen_tile.png')
blackQueenTile.convert_alpha()
blackHeliTile = pygame.image.load('assets/black_hopper_tile.png')
blackHeliTile.convert_alpha()
blackBoatTile = pygame.image.load('assets/black_ant_tile.png')
blackBoatTile.convert_alpha()
blackBeetleTile = pygame.image.load('assets/black_beetle_tile.png')
blackBeetleTile.convert_alpha()
blackSpiderTile = pygame.image.load('assets/black_spider_tile.png')
blackSpiderTile.convert_alpha()

whiteQueenTile = pygame.image.load('assets/white_queen_tile.png')
whiteQueenTile.convert_alpha()
whiteBoatTile = pygame.image.load('assets/white_ant_tile.png')
whiteBoatTile.convert_alpha()
whiteBeetleTile = pygame.image.load('assets/white_beetle_tile.png')
whiteBeetleTile.convert_alpha()
whiteSpiderTile = pygame.image.load('assets/white_spider_tile.png')
whiteSpiderTile.convert_alpha()
whiteHopperTile = pygame.image.load('assets/white_hopper_tile.png')
whiteHopperTile.convert_alpha()

windowSurface.blit(playAreaSurface, (0,0))
windowSurface.blit(sideBoardSurface, (750, 0))

tiles = []
tiles.append(Tile(800, 10, "Black Helicopter 1", blackHeliTile))
tiles.append(Tile(850, 10, "Black Helicopter 2", blackHeliTile))
tiles.append(Tile(900, 10, "Black Helicopter 3", blackHeliTile))

tiles.append(Tile(800, 60, "Black Battleship 1", blackBoatTile))
tiles.append(Tile(850, 60, "Black Battleship 2", blackBoatTile))
tiles.append(Tile(900, 60, "Black Battleship 3", blackBoatTile))

tiles.append(Tile(800, 110, "Black Queen", blackQueenTile))
tiles.append(Tile(850, 110, "Black Bettle 1", blackBeetleTile))
tiles.append(Tile(900, 110, "Black Bettle 2", blackBeetleTile))

tiles.append(Tile(800, 160, "Black Spider 1", blackSpiderTile))
tiles.append(Tile(850, 160, "Black Spider 2", blackSpiderTile))

tiles.append(Tile(800, 210, "White Battleship 1", whiteBoatTile))
tiles.append(Tile(850, 210, "White Battleship 2", whiteBoatTile))
tiles.append(Tile(900, 210, "White Battleship 3", whiteBoatTile))

tiles.append(Tile(800, 260, "White Queen", whiteQueenTile))
tiles.append(Tile(850, 260, "White Spider 1", whiteSpiderTile))
tiles.append(Tile(900, 260, "White Spider 2", whiteSpiderTile))

tiles.append(Tile(800, 310, "White Bettle 1", whiteBeetleTile))
tiles.append(Tile(850, 310, "White Bettle 2", whiteBeetleTile))
tiles.append(Tile(900, 310, "White Hopper 1", whiteHopperTile))

tiles.append(Tile(800, 360, "White Hopper 2", whiteHopperTile))
tiles.append(Tile(850, 360, "White Hopper 3", whiteHopperTile))

for t in tiles:
	t.draw(windowSurface)

pygame.display.update()

picked = None
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		if picked:
			coord = pygame.mouse.get_pos()
			picked.setCenter(coord)
			picked.draw(windowSurface)
		if event.type == MOUSEBUTTONDOWN:
			coord = pygame.mouse.get_pos()
			for t in tiles:
				if picked == t:
					t.setCenter(coord)
					print "Putdown up", t.name
					picked = None
					tiles.remove(t)
					tiles.append(t)
					continue
				if t.isOn(coord):
					picked = t
					print "Picked up", t.name
					continue

	windowSurface.blit(playAreaSurface, (0,0))
	windowSurface.blit(sideBoardSurface, (750, 0))

	for t in tiles:
		t.draw(windowSurface)

	pygame.display.update()


		
