import json
import unittest
from typing import List

from panther_sdk import detection, schema, PantherEvent


class TestPantherSDKTest(unittest.TestCase):
    def test_data_models_work(self) -> None:
        def get_name(event: PantherEvent) -> str:
            return event.get("name") or event.get("username") or ""

        def check_name_max(event: PantherEvent) -> bool:
            return bool(event.udm("name") == "max")

        def use() -> None:
            schema.DataModel(
                data_model_id="aws.alb",
                name="AWS ALB",
                log_type=schema.LogTypeAWSALB,
                enabled=True,
                mappings=[schema.DataModelMapping(name="name", func=get_name)],
            )

            schema.DataModel(
                data_model_id="aws.eks",
                name="AWS EKS",
                log_type=schema.LogTypeAmazonEKSAudit,
                enabled=True,
                mappings=[
                    schema.DataModelMapping(name="name", path="$.name"),
                ],
            )

            schema.DataModel(
                data_model_id="soc.alert",
                name="soc alert",
                log_type=schema.LogTypeAlphaSOCAlert,
                enabled=True,
                mappings=[
                    schema.DataModelMapping(name="name", path="name"),
                ],
            )

            unit_tests: List[detection.JSONUnitTest] = [
                # match
                detection.JSONUnitTest(
                    name="name is max on eks",
                    expect_match=True,
                    data=json.dumps(
                        {"p_log_type": schema.LogTypeAmazonEKSAudit, "name": "max"}
                    ),
                ),
                detection.JSONUnitTest(
                    name="name is max on alb",
                    expect_match=True,
                    data=json.dumps({"p_log_type": schema.LogTypeAWSALB, "name": "max"}),
                ),
                detection.JSONUnitTest(
                    name="name is max on soc alert",
                    expect_match=True,
                    data=json.dumps({"p_log_type": schema.LogTypeAlphaSOCAlert, "name": "max"}),
                ),
                # no match
                detection.JSONUnitTest(
                    name="name is john on eks",
                    expect_match=False,
                    data=json.dumps(
                        {"p_log_type": schema.LogTypeAmazonEKSAudit, "name": "john"}
                    ),
                ),
                detection.JSONUnitTest(
                    name="name is john on alb",
                    expect_match=False,
                    data=json.dumps({"p_log_type": schema.LogTypeAWSALB, "name": "john"}),
                ),
                detection.JSONUnitTest(
                    name="name is john on soc alert",
                    expect_match=False,
                    data=json.dumps(
                        {"p_log_type": schema.LogTypeAlphaSOCAlert, "name": "john"}
                    ),
                ),
                # missing
                detection.JSONUnitTest(
                    name="name is john on eks",
                    expect_match=False,
                    data=json.dumps({"p_log_type": schema.LogTypeAmazonEKSAudit}),
                ),
                detection.JSONUnitTest(
                    name="name is john on alb",
                    expect_match=False,
                    data=json.dumps({"p_log_type": schema.LogTypeAWSALB}),
                ),
                detection.JSONUnitTest(
                    name="name is john on soc alert",
                    expect_match=False,
                    data=json.dumps({"p_log_type": schema.LogTypeAlphaSOCAlert}),
                ),
            ]

            detection.Rule(
                rule_id="rule.use.udm",
                name="Rule Use UDM",
                log_types=[
                    schema.LogTypeAWSALB,
                    schema.LogTypeAmazonEKSAudit,
                    schema.LogTypeAlphaSOCAlert,
                ],
                severity=detection.SeverityCritical,
                filters=[
                    detection.PythonFilter(func=check_name_max),
                ],
                unit_tests=unit_tests,
            )

        use()
