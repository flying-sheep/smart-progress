# smart-progress
Smart progressbar with multiple backends supporting both explicit updating and tqdm-style iterable-wrapping

## Usage
```python
progressbar(iterable=None, length=None, label=None,
            show_eta=True, show_percent=None, show_pos=False,
            item_show_func=None, ..., info_sep=' ', ...)
```

Check [click.progressbar](http://click.pocoo.org/5/api/#click.progressbar) for the parameters and details. As of now, the IPython backend ignores all bar drawing and terminal-related parameters. (The ones not listed above)

## Example

```python
from smart_progress import progressbar

with progressbar([1,2,3]) as bar:
	for item in bar:
		do_work(item)
```

or

```python
con = connection(...)
with con, progressbar(length=con.tot_size()) as bar:
	while not con.is_eof():
		block = con.retrieve_block()
		do_work(block)
		bar.update(len(block))
```

## Dependencies

* [click](http://click.pocoo.org) [5.x](http://click.pocoo.org/5)
* [IPython](http://ipython.org) 4.x + [ipywidgets](https://github.com/ipython/ipywidgets)

	(alternatively falls back to IPython 3.x)
