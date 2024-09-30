# Example data for actions taken by different departments
actions_taken = {
    "Product Development": {
        "Action": "Fixed durability issue in Product C",
        "Date": "2024-03-01"
    },
    "Marketing": {
        "Action": "Launched campaign highlighting Product A's durability",
        "Date": "2024-03-10"
    },
    "Sales": {
        "Action": "Adjusted pricing strategy for Product B",
        "Date": "2024-03-05"
    },
    "Customer Service": {
        "Action": "Improved response times for support tickets",
        "Date": "2024-03-08"
    }
}

# Example outcomes after actions were taken
feedback_outcomes = {
    "Product Development": {
        "Outcome": "Customer complaints for Product C reduced by 60%",
        "Sales Impact": "Product C sales increased by 10%"
    },
    "Marketing": {
        "Outcome": "Increased brand perception for Product A by 20%",
        "Sales Impact": "Product A sales increased by 15%"
    },
    "Sales": {
        "Outcome": "Pricing adjustment led to 10% increase in Product B sales",
        "Customer Satisfaction": "Customers were satisfied with the new pricing"
    },
    "Customer Service": {
        "Outcome": "Customer satisfaction with service increased by 20%",
        "Support Impact": "Average response time reduced by 30%"
    }
}

# Function to generate cross-team feedback loop report
def generate_feedback_loop_report(actions_taken, feedback_outcomes):
    report = "Cross-Team Feedback Loop Report\n"
    report += "="*35 + "\n\n"
    
    for department, action_details in actions_taken.items():
        report += f"Department: {department}\n"
        report += f"Action Taken: {action_details['Action']} (Implemented on {action_details['Date']})\n"
        
        outcome_details = feedback_outcomes.get(department, {})
        report += f"Outcome: {outcome_details.get('Outcome', 'No outcome reported')}\n"
        report += f"Sales Impact: {outcome_details.get('Sales Impact', 'No sales impact reported')}\n"
        report += f"Customer Satisfaction Impact: {outcome_details.get('Customer Satisfaction', 'No customer satisfaction impact reported')}\n"
        report += "-"*35 + "\n\n"
    
    return report

# Generate and print feedback loop report
feedback_loop_report = generate_feedback_loop_report(actions_taken, feedback_outcomes)
print(feedback_loop_report)
