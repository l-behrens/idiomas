#!/usr/bin/python
import os
import sys
import json
import termios
import colorama
import time
from json import JSONDecodeError

import logging

DEFAULT_FILE = 'frases.txt'

class Trainer(object):

    def __init__(self, f=DEFAULT_FILE):
        self.logger = logging.getLogger()
        f = ('%s/%s' % (os.path.dirname(__file__), args.f))
        self._frases = self.load_voc(f)

    def load_voc(self, f):
        try:
            with open(f, 'r') as frases:
                return json.loads(frases.read())
        except IOError as e:
            self.logger.error('func: %s \ndescription: %s' %
                              (self.load_voc.__name__, e))
        except JSONDecodeError as e:
            self.logger.error('func: %s \ndescription: %s' %
                              (self.load_voc.__name__, e))

    def save_voc(self, f):
        with open(f, 'rw') as frases:
            pass

    def run(self):
        while True:

            os.system('cls' if os.name == 'nt' else 'clear')
            txt = " {:<78}\n\n"
            txt2 = " \t{:<15}{:<25}\n\n"
            menu = " {:*^78}\n\n".format(' Bienvenidos ')
            menu += txt.format("Description: type mode and press Enter terminate with crtl+c")
            menu += txt.format("Modes:")
            menu += txt2.format("start", "start learning")
            menu += txt2.format("look", "lookup word")
            menu += txt2.format("new", "save new idiom")
            menu += txt2.format("open", "open different stack")
            menu += txt2.format("show", "show available stacks")
            menu += " {:*^78}\n".format('')
            print('%s' % menu)

            i = input(' >>> ')

            if(i == 'start'):
                self.learn()
            elif(i == 'look'):
                pass
            elif(i == 'new'):
                pass
            elif(i == 'open'):
                pass
            elif(i == 'show'):
                pass
            else:
                print('Unknown Mode')
                time.sleep(0.5)

    def learn(self):

        while self._frases:
            frase = self._frases.popitem()

            os.system('cls' if os.name == 'nt' else 'clear')
            txt = " {:<78}\n\n"
            txt2 = " \t{:<15}{:<25}\n\n"
            vis = " {:*^78}\n\n".format(' Aprender las frases y idiomas ')
            vis += " \t Frase: {:<78}\n".format(frase[0])
            vis += " {:*^78}\n".format('')
            print('%s' % vis)
            i = input(' >>> ')
            print('\n\ttraduccion: %s' % frase[1])
            time.sleep(2)

            os.system('cls' if os.name == 'nt' else 'clear')
        print("{:*^78}\n{:*^78}\n{:*^78}".format('', ' End of Lection ', ''))
        time.sleep(2)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default=DEFAULT_FILE,
                        help="load vocabulary from file")

    args = parser.parse_args()

    # Path to config file
    t = Trainer(f=args.f)

    try:
        t.run()
    except KeyboardInterrupt as k:
        print('Terminating...bye!')
        sys.exit(0)
