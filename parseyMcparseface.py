#!/usr/bin/env python
'''
This parses a picture of a Kenyan ID card, into the text and 
uses the text to verify the ID. 
'''

import argparse
import os
import cv2
import csv


# Identifiers (can't think of the right word)
DOB = "DATE OF BIRTH"
SEX = "SEX"
DIST_O_B = "DISTRICT OF BIRTH"
SERIAL_NUM = "SERIAL NUMBER"
NAMES = "FULL NAMES"
DOI = "DATE OF ISSUE"
POI = "PLACE OF ISSUE"
ID = "ID NUMBER"
DIST = "DISTRICT"
DIV = "DIVISION"
LOC = "LOCATION"
SUB_LOC = "SUB-LOCATION"

# Arguements to be set in what environment the image is parsed.

def constant_list():
    pass

def extract_text():
    pass

def extract_image():
    pass

def extract_information():
    pass