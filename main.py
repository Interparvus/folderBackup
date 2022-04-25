from copy import copy
from datetime import date
from shutil import copyfile


fileBackupDate = date.today()
fileBackup = str(fileBackupDate).replace("-",",")

input = r"C:/Users/admin/OneDrive - Gymnazium/Pracovnáplocha/folderBackup/folderOriginal"
output = r"C:/Users/admin/OneDrive - Gymnazium/Pracovná plocha/folderBackup/folderOriginalBackup" + fileBackup 
copyfile(input,output)