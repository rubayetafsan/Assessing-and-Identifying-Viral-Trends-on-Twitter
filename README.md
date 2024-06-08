# Assessing and Identifying Viral Trends on Twitter 

``classification``: reproduction code for classification

``metric_analysis``: intermediate results and codes for metric stats

``othercode``: other code

It's not required to have CSV version of dataset because compressed ``parquet.gzip`` version is already in the ``viraltw.rar`` folder but it can be found here: https://drive.google.com/file/d/1E8RcY9fyTaE98dEowRQa0S6avFp9g-gh/view?usp=drive_link

## Reproduction steps

1. ``generate_requirements.py`` installs required libraries. If you get error you can install them manually.

2. In metric analysis folder, ``twitter_viral_model.ipynb`` analyzes the data and produces the final dataset from october 2022. To run it on Colab ``viraltw.rar`` folder and should be uploaded to Colab from files section.

3. In classification folder, there are 2 folders, ``model_with_extra_features`` and ``model_with_only_language_models``. In ``model_with_only_language_models``, ``classification.py`` gives results for 4 different architecture BERTweet, BERT-tiny, BERT-base-cased, and RoBERTa-base. In ``model_with_extra_features``, ``classification.py`` gives improved results with extra features for 4 different architecture BERTweet, BERT-tiny, BERT-base-cased, and RoBERTa-base. 

Finally, results are saved in ``same_day_as_viral_with_features_train_test_balanced_accuracy_with_custom_model.txt`` and ``same_day_as_viral_with_features_train_test_balanced_accuracy.txt`` files.