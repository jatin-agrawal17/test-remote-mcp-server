from fastmcp import FastMCP
import random
import json
from prefect import flow

# Create MCP server
mcp = FastMCP('Simple Calculator Server')

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(name="generate_random")
def generate_random(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

@mcp.resource('info://server')
def server_info() -> str:
    info = {
        'name': 'Simple Calculator Server',
        'version': '1.0',
        'description': 'Performs addition and generates random numbers'
    }
    return json.dumps(info, indent=2)

# ✅ ENTRYPOINT (VERY IMPORTANT)
@flow
def main():
    mcp.run(transport='http', host="0.0.0.0", port=8000)