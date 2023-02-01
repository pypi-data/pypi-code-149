# alacorder beta 0.4.9

# CLI to set these variables - CLI asks mode, batch size, in_path, out_path, print_log
#	4 modes:
#	* fast-pdf-table:				get PDF page one, getCaseInfo() map, (ADD OG CHARGE AND COURT ACTIONS)
#	* make-archive:					get all PDF pages, append case number to filename, print to .txt
#	* slow-pdf-table:				get all PDF pages, process case info, charges, fees into xls
#	* tables-from-archive: 			get PDF text from directory, run write_all without pdfplumber
from alacorder import alacorder4c as alac
import pandas as pd
import glob
import re
import numpy as np
import time
import math


in_dir = ""
outp = ""
read = 0
tot_batches = 0
case_max = 0
batch = 0
plog = True
batches = pd.DataFrame()
bsize = 0

def start(in_path, out_path, mode, batch_size=10, print_log=True):

	global in_dir
	global outp
	global batch
	global read
	global plog
	global case_max
	global tot_batches
	global batches
	global bsize
	bsize = batch_size
	plog = print_log
	in_dir = in_path
	outp = out_path
	contents = pd.DataFrame()
	out_ext: str = out_path.split(".")[-1].strip()
	in_ext: str = in_path.split(".")[-1].strip() if len(in_path.split(".")[-1])<5 else "directory"
	# read directory
	if mode == "fast-pdf-table" or mode == "make-archive" or mode == "slow-pdf-table" or mode == "pypdf2-test":
		contents['Path'] = glob.glob(in_dir + '**/*.pdf', recursive=True) # get all files

	# read archive
	elif mode == "tables-from-archive":
		if in_ext == "pkl":
			contents = pd.read_pickle(in_dir)
		if in_ext == "xls":
			contents = pd.read_excel(in_dir, "text_from_pdf",names=['Path','AllPagesText'])
		if in_ext == "json":
			contents = pd.read_json(in_dir)
		if in_ext == "csv":
			contents = pd.read_csv(in_dir, escapechar='\\')
	else:
		raise Exception(f"'mode' attribute must be 'fast-pdf-table', 'make-archive', 'slow-pdf-table', 'tables-from-archive'") 
	if len(contents) == 0:
		raise Exception(f"No cases found!")

	case_max = contents.shape[0]
	batches = np.array_split(contents, case_max / batch_size)
	tot_batches = len(batches)
	print(batches)
	
	# Print initial details: total exports, batch size, mode 

	if mode == "fast-pdf-table":
		fastCaseInfoFromPDFBulk(in_ext, out_ext)
	if mode == "make-archive":
		makeArchive(in_ext, out_ext)
	if mode == "tables-from-archive":
		makeTablesFromArchive(in_ext, out_ext)
	if mode == "slow-pdf-table":
		makeTablesFromPDFs(in_ext, out_ext)
	if mode == "pypdf2-test":
		pyPDFArchiveTest(in_ext, out_ext)


def console_log(tostr=""):
	exported = batch * bsize
	if plog == True:
		print(tostr)
		print(f'''
	    ___    __                          __         
	   /   |  / /___ __________  _________/ /__  _____
	  / /| | / / __ `/ ___/ __ \\/ ___/ __  / _ \\/ ___/
	 / ___ |/ / /_/ / /__/ /_/ / /  / /_/ /  __/ /    
	/_/  |_/_/\\__,_/\\___/\\____/_/   \\__,_/\\___/_/     
																																											
		
		ALACORDER 0.4.9
		by Sam Robson	

		Searching {in_dir} 
		Writing to {outp} 

		Exported {exported} of {case_max}

	''') 

	if plog == False:
		print(f'''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
		    ___    __                          __         
		   /   |  / /___ __________  _________/ /__  _____
		  / /| | / / __ `/ ___/ __ \\/ ___/ __  / _ \\/ ___/
		 / ___ |/ / /_/ / /__/ /_/ / /  / /_/ /  __/ /    
		/_/  |_/_/\\__,_/\\___/\\____/_/   \\__,_/\\___/_/     
																																												
			
			ALACORDER 0.4.9
			by Sam Robson	

			Searching {in_dir} 
			Writing to {outp} 

			Exported {exported} of {case_max}

		''') 

## BATCH WRITER FUNCTIONS
#  Each corresponds to a different mode - add more modes and settings via start()
#  Only one mode runs at a time
#  Process cases, print logs, concat to global, write to xls

# in_exts: directory, (pdf)
# out_exts: xls, pkl, json, csv

