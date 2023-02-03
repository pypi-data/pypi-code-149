from datetime import datetime

def generar_script(data: str, table: str, fields: str):

    script = f'insert into {table} \n'
    script += '(' + fields.replace('	', ', ') + ')\n'
    script += 'VALUES \n'
    data = data.replace(',', '')
    data = data.replace('	', ', ')
    lines = data.split('\n')
    
    result = ''
    _separator = ', '
    for _line in lines:
        _line_value = '('
        datos = _line.split(', ')
        for _value in datos:
            if _value == 'null': 
                _line_value += _value + _separator
            elif '.' in _value:
                if _value.replace('.', ',').isdigit():
                    _line_value += _value + _separator
                else:
                    _line_value += "'" + _value + "'" + _separator
            elif 'GMT' in _value:
                _line_value += "'" + str(datetime.strptime(validate_date(_date=_value), '%Y-%m-%d %H:%M:%S')) + "'" + _separator
            elif not _value.isdigit():
                _line_value += "'" + _value + "'" + _separator
            else:
                _line_value += _value + _separator
        _line_value = _line_value.rstrip(', ')
        result += _line_value + "), \n"
    result = result.rstrip(', \n')
    script += result + ';'

    return script


def validate_date(_date: str):
    if 'GMT' in _date:
        value = _date.split(' ')
        value = f'{value[3]}-{get_number_month(_value=value[2])}-{value[1]} {value[4]}'
    else:
        value = _date
    return value


def get_number_month(_value: str):
    months = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }
    if _value in months:
        _value = months[_value]
    return _value


