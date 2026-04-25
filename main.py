from fastmcp import FastMCP
import random
import json

# Create MCP server
mcp = FastMCP('Simple Calculator Server')

# ➕ Add tool
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# 🎲 Random number tool (fixed name issue)
@mcp.tool(name="generate_random")
def generate_random(min_val: int, max_val: int) -> int:
    """Generate a random number between min_val and max_val"""
    return random.randint(min_val, max_val)

# ℹ️ Resource
@mcp.resource('info://server')
def server_info() -> str:
    """Get server information"""
    info = {
        'name': 'Simple Calculator Server',
        'version': '1.0',
        'description': 'Performs addition and generates random numbers'
    }
    return json.dumps(info, indent=2)

# 🚀 Run server
if __name__ == '__main__':
    mcp.run(transport='http', host="127.0.0.1", port=8000)