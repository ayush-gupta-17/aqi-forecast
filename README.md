# AQI Forecast System

## Project Overview

The AQI Forecast System is a basic Machine Learning project developed in Python. It predicts the Air Quality Index (AQI) based on major air pollutants using a Random Forest Regression model.

## Features

* Predicts AQI from pollutant values.
* Uses Random Forest Regression.
* Console-based application.
* Beginner-friendly implementation.
* Single Python file.

## Technologies Used

* Python
* Pandas
* Scikit-learn

## Project Structure

```
aqi_forecast/
│
├── app.py
├── aqi.csv
└── README.md
```

## Dataset

The dataset contains the following features:

* PM2.5
* PM10
* NO2
* SO2
* CO
* O3
* AQI (Target)

## Installation

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## How to Run

Run the following command:

```bash
python app.py
```

Enter the pollutant values when prompted. The program will predict the AQI and display the corresponding air quality category.

## AQI Categories

| AQI Range | Category     |
| --------- | ------------ |
| 0 – 50    | Good         |
| 51 – 100  | Satisfactory |
| 101 – 200 | Moderate     |
| 201 – 300 | Poor         |
| 301 – 400 | Very Poor    |
| Above 400 | Severe       |

## Future Improvements

* Use a larger real-world AQI dataset.
* Add graphical visualizations.
* Develop a web interface using Flask or Streamlit.
* Improve prediction accuracy through hyperparameter tuning.

## Author

**Ayush Gupta**

**Intern ID:** CITS3847
