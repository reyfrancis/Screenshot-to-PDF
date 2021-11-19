import time
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
from fpdf import FPDF
import argparse
import os
from PIL import Image

# path = os.getcwd()
# num_pages = 5
# bookname = 'IRJET-V3I10180.pdf'

path = os.getcwd()
num_pages = 3
bookname = 'FEA'
left = 0
top = 18
right = 1267
bottom = 1009

dpi = 120 # note for calcs below that "pt" units are 1/72th of an inch

def main():
	for pg_num in range(num_pages):
		if pg_num == 0:
				# pdf = FPDF() # set the format for the very first page
				pdf = FPDF(unit="pt", format = [bottom, right] )
				
		pg = Image.open(path + '/page_' + str(pg_num) + '.png', 'r')
		pg_crop = pg.crop((left, top, right+left, bottom+top)).transpose(Image.ROTATE_270).save(path + '/page_crop' + str(pg_num) + '.png')
		# pg_crop1 = pg_crop
		# pdf.add_page() # add a blank page

		# page_size = pg_crop.size[0]/dpi*72, pg_crop.size[1]/dpi*72
		pdf.add_page()
		print('Adding page:' + str(pg_num+1))
		pdf.image(path + '/page_crop' + str(pg_num) + '.png', 0, 0)
	pdf.output(path + '\\' + bookname + '.pdf', 'F')

if __name__ == '__main__':
	main()


