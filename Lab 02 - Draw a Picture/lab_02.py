import arcade
arcade.open_window(1000,600, "My Drawing")
arcade.set_background_color((209, 39, 65))
arcade.start_render()
def background():
    arcade.draw_rectangle_filled(700,100,600,1000, (23, 71, 195))
    arcade.draw_rectangle_filled(700,100,600,900, (77, 61, 175))
    arcade.draw_rectangle_filled(700,100,600,800, (187, 78, 141))
    arcade.draw_rectangle_filled(700,100,600,700, (141, 51, 107))
    arcade.draw_rectangle_filled(700,100,600,600, (178, 64, 69))
    arcade.draw_rectangle_filled(700,100,600,500, (233, 103, 41))
    arcade.draw_rectangle_filled(700,100,600,400, (247, 219, 21))
    arcade.draw_rectangle_filled(700,100,600,300,  (0, 111, 56))

    arcade.draw_rectangle_filled(100,100,800,1000, (20, 20, 20))
    arcade.draw_rectangle_filled(100,100,800,900, (30, 30, 30))
    arcade.draw_rectangle_filled(100,100,800,800, (40, 40, 40))
    arcade.draw_rectangle_filled(100,100,800,700, (50, 50, 50))
    arcade.draw_rectangle_filled(100,100,800,600, (60, 60, 60))
    arcade.draw_rectangle_filled(100,100,800,500, (70, 70, 70))
    arcade.draw_rectangle_filled(100,100,800,400, (80, 80, 80))
    arcade.draw_rectangle_filled(100,100,800,300, (0, 90, 90))

    arcade.draw_circle_filled(500, 600, 75, (240, 196,32))
    arcade.draw_rectangle_filled(30, 50, 100, 450, (0,255,255))
    arcade.draw_rectangle_filled(130, 150, 100, 450, (0,255,255))
    arcade.draw_rectangle_filled(230, 125, 100, 450, (0,255,255))
    arcade.draw_rectangle_filled(330, 175, 100, 450, (0,255,255))
    arcade.draw_rectangle_filled(430, 50, 140, 450, (0,255,255))

    arcade.draw_rectangle_filled(100,00,2000,225, (255, 255, 255))
    arcade.draw_rectangle_filled(100,00,2000,200, (90, 90, 90))
    arcade.draw_rectangle_filled(100,50,2000,10, (255, 255, 255))
    arcade.draw_rectangle_filled(20,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(120,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(220,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(320,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(420,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(520,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(620,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(720,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(820,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(920,00,20,200, (90, 90, 90))
    arcade.draw_rectangle_filled(1020,00,20,200, (90, 90, 90))

    arcade.draw_rectangle_filled(650,175,25,100, (115, 83, 42))
    arcade.draw_triangle_filled(600,250,700,250,650,350, (42, 126, 25))
    arcade.draw_triangle_filled(600,225,700,225,650,350, (42, 126, 25))
    arcade.draw_triangle_filled(600,200,700,200,650,350, (42, 126, 25))
    arcade.draw_triangle_filled(600,175,700,175,650,350, (42, 126, 25))

    arcade.draw_rectangle_filled(850,175,25,100, (115, 83, 42))
    arcade.draw_triangle_filled(800,250,900,250,850,350, (42, 126, 25))
    arcade.draw_triangle_filled(800,225,900,225,850,350, (42, 126, 25))
    arcade.draw_triangle_filled(800,200,900,200,850,350, (42, 126, 25))
    arcade.draw_triangle_filled(800,175,900,175,850,350, (42, 126, 25))

background()
arcade.finish_render()
arcade.run()