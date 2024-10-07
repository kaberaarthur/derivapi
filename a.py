import asyncio
from deriv_api import DerivAPI

async def main():
    api = DerivAPI(app_id=64539)
    	
    api_token = "KhcFUhkGV46TPog"  # Replace with your actual API token
    authorize = await api.authorize(api_token)
    print(authorize)

# Run the async function
asyncio.run(main())
