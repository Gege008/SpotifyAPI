import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))


def ask_user():
    return input('Add meg a kedvenc zenészedet: ')


def title_selector(singer):
    result = sp.search(q=singer, type='artist')
    id = result['artists']['items'][0]['id']
    albums = sp.artist_albums(id, limit=50)
    index = random.randint(0, len(albums['items']))
    return albums['items'][index]['name']


def name_underliner(name):
    words = name.split()

    max_index = 0
    max = 0
    for index, word in enumerate(words):
        if len(word) > max:
            max = len(word)
            max_index = index

    original = words[max_index]
    words[max_index] = ''
    for i in range(max):
        words[max_index] += '_'

    return ' '.join(words), original


def ask_answer():
    return input('Mi lehet az aláhúzások helyén (ha nem adsz meg semmit kilépek): ').lower()


def main():
    print(
        'Ez a program kiválaszt egy albumot a kedvenc zenészedtől és ad egy feladatot, hogy találd ki az egyik albumának a nevét!')
    name = title_selector(ask_user())
    question, good_answer = name_underliner(name)
    good_answer = good_answer.lower()
    answer = '_'
    while answer != good_answer and answer != '':
        print(question)
        answer = ask_answer()
        if answer == '':
            print(f'A helyes megoldás a "{good_answer}"')
        elif answer != good_answer:
            print('Sajnos nem talált!')
    if answer != '':
        print('Gratulálok eltaláltad!')


main()
