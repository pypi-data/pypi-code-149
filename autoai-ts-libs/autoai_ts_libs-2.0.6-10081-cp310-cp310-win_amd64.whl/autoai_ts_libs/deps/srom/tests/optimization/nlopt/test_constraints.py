# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing classes under constraints.py"""
import unittest
import numpy as np
from autoai_ts_libs.deps.srom.optimization.nlopt.constraints import MinBoundFunctor, MaxBoundFunctor

class TestMinBoundFunctor(unittest.TestCase):
    """Test class for MinBoundFunctor class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        pass

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_bound_method(self):
        """test MinBoundFunctor bound method"""
        mbf = MinBoundFunctor('a', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(-1, mbf.bound())
        mbf = MinBoundFunctor('b', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(2, mbf.bound())

    def test_call_method(self):
        """test MinBoundFunctor call method"""
        mbf = MinBoundFunctor('a', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(1, mbf(np.array([0, 1])))
        mbf = MinBoundFunctor('b', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(-1, mbf(np.array([0, 1])))

class TestMaxBoundFunctor(unittest.TestCase):
    """Test class for MaxBoundFunctor class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        pass

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_bound_method(self):
        """test MaxBoundFunctor bound method"""
        mbf = MaxBoundFunctor('a', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(1, mbf.bound())
        mbf = MaxBoundFunctor('b', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(4, mbf.bound())

    def test_call_method(self):
        """test MaxBoundFunctor call method"""
        mbf = MaxBoundFunctor('a', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(1, mbf(np.array([0, 1])))
        mbf = MaxBoundFunctor('b', ['a', 'b'], dict(a=np.array([-1, 0, 1]), b=np.array([2, 3, 4])))
        self.assertEqual(3, mbf(np.array([0, 1])))

