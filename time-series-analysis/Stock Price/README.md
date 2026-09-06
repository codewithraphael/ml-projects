# Stock Price Forecasting

A time series forecasting project for analyzing historical stock prices and estimating future closing prices from the supplied market dataset.

## Overview

Stock prices are sequential observations whose behavior can change over time. This project provides a reproducible workflow for exploring historical market data, creating time-aware features, training forecasting models, and evaluating predictions on unseen future observations.

The analysis is intended for educational and research use. Forecasts are estimates and should not be treated as financial advice or guarantees of future performance.

## Objective

The project aims to:

- inspect historical price and trading-volume behavior
- identify trend, volatility, and recurring patterns
- prepare chronological data without leaking future information
- build and compare stock-price forecasting models
- evaluate predictions using out-of-sample observations
- save plots, trained models, and evaluation results for later review

## Dataset

- File: [data/stock_prices.csv](data/stock_prices.csv)
- Frequency: Trading-day observations
- Time column: `Date`
- Forecast target: `Close`
- Coverage: Historical observations beginning in June 1972

### Columns

| Column | Description |
| --- | --- |
| `Date` | Timestamp for the trading observation, including timezone information in the source file |
| `Open` | Opening price |
| `High` | Highest price during the trading session |
| `Low` | Lowest price during the trading session |
| `Close` | Closing price and primary forecasting target |
| `Volume` | Trading volume |
| `Dividends` | Dividend amount recorded for the observation |
| `Stock Splits` | Stock split factor recorded for the observation |

Before modeling, `Date` should be parsed as a datetime index, observations should be sorted chronologically, and duplicate or missing timestamps should be checked. The target and feature definitions should be adjusted if the dataset is refreshed with a different ticker or time period.

## Project Structure

```text
Stock Price/
├── data/
│   └── stock_prices.csv
├── evaluation result/       # Model metrics and evaluation summaries
├── models/                  # Serialized trained models
├── plots/                   # EDA and forecast visualizations
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── evaluation.py
│   ├── feature_engineering.py
│   ├── forecasting.py
│   ├── preprocessing.py
│   ├── train.py
│   └── utils.py
└── README.md
```

## Recommended Workflow

1. Load the CSV and parse `Date` as a timezone-aware datetime index.
2. Validate chronological order, missing values, duplicate records, and market-closure gaps.
3. Explore `Close`, daily returns, rolling averages, rolling volatility, and trading volume.
4. Create lagged prices, lagged returns, rolling statistics, and calendar features where appropriate.
5. Split the data chronologically into training, validation, and test periods.
6. Train a baseline such as the previous closing price or a moving average.
7. Train forecasting models and compare them against the baseline.
8. Evaluate predictions only on periods that were not used during training.
9. Save plots, metrics, and the selected model in the project output folders.

## Recommended Analysis

The columns in this dataset support several complementary analyses before and alongside forecasting:

### 1. Data Quality and Market Calendar

- inspect data types, missing values, duplicate timestamps, and invalid prices
- confirm that records are sorted by `Date` and that timestamps are consistently timezone-aware
- measure gaps between observations and distinguish weekends or holidays from missing data
- check for zero or unusually low `Volume` values, especially in older observations

### 2. Price and Return Behavior

- plot `Open`, `High`, `Low`, and `Close` over the full history
- calculate daily percentage returns and log returns
- compare close-to-close returns with open-to-close returns
- inspect cumulative returns and drawdowns over time
- calculate rolling means to describe long-term trend

### 3. Volatility and Risk

- calculate rolling standard deviation of returns for short-, medium-, and long-term volatility
- compare high-low price ranges across market periods
- identify unusually large positive or negative return days
- analyze maximum drawdown and recovery periods
- compare volatility during rising and falling market periods

### 4. Volume and Price Relationships

- visualize `Volume` alongside price and returns
- calculate rolling volume averages and volume changes
- investigate whether unusually high volume coincides with large price movements
- compare price and volume correlations across different time windows rather than relying only on a full-history correlation

### 5. Dividends and Stock Splits

- identify dates where `Dividends` or `Stock Splits` are non-zero
- compare raw prices with adjusted-price data when available
- assess whether corporate-action dates create apparent jumps in the series
- avoid treating a split-related price change as ordinary market movement

### 6. Trend, Seasonality, and Stationarity

- aggregate returns and volatility by year, month, weekday, or trading session period
- use rolling statistics and decomposition where the sampling frequency supports it
- apply stationarity tests to prices and returns, with care around long historical periods
- compare behavior across broad historical regimes instead of assuming one stable pattern

### 7. Forecasting Experiments

- establish naive and moving-average forecasts as baselines
- compare raw-close forecasting with return or log-return forecasting
- evaluate one-step-ahead and multi-step forecasts separately
- test lagged prices, returns, rolling volatility, price ranges, and volume features
- use walk-forward or expanding-window validation to model how forecasts would work in practice
- compare forecast accuracy across different market regimes and forecast horizons

All analyses should preserve chronological order. Statistics, transformations, and feature calculations used for a validation or test period must be fitted using information available before that period.

## Modeling Considerations

Potential approaches include:

- naive and moving-average baselines
- exponential smoothing or ARIMA-style models
- regression models using lagged prices, returns, volatility, and volume
- tree-based models such as XGBoost for engineered tabular features

Prices are often non-stationary. Modeling daily returns or log returns may be more appropriate than modeling the raw closing price, depending on the objective. Any transformation applied to the training data must be fitted using training observations only.

Random train/test splits should not be used for this task because they can expose the model to information from the future. Use chronological holdout periods or rolling/expanding-window validation instead.

## Evaluation

Recommended metrics include:

- **MAE**: average absolute prediction error in price units
- **RMSE**: gives greater weight to large errors
- **MAPE**: relative error, when the target values are non-zero
- **Directional accuracy**: proportion of periods where the predicted movement direction is correct

Metrics should be reported alongside the forecast horizon and test period. A model should be compared with a naive baseline before its performance is considered meaningful.

## Setup

From the repository root on Windows:

```powershell
cd "time-series-analysis\Stock Price"
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r ..\..\requirements.txt
```

The repository requirements include the core data-science and machine-learning packages used across the project. Add any model-specific dependency, such as `statsmodels`, `matplotlib`, or `seaborn`, before running an implementation that imports it.

## Usage

The source modules are organized by responsibility:

- `data_loader.py`: read and validate the source data
- `eda.py`: produce exploratory summaries and visualizations
- `preprocessing.py`: clean data and prepare chronological splits
- `feature_engineering.py`: create lag, return, rolling, and calendar features
- `forecasting.py`: generate forecasts from trained models and future feature values
- `train.py`: train and persist forecasting models
- `evaluation.py`: calculate metrics and compare predictions
- `config.py`: define project paths

As the project is developed, run the modules from the `Stock Price` directory so their relative paths resolve consistently. Generated artifacts should be placed in `plots/`, `models/`, and `evaluation result/` rather than committed alongside the raw dataset.

## Limitations

Historical price data alone cannot account for news, earnings, macroeconomic changes, market regime shifts, liquidity, or other external events. Long-range forecasts are especially uncertain, and strong historical performance does not imply reliable future returns.

## License

This project is part of the broader machine-learning repository and is intended for educational and research purposes.
