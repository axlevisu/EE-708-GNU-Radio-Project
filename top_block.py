#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Apr 30 20:21:57 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gaussian_code
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.P = P = 10
        self.N = N = 8
        self.M = M = 20

        ##################################################
        # Blocks
        ##################################################
        self.gaussian_code_gaussian_code_if_0 = gaussian_code.gaussian_code_if(7, N, P)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "ber.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, M-1, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.gaussian_code_gaussian_code_if_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.gaussian_code_gaussian_code_if_0, 0), (self.blocks_throttle_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
