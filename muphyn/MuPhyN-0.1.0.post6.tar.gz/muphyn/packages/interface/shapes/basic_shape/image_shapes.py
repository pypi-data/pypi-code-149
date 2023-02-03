from PyQt5.QtCore import QFileInfo, QPointF, QRectF, QSize, QSizeF, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QGradient, QImage, QImageReader, QPainter, QTransform
from PyQt5.QtWidgets import QStyleOptionGraphicsItem
from PyQt5.QtSvg import QSvgRenderer

from muphyn.packages.interface.shapes.basic_shape.abstract_shape import AbstractShape
from muphyn.packages.core.utils.log_manager import LogManager

class AbstractImage(AbstractShape):

    # -------------
    # Signals
    # -------------
    image_path_changed = pyqtSignal() 

    def __init__(self, image_path: str, position: QPointF = QPointF(0, 0), size: QSize = None, 
            border_width: int = 0, border_color: QColor | QGradient = Qt.GlobalColor.transparent, border_line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, 
            background_color: QColor | QGradient = Qt.GlobalColor.transparent, 
            aspect_ratio_mode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio, transformation_mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation, 
            parent=None):

        # Test if image file exists
        if not QFileInfo(image_path).exists():
            raise(FileNotFoundError(f"File doesn't exists:\n\t{image_path}"))

        self._image_path: str = image_path

        self._aspect_ratio_mode: Qt.AspectRatioMode = aspect_ratio_mode
        self._transformation_mode: Qt.TransformationMode = transformation_mode

        super().__init__(position, size, border_color, border_width, border_line_style, background_color, parent=parent)

        # Connect signals
        self.image_path_changed.connect(self._on_image_path_changed)

    # -------------
    # Properties
    # -------------
    @property
    def image_path(self) -> str:
        return self._image_path

    @image_path.setter
    def image_path(self, new_image_path: str) -> None:
        if self._image_path != new_image_path:
            self._image_path = new_image_path

    @property
    def aspect_ratio_mode(self) -> Qt.AspectRatioMode:
        return self._aspect_ratio_mode

    @aspect_ratio_mode.setter
    def image_path(self, new_aspect_ratio_mode: Qt.AspectRatioMode) -> None:
        if self._aspect_ratio_mode != new_aspect_ratio_mode:
            self._aspect_ratio_mode = new_aspect_ratio_mode

    @property
    def transformation_mode(self) -> Qt.TransformationMode:
        return self._transformation_mode

    @transformation_mode.setter
    def transformation_mode(self, new_transformation_mode: Qt.TransformationMode) -> None:
        if self._transformation_mode != new_transformation_mode:
            self._transformation_mode = new_transformation_mode

    @property
    def painted_area(self) -> QRectF:
        return self._painted_area

    # -------------
    # Methods
    # -------------
    def _on_image_path_changed(self):
        raise(NotImplementedError(f"{type(self).__name__}._on_image_path_changed() not overriden!"))

    def setSize(self, new_size: QSize | QSizeF):
        raise(NotImplementedError(f"{type(self).__name__}.setSize() not overriden!"))

class Image(AbstractImage):
    def __init__(self, image_path: str, position: QPointF = QPointF(0, 0), size: QSize = None, 
            border_width: int = 1, border_color: QColor | QGradient = Qt.GlobalColor.transparent, border_line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, 
            background_color: QColor | QGradient = Qt.GlobalColor.transparent, 
            aspect_ratio_mode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio, transformation_mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation, 
            parent=None):

        super().__init__(image_path, position, size, 
                            border_width, border_color, border_line_style, 
                            background_color, 
                            aspect_ratio_mode, transformation_mode, parent)

        # Load Image & calc Painted Area
        self._load_image()
    

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return self._painted_area

    def _load_image(self):
         # Load Image
        image = QImage(self._image_path)

        # Save original image in memory
        self._image = image

        # Resize Image if asked
        if self._size is not None:
            image = image.scaled(
                self._size, 
                aspectRatioMode=self._aspect_ratio_mode, 
                transformMode=self._transformation_mode
            )
        else:
            self.size = image.size()
        
        # Building painted Area
        painted_area_size: QSize = image.size()
        image_to_bounding_rect_size_diff: QSize = (self._size.toSize() - painted_area_size) / 2
        painted_area_position: QPointF = QPointF(
            image_to_bounding_rect_size_diff.width(), 
            image_to_bounding_rect_size_diff.height()
        )
        
        self._painted_area = QRectF(painted_area_position, QSizeF(painted_area_size))

    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        # Init Generator
        painter.drawImage(self._painted_area, self._image)

    def setSize(self, new_size: QSize | QSizeF):
        # Handle new size type
        new_size = QSizeF(new_size) if type(new_size) == QSize else new_size

        if new_size != self._size:
            # Update new size
            self._size = new_size

            # Resize Image
            image = self._image.scaled(
                new_size, 
                aspectRatioMode=self._aspect_ratio_mode, 
                transformMode=self._transformation_mode
            )
            
            # Building painted Area
            painted_area_size: QSize = image.size()
            image_to_bounding_rect_size_diff: QSize = (self._size.toSize() - painted_area_size) / 2
            painted_area_position: QPointF = QPointF(
                image_to_bounding_rect_size_diff.width(), 
                image_to_bounding_rect_size_diff.height()
            )
            
            self._painted_area = QRectF(painted_area_position, QSizeF(painted_area_size))

    # -------------
    # Slots
    # -------------
    def _on_image_path_changed(self):
        self._load_image()

