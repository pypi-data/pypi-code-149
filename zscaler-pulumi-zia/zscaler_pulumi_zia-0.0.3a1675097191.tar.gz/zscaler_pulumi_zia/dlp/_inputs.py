# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DLPDictionariesExactDataMatchDetailArgs',
    'DLPDictionariesIdmProfileMatchAccuracyArgs',
    'DLPDictionariesIdmProfileMatchAccuracyAdpIdmProfileArgs',
    'DLPDictionariesPatternArgs',
    'DLPDictionariesPhraseArgs',
    'DLPWebRulesAuditorArgs',
    'DLPWebRulesDepartmentsArgs',
    'DLPWebRulesDlpEnginesArgs',
    'DLPWebRulesExcludedDepartmentsArgs',
    'DLPWebRulesExcludedGroupsArgs',
    'DLPWebRulesExcludedUsersArgs',
    'DLPWebRulesGroupsArgs',
    'DLPWebRulesIcapServerArgs',
    'DLPWebRulesLabelsArgs',
    'DLPWebRulesLocationGroupsArgs',
    'DLPWebRulesLocationsArgs',
    'DLPWebRulesNotificationTemplateArgs',
    'DLPWebRulesTimeWindowsArgs',
    'DLPWebRulesUrlCategoriesArgs',
    'DLPWebRulesUsersArgs',
]

@pulumi.input_type
class DLPDictionariesExactDataMatchDetailArgs:
    def __init__(__self__, *,
                 dictionary_edm_mapping_id: Optional[pulumi.Input[int]] = None,
                 primary_field: Optional[pulumi.Input[int]] = None,
                 schema_id: Optional[pulumi.Input[int]] = None,
                 secondary_field_match_on: Optional[pulumi.Input[str]] = None,
                 secondary_fields: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        :param pulumi.Input[int] dictionary_edm_mapping_id: The unique identifier for the EDM mapping.
        :param pulumi.Input[int] primary_field: The EDM template's primary field.
        :param pulumi.Input[int] schema_id: The unique identifier for the EDM template (or schema).
        :param pulumi.Input[str] secondary_field_match_on: The EDM secondary field to match on.
               - `"MATCHON_NONE"`
               - `"MATCHON_ANY_1"`
               - `"MATCHON_ANY_2"`
               - `"MATCHON_ANY_3"`
               - `"MATCHON_ANY_4"`
               - `"MATCHON_ANY_5"`
               - `"MATCHON_ANY_6"`
               - `"MATCHON_ANY_7"`
               - `"MATCHON_ANY_8"`
               - `"MATCHON_ANY_9"`
               - `"MATCHON_ANY_10"`
               - `"MATCHON_ANY_11"`
               - `"MATCHON_ANY_12"`
               - `"MATCHON_ANY_13"`
               - `"MATCHON_ANY_14"`
               - `"MATCHON_ANY_15"`
               - `"MATCHON_ALL"`
        :param pulumi.Input[Sequence[pulumi.Input[int]]] secondary_fields: The EDM template's secondary fields.
        """
        if dictionary_edm_mapping_id is not None:
            pulumi.set(__self__, "dictionary_edm_mapping_id", dictionary_edm_mapping_id)
        if primary_field is not None:
            pulumi.set(__self__, "primary_field", primary_field)
        if schema_id is not None:
            pulumi.set(__self__, "schema_id", schema_id)
        if secondary_field_match_on is not None:
            pulumi.set(__self__, "secondary_field_match_on", secondary_field_match_on)
        if secondary_fields is not None:
            pulumi.set(__self__, "secondary_fields", secondary_fields)

    @property
    @pulumi.getter(name="dictionaryEdmMappingId")
    def dictionary_edm_mapping_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique identifier for the EDM mapping.
        """
        return pulumi.get(self, "dictionary_edm_mapping_id")

    @dictionary_edm_mapping_id.setter
    def dictionary_edm_mapping_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dictionary_edm_mapping_id", value)

    @property
    @pulumi.getter(name="primaryField")
    def primary_field(self) -> Optional[pulumi.Input[int]]:
        """
        The EDM template's primary field.
        """
        return pulumi.get(self, "primary_field")

    @primary_field.setter
    def primary_field(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "primary_field", value)

    @property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique identifier for the EDM template (or schema).
        """
        return pulumi.get(self, "schema_id")

    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "schema_id", value)

    @property
    @pulumi.getter(name="secondaryFieldMatchOn")
    def secondary_field_match_on(self) -> Optional[pulumi.Input[str]]:
        """
        The EDM secondary field to match on.
        - `"MATCHON_NONE"`
        - `"MATCHON_ANY_1"`
        - `"MATCHON_ANY_2"`
        - `"MATCHON_ANY_3"`
        - `"MATCHON_ANY_4"`
        - `"MATCHON_ANY_5"`
        - `"MATCHON_ANY_6"`
        - `"MATCHON_ANY_7"`
        - `"MATCHON_ANY_8"`
        - `"MATCHON_ANY_9"`
        - `"MATCHON_ANY_10"`
        - `"MATCHON_ANY_11"`
        - `"MATCHON_ANY_12"`
        - `"MATCHON_ANY_13"`
        - `"MATCHON_ANY_14"`
        - `"MATCHON_ANY_15"`
        - `"MATCHON_ALL"`
        """
        return pulumi.get(self, "secondary_field_match_on")

    @secondary_field_match_on.setter
    def secondary_field_match_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_field_match_on", value)

    @property
    @pulumi.getter(name="secondaryFields")
    def secondary_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        The EDM template's secondary fields.
        """
        return pulumi.get(self, "secondary_fields")

    @secondary_fields.setter
    def secondary_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "secondary_fields", value)