def pyPDFArchiveTest(in_ext, out_ext):
	global batches
	global batch
	outputs = pd.DataFrame()
	if in_ext == "directory":
		for b in batches:
			# get all pages, add to all df, write to pickle
			b['AllPagesText'] = b['Path'].map(lambda x: str(alac.getPDFTextExperimental(x)))
			b['Timestamp'] = time.time()
			outputs = pd.concat([outputs, b],ignore_index=False)
			batch += 1
			outputs.fillna('',inplace=True)
			if out_ext == "xls":
				with pd.ExcelWriter(outp) as writer:
					outputs.to_excel(writer, sheet_name="text_from_pdf")
			elif out_ext == "pkl":
				outputs.to_pickle(outp)
			elif out_ext == "json":
				outputs.to_json(outp)
			elif out_ext == "csv":
				outputs.to_csv(outp,escapechar='\\')
			else:
				raise Exception("Output file extension not supported! Must output to xls, .pkl, .json, or .csv")
			console_log()
	else:
		raise Exception("Input path not supported! Must include full path to directory of PDF cases")

def fastCaseInfoFromPDF(in_ext, out_ext):
	global batches
	global batch
	outputs = pd.DataFrame()
	if in_ext == "directory":
		for b in batches:
			# get page one info
			b['PgOneText'] = b['Path'].map(lambda x: alac.getPgOneText(x))
			b['FastCaseInfo'] = b['PgOneText'].map(lambda x: alac.getFastCaseInfo(x))
			b['CaseNumber'] = b['FastCaseInfo'].map(lambda x: x[0])
			b['Name'] = b['FastCaseInfo'].map(lambda x: x[1])
			b['Alias'] = b['FastCaseInfo'].map(lambda x: x[2])
			b['DOB'] = b['FastCaseInfo'].map(lambda x: x[3])
			b['Race'] = b['FastCaseInfo'].map(lambda x: x[4])
			b['Sex'] = b['FastCaseInfo'].map(lambda x: x[5])
			b['Address'] = b['FastCaseInfo'].map(lambda x: x[6])
			b['Phone'] = b['FastCaseInfo'].map(lambda x: x[7])

			# concat with all batches, clean, log
			b.drop(columns=['PgOneText','FastCaseInfo'],inplace=True)
			outputs = pd.concat([outputs, b],ignore_index=False)
			outputs.fillna('',inplace=True)
			console_log(outputs.to_string(columns=['CaseNumber','Name','DOB','Race','Sex']))
			# write 
			if out_ext == "xls":
				with pd.ExcelWriter(outp) as writer:
					outputs.to_excel(writer, sheet_name="fast_pdf_info")
			elif out_ext == "pkl":
				outputs.to_pickle(outp)
			elif out_ext == "json":
				outputs.to_json(outp)
			elif out_ext == "csv":
				outputs.to_csv(outp,escapechar='\\')
			else:
				raise Exception("Output file extension not supported! Please output to .xls, .pkl, .json, or .csv")
		else:
			raise Exception("Input path not supported! Must include full path to directory of PDF cases")

def fastCaseInfoFromPDFBulk(in_ext, out_ext):
	global batches
	global batch
	outputs = pd.DataFrame()
	if in_ext == "directory":
		for b in batches:
			# get page one info
			b['PgOneText'] = b['Path'].map(lambda x: alac.getPgOneText(x))
			b['FastCaseInfo'] = b['PgOneText'].map(lambda x: alac.getFastCaseInfo(x))
			b['CaseNumber'] = b['FastCaseInfo'].map(lambda x: x[0])
			b['Name'] = b['FastCaseInfo'].map(lambda x: x[1])
			b['Alias'] = b['FastCaseInfo'].map(lambda x: x[2])
			b['DOB'] = b['FastCaseInfo'].map(lambda x: x[3])
			b['Race'] = b['FastCaseInfo'].map(lambda x: x[4])
			b['Sex'] = b['FastCaseInfo'].map(lambda x: x[5])
			b['Address'] = b['FastCaseInfo'].map(lambda x: x[6])
			b['Phone'] = b['FastCaseInfo'].map(lambda x: x[7])
			batch += 1
			# concat with all batches, clean, log
			b.drop(columns=['PgOneText','FastCaseInfo'],inplace=True)
			outputs = pd.concat([outputs, b],ignore_index=False)
			outputs.fillna('',inplace=True)
			console_log(outputs.to_string(columns=['CaseNumber','Name','DOB','Race','Sex']))
			# write 
			if out_ext == "xls":
				with pd.ExcelWriter(outp) as writer:
					outputs.to_excel(writer, sheet_name="fast_pdf_info")
			elif out_ext == "pkl":
				outputs.to_pickle(outp)
			elif out_ext == "json":
				outputs.to_json(outp)
			elif out_ext == "csv":
				outputs.to_csv(outp,escapechar='\\')
			else:
				raise Exception("Output file extension not supported! Please output to .xls, .pkl, .json, or .csv")
		else:
			raise Exception("Input path not supported! Must include full path to directory of PDF cases")
