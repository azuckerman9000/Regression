import urllib.request
from optparse import OptionParser
import re

parser = OptionParser()
parser.add_option("-q", "--queue", dest="queuename")
parser.add_option("-o", "--operation", dest="operationname")
parser.add_option("-v", "--value", dest="value")
parser.add_option("-c", "--CaptureState", dest="capturestate")
(options, args) = parser.parse_args()

if options.queuename == 'fb':
	options.queuename = 'fullBatch'
elif options.queuename == 'tb':
	options.queuename = 'timedBatch'
elif options.queuename == 'gb':
	options.queuename = 'getBatchResponse'
	
if options.value == '.18':
	options.value = 'PTLS_IppfServiceId=\'4CDF800011\''
elif options.value == '.16':
	options.value = 'PTLS_IppfServiceId=\'1845100011\''
	

if options.operationname == 's':	
	options.operationname = 'send'
elif options.operationname == 'ss':	
	options.operationname = 'setStatus'
elif options.operationname == 'rs':	
	options.operationname = 'reSend'

if options.capturestate == 'bs':
	options.capturestate = 'BatchSent'
elif options.capturestate == 'c':
	options.capturestate = 'Captured'
elif options.capturestate == 'cd':
	options.capturestate = 'CaptureDeclined'
elif options.capturestate == 'ce':
	options.capturestate = 'CaptureError'
elif options.capturestate == 'cu':
	options.capturestate = 'CaptureUnknown'

	
url = ''

if options.operationname == 'send' and options.queuename == 'timedBatch':		
	url = 'http://ipc-393-pstg-05/BMS/' + options.queuename + '/' + options.operationname + '?selector=' + options.value
elif options.operationname == 'reSend' and options.queuename != 'timedBatch':
	url = 'http://ipc-393-pstg-05/BMS/' + options.queuename + '/' + options.operationname + '?batchKey=' + options.value
elif options.operationname == 'setStatus' and options.queuename != 'timedBatch' and options.capturestate:
	url = 'http://ipc-393-pstg-05/BMS/' + options.queuename + '/' + options.operationname + '?batchKey=' + options.value + '&captureState=' + options.capturestate
else:
	print('\ninvalid inputs')
	

print('\nUrl = ' + url)
f = urllib.request.urlopen(url)
obj = f.read()
pat1 = re.compile('(<IsSuccess>)(.*)(</IsSuccess>)')
pat2 = re.compile('(<Message>)(.*)(</Message>)')
status = pat1.search(str(obj))
message = pat2.search(str(obj))
print('Success = ' + status.group(2) + '\nMessage = ' + message.group(2))
