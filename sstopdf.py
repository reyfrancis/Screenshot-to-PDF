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
num_pages = 305
bookname = '22658_PMT1841-ENG-857.pdc'
# bookname = 'FEA.pdf'

# def crop_image():

# 	for pg_num in range(num_pages):
# 		im = Image.open(path + '/page_' + str(pg_num) + '.png')
# 		im_crop = im.crop((left, top, right, bottom))
# 		plt.imsave( path + '/page_' + str(pg_num) + '.png', page)

# Size of the image in pixels (size of original image)
# (This is not mandatory)
# width, height = im.size
 
# Setting the points for cropped image
left = 0
top = 7
right = 1267
bottom = 1009
 
def open_book():
	os.startfile(bookname)


def get_page():
	return np.array(pyautogui.screenshot(region=(370,30, 1620, 1010)))

def flip_page():
	pyautogui.press('pgdn')


def main():	
	pdf = None
	open_book()
	time.sleep(10)
	# pyautogui.click(1050,100) # Full screen
	# time.sleep(5)
	# pyautogui.hotkey('ctrl', 'shift', 'subtract') # Rotate Counterclockwise

	for pg_num in range(num_pages):
		print('On page', str(pg_num + 1))
		page = get_page()
		plt.imsave( path + '/page_' + str(pg_num) + '.png', page)
		if pg_num == 0:
			height, width, _ = page.shape
			pdf = FPDF(unit = "pt", format = [width, height])
		pdf.add_page()
		time.sleep(0.1)
		pdf.image( path + '/page_' + str(pg_num) + '.png', 0, 0)
		flip_page()
		time.sleep(1)

	pdf.output(path +'\\' + bookname + '_copy.pdf', 'F')

if __name__ == '__main__':
	main()
