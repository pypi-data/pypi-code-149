from typing import List
import mxdevtool as mx
import mxdevtool.xenarix as xen
import mxdevtool.termstructures as mx_t
import mxdevtool.marketconvension as mx_mc
import mxdevtool.utils as utils



# condition -----------------------------
class ANDCondition(mx.core_ANDConditionMC):
    def __init__(self, conditions):
        self._conditions = conditions
        mx.core_ANDConditionMC.__init__(self, conditions)


class ORCondition(mx.core_ORConditionMC):
    def __init__(self, conditions):
        self._conditions = conditions
        mx.core_ORConditionMC.__init__(self, conditions)


class XORCondition(mx.core_XORConditionMC):
    def __init__(self, condition1, condition2):
        self._condition1 = condition1
        self._condition2 = condition2
        mx.core_XORConditionMC.__init__(self, condition1, condition2)


class NOTCondition(mx.core_NOTConditionMC):
    def __init__(self, condition):
        self._condition = condition
        mx.core_NOTConditionMC.__init__(self, condition)


class RangeCondition(mx.core_RangeConditionMC):
    def __init__(self, po, a, b):
        self._po = po
        self._a = a
        self._b = b
        mx.core_RangeConditionMC.__init__(self, po, a, b)


class ANDDatesCondition(mx.core_DatesConditionMC):
    def __init__(self, po, dates):
        self._po = po
        self._dates = dates
        mx.core_DatesConditionMC.__init__(self, po, dates, 'and')


class ORDatesCondition(mx.core_DatesConditionMC):
    def __init__(self, po, dates):
        self._po = po
        self._dates = dates
        mx.core_DatesConditionMC.__init__(self, po, dates, 'or')


# class ANDBetweenDatesCondition(mx.core_BetweenDatesConditionMC):
#     def __init__(self, po, dates):
#         self._po = po
#         self._dates = dates
#         mx.core_BetweenDatesConditionMC.__init__(self, po, dates, 'and')


# class ORBetweenDatesCondition(mx.core_BetweenDatesConditionMC):
#     def __init__(self, po, dates):
#         self._po = po
#         self._dates = dates
#         mx.core_BetweenDatesConditionMC.__init__(self, po, dates, 'or')


class RelationalCondition(mx.core_RelationalConditionMC):
    def __init__(self, po1, operand, po2):
        self._po1 = po1
        self._operand = operand
        self._po2 = po2
        mx.core_RelationalConditionMC.__init__(self, po1, operand, po2)



# operators -----------------------------
class PlusPayoff(mx.core_PlusPayoffMC):
    def __init__(self, po):
        self._po = po
        mx.core_PlusPayoffMC.__init__(self, po)


class MinusPayoff(mx.core_MinusPayoffMC):
    def __init__(self, po):
        self._po = po
        mx.core_MinusPayoffMC.__init__(self, po)


class AdditionPayoff(mx.core_AdditionPayoffMC):
    def __init__(self, po1, po2):
        self._po1 = po1
        self._po2 = po2
        mx.core_AdditionPayoffMC.__init__(self, po1, po2)


class SubtractionPayoff(mx.core_SubtractionPayoffMC):
    def __init__(self, po1, po2):
        self._po1 = po1
        self._po2 = po2
        mx.core_SubtractionPayoffMC.__init__(self, po1, po2)


class MultiplicationPayoff(mx.core_MultiplicationPayoffMC):
    def __init__(self, po1, po2):
        self._po1 = po1
        self._po2 = po2
        mx.core_MultiplicationPayoffMC.__init__(self, po1, po2)


class DivisionPayoff(mx.core_DivisionPayoffMC):
    def __init__(self, po1, po2):
        self._po1 = po1
        self._po2 = po2
        mx.core_DivisionPayoffMC.__init__(self, po1, po2)


class IdentityPayoff(mx.core_IdentityPayoffMC):
    def __init__(self, po):
        self._po = po
        mx.core_IdentityPayoffMC.__init__(self, po)


