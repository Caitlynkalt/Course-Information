import random

def main():
    afile = open("Random.txt", "w" )

    try:
        for num in range(int(input('How many random numbers?: '))):
            afile.write(get_num() + '\n')

    except ValueError:
        print('Error: non-numeric data found in the file.')
def get_num():
    line = str(random.randint(1, 500))
    return line
main()