import asyncio
import json
from deriv_api import DerivAPI

async def main():
    api = DerivAPI(app_id=64539)
    api_token = "KhcFUhkGV46TPog"
    
    # Authorize using the API token
    authorize_response = await api.authorize(api_token)

    # Check if authorization was successful
    if authorize_response.get('error'):
        print("Authorization failed:", authorize_response['error']['message'])
        return  # Exit if authorization failed

    # Define the transaction statement request to fetch specific transaction by ID
    transaction_id = 516467606208
    statement_request = {
        "statement": 1,  # Request statement
        "description": 1,  # Include transaction descriptions
        "limit": 1,  # Limit results to 1 (since we are querying a single transaction)
        "transaction_id": transaction_id,  # Provide the transaction ID
        "req_id": 42  # Any unique request ID
    }

    # Send the statement request
    statement_response = await api.statement({"statement": 1, "description": 1, "limit": 100, "offset": 1})

    # Save response to JSON file
    with open('statement_response.json', 'w') as json_file:
        json.dump(statement_response, json_file, indent=4)

    # Output file saved path
    print("Response saved to statement_response.json")

# Run the async function
asyncio.run(main())
