#  A messaging system to send the message only to the chosen user

import logic
import validation

def start_process():
    print("**Welcome to Secure Messaging System**")
    
    try:             # using try...except to avoid unwanted error
        word=input("Enter your message : ")          # Input process
        check=validation.check_word(word)           
        b=input("Do you want to code or decode it? - ")
        check2=validation.check_b(b)
        if b=="code":            # Coding and Decoding process
            encoded_form=logic.encoding(word)
            print(f"Output in encoded form is : {encoded_form}")        # Output process for encoding
        elif b=="decode":
            decoded_form=logic.decoding(word)
            print(f"Output in decoded form is : {decoded_form}")        # Output process for decoding

    except Exception as e:
        print(f"An error occured : {e}")

if __name__ =="__main__":      # Ensures code runs only 1 time during importing modules
    start_process()