'''
filename: tests.py
author  : Erick Muuo
(C) Copyright 2023 All rights reserved

Contains the testing framework for the lazarus engine static site 
generator
'''

import unittest
from lazarus.engine import Engine
import os

class TestLazarusEngine(unittest.TestCase):
    '''Tests the lazarus engine'''

    def setUp(self):
        '''
        Create a lazarus engine instance that is to be used 
        in the test framework
        '''

        self.lazarus = Engine('Lazarus Test')

    def test_check_template_file_exists(self):
        '''
        Tests to check if the base template file exists
        '''
        basefile_path = os.path.dirname(__file__)+'/lazarus/templates/base.html'

        # Open the file and check if it has content
        with open(basefile_path) as fobj:
            lines = fobj.readlines()

        breakpoint()

        self.failIf(len(lines) < 100, 'Base might be corrupt')

        self.assertEqual(len(lines), 8, 'Base file is corrupt!')

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
