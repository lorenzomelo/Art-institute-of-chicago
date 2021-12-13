# ----------------------------------------------------------------------#
# -------------------- Some Data Manipulation --------------------------#
# ----------------------------------------------------------------------#

# Remove last column from the dataset as it is useless
df = df.iloc[:,0:92]

# Assign variable names to the columns of the dataset
col = [i for i in [dati_json["data"][0]]]
df2 = df.set_axis(col[0], axis=1, inplace=False)
df2.head()

# The thumbnail column is still a dictionary containing 4 keys.
# We need to save the values of each key in a correpsonding column named after the key itself.

# Create a list of new column names
newcol_names = list()
for i in df.iloc[:,6][1]:
    newcol_names.append(i)
print(newcol_names)

# Create lists containing data corresponding to the new column name
lqip_data = list()
width_data = list()
height_data = list()
alt_text_data = list()
for j in range(0,12):
    lqip_data.append(df.iloc[:,6][j][newcol_names[0]])
for j in range(0,12):
    width_data.append(df.iloc[:,6][j][newcol_names[1]])
for j in range(0,12):
    height_data.append(df.iloc[:,6][j][newcol_names[2]])
for j in range(0,12):
    alt_text_data.append(df.iloc[:,6][j][newcol_names[3]])
    
# Remove thumbnail from the dataset
#df2 = df2.drop(labels = 'thumbnail', axis = 1)

# Add the new columns
df2['lqip'] = lqip_data
df2['width'] = width_data
df2['height'] = height_data
df2['alt_text'] = alt_text_data

df2.head(5)

# ----------------------------------------------------------------------#
# -------------------- Some Data Exploration- --------------------------#
# ----------------------------------------------------------------------#

# Import ggplot functions from plotnine

from plotnine import *

# Plot each artwork dimension

(
    ggplot(df2)
    + geom_point(aes(x = 'width', y = 'height', color = 'title', fill = 'title'), size = 3)
    + ggtitle('Width and Height per artwork')
    + ylab('Height')
    + xlab('Width')
)

# Plot the number of artworks per place of origin

(
    ggplot(df2)
    + geom_bar(aes(x = 'place_of_origin', color = 'place_of_origin', fill = 'place_of_origin'))
    + ggtitle('Number of artworks per place of origin')
    + ylab('Number of artworks')
    + xlab('place of origin')
)

# Plot a bar timeline of artworks' realization period

import matplotlib.pyplot as plt

# Separte the modern artworks (from 18th to 20th century) from older ones (12th century)

modern_start = df2['date_start'].drop([5,9])
modern_end = df2['date_end'].drop([5,9])
modern_title = df2['title'].drop([5,9])

ancient_start = df2['date_start'].iloc[[5,9]]
ancient_end = df2['date_end'].iloc[[5,9]]
ancient_title = df2['title'].iloc[[5,9]]

# Plot the bar timeline for modern artworks
plt.barh(range(len(modern_start)),  modern_end-modern_start, left=modern_start)
plt.yticks(range(len(modern_start)), modern_title)
plt.title('Bar timeline of the modern artworks')
plt.show()

# Not so good or useful

# Plot the antique artworks bar timeline
plt.barh(range(len(ancient_start)),  ancient_end-ancient_start, left=ancient_start)
plt.yticks(range(len(ancient_start)), ancient_title)
plt.title("Bar timeline of the two most antique artworks")
plt.show()

# Better




