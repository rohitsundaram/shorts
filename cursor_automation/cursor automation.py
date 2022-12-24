
import time

from pynput.mouse import Button, Controller

mouse = Controller()

print('The current pointer position is {0}'.format(
    mouse.position))

mouse.position = (1000, 700)
print('Now we have moved it to {0}'.format(
    mouse.position))
mouse.scroll(10,-2)
time.sleep(5)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)
mouse.scroll(10,-15)

mouse.position = (1000, 1000)
print('Now we have moved it to {0}'.format(
    mouse.position))
time.sleep(5)
mouse.move(850, 25)
mouse.press(Button.left)
mouse.release(Button.left)