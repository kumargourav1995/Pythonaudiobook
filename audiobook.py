""" Audiobook or PDFtoSpeech program  using Text to speech and python PDF library by Kumar Gourav Dakhinray"""
#importing the python packages

import pyttsx3
import PyPDF2

book = open('demo.pdf','rb')                         #Selecting the pdf using a variable book
pdfreader = PyPDF2.PdfFileReader(book)              #Reading the pdf using library PyPDF2
pages = pdfreader.numPages
print("Total Number of pages in PDF:")
print(pages)                                        #To print the number of pages the pdf book has

engine = pyttsx3.init()                             #initialising the text ot speech python module
'''rate'''
rate = engine.getProperty('rate')                   #getting details of current speaking rate
#print(rate)                                        #to print the current voice rate commented out as it's not necessary
engine.setProperty('rate',125)                      # Setting the new speaking rate. Change 125 to speed up or slow the rate
"""VOLUME"""
volume = engine.getProperty('volume')               #getting to know current volume level (min=0 and max=1)
#print (volume)                                      #printing current volume level
engine.setProperty('volume',1.0)                    # setting up volume level  between 0 and 1

for num in range(0,pages):                          #for loop to play the pdf from ranges, 0 is the initial position and pages be the total
    page = pdfreader.getPage(num)                   #Extracting the page from pdf
    text = page.extractText()                       #Extracting the text from the page and store it in variable text
    engine.say(text)                                #playing the extracted text using text to speech module
    engine.runAndWait()                             #running the process and waiting for completion
