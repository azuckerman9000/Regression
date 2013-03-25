import re
from optparse import OptionParser

EMD = open("\\\\ipc-393-pstg-05\\D$\\ipcadmin\\FTP\\'FTIPCO01'\\TBC.TF01.R0BCRIPC", 'r', encoding="utf-8")
ECHO = open("\\\\ipc-393-pstg-05\\D$\\ipcadmin\\FTP\\'FTIPCO01'\\TBC.FF01.P0BCRIP1", 'r+', encoding="utf-8")
ECHOA = open("\\\\ipc-393-pstg-05\\D$\\ipcadmin\\FTP\\'FAIPCO01'\\TBC.FF01.P0BCRIP1.G0002V00", 'r+', encoding="utf-8")

parser = OptionParser()
parser.add_option("-a", action="store_true", default=False, dest="archive")
(options, args) = parser.parse_args()

EMDline = EMD.readline()
NewFileSubNo = EMDline[37:47]
print('\nNew EMD File Submission Number = ', NewFileSubNo)
print(EMDline)

ECHOline = ''
if options.archive == False:
	ECHOline = ECHO.readline()
elif options.archive == True:
	ECHOline = ECHOA.readline()	
OldFileSubNo = ECHOline[44:54]
print('Old ECHO file Submission Number = ', OldFileSubNo)
print(ECHOline)

if options.archive == False:
	ECHO.seek(0,0)
	ECHO.write(ECHOline.replace(OldFileSubNo, NewFileSubNo))
	ECHO.seek(0,0)
	print('New ECHO line = ', ECHO.readline())
elif options.archive == True:
	ECHOA.seek(0,0)
	ECHOA.write(ECHOline.replace(OldFileSubNo, NewFileSubNo))
	ECHOA.seek(0,0)
	print('New Archive ECHO line = ', ECHOA.readline())
EMD.close()
ECHO.close()
ECHOA.close()