class LinearPayoff(mx.core_LinearPayoffMC):
    def __init__(self, po, multiple, spread):
        self._po = po
        self._multiple = multiple
        self._spread = spread
        mx.core_LinearPayoffMC.__init__(self, po, multiple, spread)


class ConstantPayoff(mx.core_ConstantPayoffMC):
    def __init__(self, v):
        self._v = v
        mx.core_ConstantPayoffMC.__init__(self, v)


class ConditionPayoff(mx.core_ConditionPayoffMC):
    def __init__(self, condi, po_true, po_false):
        self._condi = condi
        self._po_true = po_true
        self._po_false = po_false
        mx.core_ConditionPayoffMC.__init__(self, condi, po_true, po_false)


class IndexPayoff(mx.core_IndexPayoffMC):
    def __init__(self, name):
        self._name = name
        mx.core_IndexPayoffMC.__init__(self, name)

    def index(self) -> mx.Index:
        return self._index()

    # parsing ex) krwirs10y
    # def as_iborIndex(self) -> mx_mc.IborIndex:
    #     mx_mc.get_iborIndex(self._name)

    def as_swapIndex(self) -> mx_mc.SwapIndex:
        mx_mc.get_swapIndex(self._name)

    @staticmethod
    def fromDict(d: dict):
        return utils.parseClassFromDict(d, globals())

    def toDict(self):
        return utils.serializeToDict(self)


class MinPayoff(mx.core_MinPayoffMC):
    def __init__(self, po1, po2):
        self._po1 = po1
        self._po2 = po2
        mx.core_MinPayoffMC.__init__(self, po1, po2, 'min')


class MaxPayoff(mx.core_MaxPayoffMC):
    def __init__(self, po1, po2):
        self._po1 = po1
        self._po2 = po2
        mx.core_MaxPayoffMC.__init__(self, po1, po2, 'max')



class MinimumBetweenDatesPayoff(mx.core_MinimumBetweenDatesPayoffMC):
    def __init__(self, po, startDate, endDate, hist_minimum=mx.nullDouble()):
        self._po = po
        self._startDate = startDate
        self._endDate = endDate
        mx.core_MinimumBetweenDatesPayoffMC.__init__(self, po, startDate, endDate, hist_minimum)


class MaximumBetweenDatesPayoff(mx.core_MaximumBetweenDatesPayoffMC):
    def __init__(self, po, startDate, endDate, hist_maximum=mx.nullDouble()):
        self._po = po
        self._startDate = startDate
        self._endDate = endDate
        mx.core_MaximumBetweenDatesPayoffMC.__init__(self, po, startDate, endDate, hist_maximum)


class AverageBetweenDatesPayoff(mx.core_AverageBetweenDatesPayoffMC):
    def __init__(self, po, startDate, endDate, hist_average=mx.nullDouble()):
        self._po = po
        self._startDate = startDate
        self._endDate = endDate
        mx.core_AverageBetweenDatesPayoffMC.__init__(self, po, startDate, endDate, hist_average)


class MinimumDatesPayoff(mx.core_MinimumDatesPayoffMC):
    def __init__(self, po, dates):
        self._po = po
        self._dates = dates
        mx.core_MinimumDatesPayoffMC.__init__(self, po, dates)


class MaximumDatesPayoff(mx.core_MaximumDatesPayoffMC):
    def __init__(self, po, dates):
        self._po = po
        self._dates = dates
        mx.core_MaximumDatesPayoffMC.__init__(self, po, dates)


class AverageDatesPayoff(mx.core_AverageDatesPayoffMC):
    def __init__(self, po, dates):
        self._po = po
        self._dates = dates
        mx.core_AverageDatesPayoffMC.__init__(self, po, dates)


class MathExpressionPayoff(mx.core_MathExpressionPayoffMC):
    def __init__(self, expression: str, **kwargs):
        self._expression = expression
        self._kwargs = kwargs

        med = utils.make_MathExpressionDictionary(kwargs)

        mx.core_MathExpressionPayoffMC.__init__(self, expression, med)


# coupons -----------------------------

