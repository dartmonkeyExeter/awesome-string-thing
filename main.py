# hello world if it was awesome
import time 
alphabet_and_numbers = list(' ') # create list with a space character 
alphabet_and_numbers += [chr(ord('a') + i) for i in range(26)] # add alphabet to the list
alphabet_and_numbers += list('0123456789!"£$%^&*()-+_=@;#<>?,./\|') # add numbers and punctuation
stuff = input() # get input
output_string = "" # set to ''
final_output = "" # set to ''
for idx, i in enumerate(stuff):
    for j in alphabet_and_numbers:
        output_string = f'{j}' # output string = the letter of the alphabet that is currently looped
        print(f'{final_output}{output_string}') # print that and the whole current word
        if j == i: # if that letter is the correct one, no longer loop
            break
        time.sleep(0.1) # wait a second before going to the next iteration
    final_output += output_string # add final output to output string
