logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encryption(plain_text,shift_amount):
#     new_text=""
#     for letter in plain_text:
#         if letter == ' ':
#             new_letter = ' '
#         else:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             if(new_position>25):
#                 new_position = new_position-26
#             new_letter = alphabet[new_position]
#         new_text += new_letter
#     print(f"The encoded text is {new_text}")
#
# def decryption(plain_text,shift_amount):
#     new_text=""
#     for letter in plain_text:
#         if letter == ' ':
#             new_letter = ' '
#         else:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_letter = alphabet[new_position]
#         new_text += new_letter
#     print(f"The decoded text is {new_text}")

def encryptionDecryption(plain_text,shift_amount,direction_text):
    new_text = ""
    if direction_text == "decode":
        shift_amount *= -1;
    for letter in plain_text:
        if letter == ' ':
            new_letter = ' '
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if (new_position > 25):
                new_position = new_position - 26
            new_letter = alphabet[new_position]
        new_text += new_letter
    print(f"The {direction_text} text is {new_text}")

encryptionDecryption(text,shift,direction)
# if(direction=="encode"):
#     encryption(plain_text=text, shift_amount=shift)
# else:
#     decryption(plain_text=text, shift_amount=shift)
