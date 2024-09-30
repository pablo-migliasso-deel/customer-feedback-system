import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Example data for feedback trends
feedback_trends = {
    'Product C Complaints': [50, 40, 30, 20],
    'Product B Sales': [20000, 22000, 24000, 26000],
    'Customer Service Satisfaction': [3.5, 3.8, 4.0, 4.3]
}
time_periods = ['Q1', 'Q2', 'Q3', 'Q4']

# Initialize Dash app
app = dash.Dash(__name__)

# Layout for feedback loop dashboard
app.layout = html.Div([
    html.H1("Customer Feedback Loop Dashboard"),
    
    dcc.Graph(id='complaints-trend'),
    dcc.Graph(id='sales-trend'),
    dcc.Graph(id='satisfaction-trend')
])

@app.callback(
    Output('complaints-trend', 'figure'),
    Input('complaints-trend', 'id')
)
def update_complaints_trend(_):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_periods, y=feedback_trends['Product C Complaints'],
                             mode='lines+markers', name='Product C Complaints'))
    fig.update_layout(title="Trend of Product C Complaints", xaxis_title="Quarter", yaxis_title="Number of Complaints")
    return fig

@app.callback(
    Output('sales-trend', 'figure'),
    Input('sales-trend', 'id')
)
def update_sales_trend(_):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_periods, y=feedback_trends['Product B Sales'],
                             mode='lines+markers', name='Product B Sales ($)'))
    fig.update_layout(title="Trend of Product B Sales", xaxis_title="Quarter", yaxis_title="Sales ($)")
    return fig

@app.callback(
    Output('satisfaction-trend', 'figure'),
    Input('satisfaction-trend', 'id')
)
def update_satisfaction_trend(_):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_periods, y=feedback_trends['Customer Service Satisfaction'],
                             mode='lines+markers', name='Customer Satisfaction'))
    fig.update_layout(title="Customer Service Satisfaction Trend", xaxis_title="Quarter", yaxis_title="Satisfaction Score")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
