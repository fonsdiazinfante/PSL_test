"""
Alfonso Díaz-Infante

Script that will read all JSON files from the provided path and
write all user id's and addresses into a new tsv file
"""

import time
import json
import csv
import glob


start = time.time() #save the time when the program started running

usersDict = {} #define an empty Dictionary to store the username and address

files = glob.glob('/home/user/Documents/user_profiles/*', recursive=True) #get all files inside the path stated as the first argumnent

for single_file in files: #loop through all the files
    with open(single_file) as json_file: #open the files
        data = json.load(json_file) #load the json data
        if data['registration_address'][0]['type']=="work": #if the users address is type "work"
            print(data['user_id'])
            print(data['registration_address'][0]['address']['address_line_1'])
            usersDict.update({data['user_id']: data['registration_address'][0]['address']['address_line_1']}) #add userid and address to the dictionary
        else:
            print("jaja")

with open('users.tsv', 'w') as f: #create a new tsv file
    writer = csv.writer(f, delimiter='\t') #separate data form the same row with a tab
    writer.writerow(['username', 'address']) #write the file header
    for k, v in usersDict.items(): #loop through all the items of the dictionary
       writer.writerow([k, v]) #write the data into rows


end = time.time() #save the time the program finished running
print(end - start, "seconds of execution time") #substract the end time with the start time to get the time spent executing
