# ETL survey 123
This project extract data from survey123, transform and loads to database.

![etl process](img/etl.png)

## Car Predict
Using Machine Learning to predict Vehicle prices in Colombia.

## Run locally
Please create your virtual environment before, for example
```bash
python3 -m venv myenv
source myenv/bin/activate
```
Create a .env file in the root folder with de follow structure
```bash
SURVEY_URL = 
SURVEY_USERNAME = 
SURVEY_PASSWORD =
SURVEY_ITEM_ID = 
PASSWORD=
PORT=
DB_NAME=
USER_NAME=
HOST=
```

Install requirements

```bash
pip install requirements.txt
```
Run python ETL script

```bash
python main.py
```

