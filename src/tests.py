'''
filename: tests.py
author  : Erick Muuo
(C) Copyright 2023 All rights reserved

Contains the testing framework for the lazarus engine static site 
generator
'''

import unittest
from lazarus.engine import Engine

class TestLazarusEngine(unittest.TestCase):
    '''Tests the lazarus engine'''

    def test_formatting_string(self):
        '''
        Tests if the Lazarus engine can perform basic conversion
        of a markdown string to a html string
        '''

        markdown_string = '#Lazarus Engine!'
        lazarus = Engine(True)
        
        self.assertEqual('<h1>Lazarus Engine!</h1>', lazarus.convert(markdown_string),
                         'Couldn\'t Convert from markdown to HTML')


# Call the test main
unittest.main()
