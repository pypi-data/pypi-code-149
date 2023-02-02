from commons.enumarate.enum_base import EnumBase


class EnumEstados(EnumBase):
    AC = 'Acre'
    AL = 'Alagoas'
    AP = 'Amapá'
    AM = 'Amazonas'
    BA = 'Bahia'
    CE = 'Ceará'
    DF = 'Distrito Federal'
    ES = 'Espírito Santo'
    GO = 'Goiás'
    MA = 'Maranhão'
    MT = 'Mato Grosso'
    MS = 'Mato Grosso do Sul'
    MG = 'Minas Gerais'
    PA = 'Pará'
    PB = 'Paraíba'
    PR = 'Paraná'
    PE = 'Pernambuco'
    PI = 'Piauí'
    RJ = 'Rio de Janeiro'
    RN = 'Rio Grande do Norte'
    RS = 'Rio Grande do Sul'
    RO = 'Rondônia'
    RR = 'Roraima'
    SC = 'Santa Catarina'
    SP = 'São Paulo'
    SE = 'Sergipe'
    TO = 'Tocantins'


class EnumFormaPagamento(EnumBase):
    DB = 'DEBITO'
    CD = 'CREDITO'
    BL = 'BOLETO'
    PX = 'PIX'
    DI = 'DINHEIRO'
    DP = 'DEPÓSITO'
    TF = 'TRANSFERÊNCIA'


class EnumSituacaoPagamento(EnumBase):
    PD = 'PENDENTE'
    PG = 'PAGO'
    RC = 'RECUSADO'


class EnumDiaSemana(EnumBase):
    SEG = 'Segunda'
    TER = 'Terça'
    QUA = 'Quarta'
    QUI = 'Quinta'
    SEX = 'Sexta'
    SAB = 'Sábado'
    DOM = 'Domingo'
