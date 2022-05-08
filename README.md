# Surfs_up
Analyzing weather data using SQLite and Pandas

![surfboard](https://github.com/Mots94/Surfs_up/blob/main/Resources/surfboard.jpg)

## Overview
In this analysis, the stakeholder would like to know if opening an ice cream shop on the island of Oahu, Hawaii would be sustainable year-round.  In order to answer this question, weather data was analyzed for the purpose of interpretation and to aid in the decision making process.  A SQLITE database containing eight years worth of weather data was used in this analysis.  The project stakeholder would like to focus on Oahu's temperature in the months of June and December, so the statistics generated were focused on those two months.

## Results

<details><summary>June & December Temperature Data</summary>                                                  
<p>                                                                                  
                                                                                     
![june_stats](https://github.com/Mots94/Surfs_up/blob/main/Resources/june_stats.PNG) ![dec_stats](https://github.com/Mots94/Surfs_up/blob/main/Resources/dec_stats.PNG)

</p>
</details>

* For the months of June and December, the sample sizes of temperature observations were 1700 and 1517 respectively.  Although December had a slightly smaller sample, the average temperatures between these two months are not drastically different.  In June, the average temperature in Oahu was 74.94 degrees Fahrenheit and the median temperature was 75 degrees Fahreneheit.  In December, the average temperature was 71.04 degrees Fahrenheit and the median temperature was 71 degrees Fahrenheit.  The means and medians for both months are quite close, so it is safe to assume that this sample of data has a normal distribution. 

* Similarly, the standard deviation for the months of June and December are not too different from one another.  The standard deviation for June was 3.26, meaning that 95% of temperature observations were between 68.42 and 81.46 degrees for that month.  December's stardard deviation was 3.75, so 95% of the observations in that month were between 63.54 and 78.54 degrees.

* In both June and December, there are low and high outliers in this dataset, though the exact number of outliers is not known.  The formulas *quartile 1 (Q1) - inter-quartile range (IQR) * 1.5* and *Q3 + IQR * 1.5* were used to make this determination.  The minimum and maximum temperatures for June were 64 and 85 degrees respectively.  These values are outside IQR * 1.5 from the Q1 and Q3 values.  The minimum and maximum temperatures for December were 56 and 83 degrees respectively.  Similar to June, these values are further than IQR * 1.5 away from the Q1 and Q3 values.  Though there are outliers, the distribution for data in both months has already been determined to be normal.  It is likely that there were either not enough outliers to skew temperature data, or that there were a similar number of outliers on both sides of the distribution.

## Summary
Overall, the temperatures in the months of June and December in Oahu do not appear to differ greatly on average.  The lowest temperature observed in December was 56 degrees, and although an individual may not want to eat ice cream in that weather, it was determined that a temperature that low was an outlier for this data set.  Therefore, lower temperatures like this one are not very common at all, even during the winter months. An ice cream store on the island of Oahu would most likely be successful year round because the weather is fairly consistent between summer and winter months.  

---
One additional query that could be insightful would be to pull elevation data from the stations table in order to find stations that are closer to beach areas.  This project stakeholder would like to open his shop near the beach to increase foot traffic.  If this business decision is based on all of the data in this database, that may include temperature observations from mountainous regions.  Since these areas would not be highly accessible to beach goers, it would be worthwhile to filter elevation data to find weather stations closer to sea level.

---
A second query that may provide context for this business decision is a query on precipitation data.  Although an area of Oahu may have consistenly high temperatures, if it experiences heavy rain during the hottest months then customers would not be as abundant.  This query could be used in conjunction with the elevation query to find an area in close proximity to a beach that does not experience too much precipitation.