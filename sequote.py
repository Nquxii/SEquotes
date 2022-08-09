import random
import os

CDIR = os.path.dirname(os.path.abspath(__file__))

'''
Algorithm R(3.4.2) (Waterman's "Reservoir Algorithm") from 
Knuth's "The Art of Computer Programming" is good (in a very simplified version):
'''
def random_line(file):
    line = next(file)
    
    for num, xline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = xline.strip()
    
    return line

with open(f'{CDIR}/quotes.txt', 'r') as quotes:
    print(random_line(quotes))
