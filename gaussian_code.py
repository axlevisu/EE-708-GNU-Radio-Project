#!/usr/bin/env python

import numpy as np
from gnuradio import blocks, gr, wxgui, channels

seed = 7
np.random.seed(seed)

class gaussian_code(object):
	"""docstring for gaussian_code"""
	def __init__(self, arg):
		super(gaussian_code, self).__init__()
		self.arg = arg
		