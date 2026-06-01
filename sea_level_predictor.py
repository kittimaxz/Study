{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOn2poKspkwkEJZupdOjQw+",
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
        "<a href=\"https://colab.research.google.com/github/kittimaxz/Study/blob/main/sea_level_predictor.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "fGR4TpjGSFQ2"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "from scipy.stats import linregress"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def draw_plot():\n",
        "    # 1. Use Pandas to import the data from epa-sea-level.csv using the direct URL link\n",
        "    df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv')\n",
        "\n",
        "    # 2. Use matplotlib to create a scatter plot\n",
        "    plt.figure(figsize=(10, 6))\n",
        "    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Actual Data', s=10)\n",
        "\n",
        "    # 3. Create first line of best fit (using all available historical data)\n",
        "    # Get slope and intercept\n",
        "    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])\n",
        "\n",
        "    # Generate years from 1880 through 2050 to plot the prediction line\n",
        "    years_extended = pd.Series([i for i in range(1880, 2051)])\n",
        "    line_all = res_all.slope * years_extended + res_all.intercept\n",
        "\n",
        "    # Plot the first line of best fit\n",
        "    plt.plot(years_extended, line_all, color='red', label='Fits all data (1880-2050)')\n",
        "\n",
        "    # 4. Create second line of best fit (using data from year 2000 through the most recent year)\n",
        "    df_recent = df[df['Year'] >= 2000]\n",
        "    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])\n",
        "\n",
        "    # Generate years from 2000 through 2050 to plot the second prediction line\n",
        "    years_recent_extended = pd.Series([i for i in range(2000, 2051)])\n",
        "    line_recent = res_recent.slope * years_recent_extended + res_recent.intercept\n",
        "\n",
        "    # Plot the second line of best fit\n",
        "    plt.plot(years_recent_extended, line_recent, color='green', label='Fits recent data (2000-2050)')\n",
        "\n",
        "    # 5. Add labels, title, and legend\n",
        "    plt.xlabel('Year')\n",
        "    plt.ylabel('Sea Level (inches)')\n",
        "    plt.title('Rise in Sea Level')\n",
        "    plt.legend()\n",
        "\n",
        "    # Adjust axis limits slightly to cleanly fit the new 2050 predictions\n",
        "    plt.xlim(1870, 2060)\n",
        "\n",
        "    # Save plot and return data for testing (boilerplate requirement)\n",
        "    plt.savefig('sea_level_plot.png')\n",
        "    return plt.gca()"
      ],
      "metadata": {
        "id": "WudKBglcSQYF"
      },
      "execution_count": 2,
      "outputs": []
    }
  ]
}