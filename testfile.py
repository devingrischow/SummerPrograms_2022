# import required module
import glob

# get the path/directory
folder_dir = 'Gfg images'

# iterate over files in
# that directory
for images in glob.iglob(f'{folder_dir}/*'):

	# check if the image ends with png
	if (images.endswith(".png")):
		print(images)
