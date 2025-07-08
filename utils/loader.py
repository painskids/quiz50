from ui.cli import colorize
from threading import Thread
import time
import itertools

class Loader:
    def __init__(self, msg: str = 'Loading', end=''):
        self.msg = msg
        self.end = '\n&[bold golden]  [QUIZ50] &[bred]' + end if end.strip() != '' else end
        self.thread = Thread(target=self.animate, daemon=True)
        self.done = False

    
    def start(self):
        self.thread.start()

    def animate(self):
        for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
            if self.done:
                break
            print(colorize(f'\r&[bold gray]{c} &[golden][QUIZ50] &[bred]{self.msg}'), flush=True, end='')
            time.sleep(0.1)
    
    def stop(self):
        self.done = True
        print(colorize(f'{self.end}'))
    
    def __enter__(self):
        self.start()
    
    def __exit__(self, exc_type, exc_value, tb):
        self.stop()
