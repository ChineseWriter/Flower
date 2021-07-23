#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Turtle.py
# @Time      :2021/6/24 19:42
# @Author    :Amundsen Severus Rubeus Bjaaland

from turtle import *
import random


def drawTree(length):
    if length > 1:
        if 30 > length > 14:
            pensize(4)
        elif 15 > length > 5:
            color('#04B486')
            pensize(3)
        elif 5 > length > 1:
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')
            pensize(5)
        RandomAngle = 2 * random.random()
        RandomLength = 2 * random.random()
        fd(length)
        right(20 * RandomAngle)
        drawTree(length - 10 * RandomLength)
        left(40 * RandomAngle)
        drawTree(length - 10 * RandomLength)
        right(20 * RandomAngle)
        up()
        backward(length)
        down()


def fallingFlowers(m):
    x, y = -1000, -750
    for i in range(30):
        up()
        goto(x, y)
        x += 100
        down()
        yval = 50
        for i in range(m):
            a = 100 * random.random()
            b = 2 * random.random()
            print(a)
            if a > 59:
                color('#FE2E9A')
            else:
                color('#04B486')
            circle(5)
            up()
            goto(x, y + (yval * b))
            fd(a)
            yval += 50
            down()


def main():
    setworldcoordinates(-1000, -750, 1000, 750)
    tracer(200, 1)
    fallingFlowers(10)
    bgcolor("#F5F6CE")
    color('#5E5E5E')
    pensize(5)
    up()
    goto(0, -700)
    down()
    left(80)
    fd(140)
    drawTree(120)
    input()
