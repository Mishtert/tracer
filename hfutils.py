import requests

# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
# headers = {"Authorization": f"Bearer {hft}"}

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# output = query({
#     "inputs": {
# 		"question": "What's my name?",
# 		"context": "My name is Clara and I live in Berkeley.",
# 	},
# })


def get_ans(question,context):
    output = query({
    "inputs": {
		"question": question,
		"context": context,
	        },
        })
    return output    



def get_label_score_dict(row, threshold):
    result_dict = dict()
    for _label, _score in zip(row['labels'], row['scores']):
        if _score > threshold:
            result_dict.update({_label: 1})
        else:
            result_dict.update({_label: 0})
    return result_dict
