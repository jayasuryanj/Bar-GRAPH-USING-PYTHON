# Bar-GRAPH-USING-PYTHON
creating bar graph using Python Library
This code utilizes Matplotlib, a Python library, to create a side-by-side bar chart visualizing the results of two teams, Team A and Team B, across different labs (Lab 1 to Lab 5).

1. **Importing Matplotlib:**
   ```python
   import matplotlib.pyplot as pyplot
   ```
   Imports the Matplotlib library under the alias `pyplot`, allowing you to use its functions and methods.

2. **Defining Constants:**
   ```python
   BAR_WIDTH = 0.35
   ```
   Sets the width of each bar in the bar chart. This constant determines the space between the bars of Team A and Team B.

3. **Data Setup:**
   ```python
   teama_results = (60, 75, 56, 62, 58)
   teamb_results = (55, 68, 80, 73, 55)
   ```
   Defines the scores or results for each team across the five labs.

4. **Index Setup:**
   ```python
   index_teama = (1, 2, 3, 4, 5)
   index_teamb = [i + BAR_WIDTH for i in index_teama]
   ```
   Sets the x-axis positions for the bars of Team A and Team B. The `index_teama` represents the positions for Team A, and `index_teamb` adjusts the parts to create the side-by-side effect.

5. **Tick Labels Setup:**
   ```python
   ticks = [i + BAR_WIDTH / 2 for i in  index_teama]
   ticks_labels = ('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5')
   ```
   Sets the positions and labels for the x-axis ticks. `ticks` defines the functions of the ticks, and `ticks_labels` provides the brands for each tick.

6. **Creating the Bar Chart:**
   ```python
   pyplot.bar(index_teama, teama_results, BAR_WIDTH, color='b', label='Team A')
   pyplot.bar(index_teamb, teamb_results, BAR_WIDTH, color='g', label='Team B')
   ```
   Plots the bars for Team A and Team B. The `bar()` function takes the x-axis positions, the corresponding results, the bar width, color, and labels for the legend.

7. **Labels and Title:**
   ```python
   pyplot.label('Labs')
   pyplot.label('Scores')
   pyplot.title('Scores by Lab')
   ```
   Sets the labels for the x-axis, y-axis, and the title of the plot.

8. **X-axis Ticks and Legend:**
   ```python
   pyplot.sticks(ticks, ticks_labels)
   pyplot.legend()
   ```
   Sets the x-axis tick positions and their labels and displays the legend.

9. **Display the Plot:**
   ```python
   pyplot.show()
   ```
   Finally, this command displays the plot with all the specified parameters and data.

The code generates a side-by-side bar chart displaying the scores of Team A and Team B for different labs, making it easy to compare the performance of the two teams across various labs.
