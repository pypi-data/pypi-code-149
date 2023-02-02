# General imports
import os
import re
from dataclasses import dataclass

# PyQt imports
from PyQt5.QtCore import QPoint, QRect, QSize
from PyQt5.QtGui import QColor

@dataclass
class OpenModelicaInput:
    type: str
    name: str
    value: float = 0

    def __str__(self):
        return f"{self.type} {self.name} (start = {self.value})"

@dataclass
class OpenModelicaOutput:
    type: str
    name: str

    def __str__(self):
        return f"{self.type} {self.name}"

@dataclass
class OpenModelicaTransformation:
    origin: QPoint
    extent: list[QPoint]
    rotation: int

    def boundingRect(self):
        return QRect(self.topLeft(), self.size())

    def size(self) -> QSize:
        if self.extent is not None:
            return QSize(self.extent[1].x() - self.extent[0].x(), self.extent[1].y() - self.extent[0].y())
        else:
            return QSize()

    def topLeft(self) -> QPoint:
        topLeft = QPoint()

        if self.origin is not None:
            topLeft += self.origin

        if self.extent is not None:
            topLeft += self.extent[0]

        return topLeft

    def transformOrigin(self) -> QPoint:
        return self.boundingRect().center()

    def __str__(self) -> str:
        string_list = []
        
        if self.origin is not None:
            string_list.append(f"origin = {{{self.origin.x()}, {self.origin.y()}}}")
            
        if self.extent is not None:
            string_list.append(f"extent = {{{{{self.extent[0].x()}, {self.extent[0].y()}}}, {{{self.extent[1].x()}, {self.extent[1].y()}}}}}")
            
        if self.rotation is not None:
            string_list.append(f"rotation = {self.rotation}")
            
        return ", ".join(string_list)
    
@dataclass
class OpenModelicaComponentAnnotation:
    visible: bool
    transformation: OpenModelicaTransformation = None

    def __str__(self) -> str:
        return f"Placement(visible = {str(self.visible).lower()}, transformation({self.transformation}))"
    
@dataclass
class OpenModelicaComponent:
    library: str
    name: str
    annotation: OpenModelicaComponentAnnotation = None

    def boundingRect(self) -> QRect:
        if self.annotation is not None and self.annotation.transformation is not None:
            return self.annotation.transformation.boundingRect()
        else:
            return QRect()

    def rotation(self) -> int:
        if self.annotation is not None and self.annotation.transformation is not None:
            return self.annotation.transformation.rotation
        else:
            return 0

    def topLeft(self) -> QPoint:
        if self.annotation is not None and self.annotation.transformation is not None:
            return self.annotation.transformation.topLeft()
        else:
            return QPoint()

    def transformOrigin(self) -> QPoint:
        if self.annotation is not None and self.annotation.transformation is not None:
            return self.annotation.transformation.transformOrigin()
        else:
            return QPoint()

    def size(self) -> QSize:
        if self.annotation is not None and self.annotation.transformation is not None:
            return self.annotation.transformation.size()
        else:
            return QSize()

    def __str__(self):
        return f"{self.library} {self.name} annotation({self.annotation})"

@dataclass
class OpenModelicaLine:
    points: list[QPoint]
    color: QColor

    def __str__(self) -> str:
        points_str = ", ".join([f"{{{point.x()}, {point.y()}}}" for point in self.points])
        color_str = f"{{{self.color.red()}, {self.color.green()}, {self.color.blue()}}}"
        return f"points = {{{points_str}}}, color = {color_str}"

@dataclass
class OpenModelicaConnectionAnnotation:
    line: OpenModelicaLine

    def __str__(self) -> str:
        return f"Line({self.line})"

@dataclass
class OpenModelicaConnection:
    node1_name: str
    node2_name: str
    annotation: OpenModelicaConnectionAnnotation = None

    def points(self) -> list[QPoint]:
        if self.annotation is not None and self.annotation.line is not None:
            return self.annotation.line.points

    def __str__(self) -> str:
        return f"connect({self.node1_name}, {self.node2_name}) annotation({self.annotation})"


