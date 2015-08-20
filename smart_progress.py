import click
from click._termui_impl import _length_hint

class IPyBackend:
	def __init__(self,
			iterable, length, label,
			show_eta, show_percent, show_pos, item_show_func,
			fill_char, empty_char, bar_template, info_sep,
			width, file, color):
		
		from traitlets import TraitError
		try:
			from ipywidgets import FloatProgress
		except ImportError:
			from IPython.html.widgets.widget_float import FloatProgress
		
		if length is None:
			length = _length_hint(iterable)
		if iterable is None:
			if length is None:
				raise TypeError('iterable or length is required')
			iterable = range(length)
		
		self.iter = iter(iterable)
		self.entered = False
		
		try:
			self.backend = FloatProgress(value=0, min=0, max=length, step=1, description=label or '')
		except TraitError:
			raise RuntimeError('IPython notebook needs to be running')
	
	
	def __enter__(self):
		from IPython.display import display
		display(self.backend)
		self.entered = True
		return self

	def __exit__(self, exc_type, exc_value, tb):
		self.backend.close()
	
	def __iter__(self):
		if not self.entered:
			raise RuntimeError('You need to use progress bars in a with block.')
		return self
	
	def __next__(self):
		v = next(self.iter)
		self.backend.value += 1
		return v
	
	def update(self, step):
		self.backend.value += step
	
	@property
	def label(self):
		return self.backend.description
	
	@label.setter
	def set_label(self, label):
		self.backend.description = label

def progressbar(
		iterable=None, length=None, label=None,
		show_eta=True, show_percent=None, show_pos=False, item_show_func=None,
		fill_char='#', empty_char='-', bar_template='%(label)s [%(bar)s] %(info)s', info_sep=' ',
		width=36, file=None, color=None):
	"""Create a progressbar that works in Jupyter/IPython notebooks and the terminal"""
	
	args = (
		iterable, length, label,
		show_eta, show_percent, show_pos, item_show_func,
		fill_char, empty_char, bar_template, info_sep,
		width, file, color)
	
	try:
		return IPyBackend(*args)
	except (ImportError, RuntimeError): #fall back if ipython is not installed or no notebook is running
		return click.progressbar(*args)
