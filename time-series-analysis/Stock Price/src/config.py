from pathlib import Path

ROOT = Path(__file__).parent.parent

DATA_PATH = ROOT / 'data/stock_prices.csv'
MODELS_PATH = ROOT / 'models'
PLOTS_PATH = ROOT / 'plots'

TARGET_COLUMN = 'close'
TEST_SIZE = 0.2
FORECAST_HORIZON = 30
RANDOM_SEED = 42

file_path = DATA_PATH