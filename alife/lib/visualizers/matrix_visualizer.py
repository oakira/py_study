from os import path
import numpy as np
from vispy import gloo, app

GLSL_PATH = path.join(path.dirname(path.abspath(__file__)), 'glsl')

class Matrix_Visualizer(object):
	"""docstring for MatrixVisualizer."""
	def __init__(self,widh=600, height=600, value_range_min=0, value_range_max=1):
		self.value_range = (value_range_min, value_range_max)
		self._canvas = app.Canvas(size=(widh, height), position=(0, 0), keys='interactive', title="Alife" + self.__class__.__name__)
		