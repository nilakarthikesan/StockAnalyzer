from langchain_openai import ChatOpenAI
from kpi_data_in_dictionary import kpis
from finding_optimal_weights import weights_dict

# List of assets to analyze
assets = [
    "Apple (AAPL)",
    "Amazon (AMZN)",
    "Bitcoin (BTC-USD)",
    "Alphabet (GOOGL)",
    "Meta (META)",
    "Microsoft (MSFT)",
    "Nvidia (NVDA)",
    "S&P 500 index (SPY)",
    "Tesla (TSLA)"
]

# Define the start and end years for the analysis
start_year = 2022
end_year = 2023

key = "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"

llm = ChatOpenAI(model = "gpt-4o", 
                 temperature = 0, 
                 api_key = key,)

prompt = f"""
Can you provide a python code that uses the yfinance library to download stock data. The stocks and tickers that I specfically want data for {assets} from {start_year} to {end_year}
"""

response = llm.invoke(prompt)

print("\nGenerated Python Code:\n")
print("=" * 40)
print(response.content)
print("=" * 40)

prompt2 = f"""
Tell me the top 10 KPIs I could use to check for the preformance of stocks, explain the KPIs and how to interpret them they are how to interpret them.  
Provide the python code to compute and visualize each of the KPIs. 
Make sure the KPIs can be easilly extracted to include in the following prompt for interpretation. 
The structure should be: 
1) What is the KPI and how to interpret 
2) Code snippet for a function to visualize over time for each of the {assets} seperatly for each KPI 
years of analysis are {start_year} and {end_year}
"""

response2 = llm.invoke(prompt2)

print("\nGenerated Python Code:\n")
print("=" * 40)
print(response2.content)
print("=" * 40)


prompt3 = f"""
Read this {kpis} data and provide me with executive summary with reccomendation
"""

response3 = llm.invoke(prompt3)

print("\nGenerated Summary:\n")
print("=" * 40)
print(response3.content)
print("=" * 40)

risk_free = 0.04

prompt4 = f"""
Explain what is the Modern Portfolio theory, with a risk free rate of {risk_free}. 
Provide the Python code snippets for the MPT for the following assets {assets} for the years {start_year} to {end_year}. 
Print the weights with two decimal cases. 
Store the results in a dictionary with the tickers as keys and the weights as values. 
"""

response4 = llm.invoke(prompt4)

print("\nGenerated Python Code:\n")
print("=" * 40)
print(response4.content)
print("=" * 40)

prompt5 = f"""
This is the portfolio allocation {weights_dict} from the MPT for the {assets}. 
Give me 5 different techniques to optimize this portfolio with pros and cons of each alternative and explain the differenece from the MPT
"""

response5 = llm.invoke(prompt5)

print("\nGenerated Python Code:\n")
print("=" * 40)
print(response5.content)
print("=" * 40)