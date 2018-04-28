#!/usr/bin/python

import os



fle=os.popen("/usr/bin/gsettings get org.gnome.desktop.background picture-uri").read()
fle=fle.replace("\n", " ")
fstored_album = open(os.getenv('HOME') + '/conky-clock/stored_color.txt', 'r')
stored_album = fstored_album.readlines()
fstored_album.close()

if (fle).strip('\n') != stored_album[0].strip('\n'):
	size=os.popen(("identify "+fle)).read().split(" ")[2].split("x")
	wall_height=(int(size[1])/1080)*350
	wall_width=(int(size[0])/1920)*400
	avgColor=os.popen("convert "+fle+" -crop " + str(wall_width) + "x"+ str(wall_height) +"+"+str((int(size[0]))-wall_width)+"+"+str(int(size[1])-wall_height)+" -scale 1x1\\! txt:-").read()[1:].split("(")[2][:-2].split(",")
	if (float(avgColor[0])*0.299 + float(avgColor[1])*0.587 + float(avgColor[2])*0.114) > 186:
		colora=str(1)
	else:
		colora=str(0)
	# 380*150
	os.system("echo \"" + colora + "\" > $HOME/conky-clock/stored_color.txt")
	#1475
else:
	colora=str(stored_album[1]).strip("\n")

print("${color"+colora+"}")
