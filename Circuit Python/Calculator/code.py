from lcd_lib import *
from time import sleep
from adafruit_matrixkeypad import *
from digitalio import DigitalInOut
import board
lcd.send('loadingO_O')
counter23 = 0
while counter23 < 5:
    lcd.curser.blink('off')
    
    sleep(0.5)
    lcd.curser.curser('left')
    lcd.send('-')
    sleep(0.5)
    lcd.curser.curser('left')
    lcd.send('O')
    counter23 = counter23 + 1
lcd.clear()

def calculate(express):
    try:
        answer = eval(express)
        return answer
    except Exception as oops:
        lcd.send(str(oops))



# Classic 4x4 matrix keypad
cols = [DigitalInOut(x) for x in (board.GP20, board.GP21, board.GP22, board.GP26)]
rows = [DigitalInOut(x) for x in (board.GP16, board.GP17, board.GP18, board.GP19)]
keys = ((1, 2, 3, '+'),
        (4, 5, 6, '-'),
        (7, 8, 9, '*'),
        ('c', 0, '=', '/'))

keypad = Matrix_Keypad(rows, cols, keys)
op = ['+','-','*','/','=','c']
op2 = ['=','c']


st = ''
st2 = ''
field = ''

while True:
    
    keys = keypad.pressed_keys
    if keys:
        st = (str(keys))
        print(st)
        st2 = st.strip(']').strip('[').strip("'")
        print(type(st2), st2)

        if st2 == 'c':
            lcd.clear()
            st = ''
            st2 = ''
            field = ''
        elif st2 == '=':
            st = ''
            st2 = ''
            calculate(field)
            field = ''
        else:
            field = field + st2
            st = ''
            st2 = ''
        
    sleep(0.3)
