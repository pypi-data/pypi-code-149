import gc
import os
import traceback as tb
from collections import defaultdict
from datetime import datetime as dt
from multiprocessing import Pool

import pandas as pd
import psutil
from polly_validator.utility.helper import chunks, print_exception
from polly_validator.validators import dataset_metadata_validator
from polly_validator.validators import sample_metadata_validator
from polly_validator.settings import DATASET_ERRORS_TABLE, DB_NAME, REPOS_FOR_DATASET_LEVEL_VALIDATION, \
    REPOS_FOR_SAMPLE_LEVEL_VALIDATION, RUN_DATASET_LEVEL_VALIDATIONS, RUN_SAMPLE_LEVEL_VALIDATIONS, SAMPLE_ERRORS_TABLE
from polly.auth import Polly
from polly.omixatlas import OmixAtlas
from sqlalchemy import create_engine
from tqdm import tqdm

# Obtain authentication tokens
try:
    if 'AUTH_KEY' in os.environ:
        AUTH_KEY = os.environ['AUTH_KEY']
        Polly.auth(AUTH_KEY)
    else:
        raise Exception(f'Polly-python authentication token missing.')
except Exception as e:
    print(tb.format_exc())
    print_exception()

# Defining OMIXATLAS object
OMIXATLAS = OmixAtlas()

