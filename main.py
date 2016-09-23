#!/usr/bin/python
import operator
import pygame
from pygame.locals import *
from sys import exit

from tile import Tile
from game import Game

pygame.init()

windowSurface = pygame.display.set_mode((980, 640), 0, 32)
pygame.display.set_caption('War in Hex')

moveSound = pygame.mixer.Sound('assets/tile_drop.wav')

playAreaSurface = pygame.image.load('assets/playarea.png')
basicFont = pygame.font.SysFont(None, 48)


sideBoardSurface = pygame.image.load('assets/sideboard.png')

blackGenTile = pygame.image.load('assets/black_general_tile.png')
blackGenTile.convert_alpha()
blackHeliTile = pygame.image.load('assets/black_helicopter_tile.png')
blackHeliTile.convert_alpha()
blackBoatTile = pygame.image.load('assets/black_boat_tile.png')
blackBoatTile.convert_alpha()
blackInfTile = pygame.image.load('assets/black_troops_tile.png')
blackInfTile.convert_alpha()
blackTankTile = pygame.image.load('assets/black_tank_tile.png')
blackTankTile.convert_alpha()

whiteGenTile = pygame.image.load('assets/white_general_tile.png')
whiteGenTile.convert_alpha()
whiteBoatTile = pygame.image.load('assets/white_boat_tile.png')
whiteBoatTile.convert_alpha()
whiteInfTile = pygame.image.load('assets/white_troops_tile.png')
whiteInfTile.convert_alpha()
whiteTankTile = pygame.image.load('assets/white_tank_tile.png')
whiteTankTile.convert_alpha()
whiteHeliTile = pygame.image.load('assets/white_helicopter_tile.png')
whiteHeliTile.convert_alpha()

windowSurface.blit(playAreaSurface, (0,0))
windowSurface.blit(sideBoardSurface, (750, 0))

game = Game()

game.addTile(Tile(800, 10, "Black Helicopter 1", blackHeliTile, windowSurface))
game.addTile(Tile(850, 10, "Black Helicopter 2", blackHeliTile, windowSurface))
game.addTile(Tile(900, 10, "Black Helicopter 3", blackHeliTile, windowSurface))

game.addTile(Tile(800, 60, "Black Battleship 1", blackBoatTile, windowSurface))
game.addTile(Tile(850, 60, "Black Battleship 2", blackBoatTile, windowSurface))
game.addTile(Tile(900, 60, "Black Battleship 3", blackBoatTile, windowSurface))

game.addTile(Tile(800, 110, "Black General", blackGenTile, windowSurface))
game.addTile(Tile(850, 110, "Black Infantry 1", blackInfTile, windowSurface))
game.addTile(Tile(900, 110, "Black Infantry 2", blackInfTile, windowSurface))

game.addTile(Tile(800, 160, "Black Tank 1", blackTankTile, windowSurface))
game.addTile(Tile(850, 160, "Black Tank 2", blackTankTile, windowSurface))

game.addTile(Tile(800, 210, "White Battleship 1", whiteBoatTile, windowSurface))
game.addTile(Tile(850, 210, "White Battleship 2", whiteBoatTile, windowSurface))
game.addTile(Tile(900, 210, "White Battleship 3", whiteBoatTile, windowSurface))

game.addTile(Tile(800, 260, "White General", whiteGenTile, windowSurface))
game.addTile(Tile(850, 260, "White Tank 1", whiteTankTile, windowSurface))
game.addTile(Tile(900, 260, "White Tank 2", whiteTankTile, windowSurface))

game.addTile(Tile(800, 310, "White Infantry 1", whiteInfTile, windowSurface))
game.addTile(Tile(850, 310, "White Infantry 2", whiteInfTile, windowSurface))
game.addTile(Tile(900, 310, "White Helicopter 1", whiteHeliTile, windowSurface))

game.addTile(Tile(800, 360, "White Helicopter 2", whiteHeliTile, windowSurface))
game.addTile(Tile(850, 360, "White Helicopter 3", whiteHeliTile, windowSurface))

game.draw()

pygame.display.update()

print "Debug:"
bh2 = game.findTileByName("Black Helicopter 2")
if(bh2 != None):
	print (bh2.x, bh2.y)

print "Debug:"
wh2 = game.findTileByLocation((850, 360))
for t in wh2:	
	print t.name

print "Debug move"
game.moveTileByCmd("Black Helicopter 1 from (800, 10) to (324, 275)")
game.moveTileByCmd("Black General from (800, 110) to (360, 325)")
game.moveTileByCmd("White General from (800, 260) to (360, 225)")


picked = None
tileStart = (0, 0)
running = True
RENDER_TIMER = pygame.USEREVENT
pygame.time.set_timer(RENDER_TIMER, int(1000/20))
while running:
	pygame.time.wait(10)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if picked:
			coord = pygame.mouse.get_pos()
			picked.setCenter(coord)
			picked.draw()
		if event.type == MOUSEBUTTONDOWN:
			coord = pygame.mouse.get_pos()
			if picked:
				picked.setCenter(coord)
				game.toTop(picked)
				print picked.name,"from",str(tileStart),"to",str((picked.x, picked.y))
				moveSound.play()
				picked = None
				continue
			for t in game.tiles:
				if t.isOn(coord):
					picked = t
					tileStart = (t.x, t.y)
#					print "Picked up", t.name
					continue
		if event.type == RENDER_TIMER:
			windowSurface.blit(playAreaSurface, (0,0))
			windowSurface.blit(sideBoardSurface, (750, 0))
			game.draw()
			pygame.display.update()

		
pygame.quit()
exit()
