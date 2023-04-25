import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = .3

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

VIEWPORT_MARGIN = 220

CAMERA_SPEED = 0.1

PLAYER_MOVEMENT_SPEED = 15

NUMBER_OF_COINS = 5
SPRITE_SCALING_COIN = .025

coolice_sound = arcade.load_sound("fullsizerender.wav")

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)


        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        self.score = 0

        # Set up the player
        self.player_sprite = None
        self.player_cream = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None
        self.physics_engine2 = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.Dead = False


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("Bc1R.png",
                                           scale=2.5)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_sprite.change_angle = False*10
        self.player_sprite.update_animation(1/60)
        self.player_sprite.Dead = False
        self.player_list.append(self.player_sprite)

        self.player_cream = arcade.Sprite("cream.png",
                                           scale=.25)
        self.player_cream.center_x = 100
        self.player_cream.center_y
        self.player_cream.change_y += 1000
        self.player_cream.change_angle = True*100
        self.player_cream.update_animation(1/60)
        self.player_list.append(self.player_cream)

        # -- Set up several columns of walls
        for x in range(0, 5000, 250):
            for y in range(0, 5000, 70):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("Block.jpg", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for x in range(0, 5000, 70):
            for y in range(0, 5000, 4999):
                # Randomly skip a box so the player can find a way through
                    wall = arcade.Sprite("Block.jpg", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)


        for x in range(0, 5000, 4999):
            for y in range(0, 5000, 70):
                # Randomly skip a box so the player can find a way through
                    wall = arcade.Sprite("Block.jpg", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for i in range(NUMBER_OF_COINS):
            coin = arcade.Sprite("arrow.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(5000)
                coin.center_y = random.randrange(5000)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.wall_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.player_cream, self.wall_list)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Render the screen. """
        self.clear()

        self.camera_sprites.use()


        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()



        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()

        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.BLUE)
        text = 'Arrows collected', self.score
        arcade.draw_text(text, 10, 10, arcade.color.BLACK, 20)

        if self.Dead == True:
            arcade.draw_rectangle_filled(self.width // 2,
                                         20,
                                         self.width,
                                         40,
                                         arcade.color.BLUE)
            text = 'YOUR DEAD'
            arcade.draw_text(text, 10, 10, arcade.color.BLACK, 20)

        if self.score == 5:
            self.player_sprite.Dead == True
            self.player_cream.change_y += 0
            arcade.draw_rectangle_filled(self.width // 2,
                                         20,
                                         self.width,
                                         40,
                                         arcade.color.BLUE)
            text = 'YOU WIN!!!!'
            arcade.draw_text(text, 10, 10, arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        self.player_cream.change_x = 0
        self.player_cream.change_y = 10


        if self.player_cream.center_y > 4900:
            self.player_cream.center_x = self.player_sprite.center_x
            self.player_cream.center_y = 100
            arcade.play_sound(coolice_sound)

        if self.up_pressed and not self.down_pressed and not self.Dead:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed and not self.Dead:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed and not self.Dead:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed and not self.Dead:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        hit_list = arcade.check_for_collision_with_list(self.player_cream,
                                                        self.player_list)
        for player in hit_list:
            player.remove_from_sprite_lists()
            self.Dead = True
            self.player_cream.change_y += 0

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        self.physics_engine.update()
        self.physics_engine2.update()

        self.scroll_to_player()



    def scroll_to_player(self):

        """

        Scroll the window to the player.



        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.

        Anything between 0 and 1 will have the camera move to the location with a smoother

        pan.

        """



        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)



    def on_resize(self, width, height):

        """

        Resize window

        Handle the user grabbing the edge and resizing the window.

        """

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))



def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()