import mir_eval
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt

### Directories for estimations and ground truth

# Large-Vocabulary Chord Transcription via Chord Structure Decomposition (ISMIR 2019)
# file naming: rwc-pop_10.lab
model1_dir = "./ISMIR_largevocab_results"

# A Bi-directional Transformer for Musical Chord Recognition (ISMIR 2019)
# file naming: rwc-pop_8.flac.lab
model2_dir = "./transformer_results"

# AUTOCHORD: AUTOMATIC CHORD RECOGNITION LIBRARY AND CHORD VISUALIZATION APP (ISMIR 2021)
# file naming: rwc-pop_8.flac.lab
model3_dir = "./autochord_results"

true_dir = "./rwc-pop-annot"  # RWC Pop Dataset

with open('master_dict.pkl', 'rb') as f:
    master_dict = pickle.load(f)


def evaluate_model(model_dir, est_id_index):
    scores = {}

    for key, value in master_dict.items():
        score = {}

        ref_id = value[0]
        ref_lab = os.path.join(true_dir, ref_id)

        est_id = value[est_id_index]
        est_lab = os.path.join(model_dir, est_id)

        (ref_intervals, ref_labels) = mir_eval.io.load_labeled_intervals(ref_lab)
        (est_intervals, est_labels) = mir_eval.io.load_labeled_intervals(est_lab)

        est_intervals, est_labels = mir_eval.util.adjust_intervals(
            est_intervals, est_labels, ref_intervals.min(),
            ref_intervals.max(), mir_eval.chord.NO_CHORD,
            mir_eval.chord.NO_CHORD)

        (intervals, ref_labels, est_labels) = mir_eval.util.merge_labeled_intervals(ref_intervals, ref_labels,
                                                                                    est_intervals, est_labels)

        durations = mir_eval.util.intervals_to_durations(intervals)

        comparisons_mirex = mir_eval.chord.mirex(ref_labels, est_labels)
        comparisons_sevenths = mir_eval.chord.sevenths(ref_labels, est_labels)

        mirex = mir_eval.chord.weighted_accuracy(comparisons_mirex, durations)
        seventh = mir_eval.chord.weighted_accuracy(comparisons_sevenths, durations)
        overseg = mir_eval.chord.overseg(ref_intervals, est_intervals)
        underseg = mir_eval.chord.underseg(ref_intervals, est_intervals)

        score["mirex"] = mirex
        score["seventh"] = seventh
        score["overseg"] = overseg
        score["underseg"] = underseg

        scores[key] = score

    return scores


# Evaluate each model
model1_scores = evaluate_model(model1_dir, 1)  # Use index 1 for Model 1
model2_scores = evaluate_model(model2_dir, 2)  # Use index 2 for Model 2
model3_scores = evaluate_model(model3_dir, 3)  # Use index 3 for Model 3


# for key, value in scores.items():
#     mirex_scores.append(value["mirex"])
#     seventh_scores.append(value["seventh"])
#     overseg_scores.append(value["overseg"])
#     underseg_scores.append(value["underseg"])

import matplotlib.pyplot as plt


# Function to extract metric scores for each model
def extract_scores(model_scores):
    mirex_scores = []
    seventh_scores = []
    underseg_scores = []
    overseg_scores = []
    for key, value in model_scores.items():
        mirex_scores.append(value["mirex"])
        seventh_scores.append(value["seventh"])
        underseg_scores.append(value["underseg"])
        overseg_scores.append(value["overseg"])
    return mirex_scores, seventh_scores, underseg_scores, overseg_scores

# Data for three models
model_names = ['Large Vocab', 'Transformer', 'Autochord']

# Extract scores for each model
model1_mirex, model1_seventh, model1_underseg, model1_overseg = extract_scores(model1_scores)
model2_mirex, model2_seventh, model2_underseg, model2_overseg = extract_scores(model2_scores)
model3_mirex, model3_seventh, model3_underseg, model3_overseg = extract_scores(model3_scores)


# Figure 1: Compare MIREX scores for 3 models
plt.figure()
plt.plot(range(1, 101), model1_mirex, label=model_names[0])
plt.plot(range(1, 101), model2_mirex, label=model_names[1])
plt.plot(range(1, 101), model3_mirex, label=model_names[2])
plt.xlabel('Song')
plt.ylabel('MIREX Score')
plt.title('Comparison of MIREX Scores for 3 Models')
plt.legend()
plt.show()

# Figure 2: Compare Seventh scores for 3 models
plt.figure()
plt.plot(range(1, 101), model1_seventh, label=model_names[0])
plt.plot(range(1, 101), model2_seventh, label=model_names[1])
plt.plot(range(1, 101), model3_seventh, label=model_names[2])
plt.xlabel('Song')
plt.ylabel('Seventh Score')
plt.title('Comparison of Seventh Scores for 3 Models')
plt.legend()
plt.show()

# Figure 3: Compare Underseg and Overseg scores for 3 models
plt.figure()
plt.plot(range(1, 101), model1_overseg, label=model_names[0], color='b', linestyle='--')
plt.plot(range(1, 101), model2_overseg, label=model_names[1], color='g', linestyle='--')
plt.plot(range(1, 101), model3_overseg, label=model_names[2], color='r', linestyle='--')
plt.xlabel('Song')
plt.ylabel('Segmentation Error')
plt.title('Comparison of Underseg and Overseg Scores for 3 Models')
plt.legend()
plt.show()









# Create figure and axis objects
fig, ax = plt.subplots()

# Plot each score as a scatter plot
ax.scatter(x_labels, mirex_scores, label='Mirex', color='r')
ax.scatter(x_labels, seventh_scores, label='Seventh', color='g')
# ax.scatter(x_labels, overseg_scores, label='Overseg', color='b')
# ax.scatter(x_labels, underseg_scores, label='Underseg', color='y')

# Connect points with lines
ax.plot(x_labels, mirex_scores, linestyle='-', color='r', alpha=0.5)
ax.plot(x_labels, seventh_scores, linestyle='-', color='g', alpha=0.5)
# ax.plot(x_labels, overseg_scores, linestyle='-', color='b', alpha=0.5)
# ax.plot(x_labels, underseg_scores, linestyle='-', color='y', alpha=0.5)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Add legend
plt.legend()

# Set labels and title
plt.xlabel('Songs')
plt.ylabel('Scores')
plt.title('Scores of Different Songs')

# Show plot
plt.show()