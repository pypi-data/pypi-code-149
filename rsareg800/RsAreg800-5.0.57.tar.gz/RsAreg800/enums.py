from enum import Enum


# noinspection SpellCheckingInspection
class AregAttRcsKeepConst(Enum):
	"""2 Members, ATTenuation ... RCS"""
	ATTenuation = 0
	RCS = 1


# noinspection SpellCheckingInspection
class AregCableCorrSour(Enum):
	"""2 Members, S2P ... USER"""
	S2P = 0
	USER = 1


# noinspection SpellCheckingInspection
class AregCconfigBw(Enum):
	"""3 Members, BW1G ... BW5G"""
	BW1G = 0
	BW2G = 1
	BW5G = 2


# noinspection SpellCheckingInspection
class AregCconfigOptMode(Enum):
	"""2 Members, FAST ... QHIG"""
	FAST = 0
	QHIG = 1


# noinspection SpellCheckingInspection
class AregCconfigSystAlign(Enum):
	"""2 Members, OFF ... TABLe"""
	OFF = 0
	TABLe = 1


# noinspection SpellCheckingInspection
class AregChanMappingGui(Enum):
	"""70 Members, IFONly ... TRX4"""
	IFONly = 0
	NONE = 1
	QAT1CH1 = 2
	QAT1CH2 = 3
	QAT1CH3 = 4
	QAT1CH4 = 5
	QAT1CH5 = 6
	QAT1CH6 = 7
	QAT1CH7 = 8
	QAT1CH8 = 9
	QAT2CH1 = 10
	QAT2CH2 = 11
	QAT2CH3 = 12
	QAT2CH4 = 13
	QAT2CH5 = 14
	QAT2CH6 = 15
	QAT2CH7 = 16
	QAT2CH8 = 17
	QAT3CH1 = 18
	QAT3CH2 = 19
	QAT3CH3 = 20
	QAT3CH4 = 21
	QAT3CH5 = 22
	QAT3CH6 = 23
	QAT3CH7 = 24
	QAT3CH8 = 25
	QAT4CH1 = 26
	QAT4CH2 = 27
	QAT4CH3 = 28
	QAT4CH4 = 29
	QAT4CH5 = 30
	QAT4CH6 = 31
	QAT4CH7 = 32
	QAT4CH8 = 33
	QAT5CH1 = 34
	QAT5CH2 = 35
	QAT5CH3 = 36
	QAT5CH4 = 37
	QAT5CH5 = 38
	QAT5CH6 = 39
	QAT5CH7 = 40
	QAT5CH8 = 41
	QAT6CH1 = 42
	QAT6CH2 = 43
	QAT6CH3 = 44
	QAT6CH4 = 45
	QAT6CH5 = 46
	QAT6CH6 = 47
	QAT6CH7 = 48
	QAT6CH8 = 49
	QAT7CH1 = 50
	QAT7CH2 = 51
	QAT7CH3 = 52
	QAT7CH4 = 53
	QAT7CH5 = 54
	QAT7CH6 = 55
	QAT7CH7 = 56
	QAT7CH8 = 57
	QAT8CH1 = 58
	QAT8CH2 = 59
	QAT8CH3 = 60
	QAT8CH4 = 61
	QAT8CH5 = 62
	QAT8CH6 = 63
	QAT8CH7 = 64
	QAT8CH8 = 65
	TRX1 = 66
	TRX2 = 67
	TRX3 = 68
	TRX4 = 69


# noinspection SpellCheckingInspection
class AregChanMappingSensor(Enum):
	"""9 Members, NONE ... SEN8"""
	NONE = 0
	SEN1 = 1
	SEN2 = 2
	SEN3 = 3
	SEN4 = 4
	SEN5 = 5
	SEN6 = 6
	SEN7 = 7
	SEN8 = 8


# noinspection SpellCheckingInspection
class AregDopplerUnit(Enum):
	"""2 Members, FREQuency ... SPEed"""
	FREQuency = 0
	SPEed = 1


