import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd


df = pd.read_csv('data/processed/ghana_indicators.csv')

inflation_df = df[df['indicator_name'] == 'inflation_rate']

def plot_inflation():
    inflation_df = df[df['indicator_name'] == 'inflation_rate']

    plt.figure(figsize=(10,5))
    plt.plot(inflation_df['year'], inflation_df['value'], marker='o',color='red')
    plt.title('Ghana Inflation Rate (2000-2025)')
    plt.xlabel('Year')
    plt.ylabel('Inflation %')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/processed/inflation.png')
    plt.show()

def plot_all_indicators():
    indicators = df['indicator_name'].unique()
    
    fig, axes = plt.subplots(len(indicators), 1, figsize=(10,5* len(indicators)))
    
    for i, indicator in enumerate(indicators):
        indicator_df = df[df['indicator_name'] == indicator]
        axes[i].plot(indicator_df['year'], indicator_df['value'], marker='o')
        axes[i].set_title(indicator)
        axes[i].set_xlabel('Year')
        axes[i].grid(True)
    
    plt.tight_layout()
    plt.savefig('data/processed/all_indicators.png')
    plt.show()

if __name__ == "__main__":
    plot_inflation()
    plot_all_indicators()