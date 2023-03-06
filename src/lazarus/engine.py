'''
Project: Lazarus
file: engine.py
author: Erick Muuo

Purpose: Contains the base code to perform mark down to html code
        conversion
'''

import markdown

class Engine():
    '''
    The engine class contains code to convert mark down to html 
    code conversion
    '''

    def __init__(self):
        self.engine_name = 'Lazarus Engine'


    def convert(self, content):
        '''Converts a markdown string given to html code'''
        return markdown.markdown(str(content))

    def convert_file(self, filename):
        '''
        Opens a markdown file, parses the markdown and returns 
        the html equivalent of the markdown file
        '''

        with open(filename, 'r') as fd:
            contentMd = fd.read()

        return markdown.markdown(contentMd)
