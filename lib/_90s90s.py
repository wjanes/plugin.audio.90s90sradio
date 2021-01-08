import xbmcgui
from lib import helper

stream_base_url = 'http://90s90s.hoerradar.de'


def list_songs():
    song_list = []

    ##################
    # 90s Boygroup
    ##################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33000))
    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_boygroups_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_boygroups_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33011)})

    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-boygroup-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_boygroups_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_boygroups_600x600.png')})

    song_list.append((url, li, False))

    #################
    # 90s Dance
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33001))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_dance_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_dance_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33012)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-eurodance-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_dance_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_dance_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s Grunge
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33002))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_grunge_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_grunge_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33013)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-grunge-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_grunge_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_grunge_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s HipHop
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33003))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hiphoprap_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hiphoprap_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33014)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-hiphop-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hiphoprap_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hiphoprap_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s HipHop DE
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33004))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2019/12/90s90s_hiphop-de_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2019/12/90s90s_hiphop-de_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33015)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-hiphopger-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2019/12/90s90s_hiphop-de_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2019/12/90s90s_hiphop-de_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s In the Mix
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33005))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2019/08/90s90s_inthemix_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2019/08/90s90s_inthemix_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33016)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-inthemix-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2019/08/90s90s_inthemix_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2019/08/90s90s_inthemix_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s Beat
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33006))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_clubhits_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_clubhits_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33017)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-main-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_clubhits_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_clubhits_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s Hits
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33007))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hits_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hits_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33018)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-pop-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hits_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_hits_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s RnB
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33008))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_blackrnb_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_blackrnb_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33019)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-rnb-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_blackrnb_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_blackrnb_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s Techno
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33009))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_techno_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_techno_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33020)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-techno-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_techno_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2018/10/90s90s_techno_1920x1080.png')})

    song_list.append((url, li, False))

    #################
    # 90s Xmas
    #################
    li = xbmcgui.ListItem(label=helper.addon.getLocalizedString(33010))

    li.setArt({'thumb': helper.get_image_url('/wp-content/uploads/2019/11/90s90s_xmas_600x600.png'),
               'fanart': helper.get_image_url('/wp-content/uploads/2019/11/90s90s_xmas_1920x1080.png')})

    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='video', infoLabels={
               'plot': helper.addon.getLocalizedString(33021)})
    url = helper.build_url({'mode': 'stream',
                            'url': stream_base_url + '/90s90s-xmas-mp3-hq',
                            'thumb': helper.get_image_url('/wp-content/uploads/2019/11/90s90s_xmas_600x600.png'),
                            'fanart': helper.get_image_url('/wp-content/uploads/2019/11/90s90s_xmas_1920x1080.png')})

    song_list.append((url, li, False))

    return song_list
