#required libraries
from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import numpy as np
import cv2

st.set_page_config(
    page_title='Image Tools',
    page_icon='🔍')
tab1, tab2 = st.tabs([
   "Segmentation",
   "Quote"
])
with tab1:
	st.header("Image Segmentation With Kmeans", divider='rainbow')
	uploaded_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])
            
	if uploaded_file is not None:
		file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
		image = cv2.imdecode(file_bytes, 1)
	#image = cv2.imread(image)
	k = int(st.text_input('Type a number',0))
	st.write('The current number is', k)

	#reading image
	if st.button('Get Photo'):
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		pixel_vals = image.reshape((-1,3))
		pixel_vals = np.float32(pixel_vals)

#
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

#performing Kmeans
		retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

		centers = np.uint8(centers)
		segmented_data = centers[labels.flatten()]


		segmented_image = segmented_data.reshape((image.shape))
	
	#Performing branding

	

		st.image(segmented_image)
with tab2:
	st.header("Instagram Quote Creator", divider='rainbow')
	#quote = st.text_input("Enter the Quote:")
	quote = st.text_area("Enter the Quote:")

# Create a new image with white background
	image = Image.open("./image_segmentation/quote.jpg")
	width, height = image.width, image.height
# Create a drawing object
	draw = ImageDraw.Draw(image)

# Define the text to be written
	text = str(quote)
	size = st.text_input("Enter the font size")
	wp =st.text_input("Enter the width Percent", key =height)
	hp =st.text_input("Enter the height Percent") 
	if st.button('generate'):
		size = int(size)
		wp = int(wp)
		hp = int(hp)
		font = ImageFont.truetype('/home/shiva/Downloads/Nova_Square/NovaSquare-Regular.ttf',size)
		x = width - ((width * wp)/100)
		y = height- ((height * hp)/100)
		draw.text((x, y), text, font=font, fill ="black", align ="center")
		st.image(image)

# font
#	size = int(st.number_input("Enter the font size"))
#	font = ImageFont.truetype('./image_segmentation/NovaSquare-Regular.ttf', size)

# Calculate the position to center the text
#text_width, text_height = draw.textlength(text, font)
#	wp =int( st.text_input("Enter the width Percent", key =height))
#hlkafaosifj
#	hp =int( st.text_input("Enter the height Percent"))
#	x = width - ((width * wp)/100)
#x = width //3
#y = height // 2
#	y = height- ((height * hp)/100)
# Write the text on the image
#	draw.text((x, y), text, font=font, fill ="black", align ="center")

# Save the image
#image.save("/home/shiva/Downloads/output.jpg")
#	st.image(image)

