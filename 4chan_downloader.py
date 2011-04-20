#4Chan Image Downloader Console Application
#Written By Nathan Paulhus in 2011
#Written in Python v2.7
#
#A program that prompts the user for the URL of
#a thread on 4chan, and then proceeds to download
#all the images in that thread

import urllib
import os

#Get the input of the user as the URL
url = raw_input("Enter the URL of the topic: ")

#Open the URL and read it
f = urllib.urlopen(url)
s = f.read()
#Split the URL at the line breaks
splits = s.split('\n')
#Close the connection to the URL
f.close
#Create a count variable with an initial value of 0
count = 0

#Define a method that will return a boolean of whether the
#number of appearances of a substring is greater than 0
def contains(string,query):
        return string.find(query) > -1
#Ask the user for the folder they want to use
folder = raw_input("Enter the name of the folder the images will be saved in: ")
#Loop through each element of the split HTML string
for i in splits:
        #If the line contains the portion of the HTML image tags...
        if (contains(i,"images.4chan.org")):
                #Extract the name of the file from the string
                name = i[i.find("src/")+4:i.find('" target="')]
                #Extract the URL location of the file from the strng
                location = i[i.find('<a href="http') + 9:i.find('" target="')]
                #Create the downloads directory if it does not exist
                try:
                        if not os.path.exists(folder):
                                os.makedirs(folder)
                #Catch any errors in the creation of the directory
                except OSError:
                        print 'Failed to create directory'
                #Attempt to download the image from the already obtained URL
                try:
                        image = urllib.URLopener()
                        image.retrieve(location,folder + '/' + name)
                        print 'Downloaded image number ' + str(count)
                #Catch any Errors. Most likely to be HTML 404 error
                except:
                        print 'Failed to download image ' + str(count) + ' at ' + location
                #Increment the count variable
                count = count + 1
#Announce to the user that all the images in the thread have been downloaded
print 'Downloads completed'
#Pause the console to give the user a chance to read the program
os.system("pause")
