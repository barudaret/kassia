#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reportlab.pdfbase import pdfmetrics
from neume import Neume

class AbstractNeume(Neume):
    def __init__(self, char: str, font_family: str, font_size: int, color: str, offset_x: int = 0, offset_y: int = 0):
        self.char: str = char  # The character in a TTF
        if font_family not in pdfmetrics.getRegisteredFontNames():
            raise Exception("Neume font is not registered")
        self.font_family = font_family
        self.font_size = font_size
        self.color = color
        self.offset_x = 0
        self.offset_y = 0
        self.width = pdfmetrics.stringWidth(self.char, self.font_family, self.font_size) # Eventually make these into junk values by that 
        ascent, descent = pdfmetrics.getAscentDescent(self.font_family, self.font_size)  # I mean just set them to zero, else it will set 
        self.height = ascent - descent                                                   # the ength of the abstract identifier (useless)