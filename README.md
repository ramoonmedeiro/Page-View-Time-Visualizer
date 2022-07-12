# Page-View-Time-Visualizer

This project aims to study the number of views of the freeCodeCamp.org forum page between the dates 2016-05-09 to 2019-12-03. The dataset used was fcc-forum-pageviews.csv. Data cleaning was performed for days when pageviews were in the top 2.5% of the dataset or the bottom 2.5% of the dataset. Such data were excluded. The full project can be seen here: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer.

# LinePlot 

The graph below shows the evolution of the number of page views as a function of date.
Note that there are some larger spikes that may represent some super interesting topic or discussion on the forum. But apart from these points, there is an increase in the number of views over the months or years.

<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/178588773-54bcb960-2f73-49a4-ad2e-5693311a844c.png" width="700px" />
</div>

# BarPlot

The figure below shows the average number of views for each month in a given year. Here we can look at the data a little more in detail, again noticing an increase in the number of views year after year.
Some months are missing for the year 2016, as they were not included in the dataset or were filtered out in the data cleaning step.

<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/178589650-165e30d3-e2af-4ae1-a139-050532235673.png" width="700px" />
</div>

# BoxPlot

In the figure below you can see two boxplot graphs. The graph on the left shows the values for each year. And the graph on the right shows the values for each month for all years.
Boxplot plots are great for looking at how values are distributed for each year and each month. Another interesting thing is to observe the oulier values, which are values above the maximum or below the minimum for the extremes established in the boxplot.

<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/178589029-d4d52561-c760-4d0a-bd56-5efc297685b9.png" width="700px" />
</div>
