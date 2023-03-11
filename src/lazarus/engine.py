'''
Project: Lazarus
file: engine.py
author: Erick Muuo

Purpose: Contains the base code to perform mark down to html code
        conversion
'''

import markdown
from tidylib import tidy_document
from jinja2 import Environment, FileSystemLoader
import os

class Engine():
    '''
    The engine class contains code to convert mark down to html 
    code conversion
    '''

    def __init__(self, author):
        self.engine_name = 'Lazarus Engine'
        self.author = author
        self.basefile_path = os.path.dirname(__file__)+'/templates'
        self.template_file = 'base.html'
        self.environment = Environment(loader=FileSystemLoader(self.basefile_path))
        self.template = self.environment.get_template(self.template_file)
        
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


    def write_html_file(self, markdown_file, output_file):
        '''
        Opens two files the markdown and the output file then 
        the markdown file is converted to html and its output is 
        dumped to the output file
        '''


        with open(markdown_file, 'r') as mf:
            md_content = mf.read()
            print('\n\nMd content\n\n'+md_content)


        # open the html dump file
        with open(output_file, 'w') as of:
            html_output = markdown.markdown(md_content)
            print('\n\nMd converted\n\n'+html_output)

            # write the html content to the markdown
            of.write(self.template.render({'title':output_file, 'content':html_output}))
