# StockSight

A stock market analytics and forecasting web application built with Streamlit. It fetches
historical price data via yFinance, plots moving average overlays, and forecasts close
prices using a trained LSTM neural network.

## Architecture

The project is split into two scripts. `train.py` handles data ingestion, preprocessing,
model construction, and saving the trained weights. `app.py` loads the saved model and
runs the Streamlit interface, accepting a ticker and date range as inputs and rendering
four charts: three moving average overlays and one original-vs-predicted price comparison.

## Model Architecture

| Layer    | Type    | Units | Dropout |
|----------|---------|-------|---------|
| 1        | LSTM    | 50    | 0.2     |
| 2        | LSTM    | 60    | 0.3     |
| 3        | LSTM    | 80    | 0.4     |
| 4        | LSTM    | 120   | 0.5     |
| Output   | Dense   | 1     | -       |

The model is compiled with the Adam optimizer and minimizes mean squared error loss.
Input data is normalized via MinMaxScaler and structured into 100-day sliding windows
over the training portion, which covers 80 percent of the fetched historical data.

## Visualizations

| Chart                        | Description                                      |
|------------------------------|--------------------------------------------------|
| Price vs MA50                | Close price overlaid with 50-day moving average  |
| Price vs MA50 and MA100      | Close price with 50 and 100-day moving averages  |
| Price vs MA100 and MA200     | Close price with 100 and 200-day moving averages |
| Original vs Predicted Price  | Test set ground truth against model output       |

## Repository Structure

```text
StockSight/
|-- model/
|   `-- .gitkeep
|-- app.py
|-- train.py
|-- requirements.txt
|-- README.md
`-- .gitignore
```

## Setup

```bash
git clone <repo-url>
cd StockSight
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Training the Model

```bash
python train.py
```

The script downloads GOOG historical data from 2012 to 2022, preprocesses the close
price into 100-day sliding windows, and trains the LSTM for 50 epochs. The trained model
is saved to `model/stock_predictions_model.keras`. This file is gitignored and must exist
before running the app.

## Running the App

```bash
streamlit run app.py
```

Enter any valid ticker symbol and a date range in the browser interface. The app fetches
data live via yFinance, computes moving averages, runs inference against the loaded model,
and renders all four charts.



## Developer
* Navadeep Nandedapu
* Indian Institute of Technology Kharagpur
