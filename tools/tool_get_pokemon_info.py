import httpx


async def get_pokemon_info(pokemon_name: str) -> str:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
        except httpx.ConnectError:
            return "ネットワーク接続エラーが発生しました。もう一度お試しください。"
        except httpx.TimeoutException:
            return "リクエストがタイムアウトしました。もう一度お試しください。"
        except httpx.HTTPError as e:
            return f"HTTPエラーが発生しました: {str(e)}"

    if not (200 <= response.status_code < 300):
        content = f"Pokemon '{pokemon_name}' not found."
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

    return content
