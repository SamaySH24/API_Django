Sportshedge - Samay Sawal

This Repo contains a Django Project on rest framework

It has an app named api_sportshedge which has one model in model.py and 3 API calls.

The three APIs include:
  1. Getting API key from Cricsheet key
  2. Getting Fantasy Points from Player ID
  3. Getting Historical Price from Player ID
  
The app connects to PostgreSQL database using psycopg2 library and fetches data from the database using Query tool. Connection parameters as of now has my local credentials but to integrate it we should write connection paramaters of PostgreSQL databse of Sportshedge.

Any doubt - samay@sportshedge.io
