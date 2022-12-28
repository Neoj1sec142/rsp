# main.py -- put your code here!
import machine as m
import utime

# Lesson #1 blinking light
# led = machine.Pin(15, machine.Pin.OUT)
# while True:
#     led.value(1)
#     utime.sleep(1)
#     led.value(0)
#     utime.sleep(1)

# Lesson #2 scrolling led 10 light bar
# pin = [6,7,8,9,10,11,12,13,14,15]
# led = []
# for i in range(10):
#     led.append(None)
#     led[i] = machine.Pin(pin[i], machine.Pin.OUT)
    
# while True:
#     for i in range(10):
#         led[i].toggle()
#         utime.sleep(0.2)

# Lesson #3 Faading LED power frequency
# l = machine.PWM(machine.Pin(15))
# l.freq(1000)

# for brightness in range(0,65535,50):
#     l.duty_u16(brightness)
#     utime.sleep_ms(10)
# l.duty_u16(0)

# Lesson #4 Colorful Light
# red = m.PWM(m.Pin(13))
# green = m.PWM(m.Pin(14))
# blue = m.PWM(m.Pin(15))
# red.freq(1000)
# green.freq(1000)
# blue.freq(1000)

# def interval_mapping(x, in_min, in_max, out_min, out_max):
#     return (x - in_min) * (out_max - out_min)/(in_max - in_min) + out_min

# def color_to_duty(rgb_value):
#     rbg_value = int(interval_mapping(rgb_value,0,255,0,65535))
#     return rgb_value

# def color_set(red_value, green_value, blue_value):
#     red.duty_u16(color_to_duty(red_value))
#     green.duty_u16(color_to_duty(green_value))
#     blue.duty_u16(color_to_duty(blue_value))
    
# color_set(255,255,255)

# Lesson #5 Reading Button Value
# button = m.Pin(14, m.Pin.IN)
# while True:
#     if button.value() == 1:
#         print("You Pressed the button")
#         utime.sleep(1)

# Lesson #6 Tilt It！
# button = m.Pin(14, m.Pin.IN)
# while True:
#     if button.value() == 0:
#         print("The switch works")
#         utime.sleep(0.5) 
        
# Lesson #7 Toggle left and right
# button = m.Pin(14, m.Pin.IN)
# while True:
#     if button.value() == 0:
#         print("The switch works")
#         utime.sleep(0.5) 
