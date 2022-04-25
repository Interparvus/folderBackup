
from datetime import date
from distutils.dir_util import copy_tree


fileBackupDate = date.today()
fileBackup = str(fileBackupDate).replace("-",",")

input = r"C:/Users/admin/OneDrive - Gymnazium/Pracovná plocha/folderBackup/folderOriginal"
output = r"C:/Users/admin/OneDrive - Gymnazium/Pracovná plocha/folderBackup/folderOriginalBackup" + fileBackup 


copy_tree(input,output)