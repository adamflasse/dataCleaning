# Becode Challenge: Cleaning data
by: Dilara P. - Ankita H. - Christophe S. - Adam F.

The purpose here is to clean a dataset with different sources of information.

Please click [here](https://drive.google.com/file/d/1YY-QRAKNAR1Kg_htWioGengq8mv5aUU5/view?usp=sharing) for the presentation.

## Dealing with duplicates
First thing first we had to find the possible duplicates in the dataset.
So there were several problems in order to make such a thing possible. The main one was to have each element of the column 'hyperlink' in the same format. 
The hyperlink column correspond to a sort of ID for each house listed in the dataset. Some of the elements were good and nothing was to change but some others were urls where we have to 'extract' the ID out of it. To do that a function that uses regex was enough. 
When this was done we can easily find any duplicates and delete them in order to have a much smaller and more concise dataset.


## Dealing with missing values
Afterwards we have to filter what would be the relevant columns to keep. 
For example a column with too much missing values wouldn't be relevant.
So in order to do that we have made a percentage of the missing values for each column. 
Some of them are important to keep even if their percentage are quite high. But we can work with the data being informed that a certain amount of data is missing.


## Get familiar with the dataset
When all of it is done we have to provide some visualizations.
So the goal here is to be really well aware of the data itself. Indeed the dataset will be used to train our future machine learning model. 




