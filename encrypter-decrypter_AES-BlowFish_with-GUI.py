from Crypto.Cipher import Blowfish
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from cryptography.hazmat.backends import default_backend
from hashlib import md5
from Cryptodome.Cipher import AES
from os import urandom
import imghdr

from PIL import Image

# Create the main window
root = tk.Tk()

# Create the label for the image path
image_path_label = tk.Label(root, text="Image Path:")
image_path_label.grid(row=0, column=0)

# Create the entry for the image path
image_path_entry = tk.Entry(root)
image_path_entry.grid(row=0, column=1)

# Create the button to open the file dialog
image_path_button = tk.Button(root, text="Browse", command=lambda: image_path_entry.insert(
    0, filedialog.askopenfilename()))
image_path_button.grid(row=0, column=2)

# Create the label for the password
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)

# Create the entry for the password
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Create the label for the encryption algorithm
encryption_algorithm_label = tk.Label(root, text="Encryption Algorithm:")
encryption_algorithm_label.grid(row=2, column=0)

algo = StringVar()
# Create the radio buttons for the encryption algorithm
aes_radio_button = tk.Radiobutton(
    root, text="AES", variable=algo,  value="AES")
aes_radio_button.grid(row=2, column=1)

blowfish_radio_button = tk.Radiobutton(
    root, text="Blowfish", variable=algo, value="BLOWFISH")
blowfish_radio_button.grid(row=2, column=2)

# Create the label for the encryption/decryption
encryption_decryption_label = tk.Label(root, text="Encrypt/Decrypt:")
encryption_decryption_label.grid(row=3, column=0)

action = StringVar()
# Create the radio buttons for the encryption/decryption
encrypt_radio_button = tk.Radiobutton(
    root, text="Encrypt", variable=action,  value="ENCRYPT")
encrypt_radio_button.grid(row=3, column=1)

decrypt_radio_button = tk.Radiobutton(
    root, text="Decrypt", variable=action,  value="DECRYPT")
decrypt_radio_button.grid(row=3, column=2)

# Create the button to execute the encryption/decryption
execute_button = tk.Button(root, text="Execute")
execute_button.grid(row=4, column=1)


def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = b''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + str.encode(password) + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]


def pad_data(data):
    block_size = 16

    # Calculating the length of the data
    data_length = len(data)

    # Calculating the number of bytes to be padded
    padding_length = block_size - (data_length % block_size)

    # Padding the data
    return data + (padding_length * os.urandom(1))


def BLOWFISH_encrypt(password, in_image_path, out_image_path):

    # Generate a key from the password
    key = password.encode('utf-8')

    # Create a cipher object
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    # Read the image file
    with open(in_image_path, 'rb') as f:
        plaintext = f.read()

    # Encrypt the image
    ciphertext = cipher.encrypt(pad_data(plaintext))

    # Write the encrypted image
    with open(out_image_path, 'wb') as f:
        f.write(ciphertext)


def BLOWFISH_decrypt(password, in_image_path, out_image_path):
    # Generate a key from the password
    key = password.encode('utf-8')

    # Create a cipher object
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    # Read the encrypted image file
    with open(in_image_path, 'rb') as f:
        ciphertext = f.read()

    # Decrypt the image
    plaintext = cipher.decrypt(ciphertext)

    # Write the decrypted image
    with open(out_image_path, 'wb') as f:
        f.write(plaintext)


def AES_encrypt(in_file, out_file, password, key_length=32):
    try:
        bs = AES.block_size
        salt = urandom(bs)
        key, iv = derive_key_and_iv(password, salt, key_length, bs)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        out_file.write(salt)
        finished = False

        while not finished:
            chunk = in_file.read(1024 * bs)
            if len(chunk) == 0 or len(chunk) % bs != 0:
                padding_length = (bs - len(chunk) % bs) or bs
                chunk += str.encode(padding_length * chr(padding_length))
                finished = True
            out_file.write(cipher.encrypt(chunk))
    except:
        print("AN [ERROR] HAS OCCURRED")


def AES_decrypt(in_file, out_file, password, key_length=32):
    try:
        bs = AES.block_size
        salt = in_file.read(bs)
        key, iv = derive_key_and_iv(password, salt, key_length, bs)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        next_chunk = ''
        finished = False
        while not finished:
            chunk, next_chunk = next_chunk, cipher.decrypt(
                in_file.read(1024 * bs))
            if len(next_chunk) == 0:
                padding_length = chunk[-1]
                chunk = chunk[:-padding_length]
                finished = True
            out_file.write(bytes(x for x in chunk))
    except:
        print("AN [ERROR] HAS OCCURRED")


def check_if_successful(new_path):
    new_file_type = imghdr.what(new_path)
    if not new_file_type == None:
        new_file_type = str(new_file_type).lower()
        if new_file_type in ["gif", "jpeg", "jpg", "png", "svg", "webp"]:
            print(
                f"[SUCCESS] the file has been decrypted and save to [{new_path}]")
        else:
            print(
                f"[FAILED] this is probably due to a wrong password, neverless the decrypted file is saved to [{new_path}]")
    else:
        print(
            f"[FAILED] this is probably due to a wrong password, neverless the decrypted file is saved to [{new_path}]")

# Function to execute the encryption/decryption


def execute():
    # Get the image path
    image_path = image_path_entry.get()
    image_path_entry.delete(0, 'end')
    # Get the password
    password = password_entry.get()
    password_entry.delete(0, 'end')

    # Get the encryption algorithm
    encryption_algorithm = algo.get()
    algo.set("")
    # Get the encryption/decryption
    encryption_decryption = action.get()
    action.set("")

    print("#"*100)
    print(f"image_path:{image_path} || password:{password} || encryption_algorithm:{encryption_algorithm} || encryption_decryption:{encryption_decryption}")
    print("#"*100)
    try:
        image_name = image_path.split("/")[-1]
        path = image_path.replace(image_name, "")
        image_ext = image_name.split(".")[-1]
    except ValueError:
        print("internal error occured! ")
    try:
        if (encryption_algorithm == "AES"):

            if encryption_decryption == 'ENCRYPT':
                new_path = path+"AES-ENCRYPTED_"+image_name
                with open(path+image_name, 'rb') as in_file, open(new_path, 'wb') as out_file:
                    AES_encrypt(in_file, out_file, password)

                print(
                    f"[SUCCESS] the file has been encrypted and save to [{new_path}]")

            elif encryption_decryption == 'DECRYPT':
                new_path = path+"AES-DECRYPTED_"+image_name
                with open(path+image_name, 'rb') as in_file, open(new_path, 'wb') as out_file:
                    AES_decrypt(in_file, out_file, password)
                check_if_successful(new_path)

        elif (encryption_algorithm == "BLOWFISH"):
            if encryption_decryption == 'ENCRYPT':
                new_path = path+"BLOWFISH-ENCRYPTED_"+image_name
                in_path = path+image_name
                BLOWFISH_encrypt(password, in_path, new_path)

            if encryption_decryption == 'DECRYPT':
                new_path = path+"BLOWFISH-DECRYPTED_"+image_name
                in_path = path+image_name
                BLOWFISH_decrypt(password, in_path, new_path)
                check_if_successful(new_path)

    except FileNotFoundError:
        print("coud not find the specified image's path")


# Set the command for the execute button
execute_button.config(command=execute)

# Run the main loop
root.mainloop()
