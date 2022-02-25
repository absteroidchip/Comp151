# ARamerProject2
import arcade
import random

def main():
    our_colors = [arcade.color.LAVENDER, arcade.color.BLUE, arcade.color.GREEN, arcade.color.BOSTON_UNIVERSITY_RED,
                  arcade.color.ORANGE, arcade.color.ALIZARIN_CRIMSON, arcade.color.ARSENIC,
                  arcade.color.ATOMIC_TANGERINE, arcade.color.AMETHYST, arcade.color.ARTICHOKE,
                  arcade.color.YELLOW, arcade.color.AMARANTH_PINK, arcade.color.AUROMETALSAURUS]
    which_file = input("Which File Would You Like To Open?")
    user_file= open(which_file, 'r')
    all_lines = user_file.readlines()
    arcade.open_window(800, 800, "project 2")
    arcade.set_background_color(arcade.color.AZURE_MIST)
    arcade.start_render()
    title_data = all_lines[0]
    x_axis_title = all_lines[1]
    y_axis_title = all_lines[2]
    arcade.draw_text(title_data, 225, 700, arcade.color.BLACK_LEATHER_JACKET, 25)
    arcade.draw_text(y_axis_title, 100, 350, arcade.color.BLACK_LEATHER_JACKET, 25, rotation= 90)
    arcade.draw_text(x_axis_title, 250, 50, arcade.color.BLACK_LEATHER_JACKET, 25)
    rest_of_the_lines = all_lines[3:]
    x_loc = 400
    y_loc = 150
    age_x_loc = 150
    age_y_loc = 150
    for line in rest_of_the_lines:
        split_line = line.split(':')
        size = int(split_line[1])
        age_range_title = split_line[0]
        arcade.draw_text(age_range_title, age_x_loc, age_y_loc, arcade.color.BLACK_LEATHER_JACKET, 15)
        this_color = random.choice(our_colors)
        our_colors.remove(this_color)
        rectangle = arcade.create_rectangle(x_loc, y_loc, size*6, 55, this_color)
        rectangle.draw()
        y_loc = y_loc + 55
        age_y_loc = age_y_loc +55


    arcade.finish_render()
    arcade.run()

main()
