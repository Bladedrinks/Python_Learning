# This file contains the three versions of a function named 'speak'.
# Source: https://www.udemy.com/the-modern-python3-bootcamp/learn/lecture/9160768#bookmarks

# ====== Intro (Function Goal & Output)======
# The function 'speak' accepts a single parameter, 'animal':

# If animal is 'dog', it returns 'woof'.
# If animal is 'cat', it returns 'meow'.
# If animal is 'duck', it returns 'quack'.
# If animal is 'pig', it returns 'oink'.
# If animal is anything else, it returns '?' (a question mark).
# If animal is not specified, the 'animal' parameter defaults to 'dog'.

# Table of Outputs:
# Function_call     Expected_output    Note
# speak()           'woof'             No argument is passed in, so the default parameter value is specified.
# speak('dog')      'woof'
# speak('cat')      'meow'
# speak('pig')      'oink'
# speak('duck')     'quack'
# speak('lion')      ?                 Compared to the four animals mentioned before, 'lion' belongs to
#                                      the 'anything else' stuff, so a question mark should be returned.


# ====== Version 1 (Using the 'if' statements) ======
def speak_v1(animal='dog'):
    """Return 'oink' if the input is 'pig';'quack' if the input is 'duck';
    'meow' if the input is 'cat'; 'woof' if the input is 'dog', which also
    is the default value set to the 'animal' parameter;
    '?' if the input is anything else. """
    if animal == 'dog':
        return 'woof'
    if animal == 'duck':
        return 'quack'
    if animal == 'pig':
        return 'oink'
    if animal == 'cat':
        return 'meow'
    return '?'


# ====== Version 2 (Using the data type of dictionary) ======

# Since the arguments 'dog', 'cat', 'duck' and 'pig'
# and their corresponding return values 'woof', 'meow', 'quack' and 'oink'
# can be thought of as a dictionary which maps animals to their sounds,
# we can make use of the membership of each argument (i.e., the input key)
# in the dictionary {'dog': 'woof', 'pig': 'oink', 'duck': 'quack', 'cat': 'meow'}
# to refactor the original version of the function definition.


def speak_v2(animal='dog'):
    """
    Return 'woof', 'meow', 'quack' and 'oink'
    if we pass in 'dog', 'cat', 'duck' and 'pig' as the animal parameter, respectively.
    Return '?' (a question mark) if we pass in anything besides the four animals mentioned before.
    Return 'woof' if the parameter is not specified since the default parameter value is 'dog'.
    """
    animal_sounds = {'dog': 'woof', 'cat': 'meow', 'duck': 'quack', 'pig': 'oink'}
    if animal_sounds.get(animal):
        return animal_sounds[animal]
    return '?'
    # Uncomment the four lines of code below to show another version with a bit difference:
    # sound = animal_sounds.get(animal)
    # if sound:  # if the variable 'sound' stores a certain value (not an empty variable), then execute the suite of if.
    #     return sound
    # return '?'

# ====== Version 3 (Using the default parameter in the dict.get(key[, default]) method) ======

# The dict.get() method has a really interesting and handy feature.
# We can use it to remove the unnecessary the 'return' statement in the last line in Version 2.
# The dict.get() method actually has two parameters:
# one is 'key', which is required,
# and the other is 'default', which is optional and has a default value - None,
# whose boolean value is False.
# The 'default' argument is returned only if the key argument is not in the dictionary.
# You can pass in some prompt words, like 'Wrong key', 'Sorry, the key is not in the dict.', etc.
# In this case, we should pass in '?' (a question mark) as the parameter.
# If the key argument is not in the dictionary 'animal_sounds' (say, 'lion', 'apple', 'Lisa', etc.),
# the ? character will be returned.
# It's like, "What?! What are you talking about?
# What you passed in as the parameter is not in the dictionary!"


def speak_v3(animal='dog'):
    """
    Return 'woof', 'meow', 'quack' and 'oink'
    if we pass in 'dog', 'cat', 'duck' and 'pig' as the animal parameter, respectively.
    Return '?' (a question mark) if we pass in anything besides the four animals mentioned before.
    Return 'woof' if the parameter is not specified since the default parameter value is 'dog'.
    """
    animal_sounds = {'dog': 'woof', 'cat': 'meow', 'duck': 'quack', 'pig': 'oink'}
    return animal_sounds.get(animal, '?')


# ====== TEST ======
print(speak_v3())
print(speak_v3('pig'))
print(speak_v3('duck'))
print(speak_v3('cat'))
print(speak_v3('dog'))
print(speak_v3('banana'))
