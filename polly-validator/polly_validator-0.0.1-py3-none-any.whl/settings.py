import json
import pathlib

from appdirs import user_config_dir

from polly_validator.config import CONFIG
from polly_validator.utility.helper import get_data_types_data_sources

ROOT_DIR = pathlib.Path(__file__).parent

# Repos to carry out validation for
REPOS_FOR_DATASET_LEVEL_VALIDATION = CONFIG.get('repos_for_dataset_level_validation')
REPOS_FOR_SAMPLE_LEVEL_VALIDATION = CONFIG.get('repos_for_sample_level_validation')

# DB Name
DB_NAME = CONFIG.get('job_details').get('env').get('DB_NAME')

# Declare table names
DATASET_ERRORS_TABLE = CONFIG.get('dataset_errors_table_name', 'Dataset_Errors')
SAMPLE_ERRORS_TABLE = CONFIG.get('sample_errors_table_name', 'Sample_Errors')

# Flags for which validation to run
RUN_DATASET_LEVEL_VALIDATIONS = CONFIG.get('run_dataset_level_validations', True)
RUN_SAMPLE_LEVEL_VALIDATIONS = CONFIG.get('run_sample_level_validations', True)

# Polly environement list
POLLY_ENV_LIST = CONFIG.get('env')

# Field mapping for referring to when using valid_names.json
FIELD_MAPPING = {'tissue': 'tissue',
                 'curated_tissue': 'tissue',

                 'kw_cell_type': 'cell_type',
                 'curated_cell_type': 'cell_type',

                 'kw_cell_line': 'cell_line',
                 'curated_cell_line': 'cell_line',

                 'disease': 'disease',
                 'curated_disease': 'disease',

                 'kw_drug': 'drug',
                 'curated_drug': 'drug',

                 'organism': 'organism',
                 'curated_organism': 'organism',

                 'kw_data_type': 'data_type',
                 'data_type': 'data_type',
                 }

with open(pathlib.Path(user_config_dir()) / 'polly-validator' / 'valid_names.json', 'r') as fp:
    VALID_NAMES = json.load(fp)

print('Getting predefined values for Data Type and Data Source...')
VALID_NAMES['data_type'], VALID_NAMES['dataset_source'] = get_data_types_data_sources()
