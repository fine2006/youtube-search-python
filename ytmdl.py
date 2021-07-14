def GrabMeta(x):
    print(search[x] ['title'])
    print(search[x] ['duration'])
    val = (search[x] ['artists'])
    print(val[0] ['name'])
    vid = (search[x] ['videoId'])
    print('https://music.youtube.com/watch?v='+vid)
    print('\n')

from ytmusicapi import YTMusic
import json
search_term = str(input("Enter A search term: "))
print('')
ytmusic = YTMusic()
search = ytmusic.search(search_term)
with open("data_file.json", "w") as write_file:
    json.dump(search, write_file)
GrabMeta(0)
GrabMeta(1)
GrabMeta(2)
GrabMeta(3)
