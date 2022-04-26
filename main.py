
from datetime import date
from distutils.dir_util import copy_tree


fileBackupDate = date.today()
fileBackup = str(fileBackupDate).replace("-",",")

input = r"C:/Users/admin/schecter/Pracovná plocha/folderBackup/original"
output = r"C:/Users/admin/schecter/Pracovná plocha/folderBackup/backup/" + fileBackup


copy_tree(input,output)
