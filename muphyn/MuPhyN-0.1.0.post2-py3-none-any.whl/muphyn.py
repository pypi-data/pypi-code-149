#-----------------------------------
# Imports
#-----------------------------------

import ctypes
import logging
import sys
import os
import traceback
from types import TracebackType
from time import sleep
from multiprocessing import Process, Manager
from threading import Thread

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication

from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibrariesManager
from muphyn.packages.interface.main_window import MainWindow 
from muphyn.packages.core.utils.log_manager import LogManager
from muphyn.packages.core.utils.directory_manager import DirectoryManager
from muphyn.packages.core.utils.global_env_variables_manager import GlobalEnvVariablesManager

from muphyn.utils.paths import ROOT_DIR

from IPython.core.magic import Magics, line_magic, magics_class
from IPython import get_ipython

def muphyn_excepthook(exc_type: type[BaseException], exc_value: BaseException, exc_tb: TracebackType):
    # Save openned project as 
    if 'win' in globals():
        global win
        win.backup_save_projects()

    # Format Exception error 
    formatted_exception = \
        f"Error while running Muphyn: \n{''.join(traceback.format_exception(exc_type, exc_value, exc_tb))}"

    # Write Error in Log File
    LogManager().error(formatted_exception)

    # Quit Applcation
    QApplication.exit(-1)

#-----------------------------------
# Main method
#-----------------------------------
def run_muphyn(globals_dict = {}):
    #_ = os.system('cls')
    myappid = 'ceref.muphyn.1.2'

    if os.name == 'nt' :
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Replace excepthook function
    sys.excepthook = muphyn_excepthook

    # Init Managers
    
    LogManager().info("Starting Muphyn application", is_global_message=True)
    GlobalEnvVariablesManager(global_vars=globals_dict)
    DirectoryManager()
    BoxesLibrariesManager()

    app = QApplication(sys.argv)

    app_icon = QIcon()
    app_icon.addFile(ROOT_DIR + "/" + "packages/interface/assets/MuPhyN.ico", QSize(400, 400))
    app.setWindowIcon(app_icon)

    # Load Style Sheet
    with open(ROOT_DIR + "/" + "themes/light.qss", "r") as styleSheetFile:
        styleSheetFileStr = styleSheetFile.read().replace("%ROOT_DIR%", ROOT_DIR).replace("\\", "/")
        app.setStyleSheet(styleSheetFileStr)

    win = MainWindow()
    win.show()

    # Launch Muphyn application
    exit_code = app.exec_()

    # Print in log the exit code
    LogManager().set_current_project_id(-1)
    LogManager().info(f"Closing MuPhyN application with code: {exit_code}", is_global_message=True)

    # Closing application
    sys.exit(exit_code)

def filter_local_variables(_global_vars = {}):
    _output = {}

    _excl_list = ['In', 'Out', 'Process', 'Thread', 'TracebackType']

    _type_incl_list = [str, int, float, list, dict, type]
    
    for _x in [key for key in _global_vars if not key.startswith('_')]:
        if type(_global_vars[_x]) in _type_incl_list and _x not in _excl_list:
            _output.update({_x:_global_vars[_x]})

    return _output

def update_globals(vars, ts = 0.25):
    while(1):
        sleep(ts)
        vars.clear()
        vars.update(filter_local_variables(globals().copy()))

def start(data = {}):
    LogManager(log_level=logging.DEBUG)
    _globals = {}
    
    if len(data) == 0:
        _globals = Manager().dict()
        _globals.update(filter_local_variables(globals().copy()))
        LogManager().info(f"Getting data from globals: {_globals}", is_global_message=True)

        LogManager().info("Creating globals synchronization thread", is_global_message=True)
        update_thread = Thread(target=update_globals, args=(_globals,))
        update_thread.start()
    else:
        _globals.update(filter_local_variables(data))

    # TODO: automatically start MuPhyN by opening a file with the same name as the ipynb file 
    # using the key ['__vsc_ipynb_file__'] in globals() 
    # If no file exists, create it

    LogManager().info("Starting MuPhyN process", is_global_message=True)
    _muphyn_process = Process(target=run_muphyn, args=(_globals,))
    _muphyn_process.start()

if __name__ == '__main__':
    start()

@magics_class
class MuphynMagics(Magics):

    def __init__(self, shell):
        super(MuphynMagics, self).__init__(shell)
        self.default_runner = self.shell.safe_execfile

    @line_magic
    def muphyn(self, line):
        ipython = get_ipython()
        get_ipython().magic("run -i " + ROOT_DIR + "/"+ "muphyn")

def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    ipython.register_magics(MuphynMagics)