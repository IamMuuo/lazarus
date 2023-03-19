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

        self.assertEqual(len(lines), 18, 'Base file is corrupt!')

    def test_basic_markdown_conversion(self):
        '''
        Tests if the Lazarus engine can perform basic conversion
        of a markdown string to a html string
        '''

        markdown_string = '#Lazarus Engine!'
        self.lazarus.convert(markdown_string)
        
        self.assertEqual('<h1>Lazarus Engine!</h1>', self.lazarus.convert(markdown_string),
                         'Couldn\'t Convert from markdown to HTML')

    def test_markdown_file_to_html_conversion(self):
        '''
        Tests if the lazarus engine can parse a markdown file
        and convert its content to its html equivalent
        '''

        content = ''
        markdown_content = """
# To Do
## At Home
* Wash dishes
* Install winter tires
## At Work
* Finish Report
* Book Team **101** meeting
"""
        with open('tests.md', 'w') as outfd:
            outfd.write(markdown_content)

        with open('tests.md', 'r') as infd:
            for line in infd.readlines():
                content += line
        
        # Try perform a simple conversion to html
        self.lazarus.write_html_file('tests.md', 'tests.html')

        with open('tests.html', 'r') as infd:
            self.assertIsNotNone(infd.readlines(), 'Text file cannot be None')
        

# Call the test main
unittest.main()