class RateAccrualCouponMC(mx.core_RateAccrualCouponMC):
    def __init__(self, paymentDate, nominal, payoffMC,
                 accrualStartDate, accrualEndDate, calendar, dayCounter, accruedAmount):

        args = utils.set_init_self_args(self, paymentDate, nominal, payoffMC,
                accrualStartDate, accrualEndDate, calendar, dayCounter, accruedAmount)

        super().__init__(*args)

    @staticmethod
    def makeLeg(schedule, payoffMC, notional=10000,
                calendar=mx.SouthKorea(), dayCounter=mx.Actual365Fixed()):

        cpns = []

        for i, d in enumerate(schedule):
            if i == 0: continue

            cpn = RateAccrualCouponMC(
                schedule[i],
                notional,
                payoffMC,
                schedule[i-1],
                schedule[i],
                calendar,
                dayCounter)

            cpns.append(cpn)

        return cpns

    def getResults(self) -> dict:
        res = {}

        # res = self.getCommonResults()

        res[mx.CLASS_TYPE_NAME] = self.__class__.__name__

        res['npv'] = self._get_result_value('npv')
        res['amount'] = self._get_result_value('amount')
        res['discount'] = self._get_result_value('discount')
        res['time'] = self.accrualPeriod()

        return res


class FloatingRateCouponMC(mx.core_FloatingRateCouponMC):
    def __init__(self, paymentDate, nominal, fixingDays, indexPayoffMC, 
                accrualStartDate, accrualEndDate, calendar,
                dayCounter, gearing=1.0, spread=0.0):

        self._paymentDate = paymentDate
        self._nominal = nominal
        self._fixingDays = fixingDays
        self._indexPayoffMC = indexPayoffMC
        self._accrualStartDate = accrualStartDate
        self._accrualEndDate = accrualEndDate
        self._calendar = calendar
        self._dayCounter = dayCounter
        self._gearing = gearing
        self._spread = spread

        mx.core_FloatingRateCouponMC.__init__(self, self._paymentDate, self._nominal,
                    fixingDays, self._indexPayoffMC, self._accrualStartDate, self._accrualEndDate, self._calendar,
                    dayCounter, self._gearing, self._spread)

    @staticmethod
    def makeLeg(schedule, indexPayoffMC, notional=10000, fixingDays=1,
                calendar=mx.SouthKorea(), dayCounter=mx.Actual365Fixed(), gearing=1.0, spread=0.0):

        cpns = []

        for i, d in enumerate(schedule):
            if i == 0: continue

            cpn = FloatingRateCouponMC(
                schedule[i],
                notional,
                fixingDays,
                indexPayoffMC,
                schedule[i-1],
                schedule[i],
                calendar,
                dayCounter,
                gearing,
                spread)

            cpns.append(cpn)

        return cpns

    def getResults(self) -> dict:
        res = {}

        # res = self.getCommonResults()

        res[mx.CLASS_TYPE_NAME] = self.__class__.__name__

        res['npv'] = self._get_result_value('npv')
        res['amount'] = self._get_result_value('amount')
        res['discount'] = self._get_result_value('discount')
        res['time'] = self.accrualPeriod()

        return res

    def getScenResults(self, scenCount):
        res = {}
        # res['indexPayoffMC'] = indexPayoffMC.getScenResults()
        return res



class ReturnCouponMC(mx.core_ReturnCouponMC):
    def __init__(self, paymentDate: mx.Date, notional: float, 
                 fixingDate: mx.Date, payoffMC: mx.PayoffMC, calendar: mx.Calendar, dayCounter: mx.DayCounter):
            
        self._paymentDate = paymentDate
        self._notional = notional
        self._fixingDate = fixingDate
        self._payoffMC = payoffMC
        self._calendar = calendar
        self._dayCounter = dayCounter

        mx.core_ReturnCouponMC.__init__(self, self._paymentDate, self._notional, self._fixingDate, self._payoffMC, 
                                        self._calendar, self._dayCounter)    


