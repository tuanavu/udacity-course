
# coding: utf-8

# In[10]:

## Show video after a break time
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("http://www.youtube.com/watch?v=nfWlot6h_JM")
    break_count = break_count + 1


# In[1]:

# Change file names

import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\temp\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+ saved_path)
    os.chdir(r"C:\temp\prank")
    
    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name -"+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()


# In[8]:



