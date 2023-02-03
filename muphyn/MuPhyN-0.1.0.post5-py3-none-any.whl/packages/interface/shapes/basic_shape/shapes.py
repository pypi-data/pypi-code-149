from copy import deepcopy
from enum import Enum
from typing import Iterable, overload

from PyQt5.QtCore import QLine, QLineF, QPointF, QRectF, QSize,  QSizeF, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QGradient, QFont, QFontMetricsF, QGradient, QPainter, QPainterPath
from PyQt5.QtWidgets import QStyleOptionGraphicsItem, QApplication

from muphyn.packages.core.utils.log_manager import LogManager

from muphyn.packages.interface.shapes.basic_shape.abstract_shape import AbstractShape

class Circle(AbstractShape):

    center_changed = pyqtSignal()
    radius_changed = pyqtSignal()

    def __init__(self, center: QPointF, radius: float, border_color: QColor = Qt.GlobalColor.black, border_width: int = 1, 
                    line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, fill_color: QColor | QGradient = Qt.GlobalColor.transparent, parent=None):

        # Calc Pos & Size
        origin = Circle.calc_pos(center, radius)
        size = Circle.calc_size(center, radius)

        # Center (reset center position from origin)
        self._center = center - origin

        # Radius
        self._radius = radius


        super().__init__(origin, size, border_color, border_width, line_style, fill_color, parent=parent)

    # -------------
    # Properties
    # -------------
    @property
    def center(self) -> QPointF:
        return self._center

    @center.setter
    def center(self, new_center: QPointF) -> None:
        # Calc new origin
        new_origin = Circle.calc_pos(new_center, self._radius)

        if new_origin != self.pos():
            # Change position
            self.setPos(new_origin)
            self.position_changed.emit()

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, new_radius: float) -> None:
        if new_radius != self._radius:
            # Set new center
            self._center = QPointF(2*new_radius, 2*new_radius)

            # Set new radius
            self._radius = new_radius

            # Calc new origin & size
            new_origin = Circle.calc_pos(self._center, new_radius)
            new_size = Circle.calc_size(self._center, new_radius)

            # Set pos
            if new_origin != self.pos():
                # Change position
                self.setPos(new_origin)
                self.position_changed.emit()

            # Set size
            if new_size != self._size:
                self._size = new_size
                self.size_changed.emit()

    # -------------
    # Methods
    # -------------
    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawEllipse(self._center, self._radius, self._radius)
        
    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def calc_pos(center: QPointF, radius: float) -> QPointF:
        top_left = center - QPointF(radius, radius)
        return top_left

    @staticmethod
    def calc_size(center: QPointF, radius: float) -> QSizeF:
        size = QSizeF(2*radius, 2*radius)
        return size

class Ellipse(AbstractShape):

    center_changed = pyqtSignal()
    rx_changed = pyqtSignal()
    ry_changed = pyqtSignal()

    def __init__(self, center: QPointF, rx: float, ry: float, border_color: QColor, border_width: int = 1, 
                    line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, fill_color: QColor | QGradient = Qt.GlobalColor.transparent, parent=None):

        # Calc Pos & Size
        origin = Ellipse.calc_pos(center, rx, ry)
        size = Ellipse.calc_size(center, rx, ry)

        # Center (reset center position from origin)
        self._center = center - origin

        # Radius
        self._rx = rx
        self._ry = ry

        super().__init__(origin, size, border_color, border_width, line_style, fill_color, parent=parent)

    # -------------
    # Properties
    # -------------
    @property
    def center(self) -> QPointF:
        return self._center

    @center.setter
    def center(self, new_center: QPointF) -> None:
        # Calc new origin
        new_origin = Ellipse.calc_pos(new_center, self._radius)

        if new_origin != self.pos():
            # Change position
            self.setPos(new_origin)
            self.position_changed.emit()

    @property
    def rx(self) -> float:
        return self._rx

    @rx.setter
    def rx(self, new_rx: float) -> None:
        if new_rx != self._rx:
            # Set new center
            self._center = QPointF(2*new_rx, 2*self._ry)

            # Set new radius
            self._rx = new_rx

            # Calc new origin & size
            new_origin = Ellipse.calc_pos(self._center, new_rx, self._ry)
            new_size = Ellipse.calc_size(self._center, new_rx, self._ry)

            # Set pos
            if new_origin != self.pos():
                # Change position
                self.setPos(new_origin)
                self.position_changed.emit()

            # Set size
            if new_size != self._size:
                self._size = new_size
                self.size_changed.emit()

    # -------------
    # Methods
    # -------------
    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawEllipse(self._center, self._rx, self._ry)
        
    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def calc_pos(center: QPointF, rx: float, ry: float) -> QPointF:
        top_left = center - QPointF(rx, ry)
        return top_left

    @staticmethod
    def calc_size(rx: float, ry: float) -> QSizeF:
        size = QSizeF(2*rx, 2*ry)
        return size

