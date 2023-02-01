# alac 5 - c extension library
import cython
import pyximport; pyximport.install()
import os
import sys
from io import StringIO
import glob
import re
import xlrd
import openpyxl
from math import floor
import datetime
import pandas as pd
import numpy as np
import PyPDF2 as pdfs


def getPDFText(path: str) -> str:
	text = ""
	pdf = pdfs.PdfReader(path)
	for pg in pdf.pages:
		text += pg.extract_text() + "\n"
	return str(text)

def getCaseInfo(text: str):
	case_num = ""
	name = ""
	alias = ""
	race = ""
	sex = ""
	address = ""
	dob = ""
	phone = ""

	try:
		county: str = re.search(r'(?:County\: )(\d{2})(?:Case)', str(text)).group(1).strip()
		case_num: str = county + "-" + re.search(r'(\w{2}\-\d{4}-\d{6}.\d{2})', str(text)).group(1).strip() 
	except (IndexError, AttributeError):
		pass

	try:
		name = re.search(r'(?: V. )(.*?)(?:Case)', str(text)).group().replace(" V. ","").replace("Case","").strip()
		alias = re.search(r'(?:Alias 1:){1}(.*)', str(text), re.MULTILINE).group().replace("Alias 1:","").strip()
	except (IndexError, AttributeError):
		try:
			namematch = re.search(r'(?:Name){1}(.{0,50}?)(?:Alias 1:){1}(.*)', str(text), re.MULTILINE).group()
			name: str = namematch.split(" Alias")[0].replace("Name: ","").strip()
			alias: str = namematch.split(" Alias 1: ")[1].replace("Alias 2:","").strip()
		except (IndexError, AttributeError):
			name = ""
			alias = ""


	try:
		dob: str = re.search(r'(\d{2}/\d{2}/\d{4})(?:.{0,5}DOB\:)', str(text), re.DOTALL).group(1)
		phone: str = re.search(r'(?:Phone\:)(.*?)(?:Country)', str(text), re.DOTALL).group(1).strip()
	except (IndexError, AttributeError):
		dob = ""
		phone = ""
	try:
		racesex = re.search(r'(B|W|H|A)\/(F|M)(?:Alias|XXX)', str(text))
		race = racesex.group(1).strip()
		sex = racesex.group(2).strip()
	except (IndexError, AttributeError):
		pass
	try:
		street_addr = re.search(r'(?:Address 1\:)(.+)', str(text), re.MULTILINE).group(1).strip()
		zip_code = re.search(r'(?:Zip\: ).+', str(text), re.MULTILINE).group().strip()
		city = re.search(r'(?:City\: ).*(?:State\: ).*', str(text), re.MULTILINE).group(1).strip()
		state = re.search(r'(?:City\: ).*(?:State\: ).*', str(text), re.MULTILINE).group(2).strip()
		address = street_addr + "	" + city + ", " + state + " " + zip_code
	except(IndexError, AttributeError):
		pass
	case = [
		case_num,
		name,
		alias,
		dob,
		race,
		sex,
		address,
		phone
		]

	return case

def getFeeSheet(text: str):
	actives = re.findall(r'(ACTIVE.*\$.*)', str(text))
	rind = range(0, len(actives))
	fees = pd.DataFrame({'Rows':actives},index=rind)
	try:
		totalrow = re.findall(r'(Total.*\$.*)', str(text), re.MULTILINE)[0]
		tbal = totalrow.split("$")[1].strip().replace("Total: $","").replace(",","").replace(" ","")
		tdue = totalrow.split("$")[3].strip().replace("$","").replace(",","").replace(" ","")
	except IndexError:
		totalrow = ""
		tbal = ""
		tdue = ""

	fees['SRows'] = fees['Rows'].map(lambda x: x.strip().split(" "))
	fees['DRows'] = fees['Rows'].map(lambda x: x.replace(",","").split("$"))
	fees['Code'] = fees['SRows'].map(lambda x: x[5] if len(x)>2 else "")
	fees['Payor'] = fees['SRows'].map(lambda x: x[6] if len(x)>3 else "")
	fees['AmtDue'] = fees['DRows'].map(lambda x: x[-1] if len(x)>1 else "")
	fees['AmtPaid'] = fees['DRows'].map(lambda x: x[2] if len(x)>2 else "")
	fees['Balance'] = fees['DRows'].map(lambda x: x[1] if len(x)>3 else "")
	fees['AmtHold'] = fees['DRows'].map(lambda x: x[3] if len(x)>4 else "")

	try:
		d999 = fees['Balance'][fees.Code == "D999"]
	except (TypeError, IndexError):
		d999 = ""

	owe_codes = " ".join(fees['Code'][fees.Balance.str.len() > 1])
	codes = " ".join(fees['Code'])
	allrows = []
	allrows.append(actives)
	allrows.append(totalrow)
	return [tdue, tbal, d999, owe_codes, codes, allrows]

