def main():
    #declares local variables
    number = 5
    number_list = [1,2,3,4,5,6,7,8,9,10]
    print('Number:', number)
    print('List of numbers:', number_list, sep='')
    print('List of numbers that are larger than ',number, ':', sep='')
    #Call the larger_than_n_list function,
    #passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)
    # The display_larger_than_n_list function accepts a list, and a number.
    # The function displays all of the numbers in the list that are greater than that number.
def display_larger_than_n_list(n, n_list):
    #Empty list
    larger_than_n_list = []
    #Loop through the values in the list.
    for value in n_list:
    #Determins if a value is greater than n.
        if value > n:
            larger_than_n_list.append(value)
    print(larger_than_n_list)
#Call the main function
main()