class Line(AbstractShape):
    def __init__(self, line: QLine | QLineF, 
                    line_color: QColor = Qt.GlobalColor.black, line_width: int = 1, 
                    line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, parent=None):
        
        # Line format handle
        if not isinstance(line, QLineF):
            line = QLineF(line)

        # Calc Pos & Size
        origin = Line.calc_pos(line)
        size = Line.calc_size(line)

        # Reset line from object origin
        self._line = line
        self._from_origin_line = line.translated(-origin)

        super().__init__(origin, size, line_color, line_width, line_style, parent=parent)

    # -------------
    # Properties
    # -------------
    @property
    def line(self) -> QPointF:
        return self._from_origin_line

    @line.setter
    def line(self, new_line: QLine | QLineF) -> None:
        if not isinstance(new_line, QLineF):
            new_line = QLineF(new_line)

        if self._line != new_line:
            # Set new line
            self._line = new_line

            # Calc from origin line
            self._from_origin_line = new_line.translated(-new_origin)

            # Calc new origin & size
            new_origin = Line.calc_pos(new_line)
            new_size = Line.calc_size(new_line)

            # Set Pos
            if new_origin != self.pos():
                self.setPos(new_origin)
                self.position_changed.emit()

            # Set size
            self.setOrigin(new_origin)
            if new_size != self._size:
                self._size = new_size
                self.size_changed.emit()

    # -------------
    # Methods
    # -------------
    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawLine(self._from_origin_line)
    
    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def calc_pos(line: QLine | QLineF) -> QPointF:
        # Calculate top left
        top_left_x = min(line.x1(), line.x2())
        top_left_y = min(line.y1(), line.y2())

        return QPointF(top_left_x, top_left_y)

    @staticmethod
    def calc_size(line: QLine | QLineF) -> QSizeF:
        # Calculate top left
        top_left_x = min(line.x1(), line.x2())
        top_left_y = min(line.y1(), line.y2())

        # Calculate bottom right
        bottom_right_x = max(line.x1(), line.x2())
        bottom_right_y = max(line.y1(), line.y2())

        width = abs(bottom_right_x - top_left_x)
        height = abs(bottom_right_y - top_left_y)

        return QSizeF(width, height)

class Path(AbstractShape):

    class StepType(Enum):
        Line = 1
        Cubic = 2

    class Step():

        @overload
        def __init__(self, point: QPointF) -> None:
            ...

        @overload
        def __init__(self, c1: QPointF, c2: QPointF, end_point: QPointF) -> None:
            ...

        def __init__(self, *args: Iterable[QPointF]) -> None:
            if len(args) == 1 and type(args[0]) == QPointF:
                # Step Type
                self.type = Path.StepType.Line

                self.point = args[0]

            elif len(args) == 3 and type(args[0]) == QPointF and type(args[1]) == QPointF and type(args[2]) == QPointF:
                # Step Type
                self.type = Path.StepType.Cubic

                # 
                self.c1 = args[0]
                self.c2 = args[1]
                self.end_point = args[2]

            else:
                # StepType.Line Step object building error
                if len(args) != 1:
                    missing_args = 1 - len(args)
                    line_object_error = f"Wrong number of args : {abs(missing_args)} {'missing_values' if missing_args > 0 else 'in excess'}"
                else:
                    line_object_error = f"Wrong type given: {type(args[0])} instead of QPointF"

                if len(args) != 3:
                    missing_args = 3 - len(args)
                    cubic_object_error = f"Wrong number of args : {abs(missing_args)} {'missing_values' if missing_args > 0 else 'in excess'}"
                else:
                    type_errors = []
                    if type(args[0]) != QPointF:
                        type_errors.append(f"c1 : {type(args[0])} instead of QPointF")
                    if type(args[1]) != QPointF:
                        type_errors.append(f"c1 : {type(args[1])} instead of QPointF")
                    if type(args[2]) != QPointF:
                        type_errors.append(f"c1 : {type(args[2])} instead of QPointF")
                    
                    cubic_object_error = f"Wrong type given: ({', '.join(type_errors)})"

                constructor_args_errors = '\n'.join([
                    f" - Step(point: QPointF) -> {line_object_error}",
                    f" - Step(c1: QPointF, c2: QPointF, end_point: QPointF) -> {cubic_object_error}"
                ])

                raise(NotImplementedError(
                        f"Wrong args given :\n{constructor_args_errors}"
                    )
                )


    def __init__(self, steps: Iterable[Step], line_color: QColor = Qt.GlobalColor.black, 
                    line_width: int = 1, line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, 
                    fill_color: QColor | QGradient = Qt.GlobalColor.transparent, pen_join_style: Qt.PenJoinStyle = Qt.PenJoinStyle.MiterJoin, parent=None):

        # Handle points
        if len(steps) < 2:
            LogManager().error(f"Path.__init__: not enough steps given to create a polygon, must give at least 2 steps instead of {len(steps)}")
            return

        self._steps = steps

        # Join Style
        self._pen_join_style = pen_join_style

        # Painter path
        self._painter_path = Path.build_path(steps)

        # Calc origin and size
        bounding_rect = self._painter_path.boundingRect()
        origin = bounding_rect.topLeft()
        size = bounding_rect.size()

        # Save old bounding rectangle
        self._old_bounding_rect = self._painter_path.boundingRect()
        
        super().__init__(origin, size, line_color, line_width, line_style, fill_color, parent=parent)


    # -------------
    # Properties
    # -------------
    @property
    def steps(self) -> Iterable[Step]:
        return self._steps

    @steps.setter
    def steps(self, new_steps) -> None:
        # Save old bounding rectangle
        self._old_bounding_rect = self._painter_path.boundingRect()

        # Build new painter path
        self._painter_path = Path.build_path(new_steps)

        # Save new steps
        self._steps = new_steps

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return self._painter_path.boundingRect().united(self._old_bounding_rect)
        
    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawPath(self._painter_path)
        
    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def build_path(steps: Iterable[Step]) -> QPainterPath:
        # Handling first step
        start_point = QPointF()
        first_step: Path.Step = steps[0]
        if first_step.type == Path.StepType.Line:
            start_point = first_step.point
        elif first_step.type == Path.StepType.Cubic:
            start_point = first_step.end_point
        else:
            raise(TypeError("Path.build_path(): Wrong step type given: {first_step.type} instead of Path.StepType.Line or Path.StepType.Cubic"))

        # Handling the rest of the path
        painter_path = QPainterPath(start_point)
        for step in steps:
            if step.type == Path.StepType.Line:
                painter_path.lineTo(step.point)
            elif step.type == Path.StepType.Cubic:
                painter_path.cubicTo(step.c1, step.c2, step.end_point)
            else:
                raise(TypeError("Path.build_path(): Wrong step type given: {step.type} instead of Path.StepType.Line or Path.StepType.Cubic"))

        return painter_path

