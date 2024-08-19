# src/prisma_client.py
from prisma import Prisma

# Initialize Prisma Client
prisma = Prisma()


async def create_user(user_id):
    """Create a new user in the database."""
    await prisma.connect()  # Connect to the database
    user = await prisma.user.create(
        data={
            "userId": user_id,
        }
    )
    await prisma.disconnect()  # Disconnect after operation
    return user
