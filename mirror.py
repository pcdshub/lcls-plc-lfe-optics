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
    y_up = Component(EpicsSignal, ':MMS:YUP', kind='normal')
    y_dwn = Component(EpicsSignal, ':MMS:YDWN', kind='omitted')
    x_up = Component(EpicsSignal, ':MMS:XUP', kind='normal')
    x_dwn = Component(EpicsSignal, ':MMS:XDWN', kind='omitted')
    pitch = Component(EpicsSignal, ':MMS:PITCH', kind='normal')
    bender = Component(EpicsSignal, ':MMS:BENDER', kind='normal')

    # Gantry components
    gantry_x = Component(EpicsSignalRO, ':GANTRY_X_RBV', kind='normal')
    gantry_y = Component(EpicsSignalRO, ':GANTRY_Y_RBV', kind='normal')
    couple_y = Component(EpicsSignal, ':COUPLE_Y', kind='omitted')
    couple_x = Component(EpicsSignal, ':COUPLE_X', kind='omitted')
    decouple_y = Component(EpicsSignal, ':DECOUPLE_Y', kind='omitted')
    decouple_x = Component(EpicsSignal, ':DECOUPLE_X', kind='omitted')
    couple_status_y = Component(EpicsSignalRO, ':ALREADY_COUPLED_Y_RBV', kind='normal')
    couple_status_x = Component(EpicsSignalRO, ':ALREADY_COUPLED_X_RBV', kind='normal')

    # RMS Components:
    y_enc_rms = Component(EpicsSignalRO, ':Y_ENC:RMS_RBV', kind='normal')
    x_enc_rms = Component(EpicsSignalRO, ':X_ENC:RMS_RBV', kind='normal')
    pitch_enc_rms = Component(EpicsSignalRO, ':PITCH_ENC:RMS_RBV', kind='normal')
    bender_enc_rms = Component(EpicsSignalRO, ':BENDER_ENC:RMS_RBV', kind='normal')

    def __init__(self, prefix, **kwargs):
        super().__init__(prefix, **kwargs)


# Testing/Debugging
mr1l0 = Mirror('MR1L0:LFE', name='mr1l0_lfe')
mr2l0 = Mirror('MR2L0:LFE', name='mr2l0_lfe')

# From the typhon README:
app = QApplication.instance() or QApplication(sys.argv)
typhon.use_stylesheet()
suite_mr1l0 = typhon.TyphonSuite.from_device(mr1l0)
suite_mr2l0 = typhon.TyphonSuite.from_device(mr2l0)
suite_mr1l0.show()
suite_mr2l0.show()
app.exec_()
