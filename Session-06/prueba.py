import os
import random
import arcade
import PIL
from arcade.draw_commands import Texture

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_PLAYER = 0.5
SCREEN_TITLE = "Bin Laden Minigame"
COIN_COUNT = 100
BULLET_SPEED = 5

coin = arcade.Sprite("../IMAGES/cor.jpeg", SPRITE_SCALING_COIN)

class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    def __init__(self, texture_list):
        super().__init__()

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.explosions_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        self.explosion_texture_list = []
        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = "../IMAGES/fbi.jpeg"

        # Load the explosions from a sprite sheet
        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("../IMAGES/ort.jpeg", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50  # Starting position
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("../IMAGES/cor.jpeg", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.explosions_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        arcade.sound.play_sound(self.gun_sound)
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.angle = 90
        bullet.change_y = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)
    def on_update(self, delta_time):
        self.bullet_list.update()
        self.explosions_list.update()
        self.coin_list.update()
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            if len(hit_list) > 0:
                # Make an explosion
                explosion = Explosion(self.explosion_texture_list)
                # Move it to the location of the coin
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y
                explosion.update()
                self.explosions_list.append(explosion)
                bullet.remove_from_sprite_lists()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1




def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()