dataset_id_list = ['20200917_MGH_Broad_Villani_to_CZI',
                   '2020_Cell_Kalucka_Carmeliet',
                   '2020_Cell_Roska_Cowan_Retina_Fovea',
                   '2020_Cell_Roska_Cowan_Retina_Organoid',
                   '2020_Cell_Roska_Cowan_Retina_Peripheral',
                   '20210217_NasalSwab_Broad_BCH_UMMC_to_CZI',
                   '2021_fimmu_Ucar_Lawlor_CITE-SEQ_RNA',
                   '2021_fimmu_Ucar_Lawlor_CITE-SEQ_protein',
                   'BALF_VIB_UGent_processed_cleaned',
                   'COV022A1',
                   'COV022A2',
                   'COV022A3',
                   'COV022B1',
                   'COV022B2',
                   'COV022B3',
                   'COV026A1',
                   'COV026A2',
                   'COV026A3',
                   'COV026A4',
                   'COV026A5',
                   'COV026A6',
                   'COV026A7',
                   'COV027A1',
                   'COV028A2',
                   'COV028A3',
                   'COV028A4',
                   'COV028A6',
                   'COV028B2',
                   'COV028B3',
                   'COV028B4',
                   'COV028B6',
                   'E-CURD-10',
                   'E-CURD-112',
                   'E-CURD-114',
                   'E-CURD-117',
                   'E-CURD-118',
                   'E-CURD-46',
                   'E-CURD-52',
                   'E-CURD-53',
                   'E-CURD-55',
                   'E-CURD-6',
                   'E-CURD-7',
                   'E-CURD-77',
                   'E-CURD-79',
                   'E-CURD-80',
                   'E-CURD-84',
                   'E-CURD-85',
                   'E-CURD-89',
                   'E-CURD-9',
                   'E-CURD-94',
                   'E-CURD-95',
                   'E-CURD-96',
                   'E-CURD-97',
                   'E-EHCA-2',
                   'E-ENAD-15',
                   'E-ENAD-20',
                   'E-ENAD-21',
                   'E-ENAD-27',
                   'E-GEOD-100426',
                   'E-GEOD-106540',
                   'E-GEOD-106973',
                   'E-GEOD-109979',
                   'E-GEOD-121891',
                   'E-GEOD-123046',
                   'E-GEOD-124472',
                   'E-GEOD-124858',
                   'E-GEOD-130148',
                   'E-GEOD-130473',
                   'E-GEOD-134144',
                   'E-GEOD-135922',
                   'E-GEOD-137537',
                   'E-GEOD-146122',
                   'E-GEOD-148360',
                   'E-GEOD-149689',
                   'E-GEOD-150728',
                   'E-GEOD-151346',
                   'E-GEOD-71585',
                   'E-GEOD-76312',
                   'E-GEOD-81547',
                   'E-GEOD-83139',
                   'E-GEOD-86618',
                   'E-GEOD-87631',
                   'E-GEOD-89232',
                   'E-GEOD-90848',
                   'E-GEOD-93593',
                   'E-GEOD-94641',
                   'E-GEOD-98556',
                   'E-GEOD-98816',
                   'E-GEOD-99058',
                   'E-GEOD-99235',
                   'E-HCAD-10',
                   'E-HCAD-11',
                   'E-HCAD-13',
                   'E-HCAD-14',
                   'E-HCAD-15',
                   'E-HCAD-16',
                   'E-HCAD-23',
                   'E-HCAD-24',
                   'E-HCAD-32',
                   'E-HCAD-35',
                   'E-HCAD-5',
                   'E-HCAD-6',
                   'E-HCAD-8',
                   'E-HCAD-9',
                   'E-MTAB-10018',
                   'E-MTAB-10050',
                   'E-MTAB-10174',
                   'E-MTAB-10196',
                   'E-MTAB-10197',
                   'E-MTAB-10221',
                   'E-MTAB-10290',
                   'E-MTAB-10432',
                   'E-MTAB-10448',
                   'E-MTAB-10485',
                   'E-MTAB-10553',
                   'E-MTAB-10869',
                   'E-MTAB-10945',
                   'E-MTAB-11011',
                   'E-MTAB-11242',
                   'E-MTAB-2805',
                   'E-MTAB-2983',
                   'E-MTAB-3321',
                   'E-MTAB-3707',
                   'E-MTAB-3929',
                   'E-MTAB-4026',
                   'E-MTAB-4388',
                   'E-MTAB-4547',
                   'E-MTAB-4619',
                   'E-MTAB-4825',
                   'E-MTAB-4850',
                   'E-MTAB-4888',
                   'E-MTAB-5058',
                   'E-MTAB-5061',
                   'E-MTAB-5208',
                   'E-MTAB-5466',
                   'E-MTAB-5485',
                   'E-MTAB-5553',
                   'E-MTAB-5661',
                   'E-MTAB-5727',
                   'E-MTAB-5802',
                   'E-MTAB-6051',
                   'E-MTAB-6058',
                   'E-MTAB-6075',
                   'E-MTAB-6142',
                   'E-MTAB-6173',
                   'E-MTAB-6308',
                   'E-MTAB-6362',
                   'E-MTAB-6379',
                   'E-MTAB-6386',
                   'E-MTAB-6487',
                   'E-MTAB-6505',
                   'E-MTAB-6653',
                   'E-MTAB-6677',
                   'E-MTAB-6678',
                   'E-MTAB-6701',
                   'E-MTAB-6818',
                   'E-MTAB-6819',
                   'E-MTAB-6879',
                   'E-MTAB-6911',
                   'E-MTAB-6912',
                   'E-MTAB-6925',
                   'E-MTAB-6945',
                   'E-MTAB-6946',
                   'E-MTAB-6970',
                   'E-MTAB-6976',
                   'E-MTAB-6987',
                   'E-MTAB-7008',
                   'E-MTAB-7037',
                   'E-MTAB-7051',
                   'E-MTAB-7052',
                   'E-MTAB-7094',
                   'E-MTAB-7142',
                   'E-MTAB-7249',
                   'E-MTAB-7303',
                   'E-MTAB-7311',
                   'E-MTAB-7316',
                   'E-MTAB-7320',
                   'E-MTAB-7324',
                   'E-MTAB-7325',
                   'E-MTAB-7365',
                   'E-MTAB-7376',
                   'E-MTAB-7381',
                   'E-MTAB-7417',
                   'E-MTAB-7427',
                   'E-MTAB-7606',
                   'E-MTAB-7660',
                   'E-MTAB-7678',
                   'E-MTAB-7703',
                   'E-MTAB-7704',
                   'E-MTAB-7869',
                   'E-MTAB-7895',
                   'E-MTAB-7901',
                   'E-MTAB-8002',
                   'E-MTAB-8077',
                   'E-MTAB-8145',
                   'E-MTAB-8205',
                   'E-MTAB-8207',
                   'E-MTAB-8221',
                   'E-MTAB-8263',
                   'E-MTAB-8271',
                   'E-MTAB-8312',
                   'E-MTAB-8322',
                   'E-MTAB-8360',
                   'E-MTAB-8381',
                   'E-MTAB-8410',
                   'E-MTAB-8414',
                   'E-MTAB-8483',
                   'E-MTAB-8495',
                   'E-MTAB-8498',
                   'E-MTAB-8509',
                   'E-MTAB-8530',
                   'E-MTAB-8559',
                   'E-MTAB-8561',
                   'E-MTAB-8656',
                   'E-MTAB-8662',
                   'E-MTAB-8751',
                   'E-MTAB-8810',
                   'E-MTAB-8884',
                   'E-MTAB-8894',
                   'E-MTAB-8911',
                   'E-MTAB-9061',
                   'E-MTAB-9067',
                   'E-MTAB-9154',
                   'E-MTAB-9221',
                   'E-MTAB-9388',
                   'E-MTAB-9435',
                   'E-MTAB-9583',
                   'E-MTAB-9689',
                   'E-MTAB-9801',
                   'E-MTAB-9906',
                   'HTAN_BU_CD45Neg',
                   'HTAN_BU_CD45Pos',
                   'HTAN_CHOP_integrated_18MLLr_normal_final_rename',
                   'HTAN_CHOP_pool_logNorm_gini_FiveHD_10Xv3_downsample10000HSPC',
                   'HTAN_CHOP_regrCycleHeatShockGenes_pool_18Infants_scRNA_VEG3000_updated_rename',
                   'HTAN_HTAPP_crc10x_L4',
                   'HTAN_MSK_NSCLC_epithelial_010920',
                   'HTAN_MSK_SCLC_RU1215_010920',
                   'HTAN_MSK_combined_mnnc_010920',
                   'HTAN_MSK_epithelial_010920',
                   'HTAN_MSK_immune_010920',
                   'HTAN_MSK_immune_SCLC_samples_only_010920',
                   'HTAN_MSK_mesenchymal_updated_010920',
                   'HTAN_MSK_myeloid_010920',
                   'HTAN_MSK_myeloid_SCLC_samples_only_010920',
                   'HTAN_MSK_tcell_010920',
                   'HTAN_Stanford',
                   'HTAN_Vanderbilt_VUMC_ABNORMALS_EPI_V2',
                   'HTAN_Vanderbilt_VUMC_HTAN_DIS_EPI_V2',
                   'HTAN_Vanderbilt_VUMC_HTAN_VAL_DIS_NONEPI_V2',
                   'HTAN_Vanderbilt_VUMC_HTAN_VAL_EPI_V2',
                   'PUBMED32079746_10k',
                   'PUBMED32079746_12k',
                   'PUBMED32079746_6k',
                   'SCP1039',
                   'SCP1049',
                   'SCP1052',
                   'SCP1060',
                   'SCP1064_1',
                   'SCP1064_2',
                   'SCP1064_3',
                   'SCP1064_4',
                   'SCP1064_5',
                   'SCP1064_6',
                   'SCP1080',
                   'SCP1081',
                   'SCP109_1',
                   'SCP109_2',
                   'SCP109_3',
                   'SCP109_4',
                   'SCP109_5',
                   'SCP109_6',
                   'SCP1106',
                   'SCP1155',
                   'SCP1182',
                   'SCP1184',
                   'SCP1186',
                   'SCP1187',
                   'SCP1213',
                   'SCP1214',
                   'SCP1216',
                   'SCP1244',
                   'SCP1245_1',
                   'SCP1245_2',
                   'SCP1245_3',
                   'SCP1245_4',
                   'SCP1245_5',
                   'SCP1245_6',
                   'SCP1248',
                   'SCP1265',
                   'SCP1289',
                   'SCP1290',
                   'SCP1311_1',
                   'SCP1311_2',
                   'SCP1311_3',
                   'SCP1311_4',
                   'SCP1311_5',
                   'SCP1318',
                   'SCP133',
                   'SCP1332',
                   'SCP1345',
                   'SCP1361',
                   'SCP1365',
                   'SCP1366',
                   'SCP1376_1',
                   'SCP1376_2',
                   'SCP1376_Homosapiens',
                   'SCP1376_Musmusculus',
                   'SCP1386',
                   'SCP1387',
                   'SCP1388',
                   'SCP1389',
                   'SCP1390',
                   'SCP1391',
                   'SCP1422',
                   'SCP1423',
                   'SCP1457',
                   'SCP1493',
                   'SCP1526',
                   'SCP1539_1',
                   'SCP1539_2',
                   'SCP1539_3',
                   'SCP1547',
                   'SCP1661',
                   'SCP167',
                   'SCP1675',
                   'SCP1677_1',
                   'SCP1677_2',
                   'SCP17',
                   'SCP1711',
                   'SCP18',
                   'SCP199',
                   'SCP207_1',
                   'SCP207_2',
                   'SCP207_3',
                   'SCP212_1',
                   'SCP212_10',
                   'SCP212_2',
                   'SCP212_3',
                   'SCP212_4',
                   'SCP212_5',
                   'SCP212_6',
                   'SCP212_7',
                   'SCP212_8',
                   'SCP212_9',
                   'SCP24',
                   'SCP241_1',
                   'SCP241_2',
                   'SCP241_3',
                   'SCP253_1',
                   'SCP253_2',
                   'SCP253_3',
                   'SCP256',
                   'SCP257_1',
                   'SCP257_2',
                   'SCP263',
                   'SCP282_1',
                   'SCP282_2',
                   'SCP282_3',
                   'SCP282_4',
                   'SCP282_5',
                   'SCP282_6',
                   'SCP282_7',
                   'SCP301',
                   'SCP31',
                   'SCP330',
                   'SCP331',
                   'SCP332',
                   'SCP344',
                   'SCP371',
                   'SCP375',
                   'SCP377',
                   'SCP381',
                   'SCP393',
                   'SCP422',
                   'SCP43',
                   'SCP454_1',
                   'SCP454_2',
                   'SCP454_3',
                   'SCP454_4',
                   'SCP454_5',
                   'SCP454_6',
                   'SCP454_7',
                   'SCP468',
                   'SCP469_1',
                   'SCP469_2',
                   'SCP471',
                   'SCP473',
                   'SCP474',
                   'SCP475',
                   'SCP476',
                   'SCP477',
                   'SCP478',
                   'SCP479',
                   'SCP482',
                   'SCP484',
                   'SCP489',
                   'SCP490',
                   'SCP498',
                   'SCP499',
                   'SCP50',
                   'SCP500',
                   'SCP503',
                   'SCP509_1',
                   'SCP509_2',
                   'SCP542',
                   'SCP548',
                   'SCP550',
                   'SCP553',
                   'SCP554',
                   'SCP557',
                   'SCP558',
                   'SCP559',
                   'SCP560',
                   'SCP563',
                   'SCP564',
                   'SCP565',
                   'SCP596',
                   'SCP60',
                   'SCP639',
                   'SCP640',
                   'SCP641',
                   'SCP644',
                   'SCP645',
                   'SCP646',
                   'SCP647',
                   'SCP648',
                   'SCP649',
                   'SCP650',
                   'SCP651',
                   'SCP652',
                   'SCP653',
                   'SCP658',
                   'SCP659',
                   'SCP660',
                   'SCP661',
                   'SCP662',
                   'SCP663',
                   'SCP664',
                   'SCP665',
                   'SCP666',
                   'SCP667',
                   'SCP708',
                   'SCP76',
                   'SCP795_1',
                   'SCP795_2',
                   'SCP795_3',
                   'SCP796_1',
                   'SCP796_2',
                   'SCP8',
                   'SCP806',
                   'SCP807_1',
                   'SCP807_2',
                   'SCP807_3',
                   'SCP807_4',
                   'SCP812',
                   'SCP812_1',
                   'SCP812_2',
                   'SCP814_1',
                   'SCP814_2',
                   'SCP817_1',
                   'SCP817_2',
                   'SCP817_3',
                   'SCP817_4',
                   'SCP822_1',
                   'SCP822_2',
                   'SCP822_3',
                   'SCP822_4',
                   'SCP829',
                   'SCP832',
                   'SCP840',
                   'SCP846',
                   'SCP860',
                   'SCP865',
                   'SCP867',
                   'SCP868',
                   'SCP869',
                   'SCP870',
                   'SCP871',
                   'SCP873',
                   'SCP874',
                   'SCP875',
                   'SCP876',
                   'SCP877',
                   'SCP878',
                   'SCP879',
                   'SCP880',
                   'SCP881',
                   'SCP883',
                   'SCP884',
                   'SCP885',
                   'SCP886',
                   'SCP887',
                   'SCP891',
                   'SCP894',
                   'SCP895',
                   'SCP897',
                   'SCP898',
                   'SCP899',
                   'SCP90',
                   'SCP900',
                   'SCP901',
                   'SCP902',
                   'SCP903',
                   'SCP919',
                   'SCP928',
                   'SCP929',
                   'SCP930',
                   'SCP931',
                   'SCP947_1',
                   'SCP947_2',
                   'SCP947_3',
                   'SCP947_4',
                   'SCP947_5',
                   'SCP947_6',
                   'SCP947_7',
                   'SCP97',
                   'SCP971',
                   'TS_Bladder',
                   'TS_Blood',
                   'TS_Bone_Marrow',
                   'TS_Eye',
                   'TS_Fat',
                   'TS_Heart',
                   'TS_Kidney',
                   'TS_Large_Intestine',
                   'TS_Liver',
                   'TS_Lung',
                   'TS_Lymph_Node',
                   'TS_Mammary',
                   'TS_Muscle',
                   'TS_Pancreas',
                   'TS_Prostate',
                   'TS_Salivary_Gland',
                   'TS_Skin',
                   'TS_Small_Intestine',
                   'TS_Spleen',
                   'TS_Thymus',
                   'TS_Tongue',
                   'TS_Trachea',
                   'TS_Uterus',
                   'TS_Vasculature',
                   'Tabula_Sapiens',
                   'adata_myeloid_SCLC_samples_only_010920',
                   'aldinger20_processed',
                   'baron16_processed',
                   'byrd20_gingiva_processed',
                   'byrd_warner_integrated_processed',
                   'cheng18_processed',
                   'deprez19_restricted.processed',
                   'guo18_donor_processed',
                   'habib17_processed',
                   'henry18_0_processed',
                   'james20_processed',
                   'lako_cornea_processed',
                   'litvinukova20_restricted_processed',
                   'lukassen20_airway_orig_processed',
                   'lukassen20_lung_orig_processed',
                   'lukassen_airway_restricted.processed',
                   'lukowski19_processed',
                   'macparland18_processed',
                   'madissoon19_lung_processed',
                   'madissoon20_oesophagus_processed',
                   'madissoon20_spleen_processed',
                   'martin19_processed',
                   'menon19_processed',
                   'meyer_nikolic_covid_airway',
                   'meyer_nikolic_covid_pbmc',
                   'miller20_processed',
                   'park20_processed',
                   'popescu19_processed',
                   'smillie19_epi_processed',
                   'stewart19_adult_processed',
                   'vallier_restricted_processed',
                   'vento18_10x_processed',
                   'vento18_ss2_processed',
                   'vento_pbmc_processed',
                   'vieira19_Alveoli_and_parenchyma_anonymised_processed',
                   'vieira19_Bronchi_anonymised_processed',
                   'vieira19_Nasal_anonymised_processed',
                   'vieira19_bronchi_restricted.processed',
                   'vieira19_nasal_restricted.processed',
                   'vieira19_parenchyma_restricted.processed',
                   'voigt19_processed',
                   'wang20_colon_processed',
                   'wang20_ileum_processed']


