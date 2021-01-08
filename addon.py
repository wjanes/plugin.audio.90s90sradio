import urlparse
import xbmcplugin
import xbmcgui
import sys
from lib import _90s90s
from lib import helper


def start():
    args = urlparse.parse_qs(sys.argv[2][1:])
    mode = args.get('mode', None)

    # initial launch of add-on
    # Creating the Directories for browsing
    if mode is None:
        build_song_list()  

    # a song from the list has been selected
    elif mode[0] == 'stream':
        play_song(args)


def build_song_list():
    xbmcplugin.addDirectoryItems(addon_handle, _90s90s.list_songs())
    xbmcplugin.setContent(addon_handle, 'songs')
    xbmcplugin.endOfDirectory(addon_handle)

def play_song(args):
    play_item = xbmcgui.ListItem(path=args['url'][0])
    play_item.setArt({'thumb': args['thumb'][0],
                      'fanart': args['fanart'][0]})
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

if __name__ == '__main__':
    
    addon_handle = int(sys.argv[1])
    start()