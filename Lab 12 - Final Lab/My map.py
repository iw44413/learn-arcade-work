"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 625
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 2
TILE_SCALING = 5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 30
LAYER_NAME_ENEMIES = "Enemies"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        # Our TileMap Object

        self.tile_map = None


        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        # Load sounds
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)


        # Name of map file to load
        map_name = "MyMap.tmj"



        # Layer specific options are defined based on Layer names in a dictionary

        # Doing this will make the SpriteList for the platforms layer

        # use spatial hashing for detection.

        layer_options = {

            "Platforms": {

                "use_spatial_hash": True,

            },

        }



        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)





        # Initialize Scene with our TileMap, this will automatically add all layers

        # from the map as SpriteLists in the scene in the proper order.

        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        # Keep track of the score
        self.score = 0

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("SP1.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)


        # --- Other stuff

        # Set the background color

        if self.tile_map.background_color:

            arcade.set_background_color(self.tile_map.background_color)



        # Create the 'physics engine'

        self.physics_engine = arcade.PhysicsEnginePlatformer(

            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Platforms"]

        )


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()


        # Draw our Scene

        self.scene.draw()


        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18,
        )

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any coins

        # Loop through each coin we hit (if any) and remove it


        # Position the camera
        self.center_camera_to_player()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()