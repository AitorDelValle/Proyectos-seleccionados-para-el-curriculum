from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fullscreen = True
window.cog_button.visible = False

sky_texture = load_texture('assets/cielo.png')
stone_texture = load_texture('assets/piedra.png')
grass_texture = load_texture('assets/grass.png')
brick_texture = load_texture('assets/ladrillo.png')
gold_texture = load_texture('assets/gold.png')
terracote_texture = load_texture('assets/terracota.png')
arm_texture = load_texture('assets/arm_texture.png')
tnt_texture = load_texture('assets/tnt.png')
block_sound = Audio('bloque.mp3', loop = False, autoplay = False)

class Voxel(Button):
	def __init__(self, position=(0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'models_compressed/Grass_block.obj',
			origin_y = 0.5,
			texture = texture,
			color = color.rgb(150,150,150),
			highlight_color = color.cyan,
			scale = 0.5
		)

	def input(self, key):
		blocktexture = 1
		if held_keys['left mouse'] or held_keys['right mouse']:
			hand.active()
		else:
			hand.passive()
		if held_keys['1']:
			blocktexture = 1
		if held_keys['2']:
			blocktexture = 2
		if held_keys['3']:
			blocktexture = 3
		if held_keys['4']:
			blocktexture = 4
		if held_keys['5']:
			blocktexture = 5
		if self.hovered:
			if key == "left mouse down":
				if blocktexture == 1:
					voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
					block_sound.play()
				elif blocktexture == 2:
					voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
					block_sound.play()
				elif blocktexture == 3:
					voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
					block_sound.play()
				elif blocktexture == 4:
					voxel = Voxel(position = self.position + mouse.normal, texture = gold_texture)
					block_sound.play()
				elif blocktexture == 5:
					voxel = Voxel(position = self.position + mouse.normal, texture = terracote_texture)
					block_sound.play()

			elif key == "right mouse down":
				destroy(self)
				block_sound.play()

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 3000,
			double_sided = True
		)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'models_compressed/arm.obj',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(695,-10,0),
			position = Vec2(0.65,-0.5)
		)
	def active(self):
		self.position = Vec2(0.55,-0.4)

	def passive(self):
		self.position = Vec2(0.65,-0.5)

chunkSize = 16

for z in range(chunkSize):
	for x in range(chunkSize):
		voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()