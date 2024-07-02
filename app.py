import streamlit as st
import numpy as np
from numpy.linalg import inv

encrypt_tab, decrypt_tab = st.tabs(["ENCRYPTION", "DECRYPTION"])

alphabet_letter_to_number = {" ":0,
                            "A":1,
                            "B":2,
                            "C":3,
                            "D":4,
                            "E":5,
                            "F":6,
                            "G":7,
                            "H":8,
                            "I":9,
                            "J":10,
                            "K":11,
                            "L":12,
                            "M":13,
                            "N":14,
                            "O":15,
                            "P":16,
                            "Q":17,
                            "R":18,
                            "S":19,
                            "T":20,
                            "U":21,
                            "V":22,
                            "W":23,
                            "X":24,
                            "Y":25,
                            "Z":26,
                            "0":27,
                            "1":28,
                            "2":29,
                            "3":30,
                            "4":31,
                            "5":32,
                            "6":33,
                            "7":34,
                            "8":35,
                            "9":36,
                            "!":37,
                            "?":38,
                            "(":39,
                            ")":40,
                             ".":41,
                             ",":42
                            }

alphabet_number_to_letter = {"0":" ",
                            "1":"A",
                            "2":"B",
                            "3":"C",
                            "4":"D",
                            "5":"E",
                            "6":"F",
                            "7":"G",
                            "8":"H",
                            "9":"I",
                            "10":"J",
                            "11":"K",
                            "12":"L",
                            "13":"M",
                            "14":"N",
                            "15":"O",
                            "16":"P",
                            "17":"Q",
                            "18":"R",
                            "19":"S",
                            "20":"T",
                            "21":"U",
                            "22":"V",
                            "23":"W",
                            "24":"X",
                            "25":"Y",
                            "26":"Z",
                            "27":"0",
                            "28":"1",
                            "29":"2",
                            "30":"3",
                            "31":"4",
                            "32":"5",
                            "33":"6",
                            "34":"7",
                            "35":"8",
                            "36":"9",
                            "37":"!",
                            "38":"?",
                            "39":"(",
                            "40":")"
                             "41":".",
                             "42":","
                             
                            }

# THE INVERTIBLE MATRIX THAT WE WILL USE TO ENCRYPT THE MESSAGE
key = [[1,-2,2],[-1,1,3],[1,-1,-4]]
key_matrix = np.array(key)
inverse_key_matrix = inv(key_matrix)

def encrypt(message):
    # REPLACE PERIODS AND COMMAS WITH BLANK, CONVERT STRING TO UPPERCASE
    text = message.upper()

    # CONVERT TEXT TO LIST OF INTEGERS
    text_converted = []

    for ltr in text:
        letter = alphabet_letter_to_number[ltr]
        text_converted.append(letter)

    # CHECK IF LIST IS DIVISIBLE BY 3. IF NOT, ADD 0 UNTIL IT BECOME DIVISIBLE
    if len(text_converted) % 3 != 0:
        text_converted.append(0)
    
    if len(text_converted) % 3 != 0:
        text_converted.append(0)

    # CONVERT LIST TO 3x3 MATRIX
    final_text_converted = [text_converted[i:i + 3] for i in range(0, len(text_converted), 3)]
    text_converted_matrix = np.array(final_text_converted)

    # MULTIPLY THE MATRIX WITH THE KEY MATRIX
    encrypted_matrix = np.matmul(text_converted_matrix, key_matrix)

    # CONVERT THE MATRIX TO A STRING LIST
    encrypted_message_flatten = encrypted_matrix.flatten()
    encrypted_message_flatten = encrypted_message_flatten.tolist()
    encrypted_message_flatten = map(str, encrypted_message_flatten)

    # CONVERT LIST TO STRING OF CODE
    final_encrypted_message = " ".join(encrypted_message_flatten)
    st.info(final_encrypted_message)

def decrypt(code):
    # CONVERT STRING TO LIST
    code_list_string = list(code.split(" "))
    # CONVERT STRING LIST TO INTEGER LIST
    code_list_integer = [eval(i) for i in code_list_string]

    # CONVERT INTEGER LIST TO 3x3 MATRIX
    code_converted = [code_list_integer[i:i + 3] for i in range(0, len(code_list_integer), 3)]
    code_converted_matrix = np.array(code_converted)

    # MULTIPLY THE MATRIX WITH THE INVERSE OF THE KEY MATRIX
    decrypted_matrix = np.matmul(code_converted_matrix, inverse_key_matrix)

    # CONVERT THE MATRIX TO A STRING LIST
    decrypted_matrix_flatten = decrypted_matrix.flatten()
    decrypted_matrix_flatten = map(int, decrypted_matrix_flatten)
    decrypted_matrix_flatten = map(str, decrypted_matrix_flatten)

    # CONVERT STRING LIST OF NUMBERS TO LETTERS
    converted_code = []

    for ltr in decrypted_matrix_flatten:
        letter = alphabet_number_to_letter[ltr]
        converted_code.append(letter)

    # CONVERT LIST TO STRING
    final_decrypted_message = "".join(converted_code)
    st.info(final_decrypted_message)

with encrypt_tab:
    st.header("ENCRYPT A MESSAGE")
    message = st.text_input(" ", placeholder="Write your message...", label_visibility="hidden")
    if st.button("ENCRYPT", use_container_width=True) and (len(message) != 0):
        encrypt(message)

with decrypt_tab:
    st.header("DECRYPT A CODE")
    message = st.text_input(" ", placeholder="Enter the code...", label_visibility="hidden")
    if st.button("DECRYPT", use_container_width=True) and (len(message) != 0):
        decrypt(message)