def getCharges(text: str):
	# get all charges matches
	c = re.findall(r'(\d{3}\s{1}.{1,100}?.{3}-.{3}-.{3}.{1,100})', str(text), re.MULTILINE)
	cind = range(0, len(c))
	charges = pd.DataFrame({'Charges': c},index=cind)
	charges['Charges'] = charges['Charges'].map(lambda x: x.strip().replace("\n",""))
	# find table fields
	split_charges = charges['Charges'].map(lambda x: x.split(" "))
	charges['Num'] = split_charges.map(lambda x: x[0].strip())
	charges['Code'] = split_charges.map(lambda x: x[1].strip())
	charges['Felony'] = charges['Charges'].map(lambda x: bool(re.search(r'FELONY',x)))
	charges['Conviction'] = charges['Charges'].map(lambda x: bool(re.search(r'GUILTY|CONVICTED',x)))
	charges['VRRexception'] = charges['Charges'].map(lambda x: bool(re.search(r'(A ATT|ATTEMPT|S SOLICIT|CONSP)',x)))
	charges['CERVCode'] = charges['Code'].map(lambda x: bool(re.search(r'(OSUA|EGUA|MAN1|MAN2|MANS|ASS1|ASS2|KID1|KID2|HUT1|HUT2|BUR1|BUR2|TOP1|TOP2|TPCS|TPCD|TPC1|TET2|TOD2|ROB1|ROB2|ROB3|FOR1|FOR2|FR2D|MIOB|TRAK|TRAG|VDRU|VDRY|TRAO|TRFT|TRMA|TROP|CHAB|WABC|ACHA|ACAL)', x)))
	charges['PardonCode'] = charges['Code'].map(lambda x: bool(re.search(r'(RAP1|RAP2|SOD1|SOD2|STSA|SXA1|SXA2|ECHI|SX12|CSSC|FTCS|MURD|MRDI|MURR|FMUR|PMIO|POBM|MIPR|POMA|INCE)', x)))
	charges['PermanentCode'] = charges['Code'].map(lambda x: bool(re.search(r'(CM\d\d|CMUR)', x)))
	charges['CERV'] = charges.index.map(lambda x: charges['CERVCode'][x] == True and charges['VRRexception'][x] == False and charges['Felony'][x] == True)
	charges['Pardon'] = charges.index.map(lambda x: charges['PardonCode'][x] == True and charges['VRRexception'][x] == False and charges['Felony'][x] == True)
	charges['Permanent'] = charges.index.map(lambda x: charges['PermanentCode'][x] == True and charges['VRRexception'][x] == False and charges['Felony'][x] == True)
	charges['Disposition'] = charges['Charges'].map(lambda x: bool(re.search(r'\d{2}/\d{2}/\d{4}', x)))
	charges['CourtActionDate'] = charges['Charges'].map(lambda x: re.search(r'\d{2}/\d{2}/\d{4}', x).group() if bool(re.search(r'\d{2}/\d{2}/\d{4}', x)) else "")
	charges['CourtAction'] = charges['Charges'].map(lambda x: re.search(r'(BOUND|GUILTY PLEA|PROBATION|WAIVED|DISMISSED|TIME LAPSED|NOL PROSS|CONVICTED|INDICTED|OTHER|DISMISSED|FORFEITURE|TRANSFER|REMANDED|PROBATION|ACQUITTED|WITHDRAWN|PETITION|PRETRIAL|COND\. FORF\.)', x).group() if bool(re.search(r'(BOUND|GUILTY PLEA|PROBATION|WAIVED|DISMISSED|TIME LAPSED|NOL PROSS|CONVICTED|INDICTED|OTHER|DISMISSED|FORFEITURE|TRANSFER|REMANDED|PROBATION|ACQUITTED|WITHDRAWN|PETITION|PRETRIAL|COND\. FORF\.)', x)) else "")
	charges['Cite'] = charges['Charges'].map(lambda x: re.search(r'([^\s]{3}-[^\s]{3}-[^\s]{3}[^s]{0,3}?\)*)', x).group() if bool(re.search(r'([^\s]{3}-[^\s]{3}-[^\s]{3}[^s]{0,3}?\)*)', x)) else re.search(r'(.{3}-.{3}-)',x).group())
	charges['TypeDescription'] = charges['Charges'].map(lambda x: re.search(r'(BOND|FELONY|MISDEMEANOR|OTHER|TRAFFIC|VIOLATION)', x).group() if bool(re.search(r'(BOND|FELONY|MISDEMEANOR|OTHER|TRAFFIC|VIOLATION)', x)) else "")
	charges['Category'] = charges['Charges'].map(lambda x: re.search(r'(ALCOHOL|BOND|CONSERVATION|DOCKET|DRUG|GOVERNMENT|HEALTH|MUNICIPAL|OTHER|PERSONAL|PROPERTY|SEX|TRAFFIC)', x).group() if bool(re.search(r'(ALCOHOL|BOND|CONSERVATION|DOCKET|DRUG|GOVERNMENT|HEALTH|MUNICIPAL|OTHER|PERSONAL|PROPERTY|SEX|TRAFFIC)', x)) else "")
	charges['Description'] = charges.index.map(lambda x: charges['Charges'][x].replace(charges['Code'][x],"").replace(charges['Cite'][x],"").replace(charges['Category'][x],"").replace(charges['TypeDescription'][x],"").replace(charges['Num'][x],"").replace(charges['CourtAction'][x],"").replace(charges['CourtActionDate'][x],"").strip())

	# charges.drop(columns=['PardonCode','PermanentCode','CERVCode','VRRexception'], inplace=True)

	# counts
	conviction_ct = charges[charges.Conviction == True].shape[0]
	charge_ct = charges.shape[0]
	cerv_ct = charges[charges.CERV == True].shape[0]
	pardon_ct = charges[charges.Pardon == True].shape[0]
	perm_ct = charges[charges.Permanent == True].shape[0]
	conv_cerv_ct = charges[charges.CERV == True][charges.Conviction == True].shape[0]
	conv_pardon_ct = charges[charges.Pardon == True][charges.Conviction == True].shape[0]
	conv_perm_ct = charges[charges.Permanent == True][charges.Conviction == True].shape[0]

	# summary strings
	convictions = "; ".join(charges[charges.Conviction == True]['Charges'].tolist())
	dcharges = "; ".join(charges[charges.Disposition == True]['Charges'].tolist())
	fcharges = "; ".join(charges[charges.Disposition == False]['Charges'].tolist())
	cerv_convictions = "; ".join(charges[charges.CERV == True][charges.Conviction == True]['Charges'].tolist())
	pardon_convictions = "; ".join(charges[charges.Pardon == True][charges.Conviction == True]['Charges'].tolist())
	perm_convictions = "; ".join(charges[charges.Permanent == True][charges.Conviction == True]['Charges'].tolist())

	return [convictions, dcharges, fcharges, cerv_convictions, pardon_convictions, perm_convictions, conviction_ct, charge_ct, cerv_ct, pardon_ct, perm_ct, conv_cerv_ct, conv_pardon_ct, conv_perm_ct]