def get_query_results(query):
    """
    Given a query for Polly-python, return the resultant DF
    Args:
        query: SQL Query

    Returns:
        DataFrame: Response to the query
    """
    return OMIXATLAS.query_metadata(query, query_api_version="v2")


"""----Functions for repo-wise dataset level metadata validation----"""


def dataset_metadata_validator_construct_args_for_pool(repos):
    """
    Function to create arguments for pool of workers to run
    Args:
        repos:

    Returns:

    """
    args_for_pool = defaultdict(list)
    for repo in repos:
        print(f'Getting datasets for: {repo}')
        t_start = dt.now()
        # todo: remove the specific condition after run
        # dataset_metadatas = get_query_results(f"SELECT * FROM {repo}.datasets")
        dataset_metadatas = get_query_results(f"SELECT * FROM {repo}.datasets where dataset_source != 'GEO'")
        print(f'Actual time taken to run the query: {dt.now() - t_start}')

        print(f'Getting schema for: {repo}')
        t_start = dt.now()
        schema_df = get_query_results(f'DESCRIBE {repo}.datasets')
        print(f'Actual time taken to run the query: {dt.now() - t_start}')

        for val in dataset_metadatas.to_dict('records'):
            args_for_pool[repo].append((repo, schema_df, val))
    return args_for_pool


