
### Directories for results and ground truth

# Junyan Jiang1,2,3 Ke Chen1,2 Wei Li1 Gus Xia (2019). Large-Vocabulary Chord Transcription
# via Chord Structure Decomposition. 20th International Society for (ISMIR 2019)
model1_dir = "./ISMIR_largevocab_results"


true_dir = "./rwc-pop-annot"  # RWC Pop Dataset

import os
import re
import mir_eval

# Iterate over files in the directory

dict = {}
for filename in os.listdir(model1_dir):
    # Check if the file ends with ".lab"
    if filename.endswith(".lab"):
        # Extract the number between underscore and ".lab" using regular expression
        match = re.search(r'_([0-9]+)\.lab$', filename)
        model1_id = int(match.group(1))  # Convert the matched string to integer
        print(f"File: {filename}, ID: {model1_id}")
        dict[model1_id] = filename

sorted_keys = sorted(dict.keys())
model1_dict = {key: dict[key] for key in sorted_keys}

# Create a new dictionary with sorted keys

dict2 = {}
for filename in os.listdir(true_dir):
    if len(filename)==16:
        true_id = int(filename[1:4])
        dict2[true_id-1] = filename

sorted_keys2 = sorted(dict2.keys())
true_dict = {key: dict2[key] for key in sorted_keys2}

master_dict = {}
for key, value in true_dict.items():
    master_dict[key] = [model1_dict[key], true_dict[key]]

scores = {}

for key, value in master_dict.items():
    score = {}

    ref = true_dict[key]
    ref_lab = os.path.join(true_dir, ref)

    est = model1_dict[key]
    est_lab = os.path.join(model1_dir, est)

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

#
# scores = {}
# for key, value in master_dict.items():
#

mirex_scores = []
seventh_scores = []
overseg_scores = []
underseg_scores = []

for key, value in scores.items():
    mirex_scores.append(value["mirex"])
    seventh_scores.append(value["seventh"])
    overseg_scores.append(value["overseg"])
    underseg_scores.append(value["underseg"])

import matplotlib.pyplot as plt
import numpy as np
# Create x-axis labels (songs)
x_labels = list(scores.keys())

# Create figure and axis objects
fig, ax = plt.subplots()

# Plot each score as a scatter plot
ax.scatter(x_labels, mirex_scores, label='Mirex', color='r')
ax.scatter(x_labels, seventh_scores, label='Seventh', color='g')
ax.scatter(x_labels, overseg_scores, label='Overseg', color='b')
ax.scatter(x_labels, underseg_scores, label='Underseg', color='y')

# Connect points with lines
ax.plot(x_labels, mirex_scores, linestyle='-', color='r', alpha=0.5)
ax.plot(x_labels, seventh_scores, linestyle='-', color='g', alpha=0.5)
ax.plot(x_labels, overseg_scores, linestyle='-', color='b', alpha=0.5)
ax.plot(x_labels, underseg_scores, linestyle='-', color='y', alpha=0.5)

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