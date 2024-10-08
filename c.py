import asyncio
from deriv_api import DerivAPI

async def main():
    api = DerivAPI(app_id=64539)
    api_token = "KhcFUhkGV46TPog"
    
    # Authorize using the API token
    authorize_response = await api.authorize(api_token)
    print("Authorization response:", authorize_response)

    # Check if authorization was successful
    if authorize_response.get('error'):
        print("Authorization failed:", authorize_response['error']['message'])
        return  # Exit if authorization failed

    # Fetch the account balance
    account_balance = await api.balance()
    print("Account Balance:", account_balance)

    # Check if balance retrieval was successful
    if account_balance.get('error'):
        print("Failed to retrieve account balance:", account_balance['error']['message'])
        return

    # Print the account balance details
    balance = account_balance.get('balance', {})
    print("Balance:", balance)

# Run the async function
asyncio.run(main())
