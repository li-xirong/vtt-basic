# vtt-basic: Video-to-Text Matching basic package
---

The task of [video-to-text matching](https://arxiv.org/abs/1709.01362) is to find amidst a set of sentences the one best describing the content of a given video clip. From a pattern recognition viewpoint, the task is essentially a two-class classification problem. Concerning the question of whether a specific sentence is relevant with respect to a given video, the answer is either yes or no.
This package provides a python-based conceptual framework for beginners.

## Data

Dataset  | Purpose  | # of videos | # of sentences
------------ | -------- | ----------- | --------------
msrvtt10k    | training   | 10,000 | 200,000
tv2016train  | validation | 200 | 200 (setA), 200 (setB)
tv2016test   | testing    | 1,915 | 1,915 (setA), 1,915 (setB)

The datasets are typically used as follows. A model is trained on msrvtt10k, with hyper parameters (if applicable) optimized on tv2016train. The performance of the model is tested on tv2016test.

The following script setups the data at a local (non-windows) machine.
```bash
mkdir $HOME/VisualSearch
cd $HOME/VisualSearch
wget http://lixirong.net/data/tv16/vtt-data.zip
unzip -r vtt-data.zip
```

## Code

See the [doit.sh](doit.sh) script, where
+ [make_submission.py](make_submission.py) uses a trained model (currently `RandomGuess`) to predict the relevance of each test sentence with respect to each test video, and subsequently saves the prediction to a local file. 
+ [eval.py](eval.py) evaluates how good the model performs, in terms of Mean Inverted Rank (MIR), higher is better. 

## Get started

Build your own model that is better than `RandomGuess` in [models.py](models.py). RandomGuess gives an MIR score of 0.004 approximately. If your model receives an MIR score lower than that, for sure something goes wrong.
