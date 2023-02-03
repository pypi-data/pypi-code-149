from PyQt5.QtCore import QPointF, QRectF, QSizeF, pyqtSignal, Qt
from PyQt5.QtGui import QBrush, QColor, QGradient, QPainter, QPen, QTransform
from PyQt5.QtWidgets import QGraphicsObject, QStyleOptionGraphicsItem

class AbstractShape(QGraphicsObject):
    # Drawing Area Signals
    position_changed = pyqtSignal()
    size_changed = pyqtSignal()

    # Shape Border Signals
    border_color_changed = pyqtSignal()
    border_width_changed = pyqtSignal()
    line_style_changed = pyqtSignal()

    # Filling Shape Signals
    background_color_changed = pyqtSignal()

    def __init__(self, origin: QPointF, size: QSizeF, color: QColor = Qt.GlobalColor.transparent, border_width: int = 1, 
                    line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, background_color: QColor | QGradient = Qt.GlobalColor.transparent, 
                    pen_cap_style: Qt.PenCapStyle = Qt.PenCapStyle.RoundCap, pen_join_style: Qt.PenJoinStyle = Qt.PenJoinStyle.RoundJoin, parent = None):
        
        # Size
        self._size = size
        
        # Pen Color
        if color is None:
            color = Qt.GlobalColor.transparent
        self._pen = QPen(color)

        # Pen width
        if border_width is None:
            border_width = 1
        self._pen.setWidth(border_width)

        # Pen line style
        if line_style is None:
            line_style = Qt.PenStyle.SolidLine
        self._pen.setStyle(line_style)

        # Pen cap/join style
        self._pen.setCapStyle(pen_cap_style)
        self._pen.setJoinStyle(pen_join_style)

        # Determine type of Brush based on type of Color
        brush_style = Qt.BrushStyle.SolidPattern 
        if isinstance(background_color, QGradient):
            if background_color.type() == QGradient.Type.LinearGradient:
                brush_style = Qt.BrushStyle.LinearGradientPattern
            elif background_color.type() == QGradient.Type.RadialGradient:
                brush_style = Qt.BrushStyle.RadialGradientPattern
            elif background_color.type() == QGradient.Type.ConicalGradient:
                brush_style = Qt.BrushStyle.ConicalGradientPattern
            else:
                brush_style = Qt.BrushStyle.NoBrush
        # Create brush
        self._brush = QBrush(background_color, brush_style)

        # parent
        super().__init__(parent)
        
        # Set pos
        self.setPos(origin)

        # Set All transformation origin to center of bounding box
        if size is not None:
            self.setTransformOriginPoint(QRectF(QPointF(), size).center())
    
    # -------------
    # Properties
    # -------------
    @property
    def position(self) -> QPointF:
        return self.pos()

    @position.setter
    def position(self, new_position) -> None:
        if new_position != self.pos():
            # Update position
            self.setPos(new_position)

            # Emit modification signals
            self.position_changed.emit()

    @property
    def size(self) -> QPointF:
        return self._size
            
    @property
    def border_color(self) -> QColor:
        return self._pen.color()

    @border_color.setter
    def border_color(self, new_color: QColor) -> None:
        if self._pen.color() != new_color:
            self._pen.setColor(new_color)

            self.border_color_changed.emit()

    @property
    def border_width(self) -> int:
        return self._pen.width()

    @border_width.setter
    def border_width(self, new_border_width: int) -> None:
        if self._pen.width() != new_border_width:
            self._pen.setWidth(new_border_width)

            self.border_width_changed.emit()

    @property
    def line_style(self) -> Qt.PenStyle:
        return self._pen.style()

    @line_style.setter
    def line_style(self, new_line_style: Qt.PenStyle) -> None:
        if self._pen.style() != new_line_style:
            self._pen.setStyle(new_line_style)

            self.line_style_changed.emit()

    @property
    def background_color(self) -> QColor:
        return self._brush.color()

    @background_color.setter
    def background_color(self, new_fill_color: QColor | QGradient) -> None:
        
        if isinstance(new_fill_color, Qt.GlobalColor):
            new_fill_color = QColor(new_fill_color)
            
        if isinstance(new_fill_color, QGradient):
            if new_fill_color != self._brush.gradient():
                # Select Brush Style
                brush_style = Qt.BrushStyle.NoBrush
                if new_fill_color.type() == QGradient.Type.LinearGradient:
                    brush_style = Qt.BrushStyle.LinearGradientPattern
                elif new_fill_color.type() == QGradient.Type.RadialGradient:
                    brush_style = Qt.BrushStyle.RadialGradientPattern
                elif new_fill_color.type() == QGradient.Type.ConicalGradient:
                    brush_style = Qt.BrushStyle.ConicalGradientPattern

                # Create new brush
                self._brush = QBrush(new_fill_color, brush_style)

                self.background_color_changed.emit()

        elif isinstance(new_fill_color, QColor):
            if new_fill_color != self._brush.color():
                self._brush.setColor(new_fill_color)
                self._brush.setStyle(Qt.BrushStyle.SolidPattern)

                self.background_color_changed.emit()

    @property
    def pen(self) -> QPen:
        return self._pen

    @pen.setter
    def pen(self, new_pen: QPen) -> None:
        self._pen = new_pen

    @property
    def brush(self) -> QBrush:
        return self._brush

    @brush.setter
    def brush(self, new_brush: QPen) -> None:
        self._brush = new_brush

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return QRectF(QPointF(), self._size)

    def draw_shape(self, painter : QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        raise(NotImplementedError(f"{type(self).__name__}: AbstractShape.draw_shape(painter, option, widget) not reimplemented"))

    def paint (self, painter : QPainter, option: QStyleOptionGraphicsItem = QStyleOptionGraphicsItem.OptionType.SO_Frame, widget=None) -> None :
        # Save painter state
        painter.save()

        # Set Pen
        painter.setPen(self._pen)

        # Set Brush
        painter.setBrush(self._brush)

        # Draw Shape
        self.draw_shape(painter, option, widget)

        # Reset painter state
        painter.restore()
