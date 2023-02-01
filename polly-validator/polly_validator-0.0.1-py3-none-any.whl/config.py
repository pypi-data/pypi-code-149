CONFIG = {
    "run_dataset_level_validations": False,
    "run_sample_level_validations": True,
    "repos_for_dataset_level_validation": [
        "sc_data_lake",
    ],
    "repos_for_sample_level_validation": [
        "sc_data_lake",
    ],

    "last_commit_for_obo_ontology_files": "39312b6",
    "last_commit_for_compressed_ontology_files": "feff3be",
    "env": ["polly", "devpolly", "testpolly"],

    "dataset_errors_table_name": "DatasetLevelErrors",
    "sample_errors_table_name": "SampleLevelErrors",
    "job_details": {
        "image": "docker.polly.elucidata.io/elucidatarnd/qa_repo",
        "tag": "repo_wise_run",
        "machineType": "mi5xlarge",
        "env": {
            "PROJECT_DIR": "polly_validator",
            "DB_NAME": "repo_wise_single_cell_sample_level_source_not_GEO_Run_2.db"
        },
        "name": "QA Validation Error Collection"
    }
}
