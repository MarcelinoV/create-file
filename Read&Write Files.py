#Read&Write Files.py - creates and writes into file for user
# Note: pdf and doc files will probably be corrupted

print('File types include .doc, .txt, .html,.pdf...')

prompt = input('enter file name and type of file: ') # first prompt to specify file name and type
prompt2 = input('Do you wish to write into the file? ') # prompt to write in file

new_file = open(prompt, "w") # creates a new file

if prompt2 == 'yes': # conditional statement
    words = input('Type what you want to write: ') # prompts user to type in file content
    new_file.write(words) # writes in new file



print('Closing file.')

new_file.close() # closes new file