# main.py -- put your code here!
import machine as m
import utime

# Section 2 Intro to MicroPython

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
#         utime.sleep(1) 
        
# Lesson #7 Toggle left and right
# button = m.Pin(14, m.Pin.IN)
# while True:
#     if button.value() == 0:
#         print("The switch works")
#         utime.sleep(0.5) 

# Lesson #8 Press Gently
# button = m.Pin(14, m.Pin.IN)
# while True:
#     if button.value() == 1:
#         print("The switch works")
#         utime.sleep(1) 

# Lesson #9 Feel the Magnetism
# reed = m.Pin(14, m.Pin.IN)
# while True:
#     if reed.value() == 1:
#         print('There are magnets in here')
#         utime.sleep(1)
'''
If you've noticed the pattern, we define the pin
and check if the condition we are waiting for
has been accessed. MicroPython interrupt
request also works in the same way, it allows
certain operations to interrupt the main
program.
'''
# reed_switch = m.Pin(14, m.Pin.IN)
# def detected(pin):
#     print("Magnet!")
# reed_switch.irq(trigger=m.Pin.IRQ_RISING, handler=detected)

# Lesson #10 Detect Human Movement
# infrared_sensor = m.Pin(14, m.Pin.IN)

# def motion_detected(pin):
#     print("Somebody here!")

# infrared_sensor.irq(trigger=m.Pin.IRQ_RISING, handler=motion_detected)

### For continuous signal sent following movement
# infrared_sensor = m.Pin(14, m.Pin.IN)

# global timer_delay
# timer_delay = utime.ticks_ms()
# print("start")

# def pir_in_high_level(pin):
#     global timer_delay
#     infrared_sensor.irq(trigger=m.Pin.IRQ_FALLING, handler=pir_in_low_level)
#     intervals = utime.ticks_diff(utime.ticks_ms(), timer_delay)
#     timer_delay = utime.ticks_ms()
#     print("the dormancy duration is " + str(intervals) + "ms")

# def pir_in_low_level(pin):
#     global timer_delay
#     infrared_sensor.irq(trigger=m.Pin.IRQ_RISING, handler=pir_in_high_level)
#     intervals2 = utime.ticks_diff(utime.ticks_ms(), timer_delay)
#     timer_delay = utime.ticks_ms()
#     print("the duration of work is " + str(intervals2) + "ms")

# infrared_sensor.irq(trigger=m.Pin.IRQ_RISING, handler=pir_in_high_level)
# ## CHECK NOTES ^^^^^^

# Lesson #11 Turn the Knob
# potentiometer = m.ADC(28)
# led = m.PWM(m.Pin(15))
# led.freq(1000)

# while True:
#     value=potentiometer.read_u16()
#     print(value)
#     led.duty_u16(value)
#     utime.sleep_ms(200)
    
# Lesson #12 Feel the Light (See Notes)
# photoresisteor = m.ADC(28)
# while True:
#     light_value = photoresisteor.read_u16()
#     print(light_value)
#     utime.sleep(10)

# Lesson #13 Thermometer (See Notes)
# import math
# thermistor = m.ADC(28)

# while True:
#     temp_val = thermistor.read_u16()
#     Vr = 3.3 * float(temp_val) / 65535
#     Rt = 10000 * Vr / (3.3 - Vr)
#     temp = 1/(((math.log(Rt/10000)) / 3950) + (1 / (273.15+25)))
#     Cel = temp - 273.15
#     Fah = Cel * 1.8 + 32
#     print(f'Celsius {Cel} Fahrenheit {Fah}')
#     utime.sleep_ms(200)

# Lesson #14 Feel the Water Level (See Notes)
# sensor = m.ADC(28)

# while True:
#     value=sensor.read_u16()
#     print(value)
#     utime.sleep_ms(200)

# There is a way to use the analog input 
# module as a digital module.
# First, take a reading of the Water Sensor
# in a dry environment first, record it, 
# and use it as a threshold value. 
# Then, complete the programming and re-read 
# the reading of the water sensor. When 
# the reading of the water sensor deviates 
# significantly from the reading in a dry 
# environment, it is exposed to liquid. 
# In other words, by placing this device 
# near a water pipe, it can detect if a water
# pipe is leaking.

# sensor = m.ADC(28)
# threshold = 30000 #This value needs to be modified with the environment.

# while True:
#     value=sensor.read_u16()
#     if value > threshold :
#         print("Liquid leakage!")
#     utime.sleep_ms(200)

# # Lesson #15 Two Kinds of Transistors
# btn = m.Pin(15, m.Pin.IN)
# signal = m.Pin(15, m.Pin.OUT)

# while True:
#     btn_status = btn.value()
#     if btn_status == 1:
#         signal.value(1)
#     elif btn_status == 0:
#         signal.value(0)

# Lesson#16 Control Another Circuit
# relay = m.Pin(15, m.Pin.OUT)
# while True:
#     relay.value(1)
#     utime.sleep(2)
#     relay.value(0)
#     utime.sleep(2)