# sqlalchemy-challenge
Module 10 Challenge

![download](https://github.com/KrissinaW/sqlalchemy-challenge/assets/162597320/9b057a58-0b00-428f-af98-65a8d5ca75c4)
![images](https://github.com/KrissinaW/sqlalchemy-challenge/assets/162597320/c5848f45-dd63-48cb-b979-13c5c23b2152)


# **Background**: 

**It's About Time!**

I have decided to treat myself to a long holiday vacation in Honolulu, Hawaii. 

To help with my trip planning, I have decided to do a climate analysis about the area. 

The following sections outline the steps that I took to accomplish this task.

# **Instructions:**

**Part 1: Analyze and Explore the Climate Data**

In this section, I will use Python and SQLAlchemy to do a basic climate analysis and data exploration of my climate database. Specifically, i'll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

You are able to view the analysis in the SurfUp file by following this link: [climate_data](SurfsUp/climate_data.ipynb)

- I’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete the climate analysis and data exploration.

- Use the SQLAlchemy create_engine() function to connect to the SQLite database.

- Use the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.

- Link Python to the database by creating a SQLAlchemy session.

- Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

**Precipitation Analysis**

* Find the most recent date in the dataset.

* Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

* Load the query results into a Pandas DataFrame. Explicitly set the column names.

* Sort the DataFrame values by "date".

* Plot the results by using the DataFrame plot method.
  
**Station Analysis**

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

      * List the stations and observation counts in descending order.

      * Filter by the station that has the greatest number of observations.

* Query the previous 12 months of TOBS data for that station.

* Plot the results as a histogram with bins=12.

# **Part 2: Design Your Climate App**
Now that I have completed the initial analysis, I will design a Flask API based on the queries that were just developed. 

You are able to view the Climate App in the SurfUp file by following this link: [climate_app](SurfsUp/Climate_app.py)

To do so, I will use Flask to create routes as follows:

1. /

        * Start at the homepage.

        * List all the available routes.

2. /api/v1.0/precipitation

        * Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

        * Return the JSON representation of your dictionary.

3. /api/v1.0/stations

        * Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs

        * Query the dates and temperature observations of the most-active station for the previous year of data.

        * Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

        * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

        * For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

        * For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

# **Resources used:** 

