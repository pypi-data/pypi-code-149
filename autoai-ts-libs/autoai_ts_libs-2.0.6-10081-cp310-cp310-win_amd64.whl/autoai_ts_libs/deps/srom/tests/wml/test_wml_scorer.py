# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Unit test cases for anomaly dag
"""
import unittest

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from autoai_ts_libs.deps.srom.wml.wrappers.cloud.scoring import WMLScorer
from sklearn.datasets import make_regression
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline


class TestWMLScorer(unittest.TestCase):
    """Test class for TestWMLScorer"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        import os

        cls.name = os.environ["WML_CREDENTIALS_NAME"]
        cls.api_key = os.environ["WML_CREDENTIALS_APIKEY"]
        cls.deployment_space_name = os.environ["WML_DEPLOYMENT_SPACE_NAME"]
        X, y = make_regression(n_samples=100, n_features=5, random_state=2)
        cls.X, cls.y = X, y
        cls.X_train, cls.X_valid, cls.y_train, cls.y_valid = train_test_split(
            cls.X, cls.y, test_size=0.2, random_state=1234
        )

        # Creating srom pipeline for execution
        cls.pipeline = SROMPipeline()
        cls.pipeline.set_stages([[("linear_reg", LinearRegression()),]])
        cls.pipeline.execute(cls.X_train, cls.y_train, exectype="single_node")
        cls.best_model = cls.pipeline.best_estimator
        cls.best_model.fit(cls.X_train, cls.y_train)

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
        self.assertTrue("name" in wml_credentials)
        self.assertIsNotNone(wml_credentials["name"])
        self.assertNotEqual(wml_credentials["name"], "")

    def test_connect(self):
        wml_credentials = {
            "name": self.name,
            "apikey": self.api_key,
            "url": "https://us-south.ml.cloud.ibm.com",
        }
        self.verify_wml_credentials(wml_credentials)

        scorer = WMLScorer()
        scorer.connect(
            wml_credentials, deployment_space_name=self.deployment_space_name
        )
        self.assertIsNotNone(scorer._wml_client)

        return_code, archive = scorer.add_pip_package(
            package_name="numpy", version="1.19.5"
        )
        self.assertEqual(return_code, 0)
        self.assertTrue("numpy-1.19.5" in archive)

    def test_wml_scorer(self):
        from autoai_ts_libs.deps.srom.wml.wrappers.cloud.scoring import WMLScorer

        wml_credentials = {
            "name": self.name,
            "apikey": self.api_key,
            "url": "https://us-south.ml.cloud.ibm.com",
        }
        self.verify_wml_credentials(wml_credentials)

        scorer = WMLScorer()
        scorer.connect(
            wml_credentials, deployment_space_name=self.deployment_space_name
        )

        prefix = "srom_travis_deployment"
        model_details, deployment_details = scorer.deploy_model(
            self.best_model,
            prefix,
            randomize_name=True,
            software_spec_type="default_py3.8",
        )
        self.assertIsNotNone(model_details)
        self.assertTrue(model_details["metadata"]["name"].startswith(prefix))
        self.assertIsNotNone(deployment_details)
        self.assertTrue(deployment_details["entity"]["name"].startswith(prefix))
        self.assertEqual(
            model_details["metadata"]["name"], deployment_details["entity"]["name"]
        )

        X_valid_scores = scorer.score(
            deployment_details, payload={"values": self.X_valid}
        )
        self.assertIsNotNone(X_valid_scores)
        self.assertEqual(
            len(X_valid_scores["predictions"][0]["values"]), self.X_valid.shape[0]
        )

        deployment_name = deployment_details["entity"]["name"]
        model_name = model_details["metadata"]["name"]
        response1 = scorer.delete_deployments(deployment_name)
        response2 = scorer.delete_models(model_name)
        self.assertEqual(response1, 1)
        self.assertEqual(response2, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)

