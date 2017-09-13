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
MUSIC_OPTIONS_ = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'best',
    'outtmpl': '~/Music/Youtube_dl/%(title)s.%(ext)s',
    'noplaylist': True,
    'externaldownloader': 'aria2c',				# fast downloader
    'externaldownloaderargs': '-x 4 -k 2M',			# number of threads for each download and split size
    'nocheckcertificate': True,
    'postprocessors': [{'key': 'FFmpegExtractAudio',		# down here is where the conversion happens,
                        'preferredcodec': 'm4a',		# preferred audio format can be changed,
                        'preferredquality': '0', },		# set to convert to best,
                       {'key': 'EmbedThumbnail'}]}		# default with ffmpeg seems like 185kbps
#/////////////////////////////////////////////#
VIDEO_OPTIONS_ = {
    'format': 'best[height<=360]',						# change high for better resolution
    'outtmpl': '~/Movies/Youtube_dl/%(uploader)s/%(title)s.%(ext)s',		# download path
    'noplaylist': True,
    'externaldownloader': 'aria2c',						# fast downloader
    # number of threads for each download and split size
    'externaldownloaderargs': '-x 4 -k 20M',
    'nocheckcertificate': True}
#/////////////////////////////////////////////#


def check_input_(user_input):
    """
    Checks if arg in input options
    """

    input_options = {
        'Yes': 'y', #not implemented
        'No': 'n',  #not implemented
        'Music': 'm',
        'Video': 'v',
        'Quit': 'q'
    }
    valid = None

    for arg in user_input:
        if arg == '' or not arg in input_options.values():
            print "\tInput not corresponding to specific format"
            valid = False
            break
        else:
            valid = True

    return valid
#/////////////////////////////////////////////#


def close_scritpt_():
    """
    Check user input to close action

    "Want more?"

    - Yes > Loop
    - No > Close

    """
    i = True
    if raw_input('\nWant more?.....Yes![y]\n>>> ') == 'y':
        i = False

    return i
#/////////////////////////////////////////////#


def download_links_(options):
    """
    Asks user to input links
    \nDownloads the links with the given [args]
    """

    # loads multiple links to a list
    links = raw_input(
        '\nInsert link (separate multiple links by space)\n>>> ').split(" ")

    print 'Links to download: %d' % len(links)

    # the actual music downloader
    while len(links) != 0:
        # links counter feedback
        link = links.pop(0)
        print '\nRemaining links %d' % (len(links))
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([link])
        except:
            links.append(link)
            print "Error: link will retry after this batch"
#/////////////////////////////////////////////#


def music_download_():
    """
    Creates and modifies [download options]
        - Playlist
    \n Calls download function with [download options]
    """

    music_options = MUSIC_OPTIONS_.copy()

    # modify some options to allow playlists and better organization of output
    if (raw_input('\nIs Playlist?.....Yes[y]\n>>> ')) == 'y':
        print 'Download option set to download playlists...'
        del music_options['noplaylist']
        music_options['outtmpl'] = '~/Music/Youtube_dl/%(uploader)s/%(playlist)s/%(title)s.%(ext)s'

    #////////////////////#
    download_links_(music_options)
    #////////////////////#
    return close_scritpt_()
#/////////////////////////////////////////////#


def video_download_():
    """
    Creates and modifies [download options]
        - Playlist
        - Output path
    \nCalls download function with [download options]
    """

    video_options = VIDEO_OPTIONS_.copy()

    # modify some options to allow playlists and better organization of output
    if (raw_input('\nIs Playlist?.....Yes[y]\n>>> ')) == 'y':
        print 'Download option set to download Playlists...'
        del video_options['noplaylist']

        if (raw_input('\nSave Playlist Index?.....Yes[y]\n>>> ')) == 'y':
            print 'Saving Playlist index...'
            video_options['outtmpl'] = '~/Movies/Youtube_dl/%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'

        else:
            video_options['outtmpl'] = '~/Movies/Youtube_dl/%(uploader)s/%(playlist)s/%(title)s.%(ext)s'

    #////////////////////#
    download_links_(video_options)
    #////////////////////#
    return close_scritpt_()
#/////////////////////////////////////////////#


def main():
    """
    Main instance
    """
    dl_type = raw_input(
        'Select type of download:.... music [m] / video [v] / quit [q]\n>>> ')
    if check_input_(dl_type):

        #////////////////////#
        while dl_type == 'm':
            # run music_download_ then check for re run
            if music_download_():
                break
        #////////////////////#
        while dl_type == 'v':
            # run video_qownload_ then check for re run
            if video_download_():
                break
        #////////////////////#
        if close_scritpt_():
            dl_type = 'close'
        #////////////////////#
        return dl_type


######################


print '\n\tYouTube downloader to m4a/mp4'
while __name__ == '__main__':

    while main() != 'close':
        pass
    break
