
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt

# -------------
# Pens
# -------------
def SelectedPen(color: QColor) -> QPen:
    selected_pen : QPen = QPen(color)
    selected_pen.setWidth(1)
    selected_pen.setDashPattern([3, 2])
    return selected_pen

def UnselectedPen(color: QColor) -> QPen:
    unselected_pen : QPen = QPen(color)
    unselected_pen.setWidth(1)
    return unselected_pen

# Black Pens
SelectedBlackPen: QPen = SelectedPen(Qt.GlobalColor.black)
UnselectedBlackPen: QPen = UnselectedPen(Qt.GlobalColor.black)

# Red Pens
SelectedRedPen : QPen = SelectedPen(Qt.GlobalColor.red)
UnSelectedRedPen : QPen = UnselectedPen(Qt.GlobalColor.red)

# -------------
# Brushes
# -------------
WhiteBrush : QBrush = QBrush(Qt.GlobalColor.white)
BlackBrush : QBrush = QBrush(Qt.GlobalColor.black)