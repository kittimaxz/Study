{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOAvEInKK81OVDWOj2qMpiM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kittimaxz/Study/blob/main/time_series_visualizer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "K80qrZ5KQoHM"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "from pandas.plotting import register_matplotlib_converters\n",
        "register_matplotlib_converters()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Import data (using the direct URL link) and set index to the date column.\n",
        "# parse_dates=True ensures the index is treated as datetime objects.\n",
        "df = pd.read_csv(\n",
        "    'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/main/fcc-forum-pageviews.csv',\n",
        "    parse_dates=['date'],\n",
        "    index_col='date'\n",
        ")"
      ],
      "metadata": {
        "id": "IzqBnYhJRN-x"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2. Clean data by filtering out days in the top 2.5% and bottom 2.5% of the dataset.\n",
        "df = df[\n",
        "    (df['value'] >= df['value'].quantile(0.025)) &\n",
        "    (df['value'] <= df['value'].quantile(0.975))\n",
        "]"
      ],
      "metadata": {
        "id": "4YqPgJ_6RRb4"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 3. Create a draw_line_plot function\n",
        "def draw_line_plot():\n",
        "    # Draw line plot\n",
        "    fig, ax = plt.subplots(figsize=(15, 5))\n",
        "    ax.plot(df.index, df['value'], color='red', linewidth=1)\n",
        "\n",
        "    # Set titles and labels\n",
        "    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')\n",
        "    ax.set_xlabel('Date')\n",
        "    ax.set_ylabel('Page Views')\n",
        "\n",
        "    # Save image and return fig (don't change this part)\n",
        "    fig.savefig('line_plot.png')\n",
        "    return fig"
      ],
      "metadata": {
        "id": "iTfOeI1NRTFI"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 4. Create a draw_bar_plot function\n",
        "def draw_bar_plot():\n",
        "    # Copy data and modify for monthly bar plot\n",
        "    df_bar = df.copy()\n",
        "    df_bar['year'] = df_bar.index.year\n",
        "    df_bar['month'] = df_bar.index.strftime('%B')\n",
        "\n",
        "    # Group data by year and month, calculating the mean page views\n",
        "    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()\n",
        "\n",
        "    # Reorder the month columns so they start at January and end at December\n",
        "    months_order = [\n",
        "        'January', 'February', 'March', 'April', 'May', 'June',\n",
        "        'July', 'August', 'September', 'October', 'November', 'December'\n",
        "    ]\n",
        "    df_pivot = df_pivot.reindex(columns=months_order)\n",
        "\n",
        "    # Draw bar plot\n",
        "    fig = df_pivot.plot(kind='bar', figsize=(15, 7), xlabel='Years', ylabel='Average Page Views').get_figure()\n",
        "    plt.legend(title='Months')\n",
        "\n",
        "    # Save image and return fig (don't change this part)\n",
        "    fig.savefig('bar_plot.png')\n",
        "    return fig"
      ],
      "metadata": {
        "id": "gZcF9KaARYMZ"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 5. Create a draw_box_plot function\n",
        "def draw_box_plot():\n",
        "    # Prepare data for box plots (this part is provided in the boilerplate)\n",
        "    df_box = df.copy()\n",
        "    df_box.reset_index(inplace=True)\n",
        "    df_box['year'] = [d.year for d in df_box.date]\n",
        "    df_box['month'] = [d.strftime('%b') for d in df_box.date]\n",
        "\n",
        "    # Set up the matplotlib figure layout (1 row, 2 columns)\n",
        "    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))\n",
        "\n",
        "    # Draw Year-wise Box Plot (Trend)\n",
        "    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])\n",
        "    axes[0].set_title('Year-wise Box Plot (Trend)')\n",
        "    axes[0].set_xlabel('Year')\n",
        "    axes[0].set_ylabel('Page Views')\n",
        "\n",
        "    # Ensure month labels on the bottom start at Jan\n",
        "    months_short_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']\n",
        "\n",
        "    # Draw Month-wise Box Plot (Seasonality)\n",
        "    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=months_short_order)\n",
        "    axes[1].set_title('Month-wise Box Plot (Seasonality)')\n",
        "    axes[1].set_xlabel('Month')\n",
        "    axes[1].set_ylabel('Page Views')\n",
        "\n",
        "    # Save image and return fig (don't change this part)\n",
        "    fig.savefig('box_plot.png')\n",
        "    return fig"
      ],
      "metadata": {
        "id": "xpaOqfKnRdDx"
      },
      "execution_count": 6,
      "outputs": []
    }
  ]
}