# Telecom Churn Prediction

This project focuses on predicting customer churn in a telecom company using a Random Forest classifier. The goal is to identify customers who are likely to cancel their service, allowing the company to take proactive measures to retain them.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

Customer churn is a significant issue in the telecom industry, where customers frequently switch service providers. Predicting churn can help telecom companies identify high-risk customers and develop strategies to improve customer retention. In this project, a Random Forest classifier is used to predict churn based on various customer features.

## Dataset

The dataset used in this project includes customer information such as:
- Customer demographics 
- Subscription details 
- Account Details
- Contract details

The dataset can be obtained from Kaggle. It typically contains features and a target variable (`Churn`) indicating whether the customer has churned.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/telecom-churn-prediction.git
   cd telecom-churn-prediction
2. Install the required packages:
   pip install -r requirements.txt
   
## Project Structure

This project is organized as follows:

- `data/`: Contains the datasets
  - `raw/`: Original, immutable data dump
  - `processed/`: Cleaned and processed data ready for modeling
- `notebooks/`: Jupyter notebooks for exploration and modeling
  - `Exploratory Data Analysis.ipynb`: Initial data exploration
  - `Churn Prediction Model.ipynb`: Model development and evaluation
- `src/`: Source code for use in this project
  - `data_preprocessing.py`: Scripts to clean and preprocess data
  - `model.py`: Scripts for training and using the model
- `app.py`: Main application file (e.g., for deploying the model)
- `requirements.txt`: The list of required Python packages
- `model.pkl`: Serialized model file
- `README.md`: The top-level README for developers using this project
