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

    # Define the proposal request
    proposal_request = {
        "proposal":1,
        "subscribe":1,
        "amount":"35",
        "basis":"stake",
        "contract_type":"DIGITODD",
        "currency":"USD",
        "symbol":"1HZ100V",
        "duration":2,
        "duration_unit":"t",
        "req_id":37
    }

    # Send the proposal request
    proposal = await api.proposal(proposal_request)
    print("Proposal:", proposal)

    # Get the proposal ID
    proposal_id = proposal.get('proposal', {}).get('id')
    
    if proposal_id:  # Check if proposal_id exists
        # Send a buy request using the proposal ID
        buy_request = {
            "buy": proposal_id,
            "price": 100  # Adjust price as needed
        }
        
        buy = await api.buy(buy_request)
        print("Buy response:", buy)
    else:
        print("Proposal ID not found.")

# Run the async function
asyncio.run(main())
