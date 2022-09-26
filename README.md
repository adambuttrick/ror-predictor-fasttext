# ror-predictor
ROR prediction service, trained using fastText

# setup
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

# usage
See [test.py](https://github.com/adambuttrick/ror-predictor/blob/main/test.py) for an example. Essentially, create an instance of the predictor class and feed it an affiliation string and prediction confidence level. In testing, 0.85 was found to be a good good threshold for returning a sufficient amount of accurate predictions (75-80% predicted at 85-90% accuracy).

# training
Prediction service was trained on a subset of affiliation strings from OpenAlex that contained ROR IDs and whose assignments could be validated. See the [OpenAlex documentation](https://docs.openalex.org/download-snapshot) for downloading their works dataset.

# limitations
Training data that could be validated was only available for 64,656 ROR IDs in the OpenAlex works dataset. See [model_ids.txt](https://github.com/adambuttrick/ror-predictor/blob/main/model_ids.txt) for a complete list of IDs that are able to be predicted. Predictions cannot be made for ROR IDs on which the service was not trained.
