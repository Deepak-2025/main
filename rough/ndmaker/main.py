import sys
from turtle import done
import cv2
import time
from run import process

"""
main.py

 How to run:
 python3 main.py
"""
iimag = cv2.imread('input.png', 1)
(height_dress,width_dress) = iimag.shape[0:2]
#Resize keep ratio
percent = 50
width_k = int(width_dress*percent/100) 
height_k = int(height_dress*percent/100)

# ------------------------------------------------- main()
def main():

	dress = cv2.resize(iimag, (width_k,height_k),cv2.INTER_LINEAR) 

	#Process
	nude = process(dress)

	# Write output image
	cv2.imwrite("output.png", nude)

	#Exit
	sys.exit()

if __name__ == '__main__':
	main()