def check_datasets_in_repo_for_errors(repos):
    """

    Args:
        repo:

    Returns:

    """
    compiled_error_df = pd.DataFrame(columns=['Field', 'Error Message', 'Error Type', 'Repo',
                                              'dataset_id', 'key'])
    try:
        num_repos = len(repos)
        args_for_pool = dataset_metadata_validator_construct_args_for_pool(repos)
        print(f'RAM Usage: {psutil.virtual_memory().percent}%')
        ctr = 1
        print(f'Compiling errors...')
        print(f'\nWill use {psutil.cpu_count(logical=False)} cores at my disposal...\n')
        chunk_size = 10000
        for repo in repos:
            chunk_no = 1
            print(f'Working on repo: {repo} | Count: {ctr}/{num_repos}')
            total_chunks = len(args_for_pool[repo]) // chunk_size
            tstart = dt.now()
            for args in chunks(args_for_pool[repo], chunk_size):
                print(f'Chunk: {chunk_no}/{total_chunks}')
                process_pool = Pool(processes=psutil.cpu_count(logical=False))
                error_df_results = process_pool.starmap(dataset_metadata_validator.validate_dataset_metadata,
                                                        tqdm(args, total=len(args)))

                # error_df_results = pd.concat(error_df_results, ignore_index=True)
                error_dfs = [res[0] for res in error_df_results]
                compiled_error_df = pd.concat([compiled_error_df, pd.concat(error_dfs, ignore_index=True)],
                                              ignore_index=True)
                del error_df_results, error_dfs
                gc.collect()
                chunk_no += 1
                print(f'RAM Usage: {psutil.virtual_memory().percent}%')
            print(f'Time Taken: {dt.now() - tstart}\n')
            ctr += 1
        compiled_error_df.reset_index(inplace=True, drop=True)
        print(f'RAM Usage: {psutil.virtual_memory().percent}%')
        return compiled_error_df
    except Exception as err:
        print(f'Error when collecting errors: {tb.format_exc()}')
        print_exception()
    return pd.DataFrame(columns=['Field', 'Error Message', 'Error Type', 'Repo',
                                 'dataset_id', 'key'])