class Polygon(AbstractShape):
    def __init__(self, points: Iterable[QPointF], border_color: QColor = Qt.GlobalColor.black, 
                    border_width: int = 1, line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, 
                    fill_color: QColor | QGradient = Qt.GlobalColor.transparent, pen_join_style: Qt.PenJoinStyle = Qt.PenJoinStyle.MiterJoin, parent=None):

        # Handle points
        if len(points) < 3:
            LogManager().error(f"Polygon.__init__: not enough points given to create a polygon, must give at least 3 points instead of {len(points)}")
            return

        # Calc Pos & Size
        origin = self.calc_pos(points)
        size = self.calc_size(points)

        # Translate all points form the origin
        self._points = [point - origin for point in points]

        # Join Style
        self._pen_join_style = pen_join_style

        super().__init__(origin, size, border_color, border_width, line_style, fill_color, parent=parent)

    # -------------
    # Properties
    # -------------
    @property
    def points(self) -> Iterable[QPointF]:
        return self._points

    @points.setter
    def points(self, new_points: Iterable[QPointF]) -> None:
        # Calc new origin & size
        new_origin = Polygon.calc_pos(new_points)
        new_size = Polygon.calc_size(new_points)

        # Set new points
        self._points = [point - new_origin for point in new_points]

        # Set Pos
        if new_origin != self.pos():
            self.setPos(new_origin)
            self.position_changed.emit()

        # Set size
        self.setOrigin(new_origin)
        if new_size != self._size:
            self._size = new_size
            self.size_changed.emit()

    @property
    def size(self) -> QSizeF:
        return self.boundingRect().size()

    
    # -------------
    # Methods
    # -------------
    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawPolygon(self._points)
        
    # --------------
    # Static Methods
    # --------------
    @staticmethod
    def calc_pos(points: Iterable[QPointF]) -> QPointF:
        # Calc bounding position
        min_x = min([point.x() for point in points])
        min_y = min([point.y() for point in points])

        return QPointF(min_x, min_y)

    @staticmethod
    def calc_size(points: Iterable[QPointF]) -> QSizeF:
        xs = [point.x() for point in points]
        ys = [point.y() for point in points]

        # Calc bounding position
        min_x = min(xs)
        min_y = min(ys)

        # Calc bounding position
        max_x = max(xs)
        max_y = max(ys)

        # Calc width & height
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)

        return QSizeF(width, height)

