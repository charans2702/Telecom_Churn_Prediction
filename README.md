# Telecom Customer Churn Prediction

## Project Overview
This project aims to predict customer churn in a telecom company using machine learning techniques. By analyzing various customer attributes and behaviors, we develop a model to identify customers who are likely to discontinue their services.

## Table of Contents
1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
4. [Data](#data)
5. [Model](#model)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

## Installation
To set up this project, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/telecom-churn-prediction.git
2. Navigate to the project directory:
   cd telecom-churn-prediction
3. Install the required packages:
   pip install -r requirements.txt

   
## Project Structure
Telecom_Churn-Prediction/
│
├── images/
│   ├── confusion_matrix.png
│   └── feature_importance.png
|   |--- final_result.png
|   |---grid1_heatmap.png
|   |---grid2_heatmap.png
|   |---grid3_heatmap.png
|   |---grid4_heatmap.png
|   |---prediction_chart.png
|   |---roc_curve.png
├── templates/
│   ├── index.html
├── app.py 
├── Churn_Prediction_model.ipynb
|--- Cleaned_Telco_data.csv
|---Exploratory_data_Analysis.ipynb
|--finalresult.png
├── requirements.txt
├── model.pkl
└── README.md
|---telco_churn.csv
## Usage
To run the prediction model:
1. Ensure all dependencies are installed
2. Run the Flask application:
3. Open a web browser and go to `http://localhost:5000`

## Data
The dataset used in this project is `telco_churn.csv`. It contains various features of telecom customers, including:
- Customer demographics
- Account information
- Services used
- Churn status

## Model
I used Random Forest Classifier to predict customer churn. The model is trained on historical customer data and evaluated using [Confusion metrics,accuracy, Roc_auc_curve,Classification_report].

## Results
Our model achieves 78% accuracy in predicting customer churn.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
MIT License