"""----Functions for repo-wise sample level metadata validation----"""


def get_samples_for_dataset_id(ds_id):
    matched_samples = get_query_results(
        f"SELECT * FROM sc_data_lake.samples_singlecell where src_dataset_id = '{ds_id}'")
    return matched_samples


def sample_metadata_validator_construct_args_for_pool(repos):
    """

    Args:
        repos:

    Returns:

    """
    args_for_pool = defaultdict(list)
    for repo in repos:
        print(f'Getting samples for: {repo}')
        t_start = dt.now()
        if repo == 'sc_data_lake':
            # samples = get_query_results(f'SELECT * FROM {repo}.samples_singlecell')
            """Code for getting all samples of sc_data_lake"""
            all_samples_df = []
            for chunk in chunks(dataset_id_list, 100):
                matched_samples = get_query_results(
                    f"SELECT * FROM {repo}.samples_singlecell where src_dataset_id in {*chunk,}")
                all_samples_df.append(matched_samples)
            samples = pd.concat(all_samples_df, ignore_index=True)
            print(f'{len(samples)} Samples collected.')
        else:
            samples = get_query_results(f'SELECT * FROM {repo}.samples')
            print(f'{len(samples)} Samples collected.')
        print(f'Actual time taken to run the query: {dt.now() - t_start}')
        if repo == 'sc_data_lake':
            schema_df = get_query_results(f'DESCRIBE {repo}.samples_singlecell')
        else:
            schema_df = get_query_results(f'DESCRIBE {repo}.samples')
        for val in samples.to_dict('records'):
            args_for_pool[repo].append((repo, schema_df, val))
    return args_for_pool


