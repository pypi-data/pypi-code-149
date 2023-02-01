
# import psutil
# mem = psutil.virtual_memory()
# print(mem)

import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
print(gpus)

#
# class AutoModel:
#     def __init__(self, is_real_time: bool = False):
#         self.is_real_time = is_real_time



# import GPUtil
#
# Gpus = GPUtil.getFirstAvailable()
# print(Gpus)
# gpulist = []
# for gpu in Gpus:
#     print(gpu.name)
#     print('gpu.id:', gpu.id)
#
#     print('total GPU:', gpu.memoryTotal)
#     print(f"Memory free {gpu.memoryFree}MB")
#     print('GPU usage:', gpu.memoryUsed)
#     print('gpu use proportion:', gpu.memoryUtil * 100)
#     print(str(gpu.temperature) + " C")
#
#     gpulist.append([gpu.id, gpu.memoryTotal, gpu.memoryUsed, gpu.memoryUtil * 100])
#
# THRESHOLD_GPU = 10
# for gpu in Gpus:
#     print(gpu.name, ' gpu.id:', gpu.id)
#     if gpu.memoryTotal / gpu.memoryUsed * 100 > THRESHOLD_GPU: print(
#         f"gpu memory usgae currently is: {gpu.memoryUtil * 100}% which exceeds the threshold of {THRESHOLD_GPU}%")
#



# import GPUtil
# from tabulate import tabulate
# print("="*40, "GPU Details", "="*40)
# gpus = GPUtil.getGPUs()
# if not gpus:
#     raise "No GPUs available"
# print(gpus)
# list_gpus = []
# for gpu in gpus:
#     # get the GPU id
#     gpu_id = gpu.id
#     # name of GPU
#     gpu_name = gpu.name
#     # get % percentage of GPU usage of that GPU
#     gpu_load = f"{gpu.load*100}%"
#     # get free memory in MB format
#     gpu_free_memory = f"{gpu.memoryFree}MB"
#     print('gpu.memoryFree', gpu.memoryFree)
#     # get used memory
#     gpu_used_memory = f"{gpu.memoryUsed}MB"
#     # get total memory
#     gpu_total_memory = f"{gpu.memoryTotal}MB"
#     # get GPU temperature in Celsius
#     gpu_temperature = f"{gpu.temperature} °C"
#     gpu_uuid = gpu.uuid
#     list_gpus.append((
#         gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
#         gpu_total_memory, gpu_temperature, gpu_uuid
#     ))
#
# print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
#                                    "temperature", "uuid")))








# import psutil
# import platform
# uname = platform.uname()
# # print(f"System: {uname.system}")  #Windows or Linux
# # print(f"Node Name: {uname.node}") # System name
# print(f"Release: {uname.release}") # OS release version like  10(Windows) or 5.4.0-72-generic(linux)
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")  # machine can be AMD64 or x86-64
# print(f"Processor: {uname.processor}") #  Intel64 Family 6 or x86_64
# print("Physical cores:", psutil.cpu_count(logical=False))
# print("Total cores:", psutil.cpu_count(logical=True))
# # CPU frequencies
# # cpufreq = psutil.cpu_freq()
# # print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
# # print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
# # print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
#
#
# def get_size(bytes, suffix="B"):
#     """
#     Scale bytes to its proper format
#     e.g:
#         1253656 => '1.20MB'
#         1253656678 => '1.17GB'
#     """
#     factor = 1024
#     for unit in ["", "K", "M", "G", "T", "P"]:
#         if bytes < factor:
#             return f"{bytes:.2f}{unit}{suffix}"
#         bytes /= factor
#
# print("="*40, "Memory Information", "="*40)
# # get the memory details
# svmem = psutil.virtual_memory()
# print(f"Total: {get_size(svmem.total)}")
# print(f"Available: {get_size(svmem.available)}")
# print(f"Used: {get_size(svmem.used)}")
# print(f"Percentage: {svmem.percent}%")
# print("="*20, "SWAP", "="*20)
# # get the swap memory details (if exists)
# swap = psutil.swap_memory()
# print(f"Total: {get_size(swap.total)}")
# print(f"Free: {get_size(swap.free)}")
# print(f"Used: {get_size(swap.used)}")
# print(f"Percentage: {swap.percent}%")