class SimpleCouponMC(ReturnCouponMC):
    def __init__(self, paymentDate: mx.Date, fixingDate: mx.Date, payoffMC: mx.PayoffMC, 
                 calendar: mx.Calendar, dayCounter: mx.DayCounter):
            
        self._paymentDate = paymentDate
        self._fixingDate = fixingDate
        self._payoffMC = payoffMC
        self._calendar = calendar
        self._dayCounter = dayCounter

        ReturnCouponMC.__init__(self, self._paymentDate, 1.0, self._fixingDate, self._payoffMC, 
                                        self._calendar, self._dayCounter)    


class RateCouponMC(mx.core_RateCouponMC):
    def __init__(self, paymentDate: mx.Date, notional: float, fixingDate: mx.Date, payoffMC: mx.PayoffMC, 
                 accrualStartDate: mx.Date, accrualEndDate: mx.Date, calendar: mx.Calendar, dayCounter: mx.DayCounter):
            
        self._paymentDate = paymentDate
        self._notional = notional
        self._fixingDate = fixingDate
        self._payoffMC = payoffMC
        self._accrualStartDate = accrualStartDate
        self._accrualEndDate = accrualEndDate
        self._calendar = calendar
        self._dayCounter = dayCounter

        mx.core_RateCouponMC.__init__(self, self._paymentDate, self._notional, self._fixingDate, 
                                      self._payoffMC, self._accrualStartDate, self._accrualEndDate, 
                                      self._calendar, self._dayCounter)


class ReturnAccrualCouponMC(mx.core_ReturnAccrualCouponMC):
    def __init__(self, paymentDate: mx.Date, notional: float, payoffMC: mx.PayoffMC, accrualStartDate: mx.Date, accrualEndDate: mx.Date, 
                 calendar: mx.Calendar, dayCounter: mx.DayCounter, accruedRate: float = mx.nullDouble()):
        
        self._paymentDate = paymentDate
        self._notional = notional
        self._payoffMC = payoffMC
        self._accrualStartDate = accrualStartDate
        self._accrualEndDate = accrualEndDate
        self._calendar = calendar
        self._dayCounter = dayCounter
        self._accruedRate = accruedRate

        mx.core_ReturnAccrualCouponMC.__init__(self, self._paymentDate, self._notional, 
                                        self._payoffMC, self._accrualStartDate, self._accrualEndDate, 
                                        self._calendar, self._dayCounter, accruedRate)


class RateAccrualCouponMC(mx.core_RateAccrualCouponMC):
    def __init__(self, paymentDate: mx.Date, notional: float, payoffMC: mx.PayoffMC, accrualStartDate: mx.Date, accrualEndDate: mx.Date, 
                 calendar: mx.Calendar, dayCounter: mx.DayCounter, accruedRate: float = mx.nullDouble()):
        
        self._paymentDate = paymentDate
        self._notional = notional
        self._payoffMC = payoffMC
        self._accrualStartDate = accrualStartDate
        self._accrualEndDate = accrualEndDate
        self._calendar = calendar
        self._dayCounter = dayCounter
        self._accruedRate = accruedRate

        mx.core_RateAccrualCouponMC.__init__(self, self._paymentDate, self._notional, 
                                        self._payoffMC, self._accrualStartDate, self._accrualEndDate, 
                                        self._calendar, self._dayCounter, accruedRate)



class MathExpressionCouponMC(mx.core_MathExpressionCouponMC):
    def __init__(self, paymentDate: mx.Date, notional: float, fixingDate: mx.Date, payoffMC: mx.PayoffMC, 
                 accrualStartDate: mx.Date, accrualEndDate: mx.Date, 
                 expr: str, calendar: mx.Calendar, dayCounter: mx.DayCounter):
            
        self._paymentDate = paymentDate
        self._notional = notional
        self._fixingDate = fixingDate
        self._payoffMC = payoffMC
        self._accrualStartDate = accrualStartDate
        self._accrualEndDate = accrualEndDate
        self._expr = expr
        self._calendar = calendar
        self._dayCounter = dayCounter

        mx.core_MathExpressionCouponMC.__init__(self, self._paymentDate, self._notional, self._fixingDate,
                 self._payoffMC, self._accrualStartDate, self._accrualEndDate, self._expr, self._calendar, self._dayCounter)


