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