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