# noinspection SpellCheckingInspection
class AregDynLoggLevel(Enum):
	"""3 Members, ALL ... ERRor"""
	ALL = 0
	EAWarning = 1
	ERRor = 2


# noinspection SpellCheckingInspection
class AregDynLoggTimeBase(Enum):
	"""2 Members, SIMulation ... SYSTem"""
	SIMulation = 0
	SYSTem = 1


# noinspection SpellCheckingInspection
class AregFeQatConnMode(Enum):
	"""6 Members, CERRor ... UPDate"""
	CERRor = 0
	CONNected = 1
	DIALing = 2
	DISConnected = 3
	UERRor = 4
	UPDate = 5


# noinspection SpellCheckingInspection
class AregFeQatMode(Enum):
	"""2 Members, MULTi ... SINGle"""
	MULTi = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class AregFeType(Enum):
	"""3 Members, NONE ... TRX"""
	NONE = 0
	QAT = 1
	TRX = 2


# noinspection SpellCheckingInspection
class AregMeasPort(Enum):
	"""2 Members, AUX ... POW"""
	AUX = 0
	POW = 1


# noinspection SpellCheckingInspection
class AregMultiInstCnctStatus(Enum):
	"""5 Members, CERRor ... TDISconnecting"""
	CERRor = 0
	CONNected = 1
	DISConnected = 2
	TCONnencting = 3
	TDISconnecting = 4


# noinspection SpellCheckingInspection
class AregMultiInstMode(Enum):
	"""3 Members, OFF ... SECondary"""
	OFF = 0
	PRIMary = 1
	SECondary = 2


# noinspection SpellCheckingInspection
class AregPlEd(Enum):
	"""4 Members, ERRor ... WARNing"""
	ERRor = 0
	INACtive = 1
	OK = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class AregPowSens(Enum):
	"""5 Members, SEN1 ... UDEFined"""
	SEN1 = 0
	SEN2 = 1
	SEN3 = 2
	SEN4 = 3
	UDEFined = 4


# noinspection SpellCheckingInspection
class AregRadarPowIndicator(Enum):
	"""4 Members, BAD ... WEAK"""
	BAD = 0
	GOOD = 1
	OFF = 2
	WEAK = 3


# noinspection SpellCheckingInspection
class ByteOrder(Enum):
	"""2 Members, NORMal ... SWAPped"""
	NORMal = 0
	SWAPped = 1


# noinspection SpellCheckingInspection
class CalDataMode(Enum):
	"""2 Members, CUSTomer ... FACTory"""
	CUSTomer = 0
	FACTory = 1


# noinspection SpellCheckingInspection
class CalDataUpdate(Enum):
	"""6 Members, BBFRC ... RFFRC"""
	BBFRC = 0
	FREQuency = 1
	IALL = 2
	LEVel = 3
	LEVForced = 4
	RFFRC = 5


# noinspection SpellCheckingInspection
class Colour(Enum):
	"""4 Members, GREen ... YELLow"""
	GREen = 0
	NONE = 1
	RED = 2
	YELLow = 3


# noinspection SpellCheckingInspection
class DevExpFormat(Enum):
	"""4 Members, CGPRedefined ... XML"""
	CGPRedefined = 0
	CGUSer = 1
	SCPI = 2
	XML = 3


# noinspection SpellCheckingInspection
class DispKeybLockMode(Enum):
	"""5 Members, DISabled ... VNConly"""
	DISabled = 0
	DONLy = 1
	ENABled = 2
	TOFF = 3
	VNConly = 4


# noinspection SpellCheckingInspection
class ErFpowSensMapping(Enum):
	"""9 Members, SENS1 ... UNMapped"""
	SENS1 = 0
	SENS2 = 1
	SENS3 = 2
	SENS4 = 3
	SENSor1 = 4
	SENSor2 = 5
	SENSor3 = 6
	SENSor4 = 7
	UNMapped = 8


# noinspection SpellCheckingInspection
class FormData(Enum):
	"""2 Members, ASCii ... PACKed"""
	ASCii = 0
	PACKed = 1


