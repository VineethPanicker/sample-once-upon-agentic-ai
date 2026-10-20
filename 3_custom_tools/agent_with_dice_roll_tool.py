from strands import Agent
# TODO: Step 1 - Import tool from strands
from strands import tool

# TODO: Step 1 - Add the decorator to transform your function into a tool
@tool
def roll_dice(faces: int = 6) -> int:
    # TODO: Step 2 - Write a docstring with the description, an Args section and the return value
    """Roll a single die with the given number of faces.

    Args:
        faces: Number of faces on the die (e.g. 4, 6, 8, 10, 12, 20). Defaults to 6.

    Returns:
        The rolled value, between 1 and faces.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    model="global.amazon.nova-2-lite-v1:0",
    # TODO: Step 3 - Add the tool to the agent
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in fantasy role-playing adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about the game mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die.
    Every die must come from the roll_dice tool: call it once per die and never invent a result."""
)

dice_master("Help me create a new fantasy character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")

