# Abigail Ramer
import arcade


def main():
    arcade.open_window(800, 600, "picture window")
    arcade.set_background_color(arcade.color.ALICE_BLUE)
    # These are all my shapes below
    left_heart = arcade.create_ellipse(300, 400, 190, 200, arcade.color.BABY_PINK)
    right_heart = arcade.create_ellipse(450, 400, 190, 200, arcade.color.BABY_PINK)
    heart_point = arcade.create_polygon([(220, 345), (530, 345), (375, 175)], arcade.color.BABY_PINK)
    heart_point_left_outline = arcade.create_line(220, 345, 375, 175, arcade.color.ALABAMA_CRIMSON)
    heart_point_right_outline = arcade.create_line(530, 345, 375, 175, arcade.color.ALABAMA_CRIMSON)
    left_heart_outline = arcade.create_ellipse_outline(300, 400, 190, 200, arcade.color.ALABAMA_CRIMSON)
    right_heart_outline = arcade.create_ellipse_outline(450, 400, 190, 200, arcade.color.ALABAMA_CRIMSON)
    # happy_text = arcade.create_text(270, 375, "HAPPY")
    # now I'm running the program below
    arcade.start_render()
    heart_point_left_outline.draw()
    heart_point_right_outline.draw()
    left_heart_outline.draw()
    right_heart_outline.draw()
    left_heart.draw()
    right_heart.draw()
    heart_point.draw()
    # happy_text.draw()
    arcade.finish_render()
    arcade.run()


main()
