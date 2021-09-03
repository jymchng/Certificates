import os
from PyPDF2 import PdfFileMerger, PdfFileReader
import pprint
import sys

current_dir = os.getcwd()
pdf_files = [file for file in os.listdir(current_dir) if '.pdf' in file]
print("Here is a list of all PDF files in this folder.")
print("-"*10)
x = input("Would you like to merge all pdf files? (y/n) ")
x = x.lower()

if x == 'y':
    output_file_name = input("Please name the output file without the .pdf extension. ")
    merger = PdfFileMerger()
    for pdf_file in pdf_files:
        merger.append(PdfFileReader(open(pdf_file, 'rb')))
    merger.write(output_file_name + ".pdf")
    print("Merge completed.")
    sys.exit("Thank you!")
else:
    sys.exit("Thank you!")