def GrabMeta(x):
    if (search[x] ['resultType']) == 'playlist':
        print(search[x] ['title'])
        print(search[x] ['itemCount'])
        val = (search[x] ['author'])
        print(val)
        browse = (search[x] ['browseId'])
        print('https://music.youtube.com/playlist?list='+browse)
        print('\n')
    elif (search[x] ['resultType']) == 'song':
        print(search[x] ['title'])
        print(search[x] ['duration'])
        val = (search[x] ['artists'])
        print(val[0] ['name'])
        vid = (search[x] ['videoId'])
        print('https://music.youtube.com/watch?v='+vid)
        print('\n')
    elif (search[x] ['resultType']) == 'video':
        print(search[x] ['title'])
        print(search[x] ['duration'])
        val = (search[x] ['artists'])
        print(val[0] ['name'])
        vid = (search[x] ['videoId'])
        print('https://music.youtube.com/watch?v='+vid)
        print('\n')
    elif (search[x] ['resultType']) == 'artist':
        pass
    else:
        pass

from ytmusicapi import YTMusic
import json
search_term = str(input("Enter A search term: "))
print('')
ytmusic = YTMusic()
search = ytmusic.search(search_term)
with open("data_file.json", "w") as write_file:
    json.dump(search, write_file)
for i in range(0,32767):
    try:
        GrabMeta(i)
    except IndexError:
        break
