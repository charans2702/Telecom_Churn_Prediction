Telecom Customer Churn Prediction

**Project Overview**

This project aims to predict customer churn in a telecom company using machine learning techniques. By analyzing various customer attributes and behaviors, we develop a model to identify customers who are likely to discontinue their services.

**Table of Contents**

* Installation
* Project Structure (Optional)
* Usage
* Data
* Model
* Results
* Contributing
* License
![Image description]('images/grid2_heatmap.png')
**Installation**

To set up this project, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/telecom-churn-prediction.git`
2. Navigate to the project directory: `cd telecom-churn-prediction`
3. Install the required packages: `pip install -r requirements.txt`

**Project Structure (Optional)**

Directory/File	Description
Telecom_Churn-Prediction	Main project directory
├── images	Visualization outputs
├── templates	Flask application templates (if applicable)
├── app.py	Main Flask application script (if applicable)
├── Churn_Prediction_model.ipynb	Jupyter Notebook for model development
├── Cleaned_Telco_data.csv	Cleaned and preprocessed data
├── Exploratory_data_Analysis.ipynb	EDA exploration notebook
├── finalresult.png	Additional result visualization (optional)
├── requirements.txt	List of required Python packages
├── model.pkl	Trained model pickle file
└── README.md	This file (project documentation)

Export to Sheets

**Usage**

To run the prediction model:

1. Ensure all dependencies are installed (`pip install -r requirements.txt`).
2. Run the Flask application (if applicable): follow instructions in `app.py`.
   - Alternatively, use the model directly through the Python code in `Churn_Prediction_model.ipynb`.

**Data**

The dataset used in this project is `telco_churn.csv`. It contains various features of telecom customers, including:

* Customer demographics
* Account information
* Services used
* Churn status

**Model**

This project uses a Random Forest Classifier to predict customer churn. The model is trained on historical customer data and evaluated using metrics like confusion matrix, accuracy, ROC AUC curve, and classification report. Refer to `Churn_Prediction_model.ipynb` for details.

**Results**

Our model achieves 78% accuracy in predicting customer churn. The `images` directory contains various visualizations that aid in understanding the model's performance and feature importance (e.g., `confusion_matrix.png`, `feature_importance.png`).

**Contributing**

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

**License**   


MIT License
