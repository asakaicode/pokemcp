from mcp.server.fastmcp import FastMCP

from tools.tool_get_pokemon_info import (
    get_pokemon_info as tool_get_pokemon_info,
)

mcp = FastMCP("PokeMCP")


@mcp.tool()
async def get_pokemon_info(pokemon_name: str) -> str:
    """
    Get Pokémon information by its English name and return it as
    a formatted string.

    Args:
        pokemon_name (str): Pokémon's English name.

    Returns:
        str: A string containing the Pokémon's name, ID, types,
            abilities, height, and weight.
    """
    return tool_get_pokemon_info(pokemon_name)


if __name__ == "__main__":
    mcp.run(transport='stdio')
