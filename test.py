#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# created 02.02.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------


from time import sleep

from SM_28BYJ48 import SM28BYJ48

__author__ = "Thomas Kaulke"
__email__ = "kaulketh@gmail.com"

if __name__ == '__main__':
    motor = SM28BYJ48(6, 13, 19, 26)
    # motor.step(-512)
    # sleep(3)
    # motor.step(512)
    # sleep(3)
    #
    motor.rotate(360)
    sleep(3)
    motor.rotate(-360)
    sleep(3)
    motor.rotate(720)
    # while True:
    #
    #     for _ in range(0, 4):
    #         motor.rotate(-90)
    #         sleep(3)
    #     for _ in range(0, 8):
    #         motor.rotate(45)
    #         sleep(3)
