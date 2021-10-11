import argparse

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import spearmanr, pearsonr


def get_predicted_scores(scores_file):
    scores = []
    with open(scores_file, 'r') as file:
        scores = [float(line.strip()) for line in file]

    return scores


def logistic_func(x, b1, b2, b3, b4, b5):
    return b1 + (0.5 - 1 / (1 + np.exp(b2 * (x - b3)))) + b4 * x + b5


def compute_metrics(y_pred, y):
    # logistic regression btw y_pred & y
    popt, _ = curve_fit(
        logistic_func,
        np.ravel(y_pred),
        np.ravel(y),
        p0=0.5 * np.ones((5,)),
        maxfev=20000
    )
    y_pred_logistic = [logistic_func(x, *popt) for x in y_pred]

    return spearmanr(y, y_pred)[0], pearsonr(y, y_pred_logistic)[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt-csv', type=str, required=True, help="Path to csv with ground truth dmos values")
    parser.add_argument('--predicted-scores-path', type=str, required=True,
                        help="Path to csv with predicted scores")

    args = parser.parse_args()
    df = pd.read_csv(args.gt_csv)
    predicted_scores = get_predicted_scores(args.predicted_scores_path)

    srcc, plcc = compute_metrics(predicted_scores, df["dmos-gt"].values)
    print(f"SRCC: {srcc:.5f} PLCC: {plcc:.5f}")
