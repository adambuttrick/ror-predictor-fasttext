# ror-predictor-fasttext
ROR prediction service, trained with fastText

## setup
Install fastText:
````
git clone https://github.com/facebookresearch/fastText.git
cd fastText
sudo pip install .
````

Install requirements.txt
````
pip install -r requirements.txt
````
[Download the model files from Hugging Face](https://huggingface.co/poodledude/ror-predictor/tree/main) and place in a directory. Pass this directory to the Predictor class when creating, e.g.:
````
PREDICTOR = Predictor('/Users/yourname/model_files_dir/')
````

## usage
See [test.py](https://github.com/adambuttrick/ror-predictor/blob/main/test.py) for an example and [test_data](https://github.com/adambuttrick/ror-predictor/tree/main/test_data) for sample datasets. Create an instance of the predictor class and feed it an affiliation string and prediction confidence level. In testing, 0.85 was found to be a good good threshold for returning a sufficient amount of accurate predictions (75-80% predicted at 85-90% accuracy).

## training
Prediction service was trained on a subset of affiliation strings from OpenAlex that contained ROR IDs whose assignments could be validated. See the [OpenAlex documentation](https://docs.openalex.org/download-snapshot) for downloading their works dataset.

## limitations
Training data that could be validated was only available for 64,656 ROR IDs (~63% of total ROR IDs) in the OpenAlex works dataset. See [model_ids.txt](https://github.com/adambuttrick/ror-predictor/blob/main/model_ids.txt) for a complete list of IDs that are able to be predicted. Predictions cannot be made for ROR IDs on which the service was not trained. Use the [affiliation service](https://ror.readme.io/docs/rest-api#affiliation-parameter) in the [ROR API](https://ror.readme.io/docs/rest-api) for more general matching (but please run it locally using the [Docker image](https://github.com/ror-community/ror-api) if you're trying to match a large volume of affiliation data).
