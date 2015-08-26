smart-progress
==============

Smart progressbar with multiple backends supporting both explicit updating and tqdm_-style iterable-wrapping

.. _tqdm: https://github.com/tqdm/tqdm

Usage
-----

.. code:: python

  progressbar(iterable=None, length=None, label=None,
              show_eta=True, show_percent=None, show_pos=False,
              item_show_func=None, ..., info_sep=' ', ...)

Check `click.progressbar`_ for the parameters and details. As of now, the IPython backend ignores all bar drawing and terminal-related parameters. (The ones not listed above)

.. _click.progressbar: http://click.pocoo.org/5/api/#click.progressbar

Example
-------

.. code:: python

	from smart_progress import progressbar
	
	with progressbar([1,2,3]) as bar:
		for item in bar:
			do_work(item)

or

.. code:: python

	con = connection(...)
	with con, progressbar(length=con.tot_size()) as bar:
		while not con.is_eof():
			block = con.retrieve_block()
			do_work(block)
			bar.update(len(block))

Dependencies
------------

* click_ 5.x
* IPython_ 4.x + ipywidgets_
  
  (alternatively falls back to IPython 3.x)

.. _click: http://click.pocoo.org
.. _IPython: http://ipython.org
.. _ipywidgets: https://github.com/ipython/ipywidgets