import random
import arcade
from pyglet.math import Vec2


SPRITE_SCALING = .3

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

VIEWPORT_MARGIN = 220

CAMERA_SPEED = 0.1

PLAYER_MOVEMENT_SPEED = 15

NUMBER_OF_COINS = 5
SPRITE_SCALING_COIN = .025
SPRITE_SCALING_LASER = 0.08
BULLET_SPEED = 15

coolice_sound = arcade.load_sound("fullsizerender.wav")

class MyGame(arcade.Window):
    """ Main application class. """

    class Entity(arcade.Sprite):
        def __init__(self, name_folder, name_file):
            super().__init__()

            # Default to facing right
            self.facing_direction = RIGHT_FACING

            # Used for image sequences
            self.cur_texture = 0
            self.scale = CHARACTER_SCALING
            self.character_face_direction = RIGHT_FACING

            main_path = f":resources:images/animated_characters/{name_folder}/{name_file}"

            self.idle_texture_pair = load_texture_pair(f"Super_idle_R1_clear.png")
            self.jump_texture_pair = load_texture_pair(f"Super_idle_R1_clear.png")
            self.fall_texture_pair = load_texture_pair(f"FALL1.png")

            # Load textures for walking
            self.walk_textures = []
            for i in range(1, 5):
                texture = load_texture_pair(f"FLY{i}.png")
                self.walk_textures.append(texture)

            # Load textures for climbing
            self.climbing_textures = []
            texture = arcade.load_texture(f"{main_path}_climb0.png")
            self.climbing_textures.append(texture)
            texture = arcade.load_texture(f"{main_path}_climb1.png")
            self.climbing_textures.append(texture)

            # Set the initial texture
            self.texture = arcade.load_texture("Super_idle_R1_clear.png")
            # Hit box will be set based on the first image used. If you want to specify
            # a different hit box, you can do it like the code below.
            # set_hit_box = [[-22, -64], [22, -64], [22, 28], [-22, 28]]
            self.hit_box = self.texture.hit_box_points

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)


        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.bullet_list = None

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

        self.background = None


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        self.background = arcade.load_texture("Untitled.jpeg")
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("Super_idle_R1_clear.png",
                                           scale=2.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150
        self.player_sprite.change_angle = False*10
        self.player_sprite.update_animation(1/60)
        self.player_sprite.Dead = False
        self.player_list.append(self.player_sprite)

        self.player_cream = arcade.Sprite("FVR1.png",
                                           scale=2.5)
        self.player_cream.center_x = 600
        self.player_cream.center_y
        self.player_cream.change_y += 1000
        self.player_cream.change_angle = 0
        self.player_cream.update_animation(1/60)
        self.player_list.append(self.player_cream)

        for x in range(0, 1000, 70):
            for y in range(0, 1000, 639):
                # Randomly skip a box so the player can find a way through
                    wall = arcade.Sprite("Block.jpg", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for x in range(-40, 1080, 1079):
            for y in range(0, 1000, 70):
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

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.bullet_list.draw()



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

        if key == arcade.key.SPACE:
            """
                    Called whenever the mouse button is clicked.
                    """
            # Gunshot sound
            # Create a bullet
            bullet = arcade.Sprite("Laser.png", SPRITE_SCALING_LASER)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = 180

            # Give the bullet a speed
            bullet.change_x = BULLET_SPEED

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x + 41
            bullet.center_y = self.player_sprite.center_y + 105

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)

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
        self.bullet_list.update()

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()