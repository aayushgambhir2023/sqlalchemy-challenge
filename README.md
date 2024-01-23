SQL Alchemy Challenge


Before diving into the climate analysis and data exploration of Honolulu, Hawaii, I followed the initial setup steps for the project. I created a new repository named "sqlalchemy-challenge" and cloned it to my local machine. Within this repository, I established a dedicated directory named "SurfsUp" to house the Jupyter notebook (`climate_starter.ipynb`) and Flask application script (`app.py`). Additionally, I included a "Resources" folder containing the essential data files (`hawaii.sqlite`) for the challenge. After organizing the project structure, I committed and pushed the changes to GitHub or GitLab.

The subsequent sections of the project involve leveraging Python, SQLAlchemy, and data visualization tools for a comprehensive climate analysis. I utilized SQLAlchemy functions like `create_engine()` and `automap_base()` to connect to the SQLite database, reflect tables into classes (station and measurement), and establish a session to interact with the database. Following these setup steps, I conducted a precipitation analysis, identifying the most recent date in the dataset and querying the preceding 12 months of precipitation data. I transformed the query results into a Pandas DataFrame, performed sorting and plotting, and summarized the precipitation data's statistical metrics.

Moving on to the station analysis, I designed queries to determine the total number of stations and identify the most active stations based on observation counts. I further calculated the lowest, highest, and average temperatures for the most active station, and proceeded to query and plot the previous 12 months of temperature observation (TOBS) data for that station.

Closing the SQLAlchemy session, the project then transitions into the design of a Flask API. The API includes routes to retrieve precipitation data, station information, and temperature observations. Additionally, it supports queries for minimum, average, and maximum temperatures for specified start or start-end date ranges. The project is structured to provide a user-friendly climate app that offers valuable insights for trip planning in Honolulu.
