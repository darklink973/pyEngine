import pygame

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_sprite(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image
	
def drawSprite(screen, image, frame, width, height, scale):
    sprite_sheet_image = pygame.image.load(image).convert_alpha()
    sprite_sheet = SpriteSheet(sprite_sheet_image)
    frame = sprite_sheet.get_sprite(frame, width, height, scale, "black")
    screen.blit(frame, (150, 0))