# noinspection SpellCheckingInspection
class FormStatReg(Enum):
	"""4 Members, ASCii ... OCTal"""
	ASCii = 0
	BINary = 1
	HEXadecimal = 2
	OCTal = 3


# noinspection SpellCheckingInspection
class HardCopyImageFormat(Enum):
	"""4 Members, BMP ... XPM"""
	BMP = 0
	JPG = 1
	PNG = 2
	XPM = 3


# noinspection SpellCheckingInspection
class HardCopyRegion(Enum):
	"""2 Members, ALL ... DIALog"""
	ALL = 0
	DIALog = 1


# noinspection SpellCheckingInspection
class HilDataReceive(Enum):
	"""3 Members, NOData ... RECeived"""
	NOData = 0
	NOTHil = 1
	RECeived = 2


# noinspection SpellCheckingInspection
class IecDevId(Enum):
	"""2 Members, AUTO ... USER"""
	AUTO = 0
	USER = 1


# noinspection SpellCheckingInspection
class IecTermMode(Enum):
	"""2 Members, EOI ... STANdard"""
	EOI = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class InclExcl(Enum):
	"""2 Members, EXCLude ... INCLude"""
	EXCLude = 0
	INCLude = 1


# noinspection SpellCheckingInspection
class KbLayout(Enum):
	"""20 Members, CHINese ... SWEDish"""
	CHINese = 0
	DANish = 1
	DUTBe = 2
	DUTCh = 3
	ENGLish = 4
	ENGUK = 5
	ENGUS = 6
	FINNish = 7
	FREBe = 8
	FRECa = 9
	FRENch = 10
	GERMan = 11
	ITALian = 12
	JAPanese = 13
	KORean = 14
	NORWegian = 15
	PORTuguese = 16
	RUSSian = 17
	SPANish = 18
	SWEDish = 19


# noinspection SpellCheckingInspection
class NetMode(Enum):
	"""2 Members, AUTO ... STATic"""
	AUTO = 0
	STATic = 1


# noinspection SpellCheckingInspection
class OsetupBw(Enum):
	"""4 Members, BW1G ... SERVice"""
	BW1G = 0
	BW2G = 1
	BW5G = 2
	SERVice = 3


# noinspection SpellCheckingInspection
class OsetupDataSource(Enum):
	"""2 Members, HIL ... SCENario"""
	HIL = 0
	SCENario = 1


# noinspection SpellCheckingInspection
class OsetupHilProtocol(Enum):
	"""4 Members, DCP ... ZMQ"""
	DCP = 0
	UDP = 1
	UDPR = 2
	ZMQ = 3


# noinspection SpellCheckingInspection
class OsetupMode(Enum):
	"""2 Members, DYNamic ... STATic"""
	DYNamic = 0
	STATic = 1


# noinspection SpellCheckingInspection
class OsetupObjRef(Enum):
	"""2 Members, MAPPed ... ORIGin"""
	MAPPed = 0
	ORIGin = 1


# noinspection SpellCheckingInspection
class Parity(Enum):
	"""3 Members, EVEN ... ODD"""
	EVEN = 0
	NONE = 1
	ODD = 2


# noinspection SpellCheckingInspection
class PowSensDisplayPriority(Enum):
	"""2 Members, AVERage ... PEAK"""
	AVERage = 0
	PEAK = 1


