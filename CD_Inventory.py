#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Tiago Rodrigues, 2022-Dez-03, update code to work with classes
#------------------------------------------#

import os

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        new_cd: Function that takes new CD data and creates a new CD while appending to list
    """
    # TODone Add Code to the CD class
    # -- Fields -- #
    cd_id = ''
    cd_title = ''
    cd_artist = ''
    # -- Construct -- #
    def __init__(self, Id, title, artist):
        # -- Atributes -- #
        self.__cd_id = Id
        self.__cd_title = title
        self.__cd_artist = artist
    def contents(self):
        return [self.cd_id, self.cd_title, self.cd_artist]
    
    def display(self):
        return '{}\t{} (by:{})'.format(*self.contents()) 
    
    
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        if str(value).isnumeric():
            self.__cd_id = value
        else:
            raise Exception('The Cd Id must be an integer!')

    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    # -- Methods -- #
    @staticmethod
    def new_cd(cdinfo):
        '''Adds new CD to list of CDs (lstOfCDObjects)
        Args:
            cdinfo(CD): Object CD consisting of CD data
        Data:
            None
        '''
        lstOfCDObjects.append(cdinfo)
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def read_from_file(self, file_name):
        '''Function to read a file write to a list
        Args:
            file_name(string): name of file used to read the data from
        Returns:
            data(object): list of CD objects
        '''
        lstOfCDObjects.clear()
        if os.path.exists(file_name):
            with open(file_name, 'r') as ObjFile:
                for line in ObjFile.readlines():
                    data = line[:-1].split(',')
                    lstOfCDObjects.append(CD(data[0], data[1], data[2]))
        else:
            print('The file {} doesn\'t exist'.format(file_name))
            while True:
                rsp = input('Would you like to create a new file? (y/n):').strip()
                if rsp.lower() == 'y':
                    with open(file_name, 'w') as objFile:
                        print('File created successfully!')
                    break
                elif rsp.lower() == 'n':
                    break
                else:
                    print('Choose one of the two options')
        '''try:
            with open(file_name, 'r') as fileObj:
                data = fileObj.read()
            return data
        except FileNotFoundError:
        '''
            


    # TODone Add code to process data to a file
    @staticmethod
    def add_to_file(self, lst, filename):
        '''Function to write into the file
        Args:
            file_name(string): name of file used to read the data from
            lst (list): data structure that holds the data during runtime
        Returns:
            None.
        '''
        
        
        
        #read = FileIO.read_from_file(FileIO, strFileName)
        #print('Here is the data to insert inside the file: ', lst)
        #if read == '':
        with open(filename, 'w') as ObjFile:
            for row in lst:
                ObjFile.write(str(row) + '\n')
        print('Data added successfully')
        '''
        else:
            with open(filename, 'a') as ObjFile:
                for row in lst:
                    ObjFile.write(str(row) + '\n')
            print('Data appended successfully')
        '''
# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    # TODone add code to show menu to user
    @staticmethod
    def show_menu():
        '''This function shows to user the menu
        Args:
            None.
        Retunrs:
            None.
        '''
        print('Menu')
        print('[d] Display the current inventory\n[a] Add data to the inventory\n[s] Save inventory to file\n[l] Load inventory from file\n[x] Exit')
    # TODone add code to captures user's choice
    @staticmethod
    def user_choice():
        '''Simple Function to request the user choice
        Args:
            None.
        Retunrs:
            Choice (string): a lower case string of the users choice
        '''
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Select the operation: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the acurrent data on screen
    @staticmethod
    def cd_list(self, lst):
        '''Display current inventory
        Args:
            lst(list of Cds): List of cds
        Retunrs:
            None.
        '''
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst:
            print(row.display())
            #print('{}\t{} (by:{})'.format(*row))
            pass
        print('======================================')
    # TODone add code to get CD data from user
    @staticmethod
    def get_user_input(self):
        '''Simple Function to get the user input
        Args:
            None.
        Retunrs:
            CD info: Object of CD that contains ID, CD Title and CD Title
        '''
        while True:
            try:
                strId = int(input('Enter Cd Id:').strip())
                break
            except ValueError:
                print('The Cd Id must be an integer!')
        strTitle = input('Enter Cd Title:').strip()
        strArtist = input('Enter Cd Artist:').strip()
        return strId, strTitle, strArtist

# -- Main Body of Script -- #
# TODone Add Code to the main body
FileIO.read_from_file(FileIO, strFileName)# Load data from file into a list of CD objects on script start
while True:
# Display menu to user
    IO.show_menu()
    strchoice = IO.user_choice()
    # let user exit program
    if strchoice == 'x':
        break
    # show user current inventory
    if strchoice == 'd':
        IO.cd_list(IO, lstOfCDObjects)
    # let user add data to the inventory
    elif strchoice == 'a':
        cd_id, cd_title, cd_artist = IO.get_user_input(IO)
        cd = CD(cd_id, cd_title, cd_artist)
        lstOfCDObjects.append(cd)
        #CD.new_cd(IO.get_user_input())
    # let user save inventory to file
    elif strchoice == 's':
        FileIO.add_to_file(FileIO, lstOfCDObjects, strFileName)
        lstOfCDObjects = []
    # let user load inventory from file
    elif strchoice == 'l':
        FileIO.read_from_file(FileIO, strFileName)
    else:
        print('Choose one option of the menu')