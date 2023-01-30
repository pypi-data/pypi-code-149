from activitysim.benchmarking.componentwise import (
    template_component_timings,
    template_setup_cache,
)

from .sandag_full import *

EXAMPLE_NAME = "placeholder_sandag_1_zone_full"
CONFIGS_DIRS = ("configs_benchmarking", "configs_1_zone", "prototype_mtc/configs")
DYNAMIC_CONFIG_DIR = "bench_configs"
DATA_DIR = "data_1"
OUTPUT_DIR = "output_1"
VERSION = "1"


def setup_cache():
    template_setup_cache(
        EXAMPLE_NAME,
        COMPONENT_NAMES,
        BENCHMARK_SETTINGS,
        dict(
            read_skim_cache=SKIM_CACHE,
            write_skim_cache=SKIM_CACHE,
        ),
        CONFIGS_DIRS,
        DATA_DIR,
        OUTPUT_DIR,
    )


template_component_timings(
    globals(),
    COMPONENT_NAMES,
    EXAMPLE_NAME,
    (DYNAMIC_CONFIG_DIR, *CONFIGS_DIRS),
    DATA_DIR,
    OUTPUT_DIR,
    PRELOAD_INJECTABLES,
    REPEAT,
    NUMBER,
    TIMEOUT,
    VERSION,
)
