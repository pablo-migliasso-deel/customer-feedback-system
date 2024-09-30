from kafka import KafkaConsumer
import openai
import json

openai.api_key = "your-openai-api-key"

# Kafka consumer to listen for real-time customer feedback
consumer = KafkaConsumer(
    'customer_feedback',  # Kafka topic for feedback
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Function to process customer feedback and update reports
def process_feedback_and_update_report(feedback):
    # Extract feedback data
    feedback_text = feedback['text']
    sentiment = feedback['sentiment']
    
    # Generate real-time report with OpenAI
    prompt = f"""
    New customer feedback received:
    "{feedback_text}"
    
    Sentiment: {sentiment}
    
    Based on this new feedback and the existing product performance data, update the report with recommendations on improving customer satisfaction.
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7
    )
    
    updated_report = response.choices[0].text.strip()
    print(f"Updated Report: \n{updated_report}")
    
    return updated_report

# Listen for real-time customer feedback and trigger report updates
for message in consumer:
    feedback = message.value
    process_feedback_and_update_report(feedback)
