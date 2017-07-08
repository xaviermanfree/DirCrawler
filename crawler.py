import os

def UserInput():
#User inputs Start Point
    Spoint = input('Where to start: \n')
#check validity of input
    if os.path.isdir(Spoint):
        print('Scraping will begin at: ' + Spoint)
    elif not os.path.isdir(Spoint):
        print('Not a valid directory')
        exit()
#User input for End Point
    Epoint = input('\n\nWhat directory would you like to stop scraping at? ')
# Check if Endpoint is a valid SubDirectory of the parent directory
    if os.path.isdir(Epoint) and len(Epoint) >= len(Spoint):
        print('\n\nScraping will end at: ' + Epoint)
    elif os.path.isdir(Epoint) or len(Epoint) >= len(Spoint):
        print('Error w/ End Point directory, make sure directory is formatted correly, and is a sub directory of your Starting Point')
        exit()

UserInput()

"""
#This will be the function that traverses the directories
for dirs, subdirs, files in os.walk(path):
        os.system('cp %s' %files )
        now = os.listdir(path)
        print(now)
"""
