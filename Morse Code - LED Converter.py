from machine import Pin
import time
position = 0

led = Pin(15, Pin.OUT)

def dot():
    led.value(1)
    time.sleep(0.25)
    led.value(0)
    time.sleep(0.25)

def dash():
    led.value(1)
    time.sleep(0.75) 
    led.value(0)
    time.sleep(0.25)

def letterspace():
    led.value(0)
    time.sleep(0.75)

def space():
    led.value(0)
    time.sleep(1)

def a():
    dot()
    dash()
    letterspace()
def b():
    dash()
    dot()
    dot()
    dot()
    letterspace()
def c():
    dash()
    dot()
    dash()
    dot()
    letterspace()
def d():
    dash()
    dot()
    dot()
    letterspace()
def e():
    dot()
    letterspace()
def f():
    dot()
    dot()
    dash()
    dot()
    letterspace()
def g():
    dash()
    dash()
    dot()
    letterspace()
def h():
    dot()
    dot()
    dot()
    dot()
    letterspace()
def i():
    dot()
    dot()
    letterspace()
def j():
    dot()
    dash()
    dash()
    letterspace()
def k():
    dash()
    dot()
    dash()
    letterspace()
def l():
    dot()
    dash()
    dot()
    dot()
    letterspace()
def m():
    dash()
    dash()
    letterspace()
def n():
    dash()
    dot()
    letterspace()
def o():
    dash()
    dash()
    dash()
    letterspace()
def p():
    dot()
    dash()
    dash()
    dot()
    letterspace()
def q():
    dash()
    dash()
    dot()
    dash()
    letterspace()
def r():
    dot()
    dash()
    dot()
    letterspace()
def s():
    dot()
    dot()
    dot()
    letterspace()
def t():
    dash()
    letterspace()
def u():
    dot()
    dot()
    dash()
    letterspace()
def v():
    dot()
    dot()
    dot()
    dash()
    letterspace()
def w():
    dot()
    dash()
    dash()
    letterspace()
def x():
    dash()
    dot()
    dot()
    dash()
    letterspace()
def y():
    dash()
    dot()
    dash()
    dash()
    letterspace()
def z():
    dash()
    dash()
    dot()
    dot()
    letterspace()

def one():
    dot()
    dash()
    dash()
    dash()
    dash()
    letterspace()
def two():
    dot()
    dot()
    dash()
    dash()
    dash()
    letterspace()
def three():
    dot()
    dot()
    dot()
    dash()
    dash()
    letterspace()
def four():
    dot()
    dot()
    dot()
    dot()
    dash()
    letterspace()
def five():
    dot()
    dot()
    dot()
    dot()
    dot()
    letterspace()
def six():
    dash()
    dot()
    dot()
    dot()
    dot()
    letterspace()
def seven():
    dash()
    dash()
    dot()
    dot()
    dot()
    letterspace()
def eight():
    dash()
    dash()
    dash()
    dot()
    dot()
    letterspace()
def nine():
    dash()
    dash()
    dash()
    dash()
    dot()
    letterspace()
def zero():
    dash()
    dash()
    dash()
    dash()
    dash()

while True:
    position = 0
    statement = input("What would you like to say?").lower()
    statement_length = len(statement)
    while statement_length > 0:
        if statement[position] == " ":
            space()
        if statement[position] == "a":
            a()
        if statement[position] == "b":
            b()
        if statement[position] == "c":
            c()
        if statement[position] == "d":
            d()
        if statement[position] == "e":
            e()
        if statement[position] == "f":
            f()
        if statement[position] == "g":
            g()
        if statement[position] == "h":
            h()
        if statement[position] == "i":
            i()
        if statement[position] == "j":
            j()
        if statement[position] == "k":
            k()
        if statement[position] == "l":
            l()
        if statement[position] == "m":
            m()
        if statement[position] == "n":
            n()
        if statement[position] == "o":
            o()
        if statement[position] == "p":
            p()
        if statement[position] == "q":
            q()
        if statement[position] == "r":
            r()
        if statement[position] == "s":
            s()
        if statement[position] == "t":
            t()
        if statement[position] == "u":
            u()
        if statement[position] == "v":
            v()
        if statement[position] == "w":
            w()
        if statement[position] == "x":
            x()
        if statement[position] == "y":
            y()
        if statement[position] == "z":
            z()
        if statement[position] == "1":
            one()
        if statement[position] == "2":
            two()
        if statement[position] == "3":
            three()
        if statement[position] == "4":
            four()
        if statement[position] == "5":
            five()
        if statement[position] == "6":
            six()
        if statement[position] == "7":
            seven()
        if statement[position] == "8":
            eight()
        if statement[position] == "9":
            nine()
        if statement[position] == "0":
            zero()
        position += 1
        statement_length -= 1