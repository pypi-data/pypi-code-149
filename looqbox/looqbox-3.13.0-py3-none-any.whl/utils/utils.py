import random
import base64
import datetime
import itertools
import re
import types
import string
from monthdelta import monthdelta
from looqbox.global_calling import GlobalCalling
from looqbox.integration.looqbox_global import Looqbox
from looqbox.utils.i18n.internationalization_manager import I18nManager
import os
import importlib.util
import json

__all__ = ["random_hash", "base64_encode", "base64_decode", "paste_if", "format", "format_cnpj", "format_cpf",
           "title_with_date", "map", "drill_if", "current_day", "partition", "library", "create_i18n_vocabulary",
           "read_response_json", "flatten"]

# Calling global variable
if GlobalCalling.looq.home is None:
    GlobalCalling.set_looq_attributes(Looqbox())


def library(file=None):
    """
    Call (import) functions from a file in the Looqbox server. The file must be in the R folder.

    The return of this function must be saved in a variable to be used like a python module.

    :param file: File's name
    :return: A module with all the functions from the file
    """
    home = GlobalCalling.looq.home
    config = os.path.join(home, "R")
    name = file.split(".")[0]

    spec = importlib.util.spec_from_file_location(name, os.path.join(config, file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def random_hash(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for pos in range(size))


def base64_encode(text):
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')

    return encoded_text


def base64_decode(text):
    decoded_text = base64.b64decode(text).decode('utf-8')

    return decoded_text


def paste_if(head, args=None, closure="", args_separator="|"):
    """
    Paste only if argument exists, otherwise returns None.

    :param head: Text to be inserted before the argument
    :param args: Value to be inserted after the head, if the value is None, the title will not be shown
    :param closure: Text to be inserted after the argument
    :param args_separator: Character string to separate the results
    :return: a string or None
    """
    if isinstance(args, dict):
        raise Exception("Dictionary not accept in paste_if")
    elif isinstance(args, list):
        args_with_sep = ""

        for arg in args[0:len(args) - 1]:
            args_with_sep = args_with_sep + str(arg) + args_separator

        return head + args_with_sep + str(args[-1]) + closure

    elif isinstance(args, str):
        return head + args + closure

    elif isinstance(args, float) or isinstance(args, int) or isinstance(args, complex):
        return head + str(args) + closure
    else:
        return ""


def format(value, value_format=None, language=GlobalCalling.looq.language):
    """
    Sets a value according to the specified format.

    For number and percent format, it's necessary to define how many decimal places will be used, since those types does
    haven't a default value. On the other hand, for currency format, one might define a specific symbol or leave it for
    the default value, which is set based on the user's language.

    :param value: Value to be formatted
    :param value_format: Format to be assigned to value. Formats allowed:
    * number:<decimal places>
    * percent:<decimal places>
    * currency
    * currency:<Symbol>
    * date
    * datetime

    Example:
      format(1.146558649, "number:1") = "1.1"
      format(1.146558649, "number:5") = "1.14656"

      format(0.754624594, "percent:0") = "75%"
      format(0.754624594, "percent:7") = "75,4624594%"

      format(42,27756, "currency:¥") = ¥42,28
      format(42,27756, "currency") = $42,28

      format("2022-01-15", "date") = "01/15/2022" or "15/01/2022" (defined by user's settings in appearance menu, the
      same is applied for "datetime" format)

    :return: A string formatted according to the value_format parameter
    """

    if value_format is None:
        # warnings.warn("Format not defined")
        return value

    if isinstance(value_format, types.FunctionType):
        return value_format(value)

    if "number" in value_format:
        value = _format_number(value, value_format)
    elif "percent" in value_format:
        value = _format_percent(value, value_format)
    elif "currency" in value_format:
        value = _format_currency(value, value_format)
    elif value_format == "Date" or value_format == "date":
        value = _format_date(value, date_format=GlobalCalling.looq.date_format)
    elif value_format == "Datetime" or value_format == "datetime":
        value = _format_datetime(value, date_format=GlobalCalling.looq.date_format)

    return value


def _format_number(value: float, number_format: str) -> str:

    decimal_size = _get_decimal_format(number_format)
    value_format = "{0:,." + str(decimal_size) + "f}"
    value = value_format.format(float(value))

    if GlobalCalling.looq.decimal_separator == ",":
        value = value.translate(str.maketrans(",.", ".,"))

    return value


def _format_percent(value: float, percent_format: str) -> str:

    decimal_size = _get_decimal_format(percent_format)
    value_format = "{0:,." + str(decimal_size) + "%}"
    value = value_format.format(float(value))

    if GlobalCalling.looq.decimal_separator == ",":
        value = value.translate(str.maketrans(",.", ".,"))

    return value


def _get_decimal_format(value_format: str) -> int:

    number_pattern = "(?<=:)\\d"
    decimal = re.findall(number_pattern, value_format)[0]

    return decimal


def _get_currency_symbol(current_format: str, language=GlobalCalling.looq.language) -> str:

    currency_symbols_options = {
        'pt-br': 'R$',
        'en-us': '$'
    }

    currency_symbol = current_format.split(":")[1] if ":" in current_format else None

    return currency_symbol or currency_symbols_options.get(language, "$")


def _format_currency(value: float, currency_format: str) -> str:

    currency_symbol = _get_currency_symbol(currency_format)

    # Since it's most common to monetary values use 2 decimal places, this format will be fixed for the time being
    formatted_value = _format_number(value, "number:2")

    return f'{currency_symbol}{formatted_value}'


def _format_date(value, date_format=GlobalCalling.looq.date_format):

    if isinstance(value, str):
        value = datetime.datetime.strptime(value, '%Y-%m-%d')

    date_format = _get_date_template(date_format)
    value = datetime.datetime.strftime(value, date_format)
    return value


def _format_datetime(value, date_format=GlobalCalling.looq.date_format):

    if isinstance(value, str):
        value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

    datetime_format = _get_date_template(date_format) + " %H:%M:%S"
    value = datetime.datetime.strftime(value, datetime_format)

    return value


def _get_date_template(date_format):

    template_options = {"dd/mm/yyyy": "%d/%m/%Y",
                        "mm/dd/yyyy": "%m/%d/%Y"}

    date_template = template_options.get(date_format, "%d/%m/%Y")

    return date_template


def format_cnpj(cnpj_string):
    """
    Formats CNPJ to standard format.

    :param cnpj_string: Unformatted CNPJ (string)
    :return: A string in the CNPJ format XX.XXX.XXX/XXXX-XX
    """
    if not isinstance(cnpj_string, str):
        return ""

    if len(cnpj_string) == 13:
        cnpj_string = '0' + cnpj_string
    elif len(cnpj_string) > 14:
        raise Exception('Invalid CNPJ string: More than 14 digits')

    return cnpj_string[:2] + "." + cnpj_string[2:5] + "." + cnpj_string[5:8] + "/" + \
           cnpj_string[8:12] + '-' + cnpj_string[12:]


def format_cpf(cpf_string):
    """
    Formats CPF to standard format.

    :param cpf_string: Unformatted CPF (string)
    :return: A string in the CPF format XXX.XXX.XXX-XX
    """
    return cpf_string[:3] + "." + cpf_string[3:6] + "." + cpf_string[6:9] + '-' + cpf_string[9:]


def week_name(date, language=GlobalCalling.looq.language):
    if language == "pt-br":
        week_rule = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    elif language == "en-us":
        week_rule = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    elif language == "it":
        week_rule = ["lun", "mar", "mer", "gio", "ven", "sab", "do"]

    date_week_day = date.timetuple()[6]

    return week_rule[date_week_day]


def date_range_name(date_int, language=GlobalCalling.looq.language):
    initial_date = date_int[0]
    finish_date = date_int[1]

    date_range = None

    # Case Day
    if initial_date == finish_date:
        if language == "pt-br":
            date_range = week_name(initial_date, language) + " sem: " + str(initial_date.isocalendar()[1]) + "/" \
                         + str(initial_date.year)
        elif language == "en-us":
            date_range = week_name(initial_date, language) + " week: " + str(initial_date.isocalendar()[1]) + "/" \
                         + str(initial_date.year)
        elif language == "it":
            date_range = week_name(initial_date, language) + " week: " + str(initial_date.isocalendar()[1]) + "/" \
                         + str(initial_date.year)

    # Case Week
    if initial_date.timetuple()[6] == 0 and initial_date + datetime.timedelta(days=6) == finish_date:
        if language == "pt-br":
            date_range = "sem: " + str(initial_date.isocalendar()[1]) + " - " + str(initial_date.year)
        elif language == "en-us":
            date_range = "week: " + str(initial_date.isocalendar()[1]) + " - " + str(initial_date.year)
        elif language == "it":
            date_range = "week: " + str(initial_date.isocalendar()[1]) + " - " + str(initial_date.year)

    # Case Month
    if initial_date.day == 1 and initial_date + monthdelta(1) - datetime.timedelta(days=1) == finish_date:
        if language == "pt-br":
            date_range = "mês: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "en-us":
            date_range = "month: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "it":
            date_range = "mese: " + str(initial_date.month) + "/" + str(initial_date.year)

    # Case MTD
    if initial_date.day == 1 and initial_date.month == finish_date.month and datetime.datetime.now().strftime(
            "%Y-%m-%d") == finish_date:
        if language == "pt-br":
            date_range = "mtd: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "en-us":
            date_range = "mtd: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "it":
            date_range = "mtd: " + str(initial_date.month) + "/" + str(initial_date.year)

    # Case Year
    if initial_date.day == 1 and initial_date.month == 1 \
            and initial_date + monthdelta(12) - datetime.timedelta(1) == finish_date:
        if language == "pt-br":
            date_range = "ano: " + str(initial_date.year)
        elif language == "en-us":
            date_range = "year: " + str(initial_date.year)
        elif language == "it":
            date_range = "ieri: " + str(initial_date.year)

    if date_range is None:
        return ""
    else:
        return " (" + date_range + ")"


def validate_datetime(date_text):

    if isinstance(date_text, datetime.datetime):
        return True
    else:
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False


def title_with_date(header=None, date_int=None, language=GlobalCalling.looq.language):
    """
    Writes a title for the specified date or date range.

    :param header: Text to be placed before the date
    :param date_int: Date(s) interval to be used in the title
    :param language: Title language
    :return: A title string
    """

    if language == "pt-br":
        var_day = " dia "
        var_from = " de "
        var_to = " a "
    elif language == "en-us":
        var_day = " day "
        var_from = " from "
        var_to = " to "
    elif language == "it":
        var_day = " gio "
        var_from = " dal "
        var_to = " al "
    else:
        raise Exception("Language {} is invalid".format(language))

    date_int_aux = date_int.copy()
    is_datetime_0 = validate_datetime(date_int_aux[0])
    is_datetime_1 = validate_datetime(date_int_aux[1])

    if is_datetime_0 and is_datetime_1:
        date_int_aux[0] = datetime.datetime.strptime(date_int[0], '%Y-%m-%d %H:%M:%S').date()
        date_int_aux[1] = datetime.datetime.strptime(date_int[1], '%Y-%m-%d %H:%M:%S').date()
    else:
        date_int_aux[0] = datetime.datetime.strptime(date_int[0], '%Y-%m-%d').date()
        date_int_aux[1] = datetime.datetime.strptime(date_int[1], '%Y-%m-%d').date()

    if isinstance(date_int_aux[0], datetime.date) and isinstance(date_int_aux[1], datetime.date):
        if date_int_aux[0] == date_int_aux[1]:
            date_result = header + var_day + "" + \
                          format(date_int_aux[0], "Date", language) + date_range_name(date_int_aux, language)
        else:
            date_result = header + var_from + "" + format(date_int_aux[0], "Date", language) + var_to \
                          + format(date_int_aux[1], "Date", language) + date_range_name(date_int_aux, language)
    else:
        if date_int_aux[0] == date_int_aux[1]:
            date_result = header + var_day + "" + format(date_int_aux[0], "datetime", language)
        else:
            date_result = header + var_from + "" + format(date_int_aux[0], "datetime", language) + var_to \
                          + format(date_int_aux[1], language)

    return date_result


def map(function_arg, *args):
    """
    Apply function with the arguments defined.

    :param function_arg: Function to apply
    :param args: Function arguments
    :return: The output of the function
    """
    # Verify if it has arguments
    if len(args) == 1 and args[0] is None:
        return function_arg(None)

    # Transforming Nones into str to find the cartesian product
    args_list = list(args)
    for i in range(len(args_list)):
        if args_list[i] is None:
            args_list[i] = ["None"]
    args = tuple(args_list)

    # Finding the cartesian product of my *args
    args_possibilities_list = list(itertools.product(*args))

    # Transform tuple into list
    args_possibilities_list = [list(possibility) for possibility in args_possibilities_list]

    # Turning str None into None type again
    for poss_list in args_possibilities_list:
        for i in range(len(poss_list)):
            if poss_list[i] == "None":
                poss_list[i] = None

    # args_possibilities_list = [args_possibilities_list]

    # Dynamically sending all the possibilities to the function
    result = [function_arg(*arg_product) for arg_product in args_possibilities_list]

    return result


def drill_if(value_link, arg):
    """
    Removes drill in case the correspondent arg is not None.

    :param value_link: value_link of the column of row
    :param arg: Arguments to be evaluated
    """

    if not isinstance(arg, list):
        arg = [arg]

    if len(value_link) == len(list(filter(None, arg))) \
            or (not isinstance(value_link, list) and len(list(filter(None, arg))) == 1):
        value_link = None
    else:
        for i in range(len(arg),0,-1):
            if arg[i-1] is not None:
                value_link.remove(value_link[i-1])


    return value_link


def current_day(format='date'):
    """
    Creates list with current day.

    :param format: Format of the date output (date or datetime)
    :return: A list with two elements of the current day. If an invalid format is specified, then it uses the 'date' format
    """

    if format.lower() == 'date':
        return [datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%Y-%m-%d")]
    elif format.lower() == 'datetime':
        return [datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]
    else:
        return [datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%Y-%m-%d")]


def partition(values):
    """
    Partitions list into overlapping sublists of length 2.

    :param list ll: List of elements for partition.
    :return: A list of sublists containing 2 elements each.

    Examples:
    --------
    values = ["Monday", 54, True]
    partition(values)
    """
    if not isinstance(values, list):
        values = [values]

    new_list = []

    if len(values) == 1:
        new_list = [values + values]
    else:
        [new_list.append([values[i], values[i + 1]]) for i in range(len(values) - 1)]

    return new_list


def create_i18n_vocabulary(new_vocabulary: dict) -> I18nManager:
    """
    Create an I18nManager object which help in script internationalization

    :param new_vocabulary: a dict containing the vocabulary in the desired languages.
    Example:
        script_vocabulary = {"pt-br": {"frame_title": "Título do Frame", "table_title": "Tabela 01"},
                             "en-us": {"frame_title": "Frame title", "table_title": "Table 01"}
                            }
        script_terms = create_i18n_vocabulary(script_vocabulary)
        table.title = script_terms.table_title
        ResponseFrame([table], title=script_terms.frame_title)
    :return: I18nManager object with vocabulary inserted as parameter

    Tips And Tricks:
        One might be useful to define a pattern to name the labels, e.g.
        vocabulary = {
                      "pt-br": {
                                "store_code_column_name": "Código Loja",
                                "store_column_name": "Nome Loja",
                                "goal_column_name": "Meta",
                                "sale_column_name": "Venda",
                               },
                      "en-us": {
                                "store_code_column_name": "Store code",
                                "store_column_name": "Store name",
                                "goal_column_name": "Goal",
                                "sale_column_name": "Sale",
                                }
                      }
    """
    i18n = I18nManager(language=GlobalCalling.looq.language)
    i18n.add_label(new_vocabulary)
    return i18n


def read_response_json(json_file: str, file_encoding='utf-8') -> json:
    """
    Function used primarily in the Python-Template called by FES to reshape the response-json (sent by the Looqbox's
    Language Service) into a python readable format.
    """

    raw_file = open(json_file, 'r', encoding=file_encoding).read()
    formatted_file = _format_quotes(raw_file)
    return json.loads(formatted_file)


def _format_quotes(file: str) -> str:
    return file.replace('\\\\"', '\\"')


def flatten(list_to_flat: list) -> list:
    flat_list = []
    for item in list_to_flat:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return [item for item in flat_list if item is not None]
