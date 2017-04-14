# Make sure you write a function that takes in 0 arguments.  You should ask the user for the filename in this function and return it.
#Your program should start and be driven from a main function.
#Create your own text file to use for this assignment.  It should have at least 5 lines in it.  Your program should not assume the number of lines in the file (use a loop).
#Add this file to a new git repo and commit it.

def main():
    #Find file name and open it.
    file_name = input('Enter the name of the file:')
    file = open(file_name, 'r')

    count = 0

    for line in file:
        name = str(line)
        count += 1
        print(count,': ', name, sep='')
        #file.readlines(count)


    #Close the file
    file.close()

main()