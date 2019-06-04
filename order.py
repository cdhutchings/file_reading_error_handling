# Opening and error handling with files


#file = open("order.txt")
# This gives a 500 error because such a file does not exist for python to retrieve

# Errors:
# 200 - OK
# 400 - they've messed up
# 500 - we've messed up

# Rather than have errors being thrown up, you might want to catch the error when it starts so the program doesn't break

# try:      # i.e: the following will be run, but if there is an error, the program will not break
#     file = open("order.txt")
#     # You can also do more
#     # than
#     # one
#     # thing
#     # in
#     # this
#     # space
#
# except:   # i.e: print the following if an error occurs
#     print("THERE HAS BEEN AN ERROR!")

# try:
#     file = open("order.txt", "r")
#     file_lines = file.readlines()
#     print(file_lines)
#     # print(file)
#
#     for line in file_lines:
#         print(line.rstrip("\n")) # strips the new line from each line so there is no whitespace when printing
#
#     # file.close() # Closes the file to free up memory. Generally this is done through slicker means
#
# except FileNotFoundError as ermsg: # one can specify the error here if that is necessary
#     print("File has not been found. Do not panic!")
#     print(ermsg) # prints the standard error message in a nice looking way

def open_print_lines(file_original):

    # defining a function makes the code a little DRYer

    try:
        with open(file_original, "r") as file: # avoids the need for closing the file after opening it

            for line in file.readlines():

                print(line.rstrip("\n"))

    except FileNotFoundError as ermsg:
        print("File has not been found!")
        print(ermsg)

    finally:
        print("\n")
        print("All done!")
        print("\n")


open_print_lines("order.txt")

open_print_lines("drinks.txt")