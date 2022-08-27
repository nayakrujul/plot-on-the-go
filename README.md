# plot-on-the-go
Update a graph while you plot!

## Installation

From PIP:

```
$ pip install plot-on-the-go
```

## Scatter

### Example output

https://user-images.githubusercontent.com/55329600/186910354-3ce5e392-3079-4a6a-8cbc-37ba567325e6.mov

Code (sorting functions not shown):

```python
from plot_on_the_go.plot import Scatter
from random_typing import List, Int
import timeit

grapher = Scatter(1000)

grapher.legend(red='bubble', blue='merge')
grapher.title('Bubble sort vs Merge sort')

for length in range(1001):
    l = List(Int(1, 100), length)

    b = timeit.timeit('bubble_sort(lst)',
                      globals={'lst': next(l), 'bubble_sort': bubble_sort},
                      number=1) * 1000
    m = timeit.timeit('merge_sort(lst)',
                      globals={'lst': next(l), 'merge_sort': merge_sort},
                      number=1) * 1000

    grapher.plot_point(length, b, 'red')
    grapher.plot_point(length, m, 'blue')

grapher.show()
```

Note: this program uses [random-typing](https://github.com/nayakrujul/typing-tools) to generate random lists of integers

### Import the module:

```python
from plot_on_the_go.plot import Scatter
```

### Initialise a grapher

```python
grapher = Scatter(1000)
```

The parameter is the maximum x-value

### Plot a point

```python
grapher.plot_point(0, 1, 'red')
```

The parameters are:
* `x`: int or float
* `y`: int or float
* `colour`: see section on accepted colours.

### Add a legend

```python
grapher.legend(red='v1', blue='v2')
```

Colours must be from the table linked in the accepted colours section.

### Add a title

```python
grapher.title('My graph')
```

### Show the graoh

```python
grapher.show()
```

## Accepted colours

Colours can be given in two formats

1. A tuple, (r, g, b), of three int or floats. E.g. `(100, 123.4, 255)`

2. An acceptable string - any colour in [this table](https://www.rapidtables.com/web/color/RGB_Color.html)
