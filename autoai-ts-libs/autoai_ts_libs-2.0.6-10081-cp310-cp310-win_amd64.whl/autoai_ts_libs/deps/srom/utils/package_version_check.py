# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


def check_pyspark_version():
    try:
        import pyspark

        # due to a bug in spark 3.1 with dill
        # we can only support 3.0 for now
        # https://issues.apache.org/jira/browse/SPARK-32079
        '''
        if pyspark.__version__.find("3.0") < 0:
            raise Exception(
                f"pyspark version {pyspark.__version__} is not supported, please use use 3.0<=pyspark<3.1"
                ""
            )
        '''
    except ImportError as _:
        print("please install 3.0<=pyspark<3.1")
        raise
