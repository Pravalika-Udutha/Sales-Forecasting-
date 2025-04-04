# Sales Forecating for a Store Using Streamlit

Welcome to the **Sales Forecating for a Store Using Streamlit** project! This is a simple web application built with Python, Streamlit, and Scikit-Learn to predict a Sales (in LPA) based on their Adversting,Discount and No.of people visited the store. The app uses a Linear Regression model trained on a sample dataset and provides an interactive interface for users to input and get predictions.

## Features
- **User-Friendly Interface**: Enter your Advertising,Discount and No.of people visited store through a simple input field in the Streamlit app.
- **Real-Time Prediction**: Get instant predictions of your Sales in lakhs based on the trained model.
- **Simple Linear Regression**: Uses Scikit-Learn's LinearRegression model for accurate predictions.

## Project Structure
``` Pattern
CGPA-Predictor-Using-Streamlit/
│
├── app.py              # Main Streamlit application file
├── store_data.csv       # Sample dataset (CGPA and Package)
├── requirements.txt    # List of required Python libraries
└── README.md           # Project documentation (this file)
```


## Installation
Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pravalika-Udutha/Sales_Prediction_for_a_Store/.git
   cd Sales_Prediction_for_a_Store
   ```
2. **Install Dependencies**:

Ensure you have Python installed (version 3.7+ recommended). Then install the required libraries:

```bash
pip install -r requirements.txt
```
3. **Launch the App**:
```bash
streamlit run app.py
```
Open your browser and go to http://localhost:8501 to see the app in action.
``

## How It Works

- **Data Loading**: The app loads the `store.csv` dataset using Pandas.  
- **Model Training**: A Linear Regression model is trained using Scikit-Learn.  
- **Prediction**: Based on the user input, it predicts the sales value in lakhs
- **Output**: The predicted package is displayed on the Streamlit interface.  

## Usage

1. Open the app in your browser.  
2. Enter your data  in the sidebar input field.  
3. Click the **"Predict Sales"** button.  
4. See the predicted sales value displayed on the screen.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

1. Fork the repo.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m "Add new feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.


## Author

 Pravalika Udutha.
 
 GitHub: [Pravalika Udutha](https://github.com/Pravalika-Udutha).






