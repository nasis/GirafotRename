import os
import re
from BeautifulSoup import BeautifulSoup

html_path = r"C:\temp\HTTrack\Girafot\girafot.org\musicpage\index.html"
music_path = r"C:\temp\HTTrack\Girafot"
parsed_html = BeautifulSoup(open(html_path))

table_records = parsed_html.findAll('tr')
albums = [tr for tr in table_records if tr['class'] == "album"]

songs = []
for album in albums:
    hrefs = album.findAll("a")
    urls = hrefs[0::2]
    names = hrefs[1::2]
    songs += zip(urls, names)

paths = []
for url, name in songs:
    file_path = os.path.sep.join([music_path, url['href'][7:]]).replace("/", "\\")
    songname = name.string
    new_path = re.sub("\d+.mp3", u"{0}.mp3".format(songname), file_path)
    paths.append((file_path, new_path))

for file_path, new_path in paths:
    print file_path, new_path
    # try:
    #     os.rename(file_path, new_path)
    # except Exception as e:
    #     print u"Failed on {0}, {1}".format(file_path, new_path)
    #     print e
