# import required module
from pathlib import Path

# get the path/directory
folder_dir = 'D:\Summer_Programs_2021\Computerized_Vision_automation_tests\Bots\Terraria\Zombie_Sprites_folder'

# iterate over files in
# that directory
images = Path(folder_dir).glob('*.png')
for image in images:
	print(image)
