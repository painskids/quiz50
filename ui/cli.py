import re
from data import data

class Debug:
    def __init__(self, msg):
        if data.CONFIG['DEBUG']: print(colorize(f'&[green][DEBUG] {msg}'))

class Error:
    def __init__(self, msg):
        print(colorize(f'&[bold red][ERROR] {msg}'))

class Raise:
    def __init__(self, msg):
        print(colorize(f'&[bold red][CODE ERROR] {msg}&[reset black] --there is an error in the code! :('))

class Quiz50:
    def __init__(self, msg, flush=False, end='\n', printing=True):
        self.msg = colorize(f'&[bold golden][QUIZ50] &[bred]{msg}')
        if printing: print(self.msg, flush=flush, end=end)

CODES = {
    'bold': '\033[1m',
    'underline': '\033[4m',
    'strike': '\033[9m',

    'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 
    'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m', 
    'cyan': '\033[36m', 'white': '\033[37m', 'gray': '\033[90m',
    'golden': '\033[38;2;255;170;0m',
    'br': '\033[38;2;255;85;85m',
    'pr': '\033[38;2;255;0;0m',

    'reset': '\033[0m'
}

def colorize(text: str):
    pattern = re.compile(r'(?<!\\)&\[((?:\w+\s*)+)\]')

    result = pattern.sub(replace, text)
    result += CODES['reset']
    return result

def replace(m):
    content = m.group(1).lower().strip()
    styles = content.split()
    coded = ''.join(CODES.get(style, '') for style in styles)
    return coded