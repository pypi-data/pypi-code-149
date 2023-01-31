import unittest
import pickle
import os.path
import shutil
import pathlib
from sklearn.linear_model import LogisticRegression
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.wml.pipeline_skeleton import *
from autoai_ts_libs.deps.srom.wml import pipeline_skeleton


class TestPipelineSkeleton(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srom_pipeline = SROMPipeline()
        cls.srom_pipeline.set_stages([[LogisticRegression()]])

        dir_path = pathlib.Path(__file__).parent.absolute()
        X = pd.read_csv(os.path.join(dir_path, "../datasets/X.csv"))
        y = pd.read_csv(os.path.join(dir_path, "../datasets/y.csv"))
        cls.X = X
        cls.y = y
        X.to_csv("X.csv", compression="gzip", index=False)
        y.to_csv("Y.csv", compression="gzip", index=False)
        cls.srom_save_path = "tmp_pipeline.pkl"

    def testPipelineSkeleton(self):
        classObj = self.__class__
        srom_pipeline = classObj.srom_pipeline
        srom_pipeline.execute(classObj.X, classObj.y)
        pickle.dump(srom_pipeline, open(classObj.srom_save_path, "wb"))
        os.environ["DATA_DIR"] = "./"
        os.environ["RESULT_DIR"] = "./"
        parser = argparse.ArgumentParser(description="SROM pipeline execution on WML")
        parser = parse_execution_cmd(parser)
        kwargs = [
            "--train_x",
            "X.csv",
            "--train_y",
            "Y.csv",
            "--exectype",
            "single_node_random_search",
        ]
        args = parser.parse_args(kwargs)

        exit_code = pipeline_skeleton.pipeline_skeleton((args))
        self.assertTrue(os.path.exists(classObj.srom_save_path))
        self.assertTrue(os.path.exists("X.csv"))
        self.assertTrue(os.path.exists("Y.csv"))
        self.assertTrue(os.path.exists("./results/"))

    @classmethod
    def tearDownClass(cls):
        os.remove("X.csv")
        os.remove("Y.csv")
        os.remove(cls.srom_save_path)
        shutil.rmtree("./results/")


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
