from __future__ import annotations

class Graph():
    def __init__(
            self, 
            datasetNodes: list = None, 
            edges: list = None,
        ):
        self.datasetNodes = datasetNodes
        self.edges = edges

class GraphEdge(object):
    def __init__(
        self, 
        sourceOutputPort: PortInfo = None, 
        destinationInputPort: PortInfo = None, 
        ):
        self.sourceOutputPort = sourceOutputPort
        self.destinationInputPort = destinationInputPort

class PortInfo(object):
    def __init__(
        self, 
        nodeId: str = None, 
        portName: str = None, 
        graphPortName: str = None, 
        isParameter: bool = False,
        ):
        self.nodeId = nodeId
        self.portName = portName
        self.graphPortName = graphPortName
        self.isParameter = isParameter 

    def __eq__(self, other: PortInfo):
        return {
            self.nodeId == other.nodeId
            and self.portName == other.portName 
            and self.graphPortName == other.graphPortName 
            and self.isParameter == other.isParameter 
        }

class GraphDatasetNode(object):
    def __init__(
        self, 
        id: str = None, 
        dataSetDefinition: DataSetDefinition = None, 
        ):
        self.id = id
        self.dataSetDefinition  = dataSetDefinition 

class DataSetDefinition(object):
    def __init__(
        self, 
        parameterName: str = None, 
        dataTypeShortName: str = None, 
        ):
        self.parameterName = parameterName
        self.dataTypeShortName = dataTypeShortName