def check_samples_in_repo_for_errors(repos):
    """
    Given a list of repos, go repo by repo and collect errors
    Args:
        repos:list of repos

    Returns:
        pandas DataFrame: containing the errors collected from all the repos
    """
    compiled_error_df = pd.DataFrame(columns=['Field', 'Error Message', 'Error Type', 'Repo',
                                              'src_dataset_id', 'data_id', 'sample_id'])
    try:
        num_repos = len(repos)
        args_for_pool = sample_metadata_validator_construct_args_for_pool(repos)
        print(f'RAM Usage: {psutil.virtual_memory().percent}%')
        ctr = 1
        print(f'Compiling errors...')
        print(f'\nWill use {psutil.cpu_count(logical=False)} cores at my disposal...\n')
        chunk_size = 100000
        for repo in repos:
            chunk_no = 1
            print(f'Working on repo: {repo} | Count: {ctr}/{num_repos}')
            total_chunks = len(args_for_pool[repo]) // chunk_size
            tstart = dt.now()
            for args in chunks(args_for_pool[repo], chunk_size):
                print(f'Chunk: {chunk_no}/{total_chunks}')
                process_pool = Pool(processes=psutil.cpu_count(logical=False))
                error_df_results = process_pool.starmap(sample_metadata_validator.validate_sample_metadata,
                                                        tqdm(args, total=len(args)))
                # error_df_results = pd.concat(error_df_results, ignore_index=True)
                error_dfs = [res[0] for res in error_df_results]
                compiled_error_df = pd.concat([compiled_error_df, pd.concat(error_dfs, ignore_index=True)],
                                              ignore_index=True)
                del error_df_results, error_dfs
                gc.collect()
                chunk_no += 1
                print(f'RAM Usage: {psutil.virtual_memory().percent}%')
            print(f'Time Taken: {dt.now() - tstart}\n')
            ctr += 1
        compiled_error_df.reset_index(inplace=True, drop=True)
        print(f'RAM Usage: {psutil.virtual_memory().percent}%')
        return compiled_error_df
    except Exception as err:
        print(f'Error when collecting errors: {tb.format_exc()}')
        print_exception()
    return pd.DataFrame(columns=['Field', 'Error Message', 'Error Type', 'Repo',
                                 'src_dataset_id', 'data_id', 'sample_id'])


