# Caesar Cipher

## Full Description

The Caesar Cipher project is a simple Python script that allows users to encrypt or decrypt messages using the Caesar Cipher technique. This method shifts the letters in the alphabet by a specified number to create an encoded message. The same process can be reversed to decode the message if the shift number is known.

**Features:**
- **Encrypt Messages:** Users can input a message and a shift value to encode the message using the Caesar Cipher technique.
- **Decrypt Messages:** Users can input an encoded message and a shift value to decode the message back to its original form.
- **Handles Non-Alphabet Characters:** The script retains spaces, numbers, and punctuation in their original form, only shifting alphabetic characters.
- **Input Validation:** Ensures that users provide valid inputs for the direction of operation (encode/decode) and for continuing or stopping the program.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### How to Use

1. Clone or download the repository to your local machine.
2. Ensure you have the `Caeserart.py` file in the same directory as the main script for the logo.
3. Run the script using Python:

   ```bash
   python caesar_cipher.py
   ```

4. Follow the on-screen prompts to:
   - Choose whether to encode or decode a message.
   - Enter the message you want to encode or decode.
   - Specify the shift number, which determines how much each letter in the message will be shifted in the alphabet.
   - View the encoded or decoded message.

5. After processing the message, you can choose to run the program again or exit.

### Customization

You can customize the Caesar Cipher by:
- **Adjusting the Alphabet:** Modify the `alphabet` list to include additional characters or create a different encryption scheme.
- **Changing the Shift Logic:** Implement different shifting logic or add support for other types of ciphers.
- **Enhancing User Interaction:** Add more features such as saving the encrypted messages to a file or supporting multiple encryption methods.
