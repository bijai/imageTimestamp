import PySimpleGUI as sg
from pyTimestamp import writeTimeStamp
import os
from os import path
import time
from datetime import datetime
import subprocess

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])


if __name__ == "__main__":


    folderName = sg.popup_get_folder('Enter the folder you wish to process')
    outputFolderName = f"output_{round(time.time())}"

    filelist = os.listdir(folderName)
    #print(filelist)
    imageFileList = [ x for x in filelist if x.lower().endswith('.jpg') or x.lower().endswith('.jpeg')]
    print(imageFileList)
    sg.popup(f'{len(imageFileList)} images found')
    os.makedirs(path.join(folderName,outputFolderName))
    try:
        for image in imageFileList:
            writeTimeStamp(path.join(folderName,image),datetime.now(),path.join(folderName,outputFolderName))
        explore(path.join(folderName,outputFolderName))
    except Exception as e:
        print(e)
        sg.popup_error_with_traceback("Error")
    

    
