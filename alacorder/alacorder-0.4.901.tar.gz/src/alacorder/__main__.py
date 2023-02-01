import cython
import pyximport; pyximport.install()
import pandas as pd
import glob
import re
import numpy as np
import os
import sys
from io import StringIO
import glob
import re
import xlrd
import openpyxl
import PyPDF2
from math import floor
from alacorder import alacorder4
from alacorder import alacorder4c as alac

print(f'''
		
	    ___    __                          __         
	   /   |  / /___ __________  _________/ /__  _____
	  / /| | / / __ `/ ___/ __ \\/ ___/ __  / _ \\/ ___/
	 / ___ |/ / /_/ / /__/ /_/ / /  / /_/ /  __/ /    
	/_/  |_/_/\\__,_/\\___/\\____/_/   \\__,_/\\___/_/     
																																														
		
		ALACORDER 0.4.9 beta
		by Sam Robson	



	Welcome to Alacorder. To start, please select an operating mode:

	A.	PDF directory to basic cases table (fast)

For a given folder, finds all PDFs and collects basic case details (case number, name, alias, dob, race, sex, address, phone). Supports export to .xls, .csv, .json, .pkl.

	B.	PDF directory to full text archive

For a given folder, finds all PDFs and collects text into archive table with full PDF text, collection timestamp, and file path columns. Supports export to .xls, .csv, .json, .pkl. Use .pkl for best performance.

	C.	Unpack archive to detailed cases table with charges and fees

Create detailed cases table with charge, fee, voting rights, and conviction information from a full text archive. Supports import from and export to .xls, .pkl, .json, .csv.

	D. 	PDF directory to detailed cases table with charges and fees (NOT RECOMMENDED)

INSTEAD, create full text archive to .pkl using operating mode B, then use mode C to unpack archive to detailed cases table. 

For a given folder, finds all PDFs and collects detailed case information with charge, fee, voting rights, and conviction information. Supports export to .xls, .pkl, .json, or .csv.

	E.	(EXPERIMENTAL) Alternative PDF parsing, operates in mode B.

Enter A, B, C, or D: ''')


mode = "".join(input()).strip()
if mode == 'A':
	mode = "fast-pdf-table"
elif mode == 'B':
	mode = "make-archive"
elif mode == 'C':
	mode = "tables-from-archive"
elif mode == 'D':
	mode = "slow-pdf-table"
elif mode == 'E':
	mode = "pypdf2-test"
else:
	raise Exception("Not a valid input.")

if mode == "fast-pdf-table" or mode == "slow-pdf-table" or mode == "make-archive" or mode == "pypdf2-test":
	print(f'''
Enter the directory in which you want Alacorder to search for PDFs. Include a forward slash after the folder title. ("just/like/this/")

PDF directory:
 ''')

if mode == "tables-from-archive":
	print(f'''
Enter the file path to the full text archive (.xls, .pkl, .json, .csv) you want Alacourt to process into a detailed cases table.

Enter path to full text archive:
 ''')

in_dir = "".join(input())


print(f'''
		
Enter output file path (.xls, .csv, .json, .pkl): 
''')

xpath = "".join(input())

print(f'''

Export in batches of: 
''')

batch_size = int("".join(input()))


print(f'''

Print log? [Y/N]: 
''')

log = True if "".join(input()) == "Y" else "N"

print(f'''


....................................


	''')

alacorder4.start(in_dir,xpath,mode,batch_size,log)