class OpenModelicaModelParser:

    # General Open Modelica model regex
    GlobalModelPattern = r"\Amodel\s(?P<model_name_1>\w+){1}\s(?P<model_content>.+);end\s(?P<model_name_2>\w+){1};\Z"

    # Declaration Part - Variables & Component patterns
    InputPattern = r"(?i)input\s*(?P<type>\w+)\s*(?P<name>\w+)\s*(?:\(start\s*\=\s*(?P<start_value>[0-9]+)\))?"
    OutputPattern = r"(?i)output\s*(?P<type>\w+)\s*(?P<name>\w+)"
    ComponentPattern = r"(?i)(?P<library>\w+(?:\.\w+)+)\s+(?P<name>\w+)\s*(?:\((?P<parameters>.*)\))?\s+annotation\s*\(\s*(?P<annotation>.*)\)"
    ComponentParameterPattern = r"(?i)(?P<name>\w+)\s*(?:\(\s*(?P<added_parameter>\w+)\s*=\s*(?P<added_parameter_value>true|false|[+-]?[0-9]+(?:\.[0-9]*)?|\"[a-z]*\")\))?\s*(?:=\s*(?P<value>true|false|[+-]?[0-9]+(?:\.[0-9]*)?|\"[a-z]*\"))?"
    ComponentAnnotationPattern = r"(?i)Placement\s*\(\s*(?:visible\s*=\s*(?P<visible>true|false),?)?\s*,?\s*\s*(?P<transformation>transformation\s*\(.*\))?\s*\)\s*"

    # Equation part - Equations, connections & annotation
    ConnectionPattern = r"(?i)connect\(\s*(?P<node_1>.*)\s*,\s*(?P<node_2>.*)\s*\)\s+annotation\(\s*(?P<annotation>.*)\s*\)"
    ConnectionAnnotationPattern = r"(?i)line\s*\(\s*points\s*=\s*{\s*(?P<points>(?:\s*{\s*[+-]?[0-9]+\s*,\s*[+-]?[0-9]+\s*}\s*,?)+)\s*}\s*,\s*color\s*=\s*(?P<color>{\s*(?P<red>[0-9]+)\s*,\s*(?P<green>[0-9]+)\s*,\s*(?P<blue>[0-9]+)})\s*\)"
    
    # Data extractor regexes
    ColorRegex = r"{\s*(?P<red>[0-9]{1,3})\s*,\s*(?P<green>[0-9]{1,3})\s*,\s*(?P<blue>[0-9]{1,3})\s*}"
    PointRegex = r"{\s*(?P<x>[+-]?[0-9]+)\s*,\s*(?P<y>[+-]?[0-9]+)\s*}"
    TransformationPattern = r"(?i)transformation\s*\(\s*(origin\s*=\s*\{\s*(?P<origin_x>[+-]?[0-9]*)\s*,\s*(?P<origin_y>[+-]?[0-9]*)\s*\}\s*,?)?\s*(extent\s*=\s*\{\{(?P<extent_0_x>[+-]?[0-9]*)\s*,\s*(?P<extent_0_y>[+-]?[0-9]*)\s*\}\s*,\s*\{(?P<extent_1_x>[+-]?[0-9]*)\s*,\s*(?P<extent_1_y>[+-]?[0-9]*)\s*\}\}\s*,?)?\s*(rotation\s*=\s*(?P<rotation>[+-]?[0-9]*),?)?\s*\)\s*"

    def __init__(self, om_file_path: str) -> None:
        # Test if file exists
        if not os.path.exists(om_file_path):
            raise(FileNotFoundError(f"File not found: {om_file_path}"))

        # Path
        self.path = om_file_path

        # Read file
        file_content = ""
        with open(self.path, mode='r') as f:
            file_content = f.read().strip()

        # Test if empty file
        if file_content == "":
            raise(Exception("Empty file"))

        # Parse file
        self.inputs: list[OpenModelicaInput] = []
        self.outputs: list[OpenModelicaOutput] = []
        self.components: list[OpenModelicaComponent] = []
        self.connections: list[OpenModelicaConnection] = []
        self.other_init_rows = []
        self.other_equation_rows = []
        self.parse_file(file_content)

    def parse_file(self, file_content):
        content = file_content.replace('\n', '')

        if re.match(OpenModelicaModelParser.GlobalModelPattern, content):
            for match in re.finditer(OpenModelicaModelParser.GlobalModelPattern, content):
                # Get component name
                model_name_1 = match.groupdict()["model_name_1"]

                # Get component name
                model_name_2 = match.groupdict()["model_name_2"]

                if model_name_1 != model_name_2:
                    raise(Exception("Model file has wrong model construction: starting model name ({model_name_1}) is not the same as the end ({model_name_2})"))

                self.model_name = model_name_1

                # Get content
                model_content = match.groupdict()["model_content"].strip()

                # Separate content into parts -> (items declaration, equations...)
                init_content, equations_content = model_content.split("equation", maxsplit=2)

                # Declaration handling
                init_rows = [row.strip() for row in init_content.split(";")]
                
                for init_row in init_rows:
                    # Input
                    if init_row == "":
                        pass
                    elif re.match(OpenModelicaModelParser.InputPattern, init_row):
                        for input_match in re.finditer(OpenModelicaModelParser.InputPattern, init_row):
                            input_match_dict = input_match.groupdict()
                            input_type = input_match_dict["type"]
                            input_name = input_match_dict["name"]
                            input_value = 0 if not "start_value" in input_match_dict else input_match_dict["start_value"]

                            self.inputs.append(OpenModelicaInput(input_type, input_name, input_value))

                    # Output
                    elif re.match(OpenModelicaModelParser.OutputPattern, init_row):
                        for output_match in re.finditer(OpenModelicaModelParser.OutputPattern, init_row):
                            output_type = output_match.groupdict()["type"]
                            output_name = output_match.groupdict()["name"]

                            self.outputs.append(OpenModelicaOutput(output_type, output_name))

                    # Component
                    elif re.match(OpenModelicaModelParser.ComponentPattern, init_row):
                        for component_match in re.finditer(OpenModelicaModelParser.ComponentPattern, init_row):
                            component_library = component_match.groupdict()["library"]
                            component_name = component_match.groupdict()["name"]
                            component_annotation = component_match.groupdict()["annotation"]

                            component = OpenModelicaComponent(component_library, component_name)

                            for annotation_match in re.finditer(OpenModelicaModelParser.ComponentAnnotationPattern, component_annotation):
                                annotation_visible = bool(annotation_match.groupdict()["visible"])
                                annotation_transformation = annotation_match.groupdict()["transformation"]

                                annotation = OpenModelicaComponentAnnotation(annotation_visible)
                                if annotation_transformation is not None: 
                                    for transformation_match in re.finditer(OpenModelicaModelParser.TransformationPattern, annotation_transformation):
                                        transformation_origin_x = int(transformation_match.groupdict()["origin_x"])
                                        transformation_origin_y = int(transformation_match.groupdict()["origin_y"])
                                        transformation_extent_0_x = int(transformation_match.groupdict()["extent_0_x"])
                                        transformation_extent_0_y = int(transformation_match.groupdict()["extent_0_y"])
                                        transformation_extent_1_x = int(transformation_match.groupdict()["extent_1_x"])
                                        transformation_extent_1_y = int(transformation_match.groupdict()["extent_1_y"])
                                        transformation_rotation = int(transformation_match.groupdict()["rotation"])

                                        origin_coords = [transformation_origin_x, transformation_origin_y]
                                        extent_coords = [transformation_extent_0_x, transformation_extent_0_y, transformation_extent_1_x, transformation_extent_1_y]

                                        # Add transformation to annotation
                                        annotation.transformation = OpenModelicaTransformation(
                                            origin=None if any(coord is None for coord in origin_coords) else QPoint(transformation_origin_x, transformation_origin_y),
                                            extent=None if any(coord is None for coord in extent_coords) else [QPoint(transformation_extent_0_x, transformation_extent_0_y), QPoint(transformation_extent_1_x, transformation_extent_1_y)],
                                            rotation = transformation_rotation
                                        )

                                # Add annotation to component
                                component.annotation = annotation

                            self.components.append(component)
                    else:
                        self.other_init_rows.append(init_row)

                # Equations handling
                equation_rows = [row.strip() for row in equations_content.split(";")]

                connections = []
                for equation_row in equation_rows:
                    if equation_row == "":
                        pass
                    elif re.match(OpenModelicaModelParser.ConnectionPattern, equation_row):
                        for connection_match in re.finditer(OpenModelicaModelParser.ConnectionPattern, equation_row):
                            connection_node_1 = connection_match.groupdict()["node_1"]
                            connection_node_2 = connection_match.groupdict()["node_2"]
                            connection_annotation = connection_match.groupdict()["annotation"]

                            connection = OpenModelicaConnection(connection_node_1, connection_node_2)
                            for connection_annotation_match in re.finditer(OpenModelicaModelParser.ConnectionAnnotationPattern, connection_annotation):

                                # Extract points
                                points_string = connection_annotation_match.groupdict()["points"]
                                points = [QPoint(int(point_match.groupdict()["x"]), int(point_match.groupdict()["y"])) for point_match in re.finditer(OpenModelicaModelParser.PointRegex, points_string)]

                                # Extract color
                                red = int(connection_annotation_match.groupdict()["red"])
                                green = int(connection_annotation_match.groupdict()["green"])
                                blue = int(connection_annotation_match.groupdict()["blue"])

                                line = OpenModelicaLine(points, QColor(red, green, blue))

                                connection.annotation = OpenModelicaConnectionAnnotation(line)

                            connections.append(connection)
                    else:
                        self.other_equation_rows.append(equation_row)

                # Save to object
                self.connections = connections

    def save_file_as(self, output_file_path: str):
        if output_file_path == "":
            raise(ValueError("Empty string given for output file path"))
        else:
            dirname = os.path.dirname(output_file_path)
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            # Build output model
            file_content = f"model {self.model_name}\n"

            # Inputs
            file_content += '\n'.join([f"  input {input_});" for input_ in self.inputs])
            file_content += '\n'

            # Outputs
            file_content += '\n'.join([f"  output {output};" for output in self.outputs])
            file_content += '\n'

            # Components
            file_content += '\n'.join([f"  {component});" for component in self.components])
            file_content += '\n'

            # Other init rows
            file_content += '\n'.join([f"{other_init_row};" for other_init_row in self.other_init_rows])
            file_content += '\n'

            # Equation part
            file_content += "equation\n"
            
            # Connection
            file_content += '\n'.join([f"  {connection};" for connection in self.connections])

            # Other init rows
            file_content += '\n'.join([f"  {other_equation_row};" for other_equation_row in self.other_equation_rows])
            file_content += '\n'

            # End of file
            file_content += f"end {self.model_name};"

            # with open(output_file_path, "w") as f:
            #     f.write(file_content)

    def set_input_value(self, input_name: str, input_value: float):
        for input_ in self.inputs:
            if input_.name == input_name:
                input_.name = input_value

    def __str__(self):
        to_print = ["* Inputs *"]
        for input_ in self.inputs:
            to_print.append(f"\t - {input_}")

        to_print.append("* Outputs *")
        for output in self.outputs:
            to_print.append(f"\t - {output}")

        to_print.append("* Components *")
        for component in self.components:
            to_print.append(f"\t - {component}")

        to_print.append("* Connections *")
        for connection in self.connections:
            to_print.append(f"\t - {connection}")

        return "\n".join(to_print)
        