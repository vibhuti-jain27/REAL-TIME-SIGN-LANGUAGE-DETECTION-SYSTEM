import cv2, os, random
import numpy as np

def get_image_size():
    img = cv2.imread('gestures/0/100.jpg', 0)
    #if img is None:
        #print("Error: Unable to read image file at 'gestures/1/100.jpg'")
        #return None
    return img.shape

'''image_size = get_image_size()
if image_size is not None:
    image_x, image_y = image_size
    # continue with the rest of the code
else:
    print("Error: Could not read image file at 'gestures/1/100.jpg'")
    exit()'''

gestures = os.listdir('gestures/')
gestures.sort(key = int)
#gestures = sorted(os.listdir('gestures/1/'), key=lambda x: int(x[:-4]) if x[-4:] == '.jpg' else float('inf'))
begin_index = 0
end_index = 5
image_x, image_y = get_image_size()

'''image = cv2.imread('gestures/1/1.jpg', 0)
image_x_resized, image_y_resized = image.shape
for img_path in gestures:
    img = cv2.imread('gestures/1/' + img_path, 0)
    if img is not None:
        img = cv2.resize(img, (image_x_resized, image_y_resized))'''

if len(gestures)%5 != 0:
	rows = int(len(gestures)/5)+1
else:
	rows = int(len(gestures)/5)

full_img = None
for i in range(rows):
	col_img = None
	for j in range(begin_index, end_index):
		img_path = "gestures/%s/%d.jpg" % (j, random.randint(1, 1200))
		#img_path = "gestures/1/%d.jpg" % (j)
		#img_path = "gestures/%s/%02d.jpg" % (j, j + 1) 
		'''Here, %02d is a format specifier that pads the number with leading zeros 
		   to ensure that it always has two digits.The j + 1 is used to get the next 
		   file name in the sequence (since the original code starts counting from 0).'''
		img = cv2.imread(img_path, 0)
		if np.any(img == None):
			img = np.zeros((image_y, image_x), dtype = np.uint8)
			#print(f"Using blank image for {img_path}")
		#if img is None:
			#print(f"Error: Unable to read image file at {img_path}")
			#continue
		if np.any(col_img == None):
			col_img = img
		else:
			col_img = np.hstack((col_img, img))
		

	begin_index += 5
	end_index += 5
	if np.any(full_img == None):
		full_img = col_img
	else:
		full_img = np.vstack((full_img, col_img))


cv2.imshow("gestures", full_img)
cv2.imwrite('full_img.jpg', full_img)
cv2.waitKey(0)
