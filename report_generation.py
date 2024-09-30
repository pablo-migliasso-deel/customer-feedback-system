import openai

openai.api_key = "your-openai-api-key"

def generate_department_specific_report(sales_summary, feedback_summary, department):
    if department == "Product Development":
        prompt = f"""
        You are a product manager. Using the following sales and customer feedback data, generate a report focusing on product improvements, quality issues, and feature requests.

        1. **Product Performance**: Summarize the performance of each product based on sales data and customer feedback.
        2. **Quality Issues**: Identify any defects or issues reported by customers and their impact on sales.
        3. **Feature Requests**: Highlight key feature requests from customers and their potential value.
        4. **Recommendations**: Suggest actions to improve product quality and customer satisfaction.

        Sales Data:
        {sales_summary}

        Customer Feedback:
        {feedback_summary}
        """
    elif department == "Marketing":
        prompt = f"""
        You are a marketing strategist. Using the following sales and customer feedback data, generate a report focusing on customer perception, brand reputation, and campaign effectiveness.

        1. **Customer Sentiment**: Summarize how customers perceive our products based on feedback.
        2. **Positive Feedback Highlights**: Identify the most positively reviewed features or products.
        3. **Negative Feedback Trends**: Highlight areas where customer dissatisfaction is growing.
        4. **Recommendations**: Suggest marketing campaigns or strategies to leverage positive feedback and address negative sentiment.

        Sales Data:
        {sales_summary}

        Customer Feedback:
        {feedback_summary}
        """
    elif department == "Sales":
        prompt = f"""
        You are a sales manager. Using the following sales and customer feedback data, generate a report focusing on pricing concerns, product demand, and customer satisfaction.

        1. **Sales Performance**: Summarize sales performance of each product based on sales data and customer feedback.
        2. **Pricing Feedback**: Highlight any customer concerns about product pricing and feature-to-price ratio.
        3. **Customer Satisfaction**: Analyze how satisfied customers are with the products, based on feedback.
        4. **Recommendations**: Suggest pricing strategies or promotional offers to improve sales and customer satisfaction.

        Sales Data:
        {sales_summary}

        Customer Feedback:
        {feedback_summary}
        """
    elif department == "Customer Service":
        prompt = f"""
        You are a customer service manager. Using the following sales and customer feedback data, generate a report focusing on customer service performance, support issues, and satisfaction.

        1. **Service Quality**: Summarize how customers feel about our customer service based on feedback.
        2. **Support Issues**: Identify common issues raised in customer support tickets and feedback.
        3. **Satisfaction Trends**: Analyze how customer satisfaction with our support team is changing over time.
        4. **Recommendations**: Suggest ways to improve response times and overall customer service experience.

        Sales Data:
        {sales_summary}

        Customer Feedback:
        {feedback_summary}
        """
    
    # Generate the tailored report using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7
    )
    
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    sales_summary = "Product A: $100,000, Product B: $85,000, Product C: $70,000"
    feedback_summary = "Positive feedback for Product A, mixed feedback for Product B, complaints for Product C."
    
    # Generate reports for Product Development, Marketing, Sales, and Customer Service
    product_report = generate_department_specific_report(sales_summary, feedback_summary, "Product Development")
    marketing_report = generate_department_specific_report(sales_summary, feedback_summary, "Marketing")
    sales_report = generate_department_specific_report(sales_summary, feedback_summary, "Sales")
    customer_service_report = generate_department_specific_report(sales_summary, feedback_summary, "Customer Service")
    
    # Print the generated reports
    print(f"Product Development Report:\n{product_report}\n")
    print(f"Marketing Report:\n{marketing_report}\n")
    print(f"Sales Report:\n{sales_report}\n")
    print(f"Customer Service Report:\n{customer_service_report}\n")
