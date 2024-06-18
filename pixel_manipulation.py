from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x160")

# Function to encrypt or decrypt the selected image file


def encrypt_or_decrypt_image():
    # Open file dialog to select a JPG file
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name  # Get the file name/path
        # Get the encryption/decryption key from the entry widget
        key = entry1.get(1.0, END)
        print("Selected File:", file_name)
        # Strip to remove any extra newline characters
        print("Key:", key.strip())

        # Read the image file in binary mode
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()

        # Perform XOR encryption/decryption on the image data
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)  # XOR operation with the key

        # Write the encrypted/decrypted image back to the file
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()

        print("Encryption/Decryption complete.")
    else:
        print("Please choose an image file.")


# Create Encrypt Button
b1 = Button(root, text="Encrypt", command=encrypt_or_decrypt_image)
b1.place(x=35, y=70)

# Create Decrypt Button
b2 = Button(root, text="Decrypt", command=encrypt_or_decrypt_image)
b2.place(x=105, y=70)

# Create Entry Widget for Key Input
entry1 = Text(root, height=1, width=10, background="grey")
entry1.place(x=50, y=30)

# Create a Label widget with text
label = Label(root, text="Enter Encryption Key")
label.pack(pady=10)
label.place(x=40, y=5)

# Start the Tkinter main loop
root.mainloop()
