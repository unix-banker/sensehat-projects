from sense_hat import SenseHat

sense = SenseHat()


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    if x == 1:
        r = 100
        g = 0
        b = 0
        sense.clear((r, g, b))
        
    if x == -1:
        r = 0
        g = 100
        b = 0
        sense.clear((r, g, b))
        
    if y == 1:
        r = 0
        g = 0
        b = 100
        sense.clear((r, g, b))
        
    if y == -1:
        r = 100
        g = 0
        b = 100
        sense.clear((r, g, b))

    print("x={0}, y={1}, z={2}".format(x, y, z))
