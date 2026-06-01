{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbPTDYwZG2R7PujA/ZUTIH",
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
        "<a href=\"https://colab.research.google.com/github/kittimaxz/Study/blob/main/mean_var_std.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "8QfPTho-BPVV"
      },
      "outputs": [],
      "source": [
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate(list_in) :\n",
        "  if len(list_in) != 9 :\n",
        "    raise ValueError(\"List must contain nine numbers.\")\n",
        "\n",
        "  matrix = np.array(list_in).reshape(3, 3)\n",
        "\n",
        "  calculations = {\n",
        "      'mean' : [\n",
        "          matrix.mean(axis=0).tolist(),\n",
        "          matrix.mean(axis=1).tolist(),\n",
        "          matrix.mean().item()\n",
        "      ],\n",
        "      'variance' : [\n",
        "          matrix.var(axis=0).tolist(),\n",
        "          matrix.var(axis=1).tolist(),\n",
        "          matrix.var().item()\n",
        "      ],\n",
        "      'standard deviation' : [\n",
        "          matrix.std(axis=0).tolist(),\n",
        "          matrix.std(axis=1).tolist(),\n",
        "          matrix.std().item()\n",
        "      ],\n",
        "      'max' : [\n",
        "          matrix.max(axis=0).tolist(),\n",
        "          matrix.max(axis=1).tolist(),\n",
        "          matrix.max().item()\n",
        "      ],\n",
        "      'min' : [\n",
        "          matrix.min(axis=0).tolist(),\n",
        "          matrix.min(axis=1).tolist(),\n",
        "          matrix.min().item()\n",
        "      ],\n",
        "      'sum' : [\n",
        "          matrix.sum(axis=0).tolist(),\n",
        "          matrix.sum(axis=1).tolist(),\n",
        "          matrix.sum().item()\n",
        "      ]\n",
        "  }\n",
        "\n",
        "  return calculations"
      ],
      "metadata": {
        "id": "dhPVfomeDyZW"
      },
      "execution_count": 5,
      "outputs": []
    }
  ]
}