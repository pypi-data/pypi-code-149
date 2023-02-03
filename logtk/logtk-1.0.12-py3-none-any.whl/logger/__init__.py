from typing import Optional, Callable, Union
from datetime import datetime
import colortk
from time import time
from .objects import LogManager, TimeLogConfig, Colorizer


def __logger_name(__file: str):
    result = __file.replace("/", ".").removesuffix(".py")
    if ".." in result:
        result = result.split("..", 1)[1]
    while result.startswith("."):
        result = result.removeprefix(".")
    return result


log_manager = LogManager(
    colorizer=Colorizer(
        name="log",
        colorize_base=colortk.colorizer("cyan")
    )
)


def __form_format_result(config:TimeLogConfig) -> Callable[[object], str]:
    if config.include_result:
        format_result = config.format_result
        message_limit = config.message_limit
        allow_newlines = config.allow_newlines
        format_base = lambda __result: str(format_result(__result))
        if message_limit:
            format_limit = lambda __result: format_base(__result)[:message_limit]
            format_mid = lambda __result: format_limit(__result)
        else:
            format_mid = lambda __result:format_base(__result)
        if allow_newlines:
            format_top = format_mid
        else:
            format_top = lambda __result:format_mid(__result).replace("\n"," ")
        result = lambda __result:f": [{format_top(__result)}]"
    else:
        result = lambda __result:""
    return result


UTC_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S.%f UTC'
def __form_timestamp_generator(config:TimeLogConfig,color:str="blue"):
    colorize_timestamp = colortk.colorizer(color=color)
    timestamp_strformat = None
    if config.timestamp_strformat:
        timestamp_strformat = config.timestamp_strformat
    elif config.include_timestamp:
        timestamp_strformat = UTC_TIMESTAMP_FORMAT
    if timestamp_strformat is not None:
        timestamp_strformat = f"[ {timestamp_strformat} ]"
        def generate_timestamp():
            return colorize_timestamp(datetime.utcnow().strftime(timestamp_strformat))
    else:
        def generate_timestamp():
            return ""
    return generate_timestamp
        


def __form_log_message(config: TimeLogConfig, func):
    name_func = func.__name__
    colorize_time = colortk.colorizer("green")
    sublogger_name = __logger_name(config.file)
    colorizer_module = log_manager.sub_colorizer(sublogger_name, color=config.color)
    module_id = colorizer_module.colorized_id()

    colorizer_func = log_manager[sublogger_name].sub_colorizer(name_func)
    log_manager[sublogger_name][name_func] = colorizer_func
    func_id = colorizer_func.colorized_id()

    form_result = __form_format_result(config)
    timestamp_generator = __form_timestamp_generator(config)

    def form_time(__elapsed:str):
        m_time_base = f"( {str(__elapsed)[:12]}s )"
        return colorize_time(m_time_base)

    def log_message(result, elapsed: str):
        args = (f"INFO:    ",timestamp_generator()," ",form_time(elapsed), ": ", module_id, ".", func_id,form_result(result))
        print(*args, sep="")

    return log_message


def __timelog_sync(config: TimeLogConfig):
    def sublog(func):
        log_message = __form_log_message(config=config, func=func)

        def inner(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            elapsed = time() - start
            log_message(result=result, elapsed=elapsed)
            return result

        return inner

    return sublog


def __timelog_async(config: TimeLogConfig):
    def sublog(func):
        log_message = __form_log_message(config=config, func=func)

        async def inner(*args, **kwargs):
            start = time()
            result = await func(*args, **kwargs)
            elapsed = time() - start
            log_message(result=result, elapsed=elapsed)
            return result

        return inner

    return sublog


def timelog(
    file: str,
    color: Optional[Union[str, int]] = None,
    include_result: bool = True,
    format_result: Callable[[object], str] = lambda value: value,
    message_limit: Optional[int] = None,
    include_timestamp:bool = False,
    timestamp_strformat:Optional[str]=None,
    is_async: bool = False,
    allow_newlines:bool = False
):
    config_kwargs = dict(
        file=file,
        color=color,
        message_limit=message_limit,
        format_result=format_result,
        include_result=include_result,
        timestamp_strformat=timestamp_strformat,
        include_timestamp=include_timestamp,
        allow_newlines=allow_newlines
    )
    config = TimeLogConfig(**config_kwargs)
    return (__timelog_async if is_async else __timelog_sync)(config=config)
