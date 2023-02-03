from muphyn.packages.core.box_library.plci_core_boxes_libraries import BoxesLibraries
from muphyn.packages.core.scheduler_library.plci_core_schedulers_libraries import SchedulersLibraries
from muphyn.packages.interface.dialogs.dialogs_holder import DialogsHolder


boxesLibraries = BoxesLibraries()
schedulersLibraries = SchedulersLibraries()
dialogsHolder = DialogsHolder(None)
dialog = dialogsHolder.show_dialog(name = 'library', modal = False, boxes_libraries = boxesLibraries, solvers_libraries = schedulersLibraries)