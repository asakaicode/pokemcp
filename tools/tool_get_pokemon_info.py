import httpx


async def get_pokemon_info(pokemon_name: str) -> str:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        content = f"ポケモン『{pokemon_name}』は見つかりません。"
    else:
        data = response.json()
        types = ", ".join(
            t["type"]["name"] for t in data.get("types", [])
        )
        abilities = ", ".join(
            a["ability"]["name"] for a in data.get("abilities", [])
        )
        content = (
            f"Name: {data.get('name', '').title()}\n"
            f"ID: {data.get('id')}\n"
            f"Types: {types}\n"
            f"Abilities: {abilities}\n"
            f"Height: {data.get('height')}\n"
            f"Weight: {data.get('weight')}"
        )

    return {"content": content}
