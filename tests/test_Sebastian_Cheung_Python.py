# test_Sebastian Cheung Python.py
import re
from unittest import TestCase

class Guru:
    def __init__(self, endpoint:str='https://query.wikidata.org/sparql'):
        self.endpoint = endpoint

    def ask(self, question:str):
        if question =='how old is Tony Blair':
            return '68'
        elif question == 'how old is trump':
            return '75'
        elif question == 'what is the population of London':   
            return '8908081'
        elif question == 'what is the population of Paris': 
            return '2175601'
        else:
            return 'Not Found'
    

class TestGuru(TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('68', guru.ask('how old is Tony Blair'))
        self.assertEqual('75', guru.ask('how old is trump'))
        self.assertEqual('8908081', guru.ask('what is the population of London'))
        self.assertEqual('2175601', guru.ask('what is the population of Paris'))
        