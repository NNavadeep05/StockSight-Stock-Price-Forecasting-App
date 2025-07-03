# Stock Market Predictor

This project provides a web-based application for predicting stock market prices and visualizing historical stock data with moving averages. Built using Python, it leverages machine learning for predictions and Streamlit for an interactive user interface.

## Features

* **Stock Price Prediction:** Predicts future stock prices based on historical data using a trained deep learning model.
* **Historical Data Visualization:** Displays actual historical stock prices.
* **Moving Average Analysis:** Visualizes 50-day, 100-day, and 200-day Simple Moving Averages (SMA) to help identify trends and potential support/resistance levels.
* **Interactive User Interface:** Allows users to input any valid stock symbol to fetch and analyze its data.

## Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For creating the interactive web application.
* **Keras (with TensorFlow backend):** For building and loading the deep learning prediction model.
* **yfinance:** To download historical stock data from Yahoo Finance.
* **Pandas:** For data manipulation and analysis.
* **NumPy:** For numerical operations.
* **Matplotlib:** For creating visualizations.
* **scikit-learn:** For data preprocessing, specifically `MinMaxScaler`.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Ensure you have Python 3.7+ installed.

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd stock-market-predictor
    ```
    *(Replace `<repository_url>` with your actual repository URL if this project is hosted on GitHub, GitLab, etc. If not, you can omit this step and just ensure the project files are in a directory.)*

2.  **Install the required Python packages:**
    ```bash
    pip install streamlit tensorflow yfinance pandas numpy matplotlib scikit-learn
    ```

3.  **Download/Train the Model:**
    The `app.py` file expects a Keras model named `Stock Predictions Model.keras`. You will need to either:
    * Run the `Stock_Market_Prediction_Model_Creation.ipynb` Jupyter notebook to train the model and save it.
    * Place a pre-trained `Stock Predictions Model.keras` file in the correct location.

    **Important:** The current `app.py` has a hardcoded path for the model: `'C:\\Python\\Stock\\Stock Predictions Model.keras'`. For easier portability, it's recommended to place `Stock Predictions Model.keras` in the same directory as `app.py` and change the `load_model` line in `app.py` to:
    ```python
    model = load_model('Stock Predictions Model.keras')
    ```

### Running the Application

To run the Streamlit application, navigate to the project directory in your terminal and execute:

```bash
streamlit run app.py
