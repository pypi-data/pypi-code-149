import mxdevtool as mx
import mxdevtool.utils as utils


class IborIndex(mx.IborIndex):
    def __init__(self, familyName, tenor, settlementDays,
                 currency, calendar, convention,
                 endOfMonth, dayCounter):

        args = utils.set_init_self_args(self, familyName, tenor, settlementDays,
                 currency, calendar, convention, endOfMonth, dayCounter)

        super().__init__(*args)

    @staticmethod
    def fromDict(d: dict):
        return utils.parseClassFromDict(d, globals())

    def toDict(self):
        return utils.serializeToDict(self)

    def getCalc(self, ir_model, fixing=None):
        from mxdevtool.xenarix.pathcalc import Libor
        return Libor(self.name(), ir_model, self, fixing)



class SwapIndex(mx.SwapIndex):
    def __init__(self, familyName, tenor, settlementDays,
                 currency, calendar, fixedLegTenor, fixedLegConvention,
                 fixedLegDayCounter, iborIndex):

        args = utils.set_init_self_args(self, familyName, tenor, settlementDays,
                 currency, calendar, fixedLegTenor, fixedLegConvention, fixedLegDayCounter, iborIndex)

        super().__init__(*args)

    @staticmethod
    def fromDict(d: dict):
        mx.check_fromDict(d, mx.CLASS_TYPE_NAME, SwapIndex.__name__)

        familyName = d['familyName']
        tenor = utils.toPeriodCls(d['tenor'])
        settlementDays = d['settlementDays']
        currency = utils.toCurrencyCls(d['currency'])
        calendar = utils.toCalendarCls(d['calendar'])
        fixedLegTenor = utils.toPeriodCls(d['fixedLegTenor'])
        fixedLegConvention = utils.toBusinessDayConvention(d['fixedLegConvention'])
        fixedLegDayCounter = utils.toDayCounterCls(d['fixedLegDayCounter'])
        iborIndex = IborIndex.fromDict(d['iborIndex'])

        return SwapIndex(familyName, tenor, settlementDays,
                 currency, calendar, fixedLegTenor, fixedLegConvention,
                 fixedLegDayCounter, iborIndex)


    def toDict(self):
        res = dict()

        res[mx.CLASS_TYPE_NAME] = self.__class__.__name__
        res['familyName'] = str(self._familyName)
        res['tenor'] = str(self._tenor)
        res['settlementDays'] = self._settlementDays
        res['currency'] = str(self._currency)
        res['calendar'] = str(self._calendar)
        res['fixedLegTenor'] = str(self._fixedLegTenor)
        res['fixedLegConvention'] = self._fixedLegConvention
        res['fixedLegDayCounter'] = str(self._fixedLegDayCounter)
        res['iborIndex'] = self._iborIndex.toDict()

        return res

    def getCalc(self, ir_model, fixing=None):
        from mxdevtool.xenarix.pathcalc import SwapRate
        return SwapRate(self.name(), ir_model, self, fixing)



class FixedBondMarketConvension(mx.core_FixedBondMarketConvension):
    def __init__(self, calendar, dayCounter, businessDayConvention,
                 settlementDays, couponTenor, compounding, familyname):

        args = utils.set_init_self_args(self, calendar, dayCounter, businessDayConvention,
                 settlementDays, couponTenor, compounding, familyname)

        # this for intellisense
        self._calendar: mx.Calendar = self._calendar
        self._dayCounter: mx.DayCounter = self._dayCounter
        self._businessDayConvention: int = self._businessDayConvention
        self._settlementDays: int = self._settlementDays
        self._couponTenor: mx.Period = self._couponTenor
        self._compounding: int = self._compounding
        self._familyname: str = self._familyname

        super().__init__(*args)

    @staticmethod
    def fromDict(d: dict):
        return utils.parseClassFromDict(d, globals())

    def toDict(self):
        return utils.serializeToDict(self)


class VanillaSwapMarketConvension(mx.core_VanillaSwapMarketConvension):
    def __init__(self, calendar, dayCounter, businessDayConvention,
                 settlementDays, couponTenor, iborIndex, familyname):

        args = utils.set_init_self_args(self, calendar, dayCounter, businessDayConvention,
                 settlementDays, couponTenor, iborIndex, familyname)

        # this for intellisense
        self._calendar: mx.Calendar = self._calendar
        self._dayCounter: mx.DayCounter = self._dayCounter
        self._businessDayConvention: int = self._businessDayConvention
        self._settlementDays: int = self._settlementDays
        self._couponTenor: mx.Period = self._couponTenor
        self._iborIndex: IborIndex = self._iborIndex
        self._familyname: str = self._familyname

        super().__init__(*args)

    @staticmethod
    def fromDict(d: dict):
        return utils.parseClassFromDict(d, globals())

    def toDict(self):
        return utils.serializeToDict(self)




def get_iborIndex(name: str, tenor: mx.Period) -> IborIndex:
    if name in ['krwcd', 'krwirs']:
        return IborIndex("KrwCD", tenor, 1, utils.toCurrencyCls('krw'), utils.toCalendarCls('kr'), mx.ModifiedFollowing, True, mx.Actual365Fixed())
    else:
        pass

    raise Exception('unknown iborIndex - {0}'.format(name))


def get_swapIndex(name: str, tenor: mx.Period) -> SwapIndex:
    if name == 'krwirs':
        return SwapIndex("krwirs", tenor, 1, utils.toCurrencyCls('krw'), utils.toCalendarCls('kr'),
                         mx.Period(3, mx.Months), mx.ModifiedFollowing, mx.Actual365Fixed(),
                         get_iborIndex('krwcd', mx.Period(3, mx.Months)))
    else:
        pass

    raise Exception('unknown SwapIndex - {0}'.format(name))


def marketConvensionFromDict(d: dict):
    if not isinstance(d, dict):
        raise Exception('dictionary is required - {0}'.format(d))

    clsnm = d[mx.CLASS_TYPE_NAME]
    if clsnm == FixedBondMarketConvension.__name__:
        return FixedBondMarketConvension.fromDict(d)
    elif clsnm == VanillaSwapMarketConvension.__name__:
        return VanillaSwapMarketConvension.fromDict(d)

    raise Exception('unknown marketConvension - {0}'.format(clsnm))


def get_marketConvension_fixedbond(name) -> FixedBondMarketConvension:
    if name == 'ktb1':
        return FixedBondMarketConvension(
            mx.SouthKorea(), mx.Actual365Fixed(), mx.ModifiedFollowing, 1, mx.Period('3m'), mx.Compounded, name)
    elif name == 'ktb2':
        return FixedBondMarketConvension(
            mx.SouthKorea(), mx.Actual365Fixed(), mx.ModifiedFollowing, 1, mx.Period('6m'), mx.Compounded, name)

    return None


def get_marketConvension_vanillaswap(name) -> VanillaSwapMarketConvension:
    if name in ('irskrw', 'irskrw_krccp'):
        iborIndex = get_iborIndex('krwcd', '3m')
        return VanillaSwapMarketConvension(
            mx.SouthKorea(), mx.Actual365Fixed(), mx.ModifiedFollowing, 1, mx.Period('3m'), iborIndex, name)

    return None


def get_marketConvension(name):
    fb = get_marketConvension_fixedbond(name)
    if fb != None: return fb

    vs = get_marketConvension_vanillaswap(name)
    if vs != None: return vs

    raise Exception('unknown marketConvension - {0}'.format(name))