# in_exts: directory, (pdf)
# out_exts: xls, pkl, json, csv
def makeArchive(in_ext: str, out_ext: str):
	global batches
	global batch
	outputs = pd.DataFrame()
	if in_ext == "directory":
		for b in batches:
			# get all pages, add to all df, write to pickle
			b['AllPagesText'] = b['Path'].map(lambda x: str(alac.getPDFTextB(x)))
			b['Timestamp'] = time.time()
			outputs = pd.concat([outputs, b],ignore_index=False)
			batch += 1
			outputs.fillna('',inplace=True)
			if out_ext == "xls":
				with pd.ExcelWriter(outp) as writer:
					outputs.to_excel(writer, sheet_name="text_from_pdf")
			elif out_ext == "pkl":
				outputs.to_pickle(outp)
			elif out_ext == "json":
				outputs.to_json(outp)
			elif out_ext == "csv":
				outputs.to_csv(outp,escapechar='\\')
			else:
				raise Exception("Output file extension not supported! Must output to .xls, .pkl, .json, or .csv")
			console_log(outputs.to_string())
	else:
		raise Exception("Input path not supported! Must include full path to directory of PDF cases")

# in_exts: pkl, xls, json, csv
def makeTablesFromArchive(in_ext: str, out_ext: str):
	global batches
	global batch
	outputs = pd.DataFrame()
	if in_ext == "directory":
		raise Exception("Directories not supported in this mode!")
	else:
		for b in batches:
			b['FastCaseInfo'] = b['AllPagesText'].map(lambda x: alac.getFastCaseInfo(x))
			b['CaseNumber'] = b['FastCaseInfo'].map(lambda x: x[0])
			b['Name'] = b['FastCaseInfo'].map(lambda x: x[1])
			b['Alias'] = b['FastCaseInfo'].map(lambda x: x[2])
			b['DOB'] = b['FastCaseInfo'].map(lambda x: x[3])
			b['Race'] = b['FastCaseInfo'].map(lambda x: x[4])
			b['Sex'] = b['FastCaseInfo'].map(lambda x: x[5])
			b['Address'] = b['FastCaseInfo'].map(lambda x: x[6])
			b['Phone'] = b['FastCaseInfo'].map(lambda x: x[7])
			b['ChargesOutputs'] = b['AllPagesText'].map(lambda x: alac.getCharges(x))
			b['Convictions'] = b['ChargesOutputs'].map(lambda x: x[0])
			b['DispositionCharges'] = b['ChargesOutputs'].map(lambda x: x[1])
			b['FilingCharges'] = b['ChargesOutputs'].map(lambda x: x[2])
			b['CERVConvictions'] = b['ChargesOutputs'].map(lambda x: x[3])
			b['PardonConvictions'] = b['ChargesOutputs'].map(lambda x: x[4])
			b['PermanentConvictions'] = b['ChargesOutputs'].map(lambda x: x[5])
			b['ConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[6])
			b['ChargeCount'] = b['ChargesOutputs'].map(lambda x: x[7])
			b['CERVChargeCount'] = b['ChargesOutputs'].map(lambda x: x[8])
			b['PardonChargeCount'] = b['ChargesOutputs'].map(lambda x: x[9])
			b['PermanentChargeCount'] = b['ChargesOutputs'].map(lambda x: x[10])
			b['CERVConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[11])
			b['PardonConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[12])
			b['PermanentConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[13])
			b['FeeOutputs'] = b['AllPagesText'].map(lambda x: alac.getFeeSheet(x))
			b['TotalAmtDue'] = b['FeeOutputs'].map(lambda x: x[0])
			b['TotalBalance'] = b['FeeOutputs'].map(lambda x: x[1])
			b['TotalD999'] = b['FeeOutputs'].map(lambda x: x[2])
			b['FeeCodesOwed'] = b['FeeOutputs'].map(lambda x: x[3])
			b['FeeCodes'] = b['FeeOutputs'].map(lambda x: x[4])
			b['FeesTable'] = b['FeeOutputs'].map(lambda x: x[5])
			b['ChargesTable'] = b['ChargesOutputs'].map(lambda x: x[0])
			b['ChargesTable'] = b['ChargesOutputs'].map(lambda x: x[0])
			b.drop(columns=['AllPagesText','FastCaseInfo','ChargesOutputs','FeeOutputs','TotalD999','ChargesTable','FeesTable'],inplace=True)
			outputs = pd.concat([outputs, b],ignore_index=True)
			outputs.fillna('',inplace=True)
			batch += 1
			# console_log(outputs.to_string())

		# write 
		if out_ext == "xls":
			with pd.ExcelWriter(outp) as writer:
				outputs.to_excel(writer, sheet_name="tables-from-archive")
		elif out_ext == "pkl":
			outputs.to_pickle(outp)
		elif out_ext == "json":
			outputs.to_json(outp)
		elif out_ext == "csv":
			outputs.to_csv(outp,escapechar='\\')
		else:
			raise Exception("Output file extension not supported! Please output to .xls, .pkl, .json, or .csv")

def makeTablesFromPDFs(in_ext: str, out_ext: str):
	global batches
	global batch
	outputs = pd.DataFrame()
	for b in batches:
		b['AllPagesText'] = b['Path'].map(lambda x: alac.getPDFText(x))
		b['FastCaseInfo'] = b['AllPagesText'].map(lambda x: alac.getFastCaseInfo(x))
		b['CaseNumber'] = b['FastCaseInfo'].map(lambda x: x[0])
		b['Name'] = b['FastCaseInfo'].map(lambda x: x[1])
		b['Alias'] = b['FastCaseInfo'].map(lambda x: x[2])
		b['DOB'] = b['FastCaseInfo'].map(lambda x: x[3])
		b['Race'] = b['FastCaseInfo'].map(lambda x: x[4])
		b['Sex'] = b['FastCaseInfo'].map(lambda x: x[5])
		b['Address'] = b['FastCaseInfo'].map(lambda x: x[6])
		b['Phone'] = b['FastCaseInfo'].map(lambda x: x[7])
		b['ChargesOutputs'] = b['AllPagesText'].map(lambda x: alac.getCharges(x))
		b['Convictions'] = b['ChargesOutputs'].map(lambda x: x[0])
		b['DispositionCharges'] = b['ChargesOutputs'].map(lambda x: x[1])
		b['FilingCharges'] = b['ChargesOutputs'].map(lambda x: x[2])
		b['CERVConvictions'] = b['ChargesOutputs'].map(lambda x: x[3])
		b['PardonConvictions'] = b['ChargesOutputs'].map(lambda x: x[4])
		b['PermanentConvictions'] = b['ChargesOutputs'].map(lambda x: x[5])
		b['ConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[6])
		b['ChargeCount'] = b['ChargesOutputs'].map(lambda x: x[7])
		b['CERVChargeCount'] = b['ChargesOutputs'].map(lambda x: x[8])
		b['PardonChargeCount'] = b['ChargesOutputs'].map(lambda x: x[9])
		b['PermanentChargeCount'] = b['ChargesOutputs'].map(lambda x: x[10])
		b['CERVConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[11])
		b['PardonConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[12])
		b['PermanentConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[13])
		b['FeeOutputs'] = b['AllPagesText'].map(lambda x: alac.getFeeSheet(x))
		b['TotalAmtDue'] = b['FeeOutputs'].map(lambda x: x[0])
		b['TotalBalance'] = b['FeeOutputs'].map(lambda x: x[1])
		b['TotalD999'] = b['FeeOutputs'].map(lambda x: x[2])
		b['FeeCodesOwed'] = b['FeeOutputs'].map(lambda x: x[3])
		b['FeeCodes'] = b['FeeOutputs'].map(lambda x: x[4])
		b['FeesTable'] = b['FeeOutputs'].map(lambda x: x[5])
		b.drop(columns=['AllPagesText','FastCaseInfo','ChargesOutputs','FeeOutputs','TotalD999','FeesTable'],inplace=True)
		outputs = pd.concat([outputs, b],ignore_index=True)
		outputs.fillna('',inplace=True)
		batch += 1
		console_log(outputs[['CaseNumber','Name']].to_string())
		# write 
		if out_ext == "xls":
			with pd.ExcelWriter(outp) as writer:
				outputs.to_excel(writer, sheet_name="tables-from-archive")
		elif out_ext == "pkl":
			outputs.to_pickle(outp)
		elif out_ext == "json":
			outputs.to_json(outp)
		elif out_ext == "csv":
			outputs.to_csv(outp,escapechar='\\')
		else:
			raise Exception("Output file extension not supported! Please output to .xls, .pkl, .json, or .csv")