@pulumi.input_type
class DLPDictionariesIdmProfileMatchAccuracyArgs:
    def __init__(__self__, *,
                 adp_idm_profile: Optional[pulumi.Input['DLPDictionariesIdmProfileMatchAccuracyAdpIdmProfileArgs']] = None,
                 match_accuracy: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['DLPDictionariesIdmProfileMatchAccuracyAdpIdmProfileArgs'] adp_idm_profile: The IDM template reference.
        :param pulumi.Input[str] match_accuracy: The IDM template match accuracy.
               - `"LOW"`
               - `"MEDIUM"`
               - `"HEAVY"`
        """
        if adp_idm_profile is not None:
            pulumi.set(__self__, "adp_idm_profile", adp_idm_profile)
        if match_accuracy is not None:
            pulumi.set(__self__, "match_accuracy", match_accuracy)

    @property
    @pulumi.getter(name="adpIdmProfile")
    def adp_idm_profile(self) -> Optional[pulumi.Input['DLPDictionariesIdmProfileMatchAccuracyAdpIdmProfileArgs']]:
        """
        The IDM template reference.
        """
        return pulumi.get(self, "adp_idm_profile")

    @adp_idm_profile.setter
    def adp_idm_profile(self, value: Optional[pulumi.Input['DLPDictionariesIdmProfileMatchAccuracyAdpIdmProfileArgs']]):
        pulumi.set(self, "adp_idm_profile", value)

    @property
    @pulumi.getter(name="matchAccuracy")
    def match_accuracy(self) -> Optional[pulumi.Input[str]]:
        """
        The IDM template match accuracy.
        - `"LOW"`
        - `"MEDIUM"`
        - `"HEAVY"`
        """
        return pulumi.get(self, "match_accuracy")

    @match_accuracy.setter
    def match_accuracy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "match_accuracy", value)


@pulumi.input_type
class DLPDictionariesIdmProfileMatchAccuracyAdpIdmProfileArgs:
    def __init__(__self__, *,
                 extensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[int]] = None):
        if extensions is not None:
            pulumi.set(__self__, "extensions", extensions)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "extensions", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class DLPDictionariesPatternArgs:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 pattern: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] action: The action applied to a DLP dictionary using patterns. The following values are supported:
        :param pulumi.Input[str] pattern: DLP dictionary pattern
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        The action applied to a DLP dictionary using patterns. The following values are supported:
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        """
        DLP dictionary pattern
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)


@pulumi.input_type
class DLPDictionariesPhraseArgs:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 phrase: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] action: The action applied to a DLP dictionary using patterns. The following values are supported:
        :param pulumi.Input[str] phrase: DLP dictionary phrase
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if phrase is not None:
            pulumi.set(__self__, "phrase", phrase)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        The action applied to a DLP dictionary using patterns. The following values are supported:
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def phrase(self) -> Optional[pulumi.Input[str]]:
        """
        DLP dictionary phrase
        """
        return pulumi.get(self, "phrase")

    @phrase.setter
    def phrase(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phrase", value)


@pulumi.input_type
class DLPWebRulesAuditorArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[int]):
        """
        :param pulumi.Input[int] id: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[int]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[int]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class DLPWebRulesDepartmentsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesDlpEnginesArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesExcludedDepartmentsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesExcludedGroupsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesExcludedUsersArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesGroupsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesIcapServerArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[int]):
        """
        :param pulumi.Input[int] id: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[int]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[int]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class DLPWebRulesLabelsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesLocationGroupsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesLocationsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesNotificationTemplateArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[int]):
        """
        :param pulumi.Input[int] id: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[int]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[int]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class DLPWebRulesTimeWindowsArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesUrlCategoriesArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


@pulumi.input_type
class DLPWebRulesUsersArgs:
    def __init__(__self__, *,
                 ids: pulumi.Input[Sequence[pulumi.Input[int]]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] ids: Identifier that uniquely identifies an entity
        """
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def ids(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        Identifier that uniquely identifies an entity
        """
        return pulumi.get(self, "ids")

    @ids.setter
    def ids(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "ids", value)


