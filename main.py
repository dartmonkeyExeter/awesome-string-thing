# hello world if it was awesome
import time
alphabet_and_numbers = list(' ')
alphabet_and_numbers += [chr(ord('a') + i) for i in range(26)]
alphabet_and_numbers += list('0123456789!"£$%^&*()-+_=@;#<>?,./\|')
stuff = input()
output_string = ""
final_output = ""
for idx, i in enumerate(stuff):
    for j in alphabet_and_numbers:
        output_string = f'{j}'
        print(f'{final_output}{output_string}')
        if j == i:
            break
        time.sleep(0.02)
    final_output += output_string       
