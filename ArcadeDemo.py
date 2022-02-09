import arcade

def main():
    arcade.open_window(800, 600, "first window ever")
    arcade.start_render
    block = arcade.create_rectangle(200, 200, 100, 200, arcade.color.BULGARIAN_ROSE)
    other_block = arcade.create_rectangle_outline(500, 400, 400, 200, arcade.color.BULGARIAN_ROSE)
    #arcade.create_ellipse()
    #arcade.create_ellipse_outline()
    #arcade.create_line(0,0,7,7,arcade.color.BULGARIAN_ROSE)
    arcade.create_polygon([(0,0),(0,300),(150,450),(300,300),(300,0)],arcade.color.FAWN)
    arcade.draw_text("OREGON", 350, 350, arcade.color.FAWN)

    block.draw()
    other_block.draw()

    arcade.finish_render()
    arcade.run()

main()

