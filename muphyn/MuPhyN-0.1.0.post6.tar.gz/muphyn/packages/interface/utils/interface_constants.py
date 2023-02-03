from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPen

MuphynColor = QColor(233, 125, 26)
ApplicationWindowTitle = "Muphyn"

# Text Font
class MuphynFonts:
    """
    This class saves all Fonts data for Muphyn application
    """
    MuphynFontFamily: str = "MS Shell Dlg 2"

    # Input / Output Connector Font
    IOConnectorFont: QFont = QFont(MuphynFontFamily, 10, weight=QFont.Weight.Normal, italic=False)

    # Box Model Details Font
    BoxModelDetailsFont: QFont = QFont(MuphynFontFamily, 10, weight=QFont.Weight.Bold, italic=False)

class MuphynPens:
    """
    This class saves all Pens data for Muphyn application
    """

    # Link Pens
    SelectedLinkPen = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.DashLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
    UnSelectedLinkPen = QPen(Qt.GlobalColor.black, 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
