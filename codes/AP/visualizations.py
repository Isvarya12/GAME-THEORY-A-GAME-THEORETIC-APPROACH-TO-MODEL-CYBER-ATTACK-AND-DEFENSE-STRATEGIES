import matplotlib.pyplot as plt
import numpy as np


def visualize_payoff_matrix(payoff_matrix):
    fig, ax = plt.subplots()
    im = ax.imshow(payoff_matrix, cmap='RdBu')
    
    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Payoff", rotation=-90, va="bottom")

    # Set tick labels
    ax.set_xticks(np.arange(payoff_matrix.shape[0]))
    ax.set_yticks(np.arange(payoff_matrix.shape[1]))
    ax.set_xticklabels(['Cooperate', 'Defect'])
    ax.set_yticklabels(['Cooperate', 'Defect'])

    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations
    for i in range(payoff_matrix.shape[0]):
        for j in range(payoff_matrix.shape[1]):
            text = ax.text(j, i, payoff_matrix[i, j], ha="center", va="center", color="w")

    ax.set_title("Payoff Matrix")
    fig.tight_layout()
    plt.ioff()
    plt.show()
    plt.pause()