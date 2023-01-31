"""
Unit test cases for AutoAIEstimator.
"""
import unittest
import time
import numpy as np
from sklearn.model_selection import train_test_split
from autoai_ts_libs.deps.srom.wml.AutoAIEstimator import AutoAIEstimator
from sklearn.datasets import make_classification
import logging

LOGGER = logging.getLogger(__name__)


class TestAutoAIEstimator(unittest.TestCase):
    """Test class for AutoAIEstimator"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        import os
        cls.start_time = time.time()
        cls.api_key = os.environ["WML_CREDENTIALS_APIKEY"]
        cls.deployment_space_name = os.environ["WML_DEPLOYMENT_SPACE_NAME"]
        cls.wml_credentials = {
            "apikey": cls.api_key,
            "url": "https://us-south.ml.cloud.ibm.com",
        }

        try:
            from ibm_watson_machine_learning.client import APIClient
        except ImportError:
            LOGGER.error("ImportError : ibm_watson_machine_learning is not installed ")
            pass

        client = APIClient(cls.wml_credentials)
        space = client.spaces.get_details()
        ans = [
            item["metadata"]["id"]
            for item in space["resources"]
            if item["entity"]["name"] == cls.deployment_space_name
        ]
        cls.space_id = ans[0]

        cls.X, cls.y = make_classification(n_samples=800)
        cls.X_train, cls.X_valid, cls.y_train, cls.y_valid = train_test_split(
            cls.X, cls.y, test_size=0.2, random_state=1234
        )
        cls.p_label = str(np.max(cls.y))
        cls.scoring = "neg_mean_absolute_error"

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        t = time.time() - cls.start_time
        print('%s: %.3f' % (cls.id(), t))

    def verify_wml_credentials(self, wml_credentials):
        """Verfiy the wml_credentials"""
        self.assertIsNotNone(wml_credentials)
        self.assertTrue("apikey" in wml_credentials)
        self.assertIsNotNone(wml_credentials["apikey"])
        self.assertNotEqual(wml_credentials["apikey"], "")
        self.assertTrue("url" in wml_credentials)
        self.assertIsNotNone(wml_credentials["url"])
        self.assertNotEqual(wml_credentials["url"], "")

    def test_autoai_estm(self):

        self.verify_wml_credentials(self.wml_credentials)

        ac1 = AutoAIEstimator(
            wml_credentials=self.wml_credentials,
            space_id=self.space_id,
            prediction_type="regression",
            target_column=str(self.X_train.shape[1]),
            background_mode=False,
            scoring=None,
            t_shirt_size="l",
            positive_label=self.p_label,
        )
        self.assertIsNotNone(ac1)

        ac = AutoAIEstimator(
            wml_credentials=self.wml_credentials,
            space_id=self.space_id,
            prediction_type="classification",
            target_column=str(self.X_train.shape[1]),
            background_mode=False,
            scoring=self.scoring,
            t_shirt_size="l",
            positive_label=self.p_label,
        )
        self.assertIsNotNone(ac.fit(self.X_train, self.y_train))
        try:
            import lale
            import lightgbm

            self.assertIsNotNone(ac.predict(self.X_valid))
            self.assertIsNotNone(ac.predict_proba(self.X_valid))
            self.assertIsNotNone(ac.check_status())
            self.assertIsNotNone(ac.summary())
            self.assertIsNotNone(ac.get_best_pipeline())
            self.assertIsNotNone(ac.get_number_of_pipeline_enhancement())
            self.assertIsNotNone(ac.get_pipeline_details())
            self.assertIsNotNone(ac.get_all_pipelines())
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)

