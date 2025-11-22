# Secure Message Encoder & Decoder

## 1. Project Overview
The **Secure Message Encoder & Decoder** is a Python-based Command Line Interface (CLI) application designed to protect sensitive text. It uses a custom algorithm to scramble (encrypt) messages and restore (decrypt) them, ensuring privacy during data handling. 

## 2. Features
* **Custom Encryption:** * Words longer than 3 characters are scrambled with random characters at the start and end.
    * Words shorter than 3 characters are simply reversed.
* **Decryption:** Restores the original message by stripping random noise and reversing the logic.
* **Input Validation:** Prevents system crashes by checking for empty inputs or invalid menu choices.
* **Modular Design:** Code is split into `main.py` (interface), `logic.py` (algorithms), and `validation.py` (checks).

## 3. Technologies Used
* **Language:** Python 3.x
* **Libraries:** `random`, `string` (Standard Python libraries).
* **Tools:** VS Code, Git.

## 4. Project Structure
```text
Secure-Messaging-System/
│
├── main.py              # Entry point (User Interface)
├── logic.py             # Core algorithms for encoding/decoding
├── validation.py        # Input checking to prevent errors
└── README.md            # Project documentation
