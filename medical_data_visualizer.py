{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOgrBTEbz9rKJ7l9jKyNRDS",
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
        "<a href=\"https://colab.research.google.com/github/kittimaxz/Study/blob/main/medical_data_visualizer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Ivu26zj3N2a4"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv')"
      ],
      "metadata": {
        "id": "m3zGNTGXOrmh"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2. Add an overweight column to the data.\n",
        "# Calculate BMI: weight (kg) / (height (m) ^ 2). Height is provided in cm, so divide by 100.\n",
        "bmi = df['weight'] / ((df['height'] / 100) ** 2)\n",
        "df['overweight'] = (bmi > 25).astype(int)"
      ],
      "metadata": {
        "id": "pc-Yn1naO9Pd"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 3. Normalize data by making 0 always good and 1 always bad.\n",
        "# If the value of cholesterol or gluc is 1, set the value to 0. If more than 1, set to 1.\n",
        "df['cholesterol'] = (df['cholesterol'] > 1).astype(int)\n",
        "df['gluc'] = (df['gluc'] > 1).astype(int)"
      ],
      "metadata": {
        "id": "2KPQjNxOPEku"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 4. Draw the Categorical Plot in the draw_cat_plot function.\n",
        "def draw_cat_plot():\n",
        "    # 5. Create a DataFrame for the cat plot using pd.melt with values from cholesterol,\n",
        "    # gluc, smoke, alco, active, and overweight in the df_cat variable.\n",
        "    df_cat = pd.melt(\n",
        "        df,\n",
        "        id_vars=['cardio'],\n",
        "        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']\n",
        "    )\n",
        "\n",
        "    # 6. Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature.\n",
        "    # We group by cardio, variable, and value, then reset index and rename the size column to 'total'.\n",
        "    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')\n",
        "\n",
        "    # 7. Convert the data into long format and create a chart using sns.catplot()\n",
        "    fig = sns.catplot(\n",
        "        x='variable',\n",
        "        y='total',\n",
        "        hue='value',\n",
        "        col='cardio',\n",
        "        data=df_cat,\n",
        "        kind='bar'\n",
        "    ).fig\n",
        "\n",
        "    # 8. Get the figure for the output and store it in the fig variable.\n",
        "    # (Achieved above by adding .fig to the catplot generation)\n",
        "\n",
        "    # 9. Do not modify the next two lines.\n",
        "    fig.savefig('catplot.png')\n",
        "    return fig"
      ],
      "metadata": {
        "id": "8PYAqTv7PQyn"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 10. Draw the Heat Map in the draw_heat_map function.\n",
        "def draw_heat_map():\n",
        "    # 11. Clean the data in the df_heat variable by filtering out incorrect patient segments.\n",
        "    df_heat = df[\n",
        "        (df['ap_lo'] <= df['ap_hi']) &\n",
        "        (df['height'] >= df['height'].quantile(0.025)) &\n",
        "        (df['height'] <= df['height'].quantile(0.975)) &\n",
        "        (df['weight'] >= df['weight'].quantile(0.025)) &\n",
        "        (df['weight'] <= df['weight'].quantile(0.975))\n",
        "    ]\n",
        "\n",
        "    # 12. Calculate the correlation matrix and store it in the corr variable.\n",
        "    corr = df_heat.corr()\n",
        "\n",
        "    # 13. Generate a mask for the upper triangle and store it in the mask variable.\n",
        "    mask = np.triu(np.ones_like(corr, dtype=bool))\n",
        "\n",
        "    # 14. Set up the matplotlib figure.\n",
        "    fig, ax = plt.subplots(figsize=(12, 12))\n",
        "\n",
        "    # 15. Plot the correlation matrix using sns.heatmap()\n",
        "    sns.heatmap(\n",
        "        corr,\n",
        "        mask=mask,\n",
        "        annot=True,\n",
        "        fmt='.1f',\n",
        "        center=0,\n",
        "        vmin=-0.1,\n",
        "        vmax=0.25,\n",
        "        square=True,\n",
        "        linewidths=.5,\n",
        "        cbar_kws={'shrink': .5}\n",
        "    )\n",
        "\n",
        "    # 16. Do not modify the next two lines.\n",
        "    fig.savefig('heatmap.png')\n",
        "    return fig"
      ],
      "metadata": {
        "id": "1z0cIqrAPpJx"
      },
      "execution_count": 6,
      "outputs": []
    }
  ]
}