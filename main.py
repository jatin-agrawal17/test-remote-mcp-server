from fastmcp import FastMCP
import random
import json

def create_app():
    mcp = FastMCP('Simple Calculator Server')

    @mcp.tool
    def add(a: int, b: int) -> int:
        return a + b

    @mcp.tool(name="generate_random")
    def generate_random(min_val: int, max_val: int) -> int:
        return random.randint(min_val, max_val)

    @mcp.resource('info://server')
    def server_info() -> str:
        return json.dumps({
            'name': 'Simple Calculator Server',
            'version': '1.0'
        }, indent=2)

    return mcp