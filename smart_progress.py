__version__ = '1.0.2'
__author__ = 'Philipp A.'
__email__ = 'flying-sheep@web.de'

import click
from click._termui_impl import ProgressBar

class IPyBackend(ProgressBar):
	def __init__(self, iterable=None, length=None, *, label=None,
			show_eta=True, show_percent=None, show_pos=False,
			item_show_func=None, info_sep=' '):
		from IPython import get_ipython
		
		try:
			from ipywidgets import FloatProgress
		except ImportError:
			from IPython.html.widgets.widget_float import FloatProgress
		
		ipython = get_ipython()
		if not ipython or ipython.__class__.__name__ != 'ZMQInteractiveShell':
			raise RuntimeError('IPython notebook needs to be running')
		
		self.backend = FloatProgress(value=0, min=0, step=1)
		# max and description are set via properties
		
		super().__init__(iterable, length, label=label,
			show_eta=show_eta, show_percent=show_percent, show_pos=show_pos,
			item_show_func=item_show_func, info_sep=info_sep)
		
		self.is_hidden = False
	
	
	def __enter__(self):
		from IPython.display import display
		display(self.backend)
		return super().__enter__()
	
	def render_finish(self):
		self.backend.close()
	
	def render_progress(self):
		info_bits = []
		if self.show_pos:
			info_bits.append(self.format_pos())
		if self.show_percent or (self.show_percent is None and not self.show_pos):
			info_bits.append(self.format_pct())
		if self.show_eta and self.eta_known and not self.finished:
			info_bits.append(self.format_eta())
		if self.item_show_func is not None:
			item_info = self.item_show_func(self.current_item)
			if item_info is not None:
				info_bits.append(item_info)
		
		self.backend.description = '{} {}'.format(self.label or '', self.info_sep.join(info_bits))
		self.backend.max = self.length
		self.backend.value = self.pos

def progressbar(
		iterable=None, length=None, label=None,
		show_eta=True, show_percent=None, show_pos=False, item_show_func=None,
		fill_char='#', empty_char='-', bar_template='%(label)s [%(bar)s] %(info)s', info_sep=' ',
		width=36, file=None, color=None):
	"""Create a progressbar that works in Jupyter/IPython notebooks and the terminal"""
	
	try:
		return IPyBackend(iterable, length, label=label,
			show_eta=show_eta, show_percent=show_percent, show_pos=show_pos,
			item_show_func=item_show_func, info_sep=info_sep)
	except (ImportError, RuntimeError): #fall back if ipython is not installed or no notebook is running
		return click.progressbar(
			iterable, length, label,
			show_eta, show_percent, show_pos, item_show_func,
			fill_char, empty_char, bar_template, info_sep,
			width, file, color)
