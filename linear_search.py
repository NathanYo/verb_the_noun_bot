from sys import argv

file_in = argv[1]
verb_file = argv[2]
noun_file = argv[3]



file_opened = open(file_in, 'r')
f = file_opened.readlines()
file_opened.close()

verb_out = open(verb_file, 'a+')
noun_out = open(noun_file, 'a+')

def read_file(f):
    for line in f:
        partitioned_line = line.partition(":")
        word = partitioned_line[0]
        if partitioned_line[0][-1].title() == 'N': #Format of 2of12 is in word N: or similar
            word = word.strip(' -:N') + '\n'
            noun_out.write(word)
        elif partitioned_line[0][-1].title() == 'V':
            word = word.strip(' -:V') + '\n'
            verb_out.write(word)
            
read_file(f)
