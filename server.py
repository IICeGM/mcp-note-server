import asyncio 
import os

# log
import  logging

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent , Tool

base_dir = os.path.dirname(os.path.abspath(__file__))
# log
log_file_path = os.path.join(base_dir,"server.log")
logging.basicConfig(
    filename = log_file_path,
    level = logging.INFO, # กำหนดระดับการเก็บ Log
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("NoteSaverServer")


# initialize server
app = Server("NoteSaverServer")

# expose the capabilities 
@app.list_tools()
async def list_tool() -> list[Tool]:
    # log
    logger.info("Claude requested the list of tools. ")
    return [
        Tool(
            name="save_note",
            description="บันทึกข้อความลงไปในไฟล์ notes.txt ในเครื่อง ",
            inputSchema={
                "type": "object",
                "properties" : {
                    "content": {
                        "type" : "string",
                        "description" : "ข้อความที่ต้องการจะบันทึกลงไปในไฟล์ notes.txt"
                    }
                },
                "required" : ["content"]
            }
        )
    ]

# execution logic || สั่งให้ tool ทำงานตอน ai เรียกใช้
@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:

    # log
    logger.info(f"Claude called tool: '{name}' with arguments : {arguments}")

    if name == "save_note" :
        content = arguments.get("content")
        if not content: 
            raise ValueError("Missing 'content' arguments ")
        # File writing logic
        file_path = os.path.join(base_dir, "notes.txt")

        with  open(file_path , "a" , encoding= "utf-8") as f:
            f.write(content + "\n")
        return [TextContent(type="text",text="Note saved successfully.")]
    else: 
        raise ValueError(f"Unknown tool {name}")


# Entry point สำหรับการรันด้วย STDIO
async def main():
    logger.info("=========================================")
    logger.info("Starting NoteSaverServer via STDIO...")
    logger.info("=========================================")
    async with stdio_server() as (read_stream , write_stream):
        await app.run(read_stream , write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())