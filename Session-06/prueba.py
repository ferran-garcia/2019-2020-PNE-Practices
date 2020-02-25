import dataclasses as dataclasses

import random
import arcade
import os


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_PLAYER = 0.5
COIN_COUNT = 50

coin = arcade.Sprite("TTT.jpeg", SPRITE_SCALING_COIN)
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.score = 0

        self.player_sprite = arcade.Sprite("BIN.jpeg", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50  # Starting position
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.set_mouse_visible(False)
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("TTT.jpeg", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

        def on_draw(self):
            """ Draw everything """
            arcade.start_render()
            self.coin_list.draw()
            self.player_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