class SVGImage(AbstractImage):
    def __init__(self, image_path: str, position: QPointF = QPointF(0, 0), size: QSize = None, 
            border_width: int = 0, border_color: QColor | QGradient = Qt.GlobalColor.transparent, border_line_style: Qt.PenStyle = Qt.PenStyle.SolidLine, 
            background_color: QColor | QGradient = Qt.GlobalColor.transparent, 
            aspect_ratio_mode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio, transformation_mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation, 
            parent = None):

        super().__init__(image_path, position, size, 
                            border_width, border_color, border_line_style, 
                            background_color, 
                            aspect_ratio_mode, transformation_mode, parent)

        # Load SVG file
        svg_renderer = QSvgRenderer()
        self._svg_renderer = svg_renderer
        self._load_svg_file()

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return self._painted_area.translated(self.pos())

    def _load_svg_file(self):
        self._svg_renderer.load(self._image_path)
        if not self._svg_renderer.isValid():
            raise(Exception("Not a valid SVG file"))

        # Convert size (QSizeF → QSize)
        if self._size is not None:
            self._size = self._size.toSize()
        else:
            self._size = self._svg_renderer.defaultSize()

        # Building painted Area
        painted_area_size: QSize = self._svg_renderer.defaultSize().scaled(
            self._size, self._aspect_ratio_mode)
        image_to_bounding_rect_size_diff: QSize = (self._size - painted_area_size) / 2
        painted_area_position: QPointF = QPointF(
            image_to_bounding_rect_size_diff.width(), 
            image_to_bounding_rect_size_diff.height()
        )
        
        self._painted_area = QRectF(painted_area_position, QSizeF(painted_area_size))

    def setWidth(self, new_width: int) -> None:
        if new_width != self._size.width():
            self.setSize(QSize(new_width, self._size.height()))

    def setHeight(self, new_height: int) -> None:
        if new_height != self._size.height():
            self.setSize(QSize(self._size.width(), new_height))

    def setSize(self, new_size: QSize | QSizeF) -> None:
        # Handle new size type
        new_size = new_size if type(new_size) == QSize else new_size.toSize()
        
        if new_size != self._size:
            # Replace value
            self._size = new_size

            # Calculate painted area size
            painted_area_size: QSize = self._svg_renderer.defaultSize().scaled(
                self._size, self._aspect_ratio_mode)
            
            # Painted area position
            image_to_bounding_rect_size_diff: QSize = (self._size - painted_area_size) / 2
            painted_area_position: QPointF = QPointF(
                image_to_bounding_rect_size_diff.width(), 
                image_to_bounding_rect_size_diff.height()
            )
            self._painted_area = QRectF(painted_area_position, QSizeF(painted_area_size))

    def draw_shape(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget) -> None:
        # Init Generator
        self._svg_renderer.render(painter, self._painted_area)

    # -------------
    # Slots
    # -------------
    def _on_image_path_changed(self):
        self._load_svg_file()

def ImageShapeFactory(
        image_path: str, 
        position: QPointF = QPointF(0, 0),
        size: QSize = None,
        border_width: int = 0,
        border_color: QColor | QGradient = Qt.GlobalColor.transparent,
        border_line_style: Qt.PenStyle = Qt.PenStyle.SolidLine,
        background_color: QColor | QGradient = Qt.GlobalColor.transparent,
        aspect_ratio_mode: Qt.AspectRatioMode = Qt.AspectRatioMode.KeepAspectRatio,
        transformation_mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
        parent=None
    ) -> AbstractImage:

    if QFileInfo(image_path).exists():
    
        if (image_format := QImageReader.imageFormat(image_path)) in QImageReader.supportedImageFormats():
            if image_format == b"svg":
                return SVGImage(
                    image_path, position, size, border_width, border_color, border_line_style,
                    background_color, aspect_ratio_mode, transformation_mode, parent)
            else:
                return Image(
                    image_path, position, size, border_width, border_color, border_line_style,
                    background_color, aspect_ratio_mode, transformation_mode, parent)
                        
        else:
            LogManager().error(f"Error while trying to create AbstractImage object : \n\tImage file format of \"{image_path}\" is not a supported image file format")

    else:
        LogManager().error(f"Error while trying to create AbstractImage object : \n\tPath \"{image_path}\" doesn't exists")