class AutoCallableCouponMC(mx.core_AutoCallableCouponMC):
    def __init__(self, paymentDate: mx.Date, condition: mx.ConditionMC, baseCoupon: mx.CouponMC) -> None:
        self._paymentDate = paymentDate
        self._condition = condition
        self._baseCoupon = baseCoupon

        mx.core_AutoCallableCouponMC.__init__(self, self._paymentDate, self._condition, self._baseCoupon)


# instruments ------------------------------------------------------------ 

class StructuredLegExerciseOption(mx.core_StructuredLegExerciseOption):
    def __init__(self, dates, settlementDates, amounts):
        args = utils.set_init_self_args(self, dates, settlementDates, amounts)

        super().__init__(*args)


class VanillaLegInfo(mx.core_VanillaLegInfo):
    def __init__(self, coupons: List[mx.CouponMC], currency=utils.toCurrencyCls('krw')):
        
        self._coupons = coupons
        self._currency = currency

        mx.core_VanillaLegInfo.__init__(self, self._coupons, self._currency)

    def getResults(self) -> dict:
        res = {}

        res[mx.CLASS_TYPE_NAME] = self.__class__.__name__

        coupons = []

        for cpn in self._coupons:
            d = cpn.getResults()
            coupons.append(d)

        res['coupons'] = coupons
        res['npv'] = self._get_result_value()
        res['leg_npv'] = self._get_result_value('leg_npv')

        return res


class StructuredLegInfo(mx.core_StructuredLegInfo):
    def __init__(self, coupons: List[mx.CouponMC], currency=utils.toCurrencyCls('krw'), option=None):
        self._coupons = coupons
        self._currency = currency
        self._option = option

        

        mx.core_StructuredLegInfo.__init__(self, self._coupons, self._currency)

    def getResults(self) -> dict:
        res = super().getResults()

        coupons = []

        for cpn in self._coupons:
            d = cpn.getResults()
            coupons.append(d)

        res['coupons'] = coupons
        res['option'] = 0.0

        return res

    def getScenResults(self):
        res = super().getResults()

        coupons = []

        for cpn in self._coupons:
            d = cpn.getScenResults()
            coupons.append(d)

        res['coupons'] = coupons
        res['option'] = 0.0

        return res

# class StructuredSwap(mx.core_StructuredSwap):
#     def __init__(self, payLegInfo: mx.LegInfo, recLegInfo: mx.LegInfo):
#         self._payLegInfo = payLegInfo
#         self._recLegInfo = recLegInfo

#         mx.core_StructuredSwap.__init__(self, payLegInfo, recLegInfo)

#     def payCpns(self) -> List[mx.CouponMC]:
#         return self._payLegInfo._coupons

#     def recCpns(self) -> List[mx.CouponMC]:
#         return self._recLegInfo._coupons

#     def setPricingParams_Scen(self, scen_filename: str, pay_discount: str, rec_discount: str, 
#                               globalVariables = mx.MathExpressionGlobalDictionary(),
#                               settingVariables = mx.SettingVariableDictionary()):
#         self._setPricingParams_Scen(scen_filename, pay_discount, rec_discount, globalVariables, settingVariables)
#         return self

#     def getResults(self):
#         res_d = super().getResults()

#         res_d['payLegInfo'] = self._payLegInfo.getResults()
#         res_d['recLegInfo'] = self._recLegInfo.getResults()

#         return res_d

#     def getScenResults(self, scenCount):
#         return self.scenario_calculate(scenCount)
        

# class StructuredBond(mx.core_StructuredBond):
#     def __init__(self, legInfo, option):
#         self._legInfo = legInfo
#         self._option = option

#         mx.core_StructuredBond.__init__(self, legInfo)

#     def cpns(self) -> List[mx.core_CouponMC]:
#         return self._legInfo._coupons

#     def setPricingParams_Scen(self, discount: str or mx.YieldTermStructure, scen: xen.ScenarioResults or xen.Scenario, 
#                               reg_index_names: str, global_variable_d: dict):
#         mes = utils.make_MathExpressionDictionary(global_variable_d)
#         self._setPricingParams_Scen(discount, reg_index_names, scen)
#         return self