'''
This is one of my first programs, the initial focus was to create a simple music/video
downloader to satisfy personal needs. While creating it, people started asking
for a copy so in the en I decided to make it more intuitive through the terminal.

The program lacks speed so for now I'll try to implement some sort of multi threading.
Possible GUI in the future.

Lets see how further we can make this small project go. Maybe an OS multi platform app??

This was mostly the easiest things I could pull out. Now the work is to level up the complexity.
'''

######################
from __future__ import unicode_literals
import youtube_dl
######################

#/////////////////////////////////////////////#
music_options_ = {
		'writethumbnail':True,
		'format':'bestaudio/best',
		'extractaudio':True,
		'audioformat':'best',
		'outtmpl': '~/Music/Youtube_dl/%(title)s.%(ext)s',
		'noplaylist':True,
		'externaldownloader':'aria2c',						# fast downloader
		'externaldownloaderargs':'-x 4 -k 1M',				# number of threads for each download and split size
		'nocheckcertificate':True,
		'postprocessors': [ {'key': 'FFmpegExtractAudio',	# down here is where the conversion happens,
							'preferredcodec': 'm4a',		# preferred audio format can be changed,
							'preferredquality': '0',},		# set to convert to best, default with ffmpeg seems like 185kbps
							{'key': 'EmbedThumbnail'}]}		
#/////////////////////////////////////////////#
video_options_ = {
		'format':'best[height<=720]',						# change high for better resolution
		'outtmpl': '~/Movies/Youtube_dl/%(title)s.%(ext)s',	# download path
		'noplaylist':True,
		'externaldownloader':'aria2c',						# fast downloader
		'externaldownloaderargs':'-x 4 -k 20M',				# number of threads for each download and split size
		'nocheckcertificate':True }
#/////////////////////////////////////////////#
def close_scritpt_():
	if raw_input('\nWant more?.....NO![n]\n>>> ') == 'n':
		return True
#/////////////////////////////////////////////#
def download_links_(options):
	# loads multiple links to a list 
	links = raw_input('\nInsert link (separate multiple links by space)\n>>> ').split(" ")
	print 'Links to download: %d' % len(links)
	count = 1
	# the actual music downloader
	for link in links:
		print '\nDownloading link %d/%d' % (count , len(links))	# links counter feedback
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([link])
		count += 1
#/////////////////////////////////////////////#
def main():
	dl_type =raw_input('Select type of download:.... music [m] / video [v] / quit [q]\n>>> ')
	#////////////////////#
	while dl_type == 'm':	# music downloader initialization 
		music_options = music_options_.copy()
		# modify some options to allow playlists and better organization of output
		if (raw_input('\nIs Playlist?.....Yes[y]\n>>> ')) == 'y':
			del music_options['noplaylist']
			music_options['outtmpl'] = '~/Music/Youtube_dl/%(uploader)s/%(playlist)s/%(title)s.%(ext)s'
			
		
		download_links_(music_options)
		# for the new wave of links
		if close_scritpt_():
			dl_type = 'q'
			break
	#////////////////////#
	while dl == 'v':	# video downloader initialization 
		video_options = video_options_.copy()
		# modify some options to allow playlists and better organization of output
		if (raw_input('\nIs Playlist?.....Yes[y]\n>>> ')) == 'y':
			del music_options['noplaylist']

			if (raw_input('\nSave Playlist Index?.....Yes[y]\n>>> ')) == 'y':
				music_options['outtmpl'] = '~/Movies/Youtube_dl/%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'

			else:
				music_options['outtmpl'] = '~/Movies/Youtube_dl/%(uploader)s/%(playlist)s/%(title)s.%(ext)s'

		download_links_(video_options)
		# for the new wave of links
		if close_scritpt_():
			dl_type = 'q'
			break
	#////////////////////#
	return dl

######################
print '\n\tYouTube downloader to m4a/mp4'
while __name__ == '__main__':
	while main() != 'q':
		pass
	break
