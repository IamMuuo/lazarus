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

    def setUp(self):
        '''
        Create a lazarus engine instance that is to be used 
        in the test framework
        '''

        self.lazarus = Engine('Lazarus Test')

    def test_basic_markdown_conversion(self):
        '''
        Tests if the Lazarus engine can perform basic conversion
        of a markdown string to a html string
        '''

        markdown_string = '#Lazarus Engine!'
        self.lazarus.convert(markdown_string)
        
        self.assertEqual('<h1>Lazarus Engine!</h1>', self.lazarus.convert(markdown_string),
                         'Couldn\'t Convert from markdown to HTML')


# Call the test main
unittest.main()
