import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)
def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 10*column + 5
            y = 10*row + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = 10*column + 305
            y = 10*row + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, (0,0,0))
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = 10*column + 605
            y = 10*row + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, (0,0,0))
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
def draw_section_4():
    for row in range(31):
        for column in range(31):
            x = 10*column + 905
            y = 10*row - 5
            arcade.draw_rectangle_filled(x, y, 5, 5, (0,0,0))
            if row % 2 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, (255,255,255))
def draw_section_5():
    for row in range(30):
        for column in range(row,30):
            x = 10*column + 5
            y = 10*row + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for column in range(30):
        for row in range(column,30):
            x = -10*row + 595
            y = 10*column + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
def draw_section_7():
    for row in range(30):
        for column in range(row,30):
            x = 10*row + 605
            y = 10*column + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
def draw_section_8():
    for column in range(30):
        for row in range(column,30):
            x = 10*row + 905
            y = -10*column + 595
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
def main():
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    draw_section_outlines()

    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()