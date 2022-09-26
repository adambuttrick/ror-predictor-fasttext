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
Download model files from Hugging Face and place in model_files directory

# usage
See test.py for an example. Essentially, create an instance of the predictor class and feed it an affiliation string and prediction confidence level. In testing, 0.85 was found to be a good threshold for returning a decent amount of accurate prediction (75-80% predicted at 85-90% accuracy).

# training
Prediction service was trained on a subset of affiliation strings from OpenAlex that contained ROR IDs and whose assignments could be validated. See the [OpenAlex documentation](https://docs.openalex.org/download-snapshot) for downloading their works dataset. See validation directory for how affiliation strings were validated. 
