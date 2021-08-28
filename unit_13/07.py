## like cat command in unix
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

## команда grep в unix
def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line, end="")

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

filenames = ['01.py','02.py','03.py','04.py']
pattern = "yield"
main(pattern, filenames)