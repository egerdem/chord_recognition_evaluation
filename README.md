# chord_recognition_evaluation

**create_master_dict.py
**loads the estimation resulting lab files of the three different chord estimation model's from the corresponding folders:

1 Large vocabulary chord transcription [1]
2 Bidirectional transformer for musical chord recognition [2] 
3 Autochord [3]

and also 2 new estimations of our real-time experimenting, named:

- large_vocab_window_100_hop_size_20
- large_vocab_window_50_hop_size_20

It extracts the "id" of a song from each of the model's directory and stores as the key in a master dictionary (master_dict) in which the "value"s are the corresponding file names for each dir.

** evaluation.py
Loads the master_dict.pkl pickle file and use mir_eval.chord metric functions to evaluate the estimations. Plots figures and create a pandas table for mean score values

[1] Jiang, J., Chen, K., Li, W. & Xia, G. (2019). Large-vocabulary chord transcription via chord structure decomposition. Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019(pp. 644-651). (Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019). International Society for Music Information Retrieval.

[2] Humphrey, E. J., Bello, J. P., LeCun, Y., & Bengio, S. (2019). Structured training for large vocabulary chord recognition. Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019(pp. 620-627). (Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019). International Society for Music Information Retrieval.

[3] Bayron, C.J. (2021) Autochord: automatic chord recognition library and chord visualization app. Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021. (Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021). International Society for Music Information Retrieval.


