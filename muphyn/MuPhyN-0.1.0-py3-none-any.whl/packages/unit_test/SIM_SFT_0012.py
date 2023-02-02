from muphyn.packages.unit_test.unit_test import get_schedulers_library

schedulersLibraries = get_schedulers_library()

print("scheduler loaded : ", schedulersLibraries.libraries[0].schedulers.__len__())