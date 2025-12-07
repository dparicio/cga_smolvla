import pandas as pd

eval_smolvla2 = pd.read_parquet("hf://datasets/danipaez/eval_smolvla2/data/chunk-000/file-000.parquet")
                   # 0    1     2      3      4     5     6     7     8     9     10    11    12    13    14    15    16     17     18    19    20    21     22     23     24
success_eval_smolvla2 = [True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, False, True, False, False, True ]
ablation_last = 5  
eval_smolvla2["success"] = success_eval_smolvla2

print(f"Number of episodes: {len(eval_smolvla2.episode_index.unique())}")




print("debug")

