alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from Caeserart import logo
print(logo)

not_go_again = True
while not_go_again:
    invalid = True
    while invalid:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            invalid = not True
        else:
            print('Wrong input!')
        

    text = input("Type your message here:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == 'decode':
                shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += char
        print(f'The {direction}d text is {end_text}')
                    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    yes_no = True
    while yes_no:
        rerun = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
        if rerun == 'yes' or rerun == 'no':
            if rerun == 'no':
                print('Goodbye.')
                not_go_again = False
            elif rerun == 'yes':
                not_go_again = True
            yes_no = False
        else:
            print('Wrong input, choose "yes" or "no".')   
    