
import os
import re
import pickle

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

# Iterate over files in each model's result directory

#model1 : ISMIR_largevocab
model1_dict = {}
for filename in os.listdir(model1_dir):
    # Check if the file ends with ".lab"
    if filename.endswith(".lab"):
        # Extract the number between underscore and ".lab" using regular expression
        # file naming: rwc-pop_10.lab
        match = re.search(r'_([0-9]+)\.lab$', filename)
        model1_id = int(match.group(1))  # Convert the matched string to integer
        print(f"File: {filename}, ID: {model1_id}")
        model1_dict[model1_id] = filename

# Create a new dictionary with sorted keys
sorted_keys = sorted(model1_dict.keys())
model1_dict_names = {key: model1_dict[key] for key in sorted_keys}

#model2 : Transformer
model2_dict = {}
for filename in os.listdir(model2_dir):
    # file naming: rwc-pop_8.flac.lab
    # Check if the file ends with ".lab"
    if filename.endswith(".lab"):
        # Extract the number between underscore and ".flac" using regular expression
        match = re.search(r'_([0-9]+)\.flac', filename)
        model2_id = int(match.group(1))  # Convert the matched string to integer
        print(f"File: {filename}, ID: {model2_id}")
        model2_dict[model2_id] = filename

# Create a new dictionary with sorted keys
sorted_keys = sorted(model2_dict.keys())
model2_dict_names = {key: model2_dict[key] for key in sorted_keys}

#model3 : Autochord
model3_dict = {}
for filename in os.listdir(model3_dir):
    # file naming: rwc-pop_8.flac.lab
    # Check if the file ends with ".lab"
    if filename.endswith(".lab"):
        # Extract the number between underscore and ".lab" using regular expression
        # file naming: rwc-pop_10.flac.lab
        match = re.search(r'_([0-9]+)\.flac', filename)
        model3_id = int(match.group(1))  # Convert the matched string to integer
        print(f"File: {filename}, ID: {model3_id}")
        model3_dict[model3_id] = filename

# Create a new dictionary with sorted keys
sorted_keys = sorted(model3_dict.keys())
model3_dict_names = {key: model3_dict[key] for key in sorted_keys}

#ground truth : RCW annotations
dict_true = {}
for filename in os.listdir(true_dir):
    if len(filename)==16:
        true_id = int(filename[1:4])
        dict_true[true_id-1] = filename

sorted_keys2 = sorted(dict_true.keys())
true_dict = {key: dict_true[key] for key in sorted_keys2}


master_dict = {}
for key, value in true_dict.items():
    master_dict[key] = [true_dict[key], model1_dict_names[key], model2_dict_names[key], model3_dict_names[key]]

with open('master_dict.pkl', 'wb') as f:
    pickle.dump(master_dict, f)
