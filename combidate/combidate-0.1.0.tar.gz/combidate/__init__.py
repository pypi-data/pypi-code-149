from combidate.classes.data_generator import DataGenerator
from combidate.classes.process import Process
from combidate.processes.combine import combine
from combidate.processes.form import form
from combidate.processes.genetate import generate



ST_COMBINE = Process("ST_COMBINE", combine)
ST_GENERATE = Process("ST_GENERATE", generate)
ST_FORM = Process("ST_FORM", form)





