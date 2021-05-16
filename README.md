# Surfs_up

## Overview of the statistical analysis:

The purpose of this analysis was to dive in to our weather observations for specific months (June and December). In order to do this, we had to query our Hawaii.sqlite file with filters to ensure we were only pulling temperature data for specific months of the year. Upon extracting the relevant data, we had to convert the data to a Pandas dataframe in order to generate our summary statistics so we could analyze the data. 

## Results

 There are three key differences in the data outlined below: 

  1) The temperature data between June and December in Hawaii was of comparable size, with 1700 observations in June and 1517 in December. Having data sets of equal  sizes should help us get a good representative comparison between tempartures of the two months. 
  
  2) There is only about a 4 degrees farenheit difference between June (74.9) and Decembers (71.0) average temperature. While this mean's can be skewed, this data suggests Hawaii's temperature is rather stable throughout the year.
  
  3) The standard deviations of both June (3.25 degrees) and December (3.75 degrees) are relatively comparable. This suggestes that there is a healther dispersion in the data, and continues to support our initial hypothesis that the temperature is relatively stable year round. In addition to a consistent standard deviation, the quartile data is relatviely comparable at both times of year

### June Data

<img width="150" alt="June Data" src="https://user-images.githubusercontent.com/80016496/118401486-8835ac80-b62b-11eb-96b1-782cbdb108b2.png">

### December Data

<img width="150" alt="Dec Data" src="https://user-images.githubusercontent.com/80016496/118401509-97b4f580-b62b-11eb-9b3b-f374bf48004b.png">


## Considerations for Further Analysis

To conduct a better analysis of temperature data in hawaii, we could include quarterly data, as a opposed to just June and December. By Collecting March, June, September, and December data, we would get a clearer picture of weather consistency. In addition to our temperature analysis for the given months, we could also evaluate precipitation and use matplotlib to plot the data and create a visual representation of wholistic weather trends as opposed to just temperatures.
