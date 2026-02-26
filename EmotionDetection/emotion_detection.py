import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=input_data)
    
    if response.status_code == 200:
        # Extract the emotion predictions
        emotions = response.json()['emotionPredictions'][0]['emotion']
        
        # Extract scores for each emotion
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Find the dominant emotion (the one with the highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Return the formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": "Unable to detect emotions", "status_code": response.status_code}

if __name__ == "__main__":
    sample_text = "I am feeling great!"
    result = emotion_detector(sample_text)
    print(result)