import PyPDF2
import os
import sys

path = input("Enter the path: ")
outputFileName = input('Enter the final file name: ')
outputFileName += '.pdf'
merger = PyPDF2.PdfFileMerger()

for file in os.listdir(path):
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write(outputFileName)
