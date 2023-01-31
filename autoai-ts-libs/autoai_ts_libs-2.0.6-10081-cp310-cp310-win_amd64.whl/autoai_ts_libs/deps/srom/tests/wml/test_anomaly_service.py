"""
Unit test cases for anomaly service trainer.
"""
import unittest
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.wml.wrappers.onprem.anomaly_service import AnomalyWMLTrainer
from pathlib import Path
import os
import subprocess
from subprocess import PIPE, run
from contextlib import contextmanager


class TestAnomalyWMLTrainer(unittest.TestCase):
    """Test class for TestWMLtrainer"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        day = 24 * 60 * 60
        year = 365.2425 * day

        def load_dataframe() -> pd.DataFrame:
            """ Create a time series x sin wave dataframe. """
            df = pd.DataFrame(columns=["date", "sin"])
            df.date = pd.date_range(start="2018-01-01", end="2018-03-01", freq="D")
            df.sin = 1 + np.sin(df.date.astype("int64") // 1e9 * (2 * np.pi / year))
            df.sin = (df.sin * 100).round(2)
            df.date = df.date.apply(lambda d: d.strftime("%Y-%m-%d"))
            return df

        cls.X = load_dataframe()
        cls.param_dict = {
            "--algorithm_type": "WINDOWAD",
            "--execution_mode": "BATCH",
            "--feature_columns": "sin",
            "--outputdataName": "sample.json",
            "--target_columns": "sin",
            "--time_column": "date",
            "--time_format": "%Y-%m-%d",
            "--total_execution_time": 2,
        }
        cls.api_key = os.environ["WML_CREDENTIALS_APIKEY"]
        cls.deployment_space_name = os.environ["WML_DEPLOYMENT_SPACE_NAME"]
        cls.wml_credentials = {
            "apikey": cls.api_key,
            "url": "https://us-south.ml.cloud.ibm.com",
        }

        @contextmanager
        def cwd(path):
            oldpwd = os.getcwd()
            os.chdir(path)
            try:
                yield
            finally:
                os.chdir(oldpwd)

        p = Path(os.path.abspath(__file__)).parents[3]
        with cwd(p):
            distdir = os.path.join(p, "dist")
            run(["rm", "-rf", "dist"], cwd=p, check=True)
            run(
                ["python", "setup.py", "sdist", "--formats=zip"],
                cwd=p,
                check=True,
                stdout=subprocess.DEVNULL,
            )
            src = (
                run(["ls"], stdout=PIPE, cwd=distdir, check=True)
                .stdout.strip()
                .decode("utf-8")
            )
            run(["mv", src, "srom.zip"], cwd=distdir, check=True)
            cls.zip_path = os.path.join(distdir, "srom.zip")

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def verify_wml_credentials(self, wml_credentials):
        """Verfiy the wml_credentials"""
        self.assertIsNotNone(wml_credentials)
        self.assertTrue("apikey" in wml_credentials)
        self.assertIsNotNone(wml_credentials["apikey"])
        self.assertNotEqual(wml_credentials["apikey"], "")

    def test_wml_trainer(self):
        self.verify_wml_credentials(self.wml_credentials)
        trainer = AnomalyWMLTrainer()
        trainer.connect(
            wml_credentials=self.wml_credentials,
            deployment_space_name=self.deployment_space_name,
            cos_credentials=None,
        )

        trainer.add_data(self.X)
        trainer.add_local_library(self.zip_path)
        trainer.set_exec_config(exec_config=self.param_dict)
        cor = trainer._cos_resource

        bucket_list = [
            trainer._metadata["train_bucket_name"],
            trainer._metadata["result_bucket_name"],
        ]
        for bucket in bucket_list:
            for object in cor.Bucket(bucket).objects.all():
                cor.Object(bucket, object.key).delete()
            cor.Bucket(bucket).delete()
        # trainer.execute()
        # trainer.clean_up()
        # trainer.display_logs()
        # self.assertIsNotNone(trainer.status())
        # self.assertIsNotNone(trainer.fetch_results())
        # self.assertIsNotNone(trainer.retrieve_logs())


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
