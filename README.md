# chord_recognition_evaluation

create_master_dict.py loads the file names corresponding to the estimation files (.lab files) of the three different chord estimation models. Estimation results of each model has slightly different naming (e.g rwc-pop_10.lab, rwc-pop_10.flac.lab, N011-M01-T08.lab etc.)  so this dictionary matches those file names by the id number of the song. The models are:

- 1. Large vocabulary chord transcription [1]
- 2. Bidirectional transformer for musical chord recognition [2] 
- 3. Autochord [3]

and also 2 new estimations from our real-time experiments:

- large_vocab_window_100_hop_size_20
- large_vocab_window_50_hop_size_20

In short, it extracts the "id" of a song from each of the model's directory and stores as the key in a master dictionary (master_dict) in which the "value"s are the corresponding file names for each dir.

** evaluation.py
Loads the master_dict.pkl pickle file and iterates over the keys (song id's) by using mir_eval.chord metric functions to evaluate the estimation scores. Lastly, plots the figures showing score per each song and create a pandas table for mean score values for each method.

[1] Jiang, J., Chen, K., Li, W. & Xia, G. (2019). Large-vocabulary chord transcription via chord structure decomposition. Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019(pp. 644-651). (Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019). International Society for Music Information Retrieval.

[2] Humphrey, E. J., Bello, J. P., LeCun, Y., & Bengio, S. (2019). Structured training for large vocabulary chord recognition. Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019(pp. 620-627). (Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019). International Society for Music Information Retrieval.

[3] Bayron, C.J. (2021) Autochord: automatic chord recognition library and chord visualization app. Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021. (Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021). International Society for Music Information Retrieval.


