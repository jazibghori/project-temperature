def on_button_pressed_a():
    basic.show_string("" + str((min2)))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("" + str((max2)))
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

min2 = 0
max2 = 0
current = input.temperature()
max2 = current
min2 = current

def on_forever():
    global current, min2, max2
    basic.show_string(".")
    current = input.temperature()
    if current < min2:
        min2 = current
        if current > max2:
            max2 = current
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)