# noinspection SpellCheckingInspection
class PowSensFiltType(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	NSRatio = 1
	USER = 2


# noinspection SpellCheckingInspection
class PowSensSource(Enum):
	"""4 Members, A ... USER"""
	A = 0
	B = 1
	RF = 2
	USER = 3


# noinspection SpellCheckingInspection
class RecScpiCmdMode(Enum):
	"""4 Members, AUTO ... OFF"""
	AUTO = 0
	DAUTo = 1
	MANual = 2
	OFF = 3


# noinspection SpellCheckingInspection
class RoscBandWidtExt(Enum):
	"""2 Members, NARRow ... WIDE"""
	NARRow = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class RoscFreqExt(Enum):
	"""3 Members, _10MHZ ... _5MHZ"""
	_10MHZ = 0
	_13MHZ = 1
	_5MHZ = 2


# noinspection SpellCheckingInspection
class RoscOutpFreqModeSmbb(Enum):
	"""3 Members, DER10M ... OFF"""
	DER10M = 0
	LOOPthrough = 1
	OFF = 2


# noinspection SpellCheckingInspection
class RoscSourSetup(Enum):
	"""3 Members, ELOop ... INTernal"""
	ELOop = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class Rs232BdRate(Enum):
	"""7 Members, _115200 ... _9600"""
	_115200 = 0
	_19200 = 1
	_2400 = 2
	_38400 = 3
	_4800 = 4
	_57600 = 5
	_9600 = 6


# noinspection SpellCheckingInspection
class Rs232StopBits(Enum):
	"""2 Members, _1 ... _2"""
	_1 = 0
	_2 = 1


# noinspection SpellCheckingInspection
class ScenarioReplyMode(Enum):
	"""2 Members, LOOP ... SINGle"""
	LOOP = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class ScenarioStatus(Enum):
	"""2 Members, RUNNing ... STOPped"""
	RUNNing = 0
	STOPped = 1


# noinspection SpellCheckingInspection
class SelftLev(Enum):
	"""3 Members, CUSTomer ... SERVice"""
	CUSTomer = 0
	PRODuction = 1
	SERVice = 2


# noinspection SpellCheckingInspection
class SelftLevWrite(Enum):
	"""4 Members, CUSTomer ... SERVice"""
	CUSTomer = 0
	NONE = 1
	PRODuction = 2
	SERVice = 3


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class StateExtended(Enum):
	"""3 Members, DEFault ... ON"""
	DEFault = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class Test(Enum):
	"""4 Members, _0 ... STOPped"""
	_0 = 0
	_1 = 1
	RUNning = 2
	STOPped = 3


# noinspection SpellCheckingInspection
class TestCalSelected(Enum):
	"""2 Members, _0 ... _1"""
	_0 = 0
	_1 = 1


# noinspection SpellCheckingInspection
class UnitAngle(Enum):
	"""3 Members, DEGree ... RADian"""
	DEGree = 0
	DEGRee = 1
	RADian = 2


# noinspection SpellCheckingInspection
class UnitAngleAreg(Enum):
	"""2 Members, DEGree ... RADian"""
	DEGree = 0
	RADian = 1


# noinspection SpellCheckingInspection
class UnitLengthAreg(Enum):
	"""3 Members, CM ... M"""
	CM = 0
	FT = 1
	M = 2


# noinspection SpellCheckingInspection
class UnitPower(Enum):
	"""3 Members, DBM ... V"""
	DBM = 0
	DBUV = 1
	V = 2


# noinspection SpellCheckingInspection
class UnitPowSens(Enum):
	"""3 Members, DBM ... WATT"""
	DBM = 0
	DBUV = 1
	WATT = 2


# noinspection SpellCheckingInspection
class UnitRcsAreg(Enum):
	"""2 Members, DBSM ... SM"""
	DBSM = 0
	SM = 1


# noinspection SpellCheckingInspection
class UnitShiftAreg(Enum):
	"""3 Members, HZ ... MHZ"""
	HZ = 0
	KHZ = 1
	MHZ = 2


# noinspection SpellCheckingInspection
class UnitSpeed(Enum):
	"""4 Members, KMH ... NMPH"""
	KMH = 0
	MPH = 1
	MPS = 2
	NMPH = 3


# noinspection SpellCheckingInspection
class UnitSpeedAreg(Enum):
	"""3 Members, KMH ... MPS"""
	KMH = 0
	MPH = 1
	MPS = 2


# noinspection SpellCheckingInspection
class UpdPolicyMode(Enum):
	"""3 Members, CONFirm ... STRict"""
	CONFirm = 0
	IGNore = 1
	STRict = 2
