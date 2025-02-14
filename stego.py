import cv2
import os
import string
import getpass  # To hide password input

# Load the image
img_path = r"D:\Steganography\wall7.jpg"  # Ensure this path is correct
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found. Check the path!")
    exit()

# Input message and password
msg = input("Enter secret message: ")
password = getpass.getpass("Enter a passcode: ")  # Hidden password input

# Character encoding dictionary
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encoding message into the image
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through BGR channels

# Save and open the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens image on Windows

# Decryption process
message = ""
n, m, z = 0, 0, 0
pas = getpass.getpass("Enter passcode for Decryption: ")

if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through BGR channels
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
