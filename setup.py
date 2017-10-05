# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 15:54:20 2017

@author: y-takeuchi
"""

from cx_Freeze import setup, Executable

exe = Executable(script = 'capture.py',  base = 'Win32Gui')




setup(name = 'AppCapture',
      version = '0.1',
      description = 'Save Screen',
      executables = [exe])