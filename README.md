# Reproducibility Project
For the paper: An interpretable deep-learning model for early prediction of Sepsis in the emergency department
Based on the code base of original implementation: https://github.com/yinchangchang/DII-Challenge

# DII-Challenge-2019
The early identification of sepsis cases.

# Install the dependencies

		pip install -r requirement.txt

# Data
We use the sample dataset for the experiments. The dataset is located in the ./file folder.

# Data preprocessing

-	Creat result folder for data preprocessing results

		mkdir result
		mkdir data
		mkdir data/models

-	Generate json files

		cd preprocessing
		python gen_master_feature.py --master-file ../file/master.csv
		python gen_feature_time.py --vital-file ../file/vital.csv				# only for task1
		python gen_vital_feature.py --vital-file ../file/vital.csv
		python gen_label_feature.py --label-file ../file/label.csv

# Train and validate the model
-	The best model will saved in ../data/models/

		python main.py --task case1		# for task1 case1
		python main.py --task task1		# for task1 case2
		python main.py --task task2		# for task2

-	You can also run the code by:

		python run.py --label-file ../file/label.csv --vital-file ../file/vital.csv --master-file  ../master.csv --task case1

# Experiment results
-	Comparison with the baselines

| Task | Prop-Repo | Prop-Repr | GRU-Repo | GRU-Repr | LSTM-Repo | LSTM-Repr |
| :------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: |
| Case 1 | 0.726 | 0.945 | 0.692 | 0.88 | 0.723 | 0.89 |
| Case 2 | 0.842 | 0.845 | 0.821 | 0.80 | 0.780 | 0.80 |

-	Comparison with the improved model

| Task | AUC-Repr | AUC-Repo | AUC-Impr | F1-Repr | F1-Repo | F1-Impr | Acc-Repr | Acc-Repo | Acc-Impr | Prec-Repr | Prec-Repo | Prec-Impr |
| :------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: | :---------: |
| Case 1 | 0.726 | 0.945 | 0.784 | 0.545 | - | 0.667 | 0.788 | - | 0.778 | 0.667 | - | 1.000 |
| Case 2 | 0.842 | 0.845 | 0.847 | 0.633 | - | 0.743 | 0.802 | - | 0.785 | 1.000 | - | 1.000 |

