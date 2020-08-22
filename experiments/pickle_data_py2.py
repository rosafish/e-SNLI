# A step for computing inter-annotator bleu scores of the gold explanations (with Oana's preprocessing of the data)
# This file retrieves Oana's processed dev set, and pickle the dict (later I will load in the jupyter notebook)

# Get dev set data
import sys
sys.path.append('./attention/')
from data_attention_bottom import get_dev_test_original_expl

#snli_dev_no_unk 
esnli_path = './'
dev = get_dev_test_original_expl(esnli_path, 'dev')
print(dev['expl_1'][0])

# pickle the dev dict (python 2 pickle)
import pickle

# Store data (serialize)
with open('dev_py2_protocol2.dict', 'wb') as handle:
    pickle.dump(dev, handle, protocol=2)
    