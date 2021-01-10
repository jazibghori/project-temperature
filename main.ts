input.onButtonPressed(Button.A, function () {
    basic.showString("" + (min))
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (max))
    basic.clearScreen()
})
let min = 0
let max = 0
let current = input.temperature()
max = current
min = current
basic.forever(function () {
    basic.showString(".")
    current = input.temperature()
    if (current < min) {
        min = current
    }
    if (current > max) {
        max = current
    }
    basic.pause(1000)
    basic.clearScreen()
    basic.pause(1000)
})
