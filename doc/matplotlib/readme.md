# Introduction to matplotlib

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.

**Considerations**:

- The figure is the window or general page in which everything is drawn. You can create multiple independent figures. A figure can have other things, like a subtitle, which is a centered title of the figure, a legend, a color bar...

- Axes are added to the figure. The axes are the area in which the data is graphed with functions such as `plot()` and `scatter()`, and can have associated labels.

- Each axis has an x-axis and a y-axis, and each contains a numbering.

   There are also the labels of the axes, the title, and the legend that must be taken into account when you want to customize the axes, but also taking into account that the scales of the axes and the grid lines can be useful.

- The vertebral lines are lines that connect the axis marks and designate the boundaries of the data area, in other words, they are the simple square that you can see when you have initialized.

- **matplotlib** is the entire Python data display package.

- **pyplot** is a module in the matplotlib package. The module provides an interface that allows you to create shapes and axes implicitly and automatically to achieve the desired frame.

- Machine learning **data** for graphing on matplotlib **should be structured under the numpy library**.

---

## Use examples

### Line diagram

```Python
import matplotlib.pyplot as plt

# Define data
x1 = [3, 4, 5, 6]
y1 = [5, 6, 3, 4]
x2 = [2, 5, 8]
y2 = [3, 4, 3]

# Configure the characteristics of the chart
plt.plot(x1, y1, label= 'Line 1', linewidth = 4, color = 'blue')
plt.plot(x2, y2, label= 'Line 2', linewidth = 4, color = 'green')

# Define title and name of axes
plt.title('Linea diagram')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

# Show legend, grid and figure
plt.legend()
plt.grid()
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/machine_learning_python/master/doc/images/matplotlib/diagram_line.png" width="70%">
</p>

### Bar chart

Used to compare data between different categories.

```Python
import matplotlib.pyplot as plt

# Define data
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]

# Configure the characteristics of the chart
plt.bar(x1, y1, label= 'Data 1', linewidth = 0.5, color = 'lightblue')
plt.bar(x2, y2, label= 'Data 2', linewidth = 0.5, color = 'orange')

# Define title and name of axes
plt.title('Bar chart')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

# Show legend and figure
plt.legend()
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/machine_learning_python/master/doc/images/matplotlib/bar_chart.png" width="70%">
</p>

### Histogram

Used to show a distribution. useful for matrices or very long lists.

```Python
import matplotlib.pyplot as plt

# Define data
a = [22,55,62,45,21,22,34,42,424,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]

# Configure the characteristics of the chart
plt.hist(a, bins, histtype = 'bar', rwidth = 0.8, color = 'lightgreen')

# Define title and name of axes
plt.title('Histograms')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

# Show figure
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/machine_learning_python/master/doc/images/matplotlib/histogram.png" width="70%">
</p>

### Scatter plots

They are used to compare variables, for example, to show how much one variable affects another.

```Python
import matplotlib.pyplot as plt

# Define data
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]

# Configure the characteristics of the chart
plt.scatter(x1, y1, label= 'Data 1', color = 'red')
plt.scatter(x2, y2, label= 'Data 2', color = 'purple')

# Define title and name of axes
plt.title('Scatter plot')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

# Show figure
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/machine_learning_python/master/doc/images/matplotlib/pie_chart.png" width="70%">
</p>

### Pie chart

It is used to show the percentages of the categories represented.

```Python
import matplotlib.pyplot as plt

# Define data
sleep = [7,8,6,11,7]
eat = [2,3,4,3,2]
work = [7,8,7,2,2]
fun = [8,5,7,8,13]
divisions = [7,2,2,13]
activities = ['Sleep', 'Eat', 'Work', 'Fun']
colors = ['red', 'purple', 'blue', 'orange']

# Configure the characteristics of the chart
plt.pie(divisions, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')

# Define title and name of axes
plt.title('Pie chart')

# Show figure
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/machine_learning_python/master/doc/images/matplotlib/scatter_plot.png" width="70%">
</p>
