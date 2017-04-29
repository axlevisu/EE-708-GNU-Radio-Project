#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Apr 30 01:28:41 2017
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
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
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
        self.var_sps = var_sps = 4
        self.samp_rate = samp_rate = 100000
        self.noise_volt = noise_volt = 0.0
        self.freq_off = freq_off = 0

        ##################################################
        # Blocks
        ##################################################
        _noise_volt_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_volt_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_volt_sizer,
        	value=self.noise_volt,
        	callback=self.set_noise_volt,
        	label="Noise Voltage",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_volt_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_volt_sizer,
        	value=self.noise_volt,
        	callback=self.set_noise_volt,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_volt_sizer)
        _freq_off_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_off_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_off_sizer,
        	value=self.freq_off,
        	callback=self.set_freq_off,
        	label="Frequency Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_off_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_off_sizer,
        	value=self.freq_off,
        	callback=self.set_freq_off,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_off_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        	size=((250,100)),
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 1, 0, 5, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	size=((400,100)),
        )
        self.GridAdd(self.wxgui_fftsink2_0.win, 1, 2, 5, 5)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=4,
          mod_code="gray",
          differential=True,
          samples_per_symbol=var_sps,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_volt,
        	frequency_offset=freq_off,
        	epsilon=1.0,
        	taps=(1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((complex(1,1), ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_psk_mod_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def get_var_sps(self):
        return self.var_sps

    def set_var_sps(self, var_sps):
        self.var_sps = var_sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self._noise_volt_slider.set_value(self.noise_volt)
        self._noise_volt_text_box.set_value(self.noise_volt)
        self.channels_channel_model_0.set_noise_voltage(self.noise_volt)

    def get_freq_off(self):
        return self.freq_off

    def set_freq_off(self, freq_off):
        self.freq_off = freq_off
        self._freq_off_slider.set_value(self.freq_off)
        self._freq_off_text_box.set_value(self.freq_off)
        self.channels_channel_model_0.set_frequency_offset(self.freq_off)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
