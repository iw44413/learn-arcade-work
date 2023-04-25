import random
import arcade
SPRITE_SCALING_PLAYER = 2.5
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
skip_sound = arcade.load_sound("kingcrimson.mp3")
Movement_speed = 5
COIN_COUNT = 25
SPRITE_SCALING_COIN = 1.5



class Coin(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None
        self.mini_plane_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self, change_x=3, change_y=3):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        # Character image from kenney.nl
        Plane = "Aerosmithl1.png"
        Tank = "Bc1R.png"
        self.player_Aero = arcade.Sprite(Plane, SPRITE_SCALING_PLAYER)
        self.player_Aero.center_x = 50
        self.player_Aero.center_y = 350
        self.player_list.append(self.player_Aero)


        self.player_Bc = arcade.Sprite(Tank, SPRITE_SCALING_PLAYER)
        self.player_Bc.center_x = 50
        self.player_Bc.center_y = 50
        self.player_list.append(self.player_Bc)

        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("Bc1R.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)


        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            mini = Coin("Aerosmithl1.png", SPRITE_SCALING_COIN)

            # Position the coin
            mini.center_x = random.randrange(SCREEN_WIDTH)
            mini.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(mini)





    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(700, 100, 600, 1000, (23, 71, 195))
        arcade.draw_rectangle_filled(700, 100, 600, 900, (77, 61, 175))
        arcade.draw_rectangle_filled(700, 100, 600, 800, (187, 78, 141))
        arcade.draw_rectangle_filled(700, 100, 600, 700, (141, 51, 107))
        arcade.draw_rectangle_filled(700, 100, 600, 600, (178, 64, 69))
        arcade.draw_rectangle_filled(700, 100, 600, 500, (233, 103, 41))
        arcade.draw_rectangle_filled(700, 100, 600, 400, (247, 219, 21))
        arcade.draw_rectangle_filled(700, 100, 600, 300, (0, 111, 56))

        arcade.draw_rectangle_filled(100, 100, 800, 1000, (20, 20, 20))
        arcade.draw_rectangle_filled(100, 100, 800, 900, (30, 30, 30))
        arcade.draw_rectangle_filled(100, 100, 800, 800, (40, 40, 40))
        arcade.draw_rectangle_filled(100, 100, 800, 700, (50, 50, 50))
        arcade.draw_rectangle_filled(100, 100, 800, 600, (60, 60, 60))
        arcade.draw_rectangle_filled(100, 100, 800, 500, (70, 70, 70))
        arcade.draw_rectangle_filled(100, 100, 800, 400, (80, 80, 80))
        arcade.draw_rectangle_filled(100, 100, 800, 300, (0, 90, 90))

        arcade.draw_circle_filled(500, 600, 75, (240, 196, 32))
        arcade.draw_rectangle_filled(30, 50, 100, 450, (0, 255, 255))
        arcade.draw_rectangle_filled(130, 150, 100, 450, (0, 255, 255))
        arcade.draw_rectangle_filled(230, 125, 100, 450, (0, 255, 255))
        arcade.draw_rectangle_filled(330, 175, 100, 450, (0, 255, 255))
        arcade.draw_rectangle_filled(430, 50, 140, 450, (0, 255, 255))

        arcade.draw_rectangle_filled(100, 00, 2000, 225, (255, 255, 255))
        arcade.draw_rectangle_filled(100, 00, 2000, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(100, 50, 2000, 10, (255, 255, 255))
        arcade.draw_rectangle_filled(20, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(120, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(220, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(320, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(420, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(520, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(620, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(720, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(820, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(920, 00, 20, 200, (90, 90, 90))
        arcade.draw_rectangle_filled(1020, 00, 20, 200, (90, 90, 90))

        arcade.draw_rectangle_filled(650, 175, 25, 100, (115, 83, 42))
        arcade.draw_triangle_filled(600, 250, 700, 250, 650, 350, (42, 126, 25))
        arcade.draw_triangle_filled(600, 225, 700, 225, 650, 350, (42, 126, 25))
        arcade.draw_triangle_filled(600, 200, 700, 200, 650, 350, (42, 126, 25))
        arcade.draw_triangle_filled(600, 175, 700, 175, 650, 350, (42, 126, 25))

        arcade.draw_rectangle_filled(850, 175, 25, 100, (115, 83, 42))
        arcade.draw_triangle_filled(800, 250, 900, 250, 850, 350, (42, 126, 25))
        arcade.draw_triangle_filled(800, 225, 900, 225, 850, 350, (42, 126, 25))
        arcade.draw_triangle_filled(800, 200, 900, 200, 850, 350, (42, 126, 25))
        arcade.draw_triangle_filled(800, 175, 900, 175, 850, 350, (42, 126, 25))
        self.player_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.player_Bc.center_x > 1000:
            self.player_Bc.center_x = 0
            arcade.play_sound(skip_sound)
        if self.player_Bc.center_x < 0:
            self.player_Bc.center_x = 1000
            arcade.play_sound(skip_sound)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_Bc.update()
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_Bc,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_Aero,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score -= 1

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_Aero.center_x = x
        self.player_Aero.center_y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        arcade.play_sound(skip_sound)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_Bc.center_x = self.player_Bc.center_x + 25
        elif key == arcade.key.LEFT:
            self.player_Bc.center_x = self.player_Bc.center_x - 25

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player_Bc.center_x = self.player_Bc.center_x + 25
        elif key == arcade.key.LEFT:
            self.player_Bc.center_x = self.player_Bc.center_x - 25

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()