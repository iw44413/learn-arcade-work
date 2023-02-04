import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color((0,255,255))
arcade.start_render()
def draw_tree(x,y):
  arcade.draw_rectangle_filled(x,y,25,100, (115, 83, 42))
  arcade.draw_triangle_filled(x-100,y+60,x+100,y+60,x,y+200, (42, 126, 25))
  arcade.draw_triangle_filled(x-100,y+45,x+100,y+45,x,y+200, (42, 126, 25))
  arcade.draw_triangle_filled(x-100,y+30,x+100,y+30,x,y+200, (42, 126, 25))
  arcade.draw_triangle_filled(x-100,y+15,x+100,y+15,x,y+200, (42, 126, 25))

def on_draw(deltatime):
  arcade.start_render()
  draw_tree(on_draw.tree1_x, 200)
  draw_tree(on_draw.tree2_x, 200)
  draw_tree(500, on_draw.tree3_y)
  draw_tree(500, on_draw.tree4_y)
  draw_tree(on_draw.tree5_x, on_draw.tree5_y)
  draw_tree(on_draw.tree6_x, on_draw.tree6_y)
  draw_tree(on_draw.tree7_x, on_draw.tree7_y)
  draw_tree(on_draw.tree8_x, on_draw.tree8_y)


  on_draw.tree1_x -= 10
  on_draw.tree2_x += 10
  on_draw.tree3_y += 10
  on_draw.tree4_y -= 10
  on_draw.tree5_x += 10
  on_draw.tree5_y += 10
  on_draw.tree6_x -= 10
  on_draw.tree6_y -= 10
  on_draw.tree7_x -= 10
  on_draw.tree7_y += 10
  on_draw.tree8_x += 10
  on_draw.tree8_y -= 10


on_draw.tree1_x=500
on_draw.tree2_x=500
on_draw.tree3_y=200
on_draw.tree4_y=200
on_draw.tree5_x=500
on_draw.tree5_y=200
on_draw.tree6_x=500
on_draw.tree6_y=200
on_draw.tree7_x=500
on_draw.tree7_y=200
on_draw.tree8_x=500
on_draw.tree8_y=200

arcade.schedule(on_draw, 1/60)
arcade.run()