"""
mirror.py

Python file for ophyd class of mirror - for testing purposes
"""

from ophyd import Device, Component, EpicsSignal, EpicsSignalRO
from qtpy.QtWidgets import QApplication
import sys
import typhon

class Mirror(Device):
    """
    Class for Offset Mirror System (test)
    """
    # Motor components: can read/write positions
    y_up = Component(EpicsSignal, ':MMS:YUP')
    y_dwn = Component(EpicsSignal, ':MMS:YDWN')
    x_up = Component(EpicsSignal, ':MMS:XUP')
    x_dwn = Component(EpicsSignal, ':MMS:XDWN')
    pitch = Component(EpicsSignal, ':MMS:PITCH')
    bender = Component(EpicsSignal, ':MMS:BENDER')

    # Gantry components
    gantry_x = Component(EpicsSignalRO, ':GANTRY_X_RBV')
    gantry_y = Component(EpicsSignalRO, ':GANTRY_Y_RBV')
    couple_y = Component(EpicsSignal, ':COUPLE_Y')
    couple_x = Component(EpicsSignal, ':COUPLE_X')
    decouple_y = Component(EpicsSignal, ':DECOUPLE_Y')
    decouple_x = Component(EpicsSignal, ':DECOUPLE_X')
    couple_status_y = Component(EpicsSignalRO, ':ALREADY_COUPLED_Y_RBV')
    couple_status_x = Component(EpicsSignalRO, ':ALREADY_COUPLED_X_RBV')

    def __init__(self, prefix, **kwargs):
        super().__init__(prefix, **kwargs)

# Instantiate mirror:
mr1l0 = Mirror('MR1L0:LFE', name='mr1l0_lfe')

# From the typhon README:
app = QApplication.instance() or QApplication(sys.argv)
typhon.use_stylesheet()
suite = typhon.TyphonSuite.from_device(mr1l0)
suite.show()
app.exec_()

