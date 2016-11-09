'''
This is one of my first programs, the initial focus was to create a simple music/video
downloader to satisfy personal needs. While creating it, people started asking
for a coppy so in the en I decided to make it more intuitive through the terminal.

The program lacks speed so for now il'l try to implement some sort of multithreading.
Possible GUI in the future.


Lets see how further we can make this small proyect go. Maybe an OS multi plataform app??


This was mostly the easiest thigs I could pull out. Now the work is to level up the complicity.
'''

from __future__ import unicode_literals
import youtube_dl

music_options = { 'writethumbnail':True,
				'format':'bestaudio/best',
				'extractaudio':True,
				'audioformat':'best',
				'outtmpl': '~/Music/Youtube_dl/%(title)s.%(ext)s',
				'noplaylist':True,
				'nocheckcertificate':True,
				'postprocessors': [{'key': 'FFmpegExtractAudio',			# down here is where the conversion happens,
									'preferredcodec': 'mp3',	# preferred audio format can be changed,
									'preferredquality': '0',},	# the quality has not much difference because
									{'key': 'EmbedThumbnail'}]}	# the audio scrapped is already downgraded by YT
													# did some research... not true HD audio.

# for now resolution is hardcoded to 720p (better for my kind of bandwidth)
video_options = { 'format':'bestvideo[height<=720]+bestaudio/best[height<=720]',
				'outtmpl': '~/Movies/Youtube_dl/%(title)s.%(ext)s',
				'noplaylist':True,
				'nocheckcertificate':True }


print '\n\tYouTube downloader to mp3/mp4'

while True:
	dl =raw_input('Select type of download:.....music [m] / video [v] / quit [q]\n>>> ')


	while dl == 'm':	# music downloader initialization 

		# modify some options to allow playlists and better organization of output
		if (raw_input('\nIs Playlist?.....Yes[y]\n>>> ')) == 'y':
			music_options['outtmpl'] = '~/Music/Youtube_dl/%(uploader)s/%(playlist)s/%(title)s.%(ext)s'
			del music_options['noplaylist']

		# loads multiple links to a list 
		links = raw_input('\nInsert link (separate multiple liks by space)\n>>> ')
		links = links.split(" ")

		print 'Files to download: %d' % len(links)
		count = 1

		# the actual music downloader
		for link in links:
			print '\nDownloading %d/%d' % (count , len(links))	# file counter feedback
			with youtube_dl.YoutubeDL(music_options) as ydl:
				ydl.download([link])
			count += 1

		# for the new wave of links
		iterate = raw_input('\nWant moar?.....NO![n]\n>>> ')
		if iterate == 'n':
			dl = 'q'
			break

	while dl == 'v':	# music downloader initialization 

		# modify some options to allow playlists and better organization of output
		if (raw_input('\nIs Playlist?.....Yes[y]\n>>> ')) == 'y':
			music_options['outtmpl'] = '~/Movies/Youtube_dl/%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'
			del music_options['noplaylist']

		# loads multiple links to a list 
		links = raw_input('\nInsert link (separate multiple liks by space)\n>>> ')
		links = links.split(" ")

		print 'Files to download: %d' % len(links)
		count = 1

		# the actual video downloader
		for link in links:
			print '\nDownloading %d/%d' % (count , len(links))	# file counter feedback
			with youtube_dl.YoutubeDL(video_options) as ydl:
				ydl.download([link])
			count += 1

		# for the new wave of links
		iterate = raw_input('\nWant moar? NO![n]\n>>> ')
		if iterate == 'n':
			dl = 'q'
			break

	if dl == 'q':
		break

