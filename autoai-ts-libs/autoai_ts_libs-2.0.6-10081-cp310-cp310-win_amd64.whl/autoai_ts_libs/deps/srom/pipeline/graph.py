# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
    .. module:: graph
       :synopsis: SROM Graph Management.

    .. moduleauthor:: SROM Team
"""
import logging
import tempfile
import os
from pkg_resources import resource_filename

import networkx as nx
from networkx.drawing.nx_pydot import write_dot

from autoai_ts_libs.deps.srom.utils import pipeline_utils
from autoai_ts_libs.deps.srom.utils.copy_utils import deeper_copy
from autoai_ts_libs.deps.srom.utils.pipeline_utils import GraphType
from inspect import signature

LOGGER = logging.getLogger(__name__)


class SROMGraph(object):
    """
    SROMGraph is the object which store the information and the meta information \
    of the SROM graph.

    This class expands the definition of srom graph. The current graph can be thought of \
    as a 2 dimensional graph where layers can be specified pertaining to a machine learning \
    task like 'scaling', 'feature engineering' and 'modelling'. Each layer has certain \
    components for that layer. It is refered to as a 2d `stages`: It refers to a list of list, \
    where each element of the inner list may be a python object or a tuple in this format- \
    ('object name', object).

    This class expands on the definition by making srom `stages` as a 3D object; where it comprises \
    of multiple 2d graphs.
    """

    SOURCE_NODE_LABEL = "Start"

    def __init__(self, graphtype=GraphType.Default.value):
        self._stages = None
        self.stage_dim = None
        self._total_nodes = 0
        self.graphtype = graphtype
        self._graph = nx.DiGraph()

    def _validate_2d_stages(self, stages):
        """
        Validates and updates the 2d `stages` from the user.

        This function performs 2 kinds of checks:
            - if a 2d stage is list of list of tuples or not.
                If not, then it replaces the standalone object with a tuple \
                which looks like - ('object name', object).
            - if there any duplicate components in the 2d stages.

        Parameters:
            stages: User defined 2d stage value.

        Returns:
            validated_stages: Stages on which necessary checks and updates \
                have been performed.
        """
        validated_stages = []

        hashables = set()
        for stage in stages:
            tmp_opt = []
            for option in stage:

                # check to see if the item in list of lists is a tuple or not,
                # if not, update is performed through some text wrangling.
                if not isinstance(option, tuple):
                    # temp hack
                    # (see https://github.ibm.com/srom/srom/issues/121#issuecomment-4620387)
                    taskname = "%s" % option.__class__.__name__.lower()
                    if taskname in hashables:
                        LOGGER.warning(
                            "Found duplicate stage name %s, will rename with index.",
                            taskname,
                        )
                        count = 1
                        while taskname in hashables:
                            taskname = "%s_%d" % (taskname, count)
                            count += 1
                    option = (taskname, option)
                # two liner replaces a big function
                # pipeline_utils.check_duplicate_stage_names(stages)

                if self.graphtype == GraphType.Functional.value:
                    if not callable(option[1]):
                        raise Exception(
                            "%s is not a callable function in FunctionalPipeline."
                            % repr(option)
                            + " Only callable function objects allowed!"
                        )

                if option[0] in hashables or id(option[1]) in hashables:
                    raise Exception(
                        "duplicate pipeline name (or object) %s detected, \
                    this is not allowed!"
                        % repr(option)
                    )

                if self.graphtype == GraphType.Default.value:
                    hashables.add(option[0])
                    hashables.add(id(option[1]))
                elif self.graphtype == GraphType.Functional.value:
                    hashables.add(option[0])

                tmp_opt.append(deeper_copy(option))
            validated_stages.append(tmp_opt)

        return validated_stages

    def set_stages(self, stages):
        """
        Method for setting a 2d stage by the user.

        NOTE: This method also resets the self._stages.

        Parameters:
            stages: User defined 2d stage value.
        """
        # refresh and 2D graph init
        pipeline_utils.check_srom_pipeline_stages(stages)
        self._stages = self._validate_2d_stages(stages)
        self.stage_dim = 2
        self._compile_graph()

    def add_stages(self, stages):
        """
        Method for adding additional 2d stage by the user. \
        If the user has already called `set_stages()` before \
        then it converts self._stages to 3D stages.s.

        NOTE: This method does not resets the self._stages.

        
        Parameters:
            stages: User defined 2d stage value.
        """
        pipeline_utils.check_srom_pipeline_stages(stages)

        if self._stages is None:
            # if not initialized yet
            self._stages = self._validate_2d_stages(stages)
            self.stage_dim = 2
        else:
            # if already initialized once but 2d stages
            if self.stage_dim == 2:
                meta_stages = [self._stages]
            else:
                # if already initialized but already 3d stages
                meta_stages = self._stages

            meta_stages.append(self._validate_2d_stages(stages))
            self._stages = meta_stages
            self.stage_dim = 3

        self._compile_graph()

    def reset_stages(self):
        """
        Methods to reset the self._stages.
        """
        self._stages = None
        self.stage_dim = None

    def _init_graph_2d(self, stages, graph):
        """
        Generates the networkx graph for a 2d stage.
        """
        total_nodes_ = 0

        if self.graphtype == GraphType.Functional.value:
            for stage_arr in stages:
                for i, obj in enumerate(stage_arr):
                    total_nodes_ = total_nodes_ + 1
                    graph.add_node(obj, label=obj[0])
                    if i == 0:
                        parent = self.SOURCE_NODE_LABEL
                    else:
                        parent = stage_arr[i - 1]
                    graph.add_edge(parent, obj)
            return graph, total_nodes_

        if self.graphtype == GraphType.Default.value:
            last_level_nodes = [self.SOURCE_NODE_LABEL]

            for stage_arr in stages:
                for obj in stage_arr:
                    total_nodes_ = total_nodes_ + 1
                    graph.add_node(obj, label=obj[0])
                    for parent in last_level_nodes:
                        graph.add_edge(parent, obj)
                last_level_nodes = stage_arr

            return graph, total_nodes_

    def _init_graph(self):
        """
        Generates the networkx graph for current self.stage. \
        This should be called after set_stages. \

        Returns:
            total_nodes (int): Number of total nodes.
        """
        self._paths = []
        # A source node is added just for display purposes,
        # so that there is some start to all the pipeline paths
        # in the graph
        # initializing main graph
        try:
            self._graph = nx.DiGraph()
            total_nodes = 0
            self._graph.add_node(self.SOURCE_NODE_LABEL, label=self.SOURCE_NODE_LABEL)

            if self.stage_dim == 2:
                self._graph, total_nodes = self._init_graph_2d(
                    self._stages, self._graph
                )
            elif self.stage_dim == 3:
                for stage2d in self._stages:
                    self._graph, total_nodes_ = self._init_graph_2d(
                        stage2d, self._graph
                    )
                    total_nodes += total_nodes_

            self._total_nodes = total_nodes
            return total_nodes
        except Exception as ex:
            raise ex
            '''
            LOGGER.warning(ex)
            LOGGER.warning("falling back to simplified graph representation")
            self._graph = None
            import itertools

            nodes = 0
            for alist in self._stages:
                nodes += len(alist)
            self._simplegraph = list(itertools.product(*self._stages))
            return nodes
            '''
    def asimage(self, num_nodes=40):
        """
        From the stages set in the pipeline, create a graph object using networkx. \
        The graph is saved as dot file, pickle and image at the pipeline's storage location. \
        Graph File is generated only if number of node is < num_nodes.

        Parameters:
            num_nodes: Max value of nodes to display in the graph. Recommended to not exceed more than 40 as time 
                taken can be high.

        Returns:
             path_graph_image (String): Location where graph is stored.

        Raises:
            ImportError:
                If pydot module is not available. In this case, graph will not be drawn.
        """
        if self._graph is None:
            return resource_filename("srom.resources", "NoImageAvailable.png")

        if self._total_nodes > num_nodes:
            # if number of node > 40, we see there is a huge time taken by graph library
            LOGGER.warning(
                "Skipping creation of graph image, there are more than `num_nodes="
                + str(num_nodes)
                + "` nodes in the graph. Use parameter `num_nodes` to modify the number of nodes allowed "
                + "for display. Recommended is maximum 40 nodes due to time to render."
            )
            return resource_filename("srom.resources", "NoImageAvailable.png")
        else:
            # don't force pydot on us
            # sometimes it's not easy to install
            # like on CRL's showcase system
            try:
                import pydot
            except ImportError as _:
                LOGGER.warning(
                    "Can not import pydot, drawing of graph will not be possible."
                )
                return resource_filename("srom.resources", "NoImageAvailable.png")

            try:
                file_handle, path_graph = tempfile.mkstemp(suffix=".dot")
                os.close(file_handle)
                file_handle, path_graph_image = tempfile.mkstemp(suffix=".png")
                os.close(file_handle)
                # write .dot file
                write_dot(self._graph, path_graph)
                graph1 = pydot.graph_from_dot_file(path_graph)
                graph1[0].write_png(path_graph_image)
                # return a path of an image file so that user can print on Jupyter Notebook
                return path_graph_image
            except FileNotFoundError as fnfe:
                LOGGER.warning(fnfe)
                return resource_filename("srom.resources", "NoImageAvailable.png")

    @property
    def stages(self):
        return self._stages

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, value):
        self._paths = value

    @property
    def digraph(self):
        return self._graph

    @property
    def number_of_nodes(self):
        return self._graph.number_of_nodes()

    @property
    def number_of_edges(self):
        return self._graph.number_of_edges()

    def has_node(self, anode):
        # return self._total_nodes
        return self._graph.has_node(anode)

    def _generate_pipeline_paths(self):
        """
        Traverses the directed acyclic graph created in _init_graph \
        to obtain all pipeline execution paths.

        Add `self._paths` which is a unique list of modelling paths.
        """
        # Reset path
        self._paths = []
        # find the node with label - self.SOURCE_NODE_LABEL
        if self._graph:
            for node, data in self._graph.nodes.items():
                if data["label"] == self.SOURCE_NODE_LABEL:
                    source_node = node
                    break
        else:
            source_node = self._simplegraph
        # call a recursive function
        self._generate_pipeline_paths_from_a_node([], source_node)

    def _generate_pipeline_paths_from_a_node(self, path, node):
        """
        Recursive function to get all the paths reachable \
        from a particular node.

        Parameters:
            path (list): The path built so far.
            node: The node to currently traverse.
        """

        if isinstance(node, list):
            for apath in node:
                self._paths.append(apath)
            return

        # Do not add the source node to the path so that the paths can be directly
        # converted to pipelines
        if node != self.SOURCE_NODE_LABEL:
            path.append(node)
        # note: neighbors method used below is nondeterministic,
        # for same input, it can give different order of nodes
        nodes = self._graph.neighbors(node)

        # nodes = sorted(nodes) # Make order deterministic
        neighbors = []
        for node in nodes:
            neighbors.append(node)

        if not neighbors:
            path_copy = path[:]
            self._paths.append(path_copy)
            return

        for neighbor in neighbors:
            self._generate_pipeline_paths_from_a_node(path, neighbor)
            del path[-1]

    def _compile_graph(self):
        """
        Final function which compiles the self._stages to create \
        - pipeline graph in self._graph \
        - self._paths
        """
        self._init_graph()
        self._generate_pipeline_paths()
