# smart-progress
Smart progressbar with multiple backends supporting both explicit updating and tqdm-style iterable-wrapping

## Usage
`progressbar(iterable=None, length=None, label=None, ...)`

Check [click.progressbar](http://click.pocoo.org/5/api/#click.progressbar) for the parameters and details. As of now, the IPython backend ignores all parameters except from `iterable`, `length`, and `label`.

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
