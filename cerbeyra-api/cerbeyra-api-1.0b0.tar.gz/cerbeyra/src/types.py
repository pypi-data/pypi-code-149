from enum import Enum


class APIurls(Enum):
    login = '/api/login'
    cerbeyra_index = '/api/cerbeyraindex'
    report_network = '/api/reportnetworkvuln'
    report_web = '/api/reportwebvuln'


class PartnerAPIurls(Enum):
    clients_list = '/api/clients'
    report_network = '/api/clients/{client_id}/reportnetworkvuln'
    report_web = '/api/clients/{client_id}/reportwebvuln'
    cerbeyra_index = '/api/clients/{client_id}/cerbeyraindex'
    probes_list = '/api/clients/probes'
    sensor_list = '/api/clients/sensors'


class IoTStatus(Enum):
    ALIVE = 'ALIVE'
    WARNING = 'WARNING'
    DANGER = 'DANGER'


class NetworkReportFields(Enum):
    asset = 'asset'
    host = 'host'
    hostname = 'hostname'
    vulnerability = 'vulnerability'
    description = 'description'
    threat = 'threat'
    solution = 'solution'
    vuln_id = 'vuln_id'
    last_detection = 'last_detection'
    first_detection = 'first_detection'
    protocol = 'protocol'
    port = 'port'
    cvss = 'cvss'
    summary = 'summary'
    insight = 'insight'
    impact = 'impact'
    affected = 'affected'
    references = 'references'


class WebReportFields(Enum):
    asset = 'asset'
    host = 'host'
    hostname = 'hostname'
    vulnerability = 'vulnerability'
    description = 'description'
    threat = 'threat'
    solution = 'solution'
    vuln_id = 'vuln_id'
    last_detection = 'last_detection'
    first_detection = 'first_detection'
    other = 'other'
    param = 'param'
    attack = 'attack'
    evidence = 'evidence'
    response = 'response'
    request = 'request',
    family = 'family'
    url = 'url'
    method = 'method'


network_default_columns = [
    el.value for el in [
        NetworkReportFields.asset, NetworkReportFields.host, NetworkReportFields.hostname, NetworkReportFields.protocol,
        NetworkReportFields.port, NetworkReportFields.threat, NetworkReportFields.cvss,
        NetworkReportFields.vulnerability,
        NetworkReportFields.description, NetworkReportFields.summary, NetworkReportFields.insight,
        NetworkReportFields.impact,
        NetworkReportFields.affected, NetworkReportFields.solution, NetworkReportFields.references,
        NetworkReportFields.vuln_id,
        NetworkReportFields.last_detection, NetworkReportFields.first_detection
    ]
]

web_default_columns = [
    el.value for el in [
        WebReportFields.asset, WebReportFields.host, WebReportFields.family, WebReportFields.vulnerability,
        WebReportFields.description, WebReportFields.threat, WebReportFields.solution, WebReportFields.url,
        WebReportFields.method, WebReportFields.vuln_id, WebReportFields.last_detection
    ]
]
