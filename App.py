from PIL import Image
import os, os.path
import sys

fileObject = open("browse.txt", "r")
data = fileObject.read()

browse_files = data

if browse_files == "True":
	import wx

	def get_path(wildcard):
	    app = wx.App(None)
	    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
	    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
	    if dialog.ShowModal() == wx.ID_OK:
	        path = dialog.GetPath()
	    else:
	        path = None
	    dialog.Destroy()
	    return path

	path_to_image = get_path('*')

elif browse_files == "False":
	path_to_image = input('Your Image Path: ')

work = True

while work:
	#get image
	image = Image.open(path_to_image)

	#get line
	print("Lets Choose Your Line\n | 1 - Horizontal | 2 - Vertical | 3 - Squares | 4 - Circles | 5 - Grid  |")
	line = input('Just Write Number: ')

	watermark = Image.open("lines/" + line + ".png")

	if line == "5":

		width, height = image.size

		size = width, height

		resized_line = watermark.resize(size)

		resized_line.save('lines/resized.png')

		image.paste(resized_line, resized_line)

		os.remove('lines/resized.png')

	else:

		image.paste(watermark, watermark)

	DIR = 'Saves'

	folder_files_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

	file = open("txt.txt","w+")

	file.write(str(folder_files_count))

	file.close()

	fileObject = open("txt.txt", "r")
	data = fileObject.read()

	act = int(data) + 1

	fileObject.close()

	os.remove("txt.txt")

	f = open("txt.txt","w+")

	f.write(str(act))

	f.close()

	saved = "Saves/Compiled(" + str(act) + ").png"
	image.save(saved)
	image.show()

	work = False