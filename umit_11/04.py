# callable objects in the presence of sentinel

with open('example.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line[0])

# Here, the program will read the lines of file example.txt, until the sentinel character  ' ' (empty string) is encountered.
