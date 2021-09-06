"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: project_03_page_132.py
Problem:
    Write a script that inputs a line of encrypted text and a distance value and outputs
    plaintext using a Caesar cipher. The script should work for any printable characters.
Solution:

"""
# the name of the input file.
infileName = input("Enter the input file name: ")

# Prompt the user to enter
# the name of the output file.
outFileName = input("Enter the output file name: ")

# Prompt the user to enter
# the distance value.
distance = int(input("Enter the distance value: "))

# Open the input file to be read.
inFile = open(infileName, "r")

# Open the output file.
outFile = open(outFileName, "w")
code = ""

final = ""
for chac in infileName:
    ordvalue = ord(chac)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordvalue + 1)
    final += chr(cipherValue)
print(final)

# Write the data
outFile.write(code)

# Close the files.
inFile.close()
outFile.close()
