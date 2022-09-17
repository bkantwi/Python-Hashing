#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:45:42 2022

@author: kowalski
"""
from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen=Tk()
    screen.geometry("375x398")

    #icon
    image_icon=PhotoImage(file="keys.png")
    screen.iconphoto(False,image_icon)

    screen.title("Bkantwi Hashing")

    screen.mainloop()
    
main_screen()