if __name__ == '__main__':
    # Run the error collection routine
    try:
        # Initialize DB connection and connect
        engine = create_engine(f'sqlite:///polly_validator/{DB_NAME}')
        # Create an SQLAlchemy connection tob an SQLite object with name: DB_NAME
        conn = engine.connect()
        if RUN_DATASET_LEVEL_VALIDATIONS:
            """Running Dataset Level Error Collection"""
            print(f'\nCollecting errors in dataset metadata from repos: {REPOS_FOR_DATASET_LEVEL_VALIDATION}')
            # Get the compiled error table.
            compiled_dataset_level_errors_df = check_datasets_in_repo_for_errors(REPOS_FOR_DATASET_LEVEL_VALIDATION)
            if not compiled_dataset_level_errors_df.empty:
                # If the DB exists, append to the table.
                compiled_dataset_level_errors_df = compiled_dataset_level_errors_df.astype(str)
                compiled_dataset_level_errors_df.to_sql(DATASET_ERRORS_TABLE, conn, if_exists='replace', chunksize=1000)
                print(f'\nErrors added to table: {DATASET_ERRORS_TABLE}\nDB: {DB_NAME}\n')
            else:
                print(f'Empty Errors Table Compiled.')

        if RUN_SAMPLE_LEVEL_VALIDATIONS:
            """Running Sample Level Error Collection"""
            print(f'\nCollecting errors in sample metadata from repos: {REPOS_FOR_SAMPLE_LEVEL_VALIDATION}')
            compiled_sample_level_errors_df = check_samples_in_repo_for_errors(REPOS_FOR_SAMPLE_LEVEL_VALIDATION)
            if not compiled_sample_level_errors_df.empty:
                # If the table exists, append to the table.
                compiled_sample_level_errors_df = compiled_sample_level_errors_df.astype(str)
                compiled_sample_level_errors_df.to_sql(SAMPLE_ERRORS_TABLE, conn, if_exists='replace', chunksize=1000)
                print(f'\nErrors added to table: {SAMPLE_ERRORS_TABLE}\nDB: {DB_NAME}\n')
            else:
                print(f'Empty Errors Table Compiled.')

        # Close the DB connection
        conn.close()
    except Exception as e:
        print(tb.format_exc())
        print_exception()
