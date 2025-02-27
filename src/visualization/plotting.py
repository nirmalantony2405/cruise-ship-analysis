import matplotlib.pyplot as plt
import seaborn as sns

def plot_kpi_comparison(df, kpi_column, title, save_path):
    """Plot a bar comparison of a KPI across vessels."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Vessel Name', y=kpi_column, data=df)
    plt.title(title)
    plt.ylabel(kpi_column)
    plt.xlabel('Vessel')
    plt.savefig(save_path)
    plt.show()