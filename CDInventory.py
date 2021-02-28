#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#bhujun, modified file to add docstrings and structured error handling where there is user interaction, and modify permanent data to store binary data
#------------------------------------------#
import pickle

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {'id':3, 'Artist':'Pink Floyd','Title':'ABC'}
strFileName = 'CDInventory.bin'  # data storage file
objFile = None  # file object

lstTbl.append(dicRow)


# -- PROCESSING -- #
# TODOne add functions for processing here
# menu = '[1] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory [d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n' 

# # def print_menu():
# def print_menu(menu):
#     return menu   

# def menu_choice():
#     return int(input('Please enter a menu choice: '))

# @staticmethod
# def add_append(strID, strTitle, stArtist):
#         """This function appends the information take from DataProcessor. input_user(strFileName, lstTbl)
#         then uses it to append dicrRow
#          Args:
#             dicRow: dictionary row.
#             Table (List of dicts)
#          Returns:
#              None
            
#         """
#         strID = input('Enter an ID: ')
#         strTitle = input('Enter the CD\'s Title: ')
#         strArtist = input('Enter the Artist\'s Name: ')
#         intID = int(strID)
#         dicRow1 = {'id': intID, 'Title': strTitle, 'Artist': strArtist}
#         lstTbl.append(dicRow1)

class DataProcessor:
    class Error(Exception):
        """Base class for other exception"""
        pass 
    @staticmethod
    def add_to_inventory(strID, strTitle, stArtist, table):
        """
            Add an entry to inventory
        """
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        table.append(dicRow)
        if intID < 0:
         raise Exception(print('Value too small, try again'))
                                          
    @staticmethod
    def remove_from_inventory(id_to_remove, table):
        """
            Remove an entry from inventory
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == id_to_remove:
                del table[intRowNr]
                blnCDRemoved = True
                break

        return blnCDRemoved


class FileProcessor:
    """Processing the data to and from text file"""
  
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'rb') as objFile:
            data = pickle.load(objFile)
        return data 
        table.clear()  # this clears existing data and allows to load data from file
        # objFile = open(strFileName, 'r')
        objFile = open(file_name, 'rb')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    # def write_file(strFileName, lstTbl):
    def write_file(StrFile_name, lstTbl):
        """Function to write the contents of a file to disk
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(StrFile_name, 'wb') as objFile:
            pickle.dump(objFile)
        # TODOne Add code here
        # objFile = open(strFileName, 'w')
        objFile = open(StrFile_name, 'wb')
        # for row in lstTbl:
        for row in lstTbl:
            strRow = "{},{},{}".format(row['ID'], row['Title'], row['Artist']) + '\n'
            objFile.write(strRow)
        objFile.close()

        # objFile = open(strFileName, 'w')
        # for row in lstTbl:
        #     lstValues = list(row.values())
        #     lstValues[0] = str(lstValues[0])
        #     objFile.write(','.join(lstValues) + '\n')
        # objFile.close()

     
# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
   
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def get_cd_input():
        # TODOne move IO code into function
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()

        return strID, strTitle, stArtist
        
    # TODOne add I/O functions as needed

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
 # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        str_id, str_title, str_artist = IO.get_cd_input()

        # 3.3.2 Add item to the table
        # TODOne move processing code into function
        DataProcessor.add_to_inventory(str_id, str_title, str_artist, lstTbl)

        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # TODOne move processing code into function
        was_cd_removed = DataProcessor.remove_from_inventory(intIDDel, lstTbl)

        if was_cd_removed:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODOne move processing code into function
            FileProcessor.write_file(strFileName, lstTbl)

        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
