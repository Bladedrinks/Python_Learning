# This is a program which helps people create a Spotify playlist.

import math


# An UDF for converting cardinal number into its ordinal form (say, 2 --> 2nd, 21 --> 21st, etc):
def ord_form(num):
    """Return the ordinal form of any positive integer."""
    num = str(num)
    if num[-2:] == "11" or num[-2:] == "12" or num[-2:] == "13":
        return num + "th"
    elif num[-1] == "1":
        return num + "st"
    elif num[-1] == "2":
        return num + "nd"
    elif num[-1] == "3":
        return num + "rd"
    else:
        return num + "th"


# An UDF for helping people make decision:
def decision_making_with(object):
    """
    Return a decision choice (case insensitive) which is either 'y' or 'n'.
    This function is created for reducing repetitive blocks of code.
    The input/parameter of this function is the ___ part in the sentence "Do you want to keep adding ___ ?"
    In different parts of the program, this ___ part should be replaced with different object.
    """
    decision = input(f"Do you want to keep adding {object}? (y/n) ")
    while not(decision.lower() == 'y' or decision.lower() == 'n'):
        decision = input(f'''
        ----------------------------------------------
         User Tip: Only 'y' and 'n' are valid inputs.
        ----------------------------------------------
        \nDo you want to keep adding {object}? (y/n) ''')
    return decision


# An UDF for interpolating a conjunction 'and' into a list of words (say, [1, 2, 3] --> '1, 2 and 3')
def insert_and_in(list):
    """
    Return a string where each pair of neighboring items (except the last and penultimate ones) in the given list
    are separated by a combination of a commma and a whitespace character, and the last and penultimate items are
    separated by a conjunction 'and'.

    example:
        Input: [3, 2, 3, 4]
        #       0  1  2  3
        #      -4 -3 -2 -1
        Output: '3, 2, 3 and 4'
    """
    list_in_str = ""
    for i in range(-len(list), 0):
        if i == -2:
            list_in_str += f"{list[i]} and "
        else:
            list_in_str += f"{list[i]}, "
    return list_in_str[:-2]


playlist = {}.fromkeys(['name', 'image', 'description', 'creator', 'songs', 'num_songs', 'total_length', 'followers'],
                       None)
for key in playlist:
    if key == 'image':
        playlist[key] = input(f"Your playlist's {key}: ")
        if playlist[key] == 'None':
            playlist[key] = None
    elif key == 'songs':
        playlist[key] = []  # This line returns: 'songs': []
        ord_num = 1
        while True:
            keys = ['TITLE', 'ARTIST', 'ALBUM', 'ADDED TIME', 'DURATION']
            song = dict.fromkeys(keys, None)
            for song_key in list(song):  # 'list(song)' can be replaced by 'song.keys()'.
                # Performing list() on a dictionary returns a list of all the keys in the dictionary.
                # It is equivalent to list(dict.keys()).
                if song_key == 'DURATION':
                    song[song_key] = float(input(f"Enter the {ord_form(ord_num)} song's {song_key}: "))
                elif song_key == 'ARTIST':
                    song[song_key] = []
                    ordinal = 1
                    while True:
                        song[song_key].append(
                            input(f"Enter the {ord_form(ord_num)} song's {ord_form(ordinal)} songwriter: ")
                        )
                        decision = decision_making_with('songwriter')
                        if decision.lower() == 'n':
                            break
                        ordinal += 1
                    song[song_key] = insert_and_in(song[song_key])
                else:
                    song[song_key] = input(f"Enter the {ord_form(ord_num)} song's {song_key}: ")
            playlist[key].append(song)
            decision = decision_making_with('songs')
            if decision.lower() == 'n':
                break
            ord_num += 1
    elif key == 'num_songs':
        playlist[key] = len(playlist['songs'])
    elif key == 'total_length':
        playlist[key] = math.fsum(playlist['songs'][i]['DURATION'] for i in range(len(playlist['songs'])))
        # Here, I import the 'math' module and use the math.fsum() method
        # in order to add floating numbers with exact precision. Inside the math.fsum() method, the parameter doesn't
        # have to be enclosed by [ ], or the list symbol.
    else:
        playlist[key] = input(f"Your playlist's {key}: ")
print(f'''\n
    -------------------------
        The new playlist:
    -------------------------
''')
for key, value in playlist.items():  # Notice: The dict.items() method returns a 'dict_items' object, which generates
    # a series of tuples - (key1, value1), (key2, value2), (key3, value3), etc.
    if key == 'songs':
        print(f"\n[ {key} ]")
        ord_num = 1
        for song in playlist['songs']:
            print(f"\n<The {ord_form(ord_num)} song>")
            for song_item in song.items():
                print(f"{song_item[0]}: {song_item[1]}")
            ord_num += 1
    else:
        print(f"\n[ {key} ]   {value}")
