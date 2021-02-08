def most_popular_artist(our_data):
    
    counter_dict = {}
    for artist in all_artists(our_data): #loops over list of the artists for all albums includes repeats
        if artist in counter_dict: #checking to see if artist alread in counter_dict
            counter_dict[artist] += 1 #if it is, increment by 1
        else: #if 
            counter_dict[artist] = 1 #add artist to the dictionary
    maximum_albums = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_lists.append(keys) 
    return artist_lists

---------------------------

def findname(name, data):
    for entry in data:
        if entry['album'] == name:
            return entry
    else:
        return None
    
def findbyrank(rank, data):
    for entry in data:
        if entry['number'] == str(rank):
            return entry
    else:
        return None
    
def findbyyear(year, data):
    return [entry['album'] for entry in data
            if entry['year'] == str(year)]

def findbyyears(start, stop, data):
    return [entry['album'] for entry in data 
            if int(entry['year']) in range(start, stop+1)]

def findbyranks(start, stop, data):
    return [entry['album'] for entry in data
           if int(entry['number']) in range(start, stop+1)]

def alltitles(data):
    return list(set([entry['album'] for entry in data]))

def allartist(data):
    return list(set([entry['artist'] for entry in data]))

def artistmostalbums(data):
    most_albums = {}
    
    for entry in data:
        if entry['artist'] in most_albums:
            most_albums[entry['artist']] +=1
        else:
            most_albums[entry['artist']]=1
            
    most = max(most_albums.values())
    
    artist_w_most = []
    
    for singer, album in most_albums.items():
        if album == most:
            artist_w_most.append(singer)
    return artist_w_most

def popword(data):
    word_count = {}
    
    albums = alltitles(data)
    words = [album.split() for album in albums]
    
    for album in words:
        for word in album:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word]=1
                
    highest = max(word_count.values())
    
    for word, count in word_count.items():
        if count == highest:
            return word

def by_decades(data):
    years = [int(str(int(entry['year'])//10)+'0') for entry in data]
    
    year_count = {}
    
    for year in years:
        if year in year_count:
            year_count[year]+=1
        else:
            year_count[year]=1
            
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    plt.bar(year_count.keys(), year_count.values())
    plt.xlabel('Years')
    plt.ylabel('Counts')
    plt.xticks(list(range(1950, 2011, 10)))
    return plt.show()

def bygenre(data):
    for entry in data:
        entry['genre'] = entry['genre'].split(',')
    
    genre_list = [genre for entry in data
                 for genre in entry['genre']]
    
    genre_count = {}
    for genre in genre_list:
        if genre in genre_count:
            genre_count[genre]+=1
        else:
            genre_count[genre]=1
    
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    fig, ax = plt.subplots()
    ax.bar(genre_count.keys(), genre_count.values())
    ax.set_title('Top Albums by Genre')
    ax.set_xticklabels(genre_count.keys(), rotation='vertical')
    ax.set_xlabel('Genres')
    ax.set_ylabel('Count')
    
    return plt.tight_layout()

def albummostsongs(wholedata, songdata):
    most_songs = {}
    
    for entry in wholedata:
        for song in songdata:
            for track in entry['tracks']:
                if song['name'] == track:
                    if entry['album'] in most_songs:
                        most_songs[entry['album']] +=1
                    else:
                        most_songs[entry['album']] = 1
    most = max(most_songs.values())
    
    for album, number in most_songs.items():
        if number == most:
            top_album = album
            
    for entry in wholedata:
        if entry['album'] == top_album:
            top_artist = entry['artist']
            
    return (top_album, top_artist)
                
def albumontop500(wholedata, songdata):
    albums_on_list = []
    
    for entry in wholedata:
        for track in entry['tracks']:
            for song in songdata:
                if track == song['name']:
                    albums_on_list.append(entry['album'])
    return set(albums_on_list)
    

def songstopalbums(wholedata, albumdata):
    songs = []
    
    for entry in wholedata:
        for album in albumdata:
            if entry['album'] == album['album']:
                for track in entry['tracks']:
                    songs.append(track)
    return songs
                
                
def tenalbummostsongs(wholedata, songdata):
    most_songs = {}
    
    for entry in wholedata:
        for track in entry['tracks']:
            for song in songdata:
                if track == song['name']:
                    if entry['album'] in most_songs:
                        most_songs[entry['album']]+=1
                    else:
                        most_songs[entry['album']]=1
    
    sorting_them = sorted(list(most_songs.items()), 
                          key = lambda x: x[1], reverse = True)[:10]
    
    tenalbumdict = {}
    for entry in sorting_them:
        tenalbumdict[entry[0]]=entry[1]
    
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    fig, ax = plt.subplots()
    ax.bar(tenalbumdict.keys(), tenalbumdict.values())
    ax.set_xlabel('Albums')
    ax.set_title('Ten Albums With Most Songs on Top Songs')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(tenalbumdict.keys(), rotation = 60)
    return ax.plot()

def artistmostsongsandalbums(songdata, albumdata):
    top_song_and_album = {}
    for song in songdata:
        if song['artist'] in top_song_and_album:
            top_song_and_album[song['artist']] +=1
        else:
            top_song_and_album[song['artist']]=1
            
    for album in albumdata:
        if album['artist'] in top_song_and_album:
            top_song_and_album[album['artist']] +=1
        else:
            top_song_and_album[album['artist']]=1
      
    most = max(top_song_and_album.values())
    
    for key, value in top_song_and_album.items():
        if value == most:
            return key


