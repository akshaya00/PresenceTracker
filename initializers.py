"""
This module will initialize folders for school, classes and students
"""


import pathlib
import os
import datetime

#Fucntion to initialize a school
def createFolderForSchool(id_generated_for_school):
    #creates a folder in the data folder
    pathlib.Path('data/'+str(id_generated_for_school)).mkdir(parents=False, exist_ok=True)

    #creates a folder in encodings folder
    pathlib.Path('encodings/'+ str(id_generated_for_school)).mkdir(parents=False, exist_ok=True)

"""
test scrip for createFolderForSchool

createFolderForSchool('strw239')
"""

#Fuction to create encodings file
def createEncodingsFile(path):
    file = pathlib.Path(path+'/'+'encodings.pickle')
    #create a version of current pickle file
    if file.exists():
        os.rename(path+'/'+'encodings.pickle',path+'/'+'encodings '+str(datetime.datetime.now())+'.pickle')
    encodings_file = open(path+'/'+'encodings.pickle', "a")
    encodings_file.close()

"""
test scrip for createEncodingsFile

createEncodingsFile('strw239')
"""



#Function to add a classroom to the school
def addFolderForClassroom(id_generated_for_school,standard,section,number_of_students):
    # creates a folder in the folder for school
    pathlib.Path('data/' + str(id_generated_for_school)+'/'+str(standard)+'-'+str(section)).mkdir(parents=False, exist_ok=True)

    #create folders for all students
    for iterator in range(number_of_students):
        pathlib.Path('data/' + str(id_generated_for_school) + '/' + str(standard) + '-' + str(section)+'/'+str(iterator)).mkdir(
            parents=False, exist_ok=True)

    # creates a folder in encodings folder
    pathlib.Path('encodings/' + str(id_generated_for_school) + '/' + str(standard) + '-' + str(section)).mkdir(parents=False,
                                                                                                          exist_ok=True)
    #generate a encodings file
    createEncodingsFile('encodings/' + str(id_generated_for_school) + '/' + str(standard) + '-' + str(section))

"""
test script for addFolderForClassroom

addFolderForClassroom('strw239',7,'C',4)
"""
