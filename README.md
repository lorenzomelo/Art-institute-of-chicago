# Art-institute-of-chicago

FIRST TASK

The first task is a data collection task: we are are required to collect data by accessing the API of third party services. The task is completed when a full dataset is built.

The project that we have chosen in order to complete this task is the project #5: the Art Institute of Chicago's API provides JSON-formatted data as a REST-style service that allows developers to explore and integrate the museum’s public data into their projects.

In order to do this we first needed to retrieve the contents from a web ULR using the requests module. In this particular case the URL contains all the published artworks in the collection. The format of the response is JSON (JavaScript Object Notation), that is a lightweigh data-interchange format.

The second step is to write the contents to a .json file. In order to do this, we can use the following lines:
file = open("./file-" + ".json", "w+")
file.writelines(response.text)
file.close()

Finally we need to manipulate the data and load them in a dataframe (two-dimensional, size-mutable, potentially heterogeneous tabular data), so that we can use the to_csv() function to create a .csv.
In order to do this, we first use json.loads() to load the .json content in a python object (e.g, a list) and then the latter is transformed into a dataframe using pandas.DataFrame() from pandas library. Once we have done this, the final step before converting the dataframe in .csv is to name the columns through the .columns function.



SECOND TASK

Data manipulation task
The first thing we had to do to complete our task was to extract some useful information that was saved inside dictionaries in the “thumbnail” column. We created new column named after the keys of the dictionaries and containing the associated values for each observation.

Data Exploration task
After doing this, we started looking at our dataset to find some information that could be visualized to extract some insights. Unfortunately, given the nature of the data we found very little useful information to be shown.
To carry out our data exploration task we used both the ggplot functions imported from plotnine and the matplotlib library to plot a bar timeline.
The first plot we made is a scatterplot of dimensions per artwork.

<img width="482" alt="image" src="https://user-images.githubusercontent.com/93518256/145825961-4198e0a6-771c-472b-af76-0f2b4ac525ca.png">
 

The second one is a bar plot showing the number of artworks per country of origin.
 
 <img width="482" alt="image" src="https://user-images.githubusercontent.com/93518256/145826028-f2ec3697-8959-4e3c-ac90-a48fb8ba2614.png">


The last two are bar timelines of the estimated period in which the artists worked on the artworks. We divided the two in modern and antique artworks for better visualization. The first plot is not very useful and clear because some for some artworks a very short period of time was spent in realizing them.

 <img width="482" alt="image" src="https://user-images.githubusercontent.com/93518256/145826058-a90f12a2-0489-4a13-98a5-4d0a5fa5d538.png">


On the other end, for the two most antique artworks, the bar timeline looks better. 

<img width="482" alt="image" src="https://user-images.githubusercontent.com/93518256/145826085-9e410d93-feb7-4dcf-81b1-b96afa7f232f.png">
