import os
import time


def __get_memory(order):
    r = os.popen(order)
    mem = int(r.read())
    r.close()
    return mem


def used_memory():
    mem = __get_memory("cat /sys/fs/cgroup/memory/memory.usage_in_bytes")
    return mem


def limit_memory():
    mem = __get_memory("cat /sys/fs/cgroup/memory/memory.limit_in_bytes")
    return mem


def used_cpu():
    start = time.time_ns()
    a = __get_memory("cat /sys/fs/cgroup/cpu/cpuacct.usage")
    time.sleep(0.5)
    end = time.time_ns()
    b = __get_memory("cat /sys/fs/cgroup/cpu/cpuacct.usage")
    cpu = ((b - a) / (end - start)) * 100
    return cpu


def shared_spu():
    cpu = __get_memory("cat /sys/fs/cgroup/cpu/cpu.shares")
    return cpu