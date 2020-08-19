basic.show_icon(IconNames.SMALL_HEART)
basic.pause(100)
basic.show_icon(IconNames.HEART)

def on_forever():
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(1000)
    pins.servo_write_pin(AnalogPin.P0, 0)
basic.forever(on_forever)