class Rectangle(AbstractShape):

    def __init__(self, top_left: QPointF, width: float, height: float, border_color: QColor = Qt.GlobalColor.black, border_width: int = 1, 
                    line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, fill_color: QColor | QGradient = Qt.GlobalColor.transparent, parent=None):
        
        # Calc Size
        size = QSizeF(width, height)

        super().__init__(top_left, size, border_color, border_width, line_style, fill_color, parent=parent)

    # -------------
    # Properties
    # -------------
    @property
    def width(self) -> float:
        return self._size.width()

    @width.setter
    def width(self, new_width: float):
        if new_width != self._size.width():
            self._size.setWidth(new_width)

    @property
    def height(self) -> float:
        return self._size.heigth()

    @height.setter
    def height(self, new_height: float):
        if new_height != self._size.heigth():
            self._size.setHeight(new_height)

    @property
    def size(self) -> QSizeF:
        return self._size

    @size.setter
    def size(self, new_size) -> None:
        if new_size != self._size:
            self._size = new_size
    
    # -------------
    # Methods
    # -------------
    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        painter.drawRect(QRectF(QPointF(0, 0), self._size))

class Square(Rectangle):

    def __init__(self, top_left: QPointF, side_size: float, 
                    border_color: QColor, border_width: int = 1, line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, 
                    fill_color: QColor | QGradient = Qt.GlobalColor.transparent, parent=None):
        
        super().__init__(top_left, side_size, side_size, border_color, 
                            border_width, line_style, 
                            fill_color, parent=parent)

    
    # -------------
    # Properties
    # -------------
    @property
    def side_size(self) -> float:
        return self._size.width()

    @side_size.setter
    def side_size(self, new_side_size: float):
        if new_side_size != self._size.width():
            self._size.setWidth(new_side_size)
            self._size.setHeight(new_side_size)

class Text(AbstractShape):

    def __init__(self, text: str, position: QPointF = QPointF(), 
                    text_max_width: float = 0.0, text_max_height: float = 0.0, 
                    font: QFont = None, font_color: QColor = Qt.GlobalColor.black, 
                    background_color: QColor | QGradient = QColor(0, 0, 0, 0), 
                    alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft, 
                    parent=None):

        # Text
        self._text = text

        # Text size parameters
        self._text_max_width = text_max_width
        self._text_max_height = text_max_height

        # Text option
        word_wrap = Qt.TextFlag.TextWordWrap if text_max_width > 0.0 else Qt.TextFlag.TextSingleLine
        self._text_flags = alignment | word_wrap

        # Font
        if font is None :
            font = QFont()
        self._font = font

        # Font metrics
        font_copy = QFont(font)
        font_copy.setPointSize(int(font.pointSize() * QApplication.desktop().logicalDpiX()/96.0))
        self._font_metrics = QFontMetricsF(font_copy)

        # Calculate rectangle
        bounding_rect = QRectF(position, QSizeF(text_max_width, text_max_height))
        bounding_rect = self._font_metrics.boundingRect(bounding_rect, self._text_flags, text)

        # Translate Rectangle
        if bounding_rect.y() < position.y():
            offset_y = position.y() - bounding_rect.y() 
            bounding_rect.translate(0, offset_y)

        # Reset drawing position from the origin
        self._drawing_rect = bounding_rect
        self._drawing_rect.translate(-position)

        # 
        super().__init__(position, bounding_rect.size(), font_color, background_color=background_color, parent=parent)

    # -------------
    # Properties
    # -------------
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, new_text) -> None:
        print(new_text,  self._text, new_text != self._text)
        if new_text != self._text:
            # Get old bounding rect
            old_bounding_rect = self.boundingRect()

            # Replace value
            self._text = new_text

            # Calculate text rectangle
            bounding_rect = QRectF(QPointF(0, 0), QSizeF(self._text_max_width, self._text_max_height))
            bounding_rect = self._font_metrics.boundingRect(bounding_rect, self._text_flags, new_text)
            
            # Set new bounding rect
            self._drawing_rect = bounding_rect

            self.update()

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return self._drawing_rect

    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        # Set Font
        painter.setFont(self._font)

        # Painter set brush as transparent
        painter.setBrush(QColor(0, 0, 0, 0))

        # Draw Text
        painter.drawText(self._drawing_rect, self._text_flags, self._text)

    def setSize(self, new_size: QSize | QSizeF):
        # Handle new size type
        new_size = QSizeF(new_size) if type(new_size) == QSize else new_size

        if self._size != new_size:
            # Update size value
            self._size = new_size
            self._text_max_width = new_size.width()
            self._text_max_height = new_size.height()

            # Calculate text rectangle
            bounding_rect = QRectF(QPointF(0, 0), QSizeF(self._text_max_width, self._text_max_height))
            bounding_rect = self._font_metrics.boundingRect(bounding_rect, self._text_flags, self._text)
                
            self._drawing_rect = bounding_rect