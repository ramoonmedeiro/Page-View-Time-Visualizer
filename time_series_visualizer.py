import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv')
df1 = pd.read_csv('./fcc-forum-pageviews.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df1['date'] = pd.to_datetime(df1['date'])

# Clean data
mask1 = (df['value'] > df['value'].quantile(q=0.025)) & (df['value'] < df['value'].quantile(q=0.975))
mask2 = (df1['value'] > df1['value'].quantile(q=0.025)) & (df1['value'] < df1['value'].quantile(q=0.975))
df_clean = df[mask1].copy()
df1_clean = df1[mask2].copy()



def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df_clean.index, df_clean['value'], c = 'red', lw = 1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df1_clean['Year'] = df1_clean['date'].dt.year
    df1_clean['Month'] = df1_clean['date'].dt.month
    df_bar = df1_clean.copy()
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
             'August', 'September', 'October', 'November', 'December']
    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    legenda = plt.legend(title= 'Months', fontsize = 15, labels = meses)
    title = legenda.get_title()
    title.set_fontsize(15)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(15, 5))


    axes[0] = sns.boxplot(data=df_box, x = "year", y = "value", ax = axes[0])
    axes[1] = sns.boxplot(data=df_box, x = "month", y = "value", ax = axes[1])

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title("Month-wise Box Plot (Trend)")
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
