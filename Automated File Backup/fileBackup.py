import os
import shutil
import datetime
import schedule
import time

source_dir = "C:\\Users\\xyz\\Documents\\folder1" #The file you want to backup
destination_dir = "C:\\Users\\xyz\\Documents\\Backups" #The destination you want to backup to

def copy_folder_to_directory(source, dest):
    today = datetime.date.today() #Gives the current date
    dest_dir = os.path.join(dest, str(today)) #Creates the backup in directory with folders being labelled based on the date today
    
    try:
        shutil.copytree(source, dest_dir) #Copytree copies everything recursively and anything in the file
        print(f"The folder has been copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in the destination: {dest}")
        
#This inline/anonymous function will schedule to backup the folders at a specific time
schedule.every().day.at("19:00").do(lambda: copy_folder_to_directory(source_dir,destination_dir))       
        
while True:
    schedule.run_pending() #Allows for the line above to actually schedule the backup/checks for schedules that havent been run
    time.sleep(60)