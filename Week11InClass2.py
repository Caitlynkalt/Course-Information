import random

def main():
    total = 0.0
    count = 0

    try:
        afile = open("Random.txt", "r" )
        for num in afile:
            amount = float(num)
            total += amount
            count += 1
        afile.close()
    except ValueError:
        print('Error: file not found')
    except IOError:
        print('Error: Value Error')
    else:
        print('The total of the numbers is:', total, sep='')
        print('The number of random numbers read from the file is:', count ,sep='')

main()