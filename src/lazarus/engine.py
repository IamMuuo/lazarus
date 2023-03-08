'''
Project: Lazarus
file: engine.py
author: Erick Muuo

Purpose: Contains the base code to perform mark down to html code
        conversion
'''

import markdown
from tidylib import tidy_document

class Engine():
    '''
    The engine class contains code to convert mark down to html 
    code conversion
    '''

    def __init__(self, author):
        self.engine_name = 'Lazarus Engine'
        self.author = author


    def convert(self, content, format=False):
        '''Converts a markdown string given to html code'''
        if format:
            return tidy_document(markdown.markdown(str(content)),{'indent':1, 'doctype': 'strict'})
        else:
            return markdown.markdown(str(content))

    def convert_file(self, filename):
        '''
        Opens a markdown file, parses the markdown and returns 
        the html equivalent of the markdown file
        '''

        with open(filename, 'r') as fd:
            contentMd = fd.read()

        return markdown.markdown(contentMd)
