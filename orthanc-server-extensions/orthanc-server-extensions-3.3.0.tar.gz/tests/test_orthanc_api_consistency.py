import re

import httpx

from orthanc_ext.orthanc import OrthancApiHandler

orthanc = OrthancApiHandler()


def test_change_type_list_should_be_complete():
    events = get_type_enum_values('OrthancPluginChangeType')
    assert len(events) > 16
    for event in events:
        assert orthanc.ChangeType.__dict__.get(
            event) is not None, f'{event} should be added on {orthanc.ChangeType}'


def test_resource_type_list_should_be_complete():
    events = get_type_enum_values('OrthancPluginResourceType')
    assert len(events) > 4
    for event in events:
        assert (
            orthanc.ResourceType.__dict__.get(event)
            is not None), f"'{event} should be added on {orthanc.ResourceType}"


def get_type_enum_values(type_under_test):
    resp = httpx.get(
        f'https://hg.orthanc-server.com/orthanc-python/raw-file/'
        f'tip/Sources/Autogenerated/sdk_{type_under_test}.impl.h')
    resp.raise_for_status()
    return re.findall(f'sdk_{type_under_test}_Type.tp_dict, "([A-Z_]+)"', resp.text)
