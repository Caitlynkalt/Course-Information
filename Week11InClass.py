def main():
    import random
    afile = open("Random.txt", "w" )

    try:
        for i in range(int(input('How many random numbers?: '))):
            line = str(random.randint(1, 500))
            afile.write(line)
            print(line)
    except ValueError:
        print('Error')

main()