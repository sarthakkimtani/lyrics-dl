import os
import sys
import time 

try:
	import pyfiglet
	import lyricsgenius as genius
	import colorama
except:
	print("ERROR! Modules not installed. Install it using 'pip install -r requirements.txt'")
	sys.exit()

colorama.init()

banner = pyfiglet.figlet_format("lyrics-dl")

print(colorama.Fore.GREEN+banner)

api = genius.Genius('zGLiwaynPFQQAQcZ8js4y0RFB3r-6RK2mMApxBK-hK63GPa1HNaXnyJt9nCdHlRM')

def get_lyrics(track,artist):
	song = api.search_song(track,artist)

	if song == None:
		print(colorama.Fore.RED+'ERROR! could not find requested song')
		sys.exit()
	else:
		if "Lyrics" in os.listdir():
			os.chdir('Lyrics')
			file = open("{}.lrc".format(track),"a")
			print(colorama.Fore.GREEN+'Creating Lyrics File...')
		else:
			os.mkdir("Lyrics")
			os.chdir('Lyrics')
			file = open("{}.lrc".format(track),"a")
			print(colorama.Fore.GREEN+'Creating Lyrics File...')
		
		try:
			file.write(song.lyrics)
		except:
			print(colorama.Fore.RED+"ERROR! could not create lyrics file")
			sys.exit()
		path = os.getcwd()
		print("Lyrics File saved in "+path)
		file.close()

time.sleep(1)

song = input(colorama.Fore.GREEN+" Name of the song: ")
artist = input(colorama.Fore.GREEN+" Name of thr artist: ")

get_lyrics(song,artist)