import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

from config import PLOTS_PATH

def eda(data):

    print('='*80)
    print(' '*30 + 'STOCK PRICE FORECASTING')
    print('='*80)

    print(data.head(10))

    print(f'\n ===== SHAPE OF THE DATASET ===== \n {data.shape}')
    print(f'\n ===== DATASET INFORMATION ===== \n')
    print(data.info())
    print(f' \n ===== CHECKING MISSING VALUES ===== \n {data.isnull().sum()}')
    print(f'\n ===== CHECKING DUPLICATE VALUES ===== \n {data.duplicated().sum()}')
    print(f'\n ===== SUMMARY STATISTICS ===== \n {data.describe()}')


def visualize_data(data):

    fig, axes = plt.subplots(1, 7, figsize=(80, 6))

    data['open'].plot(ax=axes[0], color='steelblue')
    axes[0].set_title('Stock Open Price')
    axes[0].set_ylabel('Open')

    data['high'].plot(ax=axes[1], color='coral')
    axes[1].set_title('High Stock Price')
    axes[1].set_ylabel('High Price')

    data['low'].plot(ax=axes[2], color='green')
    axes[2].set_title('Low Stock Prie')
    axes[2].set_ylabel('Low Price')

    data['close'].plot(ax=axes[3], color='purple')
    axes[3].set_title('Close Stock Price')
    axes[3].set_ylabel('Close Price')   

    data['volume'].hist(ax=axes[4], color='tomato')
    axes[4].set_title('Volume of Stock Purchased')
    axes[4].set_ylabel('Volume')

    data['dividends'].plot(ax=axes[5], color='mediumpurple')
    axes[5].set_title('Dividends')
    axes[5].set_ylabel('Dividends')

    data['stock splits'].plot(ax=axes[6], color='purple')
    axes[6].set_title('Stock Splits')
    axes[6].set_ylabel('Stock Splits')


    plt.tight_layout()
    plt.savefig(PLOTS_PATH / 'stock_distribution.png')
    plt.close()