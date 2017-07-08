import os

#request user to input directory to  begin scraping at
Spoint = input('What directory would you like to begin scraping? E.g: /home/user/Pictures')

#request user to input directory to end scraping at
Epoint = input('What directory would you like to stop scraping files? E.g /home/user/Pictures/VacationPics')

#request user to input directory to copy scraped files to
Cpoint = input('What directory would you like to copy files that are scraped to?')

#function to print
def dict_list(dict):
    for key in sorted(dict):
        print(key, dict[key])


#Dictionary containing options for file types to scrape for
images = {"1":".jpg", "2":".png", "3":".jpeg", "4":".gif"}


dict_list(images)



#request user to input type(s) of files to scrape for
Ftype = input('What type of file(s) would you like to scrape? ' '\n')


if Ftype in images:
    chose = images[Ftype]

print(chose)


#statement to walk directorys
for dirs, subdirs, chose in os.walk(Spoint):
        os.system('cp %s' %chose )
        now = os.listdir(Spoint)
        print(now)
