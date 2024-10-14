import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine  # Import SQLAlchemy

from text_to_sql import get_sql_query_from_nl

# Set up SQLAlchemy engine (use your own connection string)
engine = create_engine("postgresql://customer-feedback:admin@localhost:5432/customer-feedback")

# Set up Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Customer Feedback Dashboard with LLM Querying"),
    
    # Input field for natural language queries
    dcc.Input(id='input-nl-query', type='text', placeholder="Ask a question about the feedback data...", style={'width': '80%'}),
    
    # Submit button
    html.Button('Submit', id='submit-button', n_clicks=0),
    
    # Output for SQL query
    html.Div(id='sql-query-output', style={'margin-top': '20px'}),
    
    # Table for displaying query results
    html.Div(id='table-output'),
    
    # Chart placeholder
    dcc.Graph(id='chart-output')
])

# Function to execute SQL and return results
def execute_sql_query(sql_query):
    try:
        df = pd.read_sql(sql_query, engine)
        return df
    except Exception as e:
        return str(e)

# Callback to handle query submission
@app.callback(
    [Output('sql-query-output', 'children'), Output('table-output', 'children'), Output('chart-output', 'figure')],
    [Input('submit-button', 'n_clicks')],
    [Input('input-nl-query', 'value')]
)
def update_dashboard(n_clicks, question):
    if n_clicks > 0 and question:
        # Convert NL query to SQL
        sql_query = get_sql_query_from_nl(question)
        
        # Display SQL query
        query_output = f"Generated SQL Query: {sql_query}"
        
        # Execute SQL and get results
        df = execute_sql_query(sql_query)
        
        # Create table and chart if results are valid
        if isinstance(df, pd.DataFrame) and not df.empty:
            table_output = html.Table(
                [html.Tr([html.Th(col) for col in df.columns])] +
                [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
            )
            fig = px.bar(df, x=df.columns[0], y=df.columns[1])
        else:
            table_output = "No results found or invalid query."
            fig = {}
        
        return query_output, table_output, fig
    return "", "", {}

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
