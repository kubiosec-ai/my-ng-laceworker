import asyncio
from agents import Agent, Runner

async def main():
    # Define the agent with a name and instructions
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
    )

    # Run the agent with an input prompt
    result = await Runner.run(agent, "Tell me a joke.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
