# src/prisma_client.py
from prisma import Prisma

# Initialize Prisma Client
prisma = Prisma()


async def create_user(user_id):
    """Create a new user in the database."""
    try:
        await prisma.connect()  # Connect to the database
        user = await prisma.user.create(
            data={
                'userId': str(user_id)
            }
        )
        await prisma.disconnect()  # Disconnect after operation
    except Exception as e:
        print("Error creating user: ", e)


async def query_db():
    await prisma.connect()
    await prisma.disconnect()


async def clear_all_data():
    """Clear all data from the database."""
    await prisma.connect()  # Connect to the database

    try:
        # List of models to clear
        models = [prisma.user]  # Add other models as needed

        for model in models:
            await model.delete_many()  # Delete all records from each model

    except Exception as e:
        print(f"An error occurred while clearing data: {e}")

    finally:
        await prisma.disconnect()  # Disconnect from the database
