import sys
import urllib
import os
import xbmcaddon
import xbmc
from ConfigParser import SafeConfigParser

addon = xbmcaddon.Addon(id='plugin.audio.90s90sRadio')
addon_dir = xbmc.translatePath(addon.getAddonInfo('path'))
picture_path = "http://aggregatorservice.loverad.io"

# Build Url String for Kodi
def build_url(query):
    base_url = sys.argv[0]
    return base_url + '?' + urllib.urlencode(query)

#Get Image from the image folder
def get_image(folder, image):
    return os.path.join(addon_dir, "resources", "images", folder, image)

#Get the image url
def get_image_url(link):
    return picture_path + link