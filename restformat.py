#!/usr/bin/env python

def title(mytitle='reStructeredText Title'):
    'Returns mytitle formatted as a reStructeredText title.'
    return '=================================' + '\n' + mytitle + '\n' + '================================='

def subtitle(mysubtitle='reStructeredText Subtitle'):
    'Returns mysubtitle formatted as a reStructeredText subtitle.'
    return '\n' + mysubtitle + '\n' + '---------------------------------'
