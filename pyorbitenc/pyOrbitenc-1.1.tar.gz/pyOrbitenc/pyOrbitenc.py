
# crcker911181
# developed by cracker911181

import base64

def encryptionFirst(variabler):
	encChar = {"A":"AAh", "B":"Aaf", "C":"B19", "D":"Ag9", "E":"Q1v", "F":"d1k", "G":"f22", "H":"gs0", "I":"x4p", "J":"c7t", "K":"i1m", "L":"bb0", "M":"bft", "N":"kus", "O":"2vx", "P":"hnb", "Q":"dyf", "R":"d8b", "S":"jCd", "T":"m4s", "U":"d5b", "V":"nn3", "W":"hch", "X":"vt2", "Y":"d6h", "Z":"fh1", "a":"t9I", "b":"xk2", "c":"cc0", "d":"kx9", "e":"flf", "f":"5pk", "g":"m18", "h":"62v", "i":"9c1", "j":"tx5", "k":"4kp", "l":"K5c", "m":"jys", "n":"ma9", "o":"cvx", "p":"yqt", "q":"anr", "r":"cr3", "s":"n81", "t":"a0c", "u":"fwd", "v":"g6a", "w":"5dr", "x":"y9c", "y":"8tc", "z":"52v", "0":"k5i", "1":"lcv", "2":"mvg", "3":"kv2", "4":"c9s", "5":"y3g", "6":"0an", "7":"4mh", "8":"lkc", "9":"bOf", "+":"jLf", "/":"vMm", "=":"mtc"}
	
	decCharList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","+","/","="]
	
	encFistAll = ""
	encLastCharAll = ""
	
	variable = variabler.encode('utf-8')
	b64encoded = (base64.b64encode(variable)).decode('utf-8')
	
	encSplit = [*b64encoded]
	
	for char in encSplit:
		encFist = str((str(encChar[char]))[0:2])
		encLastChar = str((str(encChar[char]))[2])
		
		encFistAll = encFistAll+encFist
		encLastCharAll = encLastCharAll+encLastChar
	
	
	encodeAll = encFistAll+"gfG"+encLastCharAll
	
	return (encodeAll)



def encode(variabler):
	try:
		main =('try:	import pyOrbitenc;\nexcept:	import os; os.system("pip install pyOrbitenc");\nimport pyOrbitenc \npyOrbitenc.exicute("'+encryptionFirst(variabler)+'")')
		return main
		
		
	except:
		print("Something maybe wrong")
		




def decAndExec(variabler):
	
	encChar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/", "="]
	
	decChar = {"AAh":"A", "Aaf":"B", "B19":"C", "Ag9":"D", "Q1v":"E", "d1k":"F", "f22":"G", "gs0":"H", "x4p":"I", "c7t":"J", "i1m":"K", "bb0":"L", "bft":"M", "kus":"N", "2vx":"O", "hnb":"P", "dyf":"Q", "d8b":"R", "jCd":"S", "m4s":"T", "d5b":"U", "nn3":"V", "hch":"W", "vt2":"X", "d6h":"Y", "fh1":"Z", "t9I":"a", "xk2":"b", "cc0":"c", "kx9":"d", "flf":"e", "5pk":"f", "m18":"g", "62v":"h", "9c1":"i", "tx5":"j", "4kp":"k", "K5c":"l", "jys":"m", "ma9":"n", "cvx":"o", "yqt":"p", "anr":"q", "cr3":"r", "n81":"s", "a0c":"t", "fwd":"u", "g6a":"v", "5dr":"w", "y9c":"x", "8tc":"y", "52v":"z", "k5i":"0", "lcv":"1", "mvg":"2", "kv2":"3", "c9s":"4", "y3g":"5", "0an":"6", "4mh":"7", "lkc":"8", "bOf":"9", "jLf":"+", "vMm":"/", "mtc":"="}
	
	
	variablerSplit = variabler.split("gfG")

	variableSplit1 = [*(variablerSplit[0])]
	
	variableSplit2 = [*(variablerSplit[1])]
	
	count = 0
	
	decodeAll = ''
	
	base64All = ''
	
	
	for cunt in range(len(variableSplit2)):
		decode1Char = str(str(variableSplit1[count])+str(variableSplit1[count+1]))
		
		decode2Char = str(variableSplit2[cunt])
		
		decodeChar = decode1Char+decode2Char
		decodeAll = decodeAll + decodeChar
		
			
		count=count+(2)
	
	
	count2 = 0
	for cnt in range(len(variableSplit2)):
		decoderToBase64 = str(decodeAll[count2:count2+3])
		
		decodedToBase64 = decChar[decoderToBase64]
		
		base64All = base64All+decodedToBase64
		count2=count2+(3)
		
		
	
	mainer = base64.b64decode(base64All.encode('utf-8'))
	
	main = mainer.decode('utf-8')
	
	
	
	try:
		exec(main)
	except Exception as e:
		print("Your Code error: "+str(e))


#DEVELOPED BY CRACKER911181

def exicute(variabler):
	try:
		decAndExec(variabler)
	except Exception as e:
		print("Maybe Encoded Data was Invalid")
		

# CRACKER911181
