# 📝 MCP Note Saver Server

เซิร์ฟเวอร์ Model Context Protocol (MCP) ขนาดเล็กที่พัฒนาด้วย Python โปรเจกต์นี้ช่วยให้ AI Assistant (เช่น Claude Desktop) สามารถทำงานร่วมกับระบบไฟล์ในเครื่องของคุณ โดยรับคำสั่งให้จดบันทึกและบันทึกลงไฟล์ข้อความ (Text file) ได้โดยตรง

##  เกี่ยวกับโปรเจกต์
โปรเจกต์นี้คือการสร้างระบบพื้นฐานของ **Model Context Protocol (MCP)** เพื่อเชื่อมต่อ AI Agent เข้ากับสภาพแวดล้อมในเครื่อง (Local Environment) ผ่านการสื่อสารด้วยโปรโตคอล `STDIO` 

**ฟีเจอร์หลัก:**
- เชื่อมต่อและทำงานร่วมกับ AI Client ได้อย่างไร้รอยต่อ (Claude Desktop, Cursor IDE)
- เขียนและเพิ่มข้อความ (Append) ลงไฟล์ `notes.txt` ในเครื่องได้อย่างปลอดภัยโดยไม่ทับข้อมูลเดิม
- มีระบบบันทึกการทำงาน (`server.log`) สำหรับติดตาม Request JSON-RPC และกระบวนการทำงานเบื้องหลัง

---

## 🛠️ สิ่งที่ต้องเตรียมพร้อม (Prerequisites)
ก่อนเริ่มต้นใช้งาน ตรวจสอบให้แน่ใจว่าเครื่องของคุณมีสิ่งเหล่านี้:
* ติดตั้ง **Python 3.10+** ไว้ในเครื่อง
* ติดตั้งโปรแกรม **Claude Desktop** (หรือ AI IDE ที่รองรับ MCP เช่น Cursor)
* ระบบปฏิบัติการ: Windows, macOS หรือ Linux

---

## การติดตั้งและตั้งค่า (Installation & Setup)

**1. Clone โปรเจกต์ลงเครื่อง (Clone the repository)**
```bash
git clone [https://github.com/](https://github.com/)[ชื่อผู้ใช้ GitHub ของคุณ]/mcp-note-server.git
cd mcp-note-server
2. สร้างและเปิดใช้งาน Virtual Environment
สำหรับ Windows:

Bash
python -m venv venv
venv\Scripts\activate
สำหรับ macOS/Linux:

Bash
python -m venv venv
source venv/bin/activate
3. ติดตั้ง Dependencies

Bash
pip install mcp
⚙️ การตั้งค่าการเชื่อมต่อ (Configuration สำหรับ Claude Desktop)
เพื่อเชื่อมต่อเซิร์ฟเวอร์นี้เข้ากับ Claude Desktop คุณต้องทำการชี้เป้าหมายให้ AI รู้จักเซิร์ฟเวอร์ก่อน

ไปที่ตำแหน่งไฟล์ Configuration ของ Claude:

Windows: %APPDATA%\Claude\claude_desktop_config.json

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

เพิ่มโครงสร้าง JSON ด้านล่างนี้ลงไป (สำคัญ: ต้องเปลี่ยนเป็น Absolute Path ของเครื่องคุณเองให้ถูกต้อง):

JSON
{
  "mcpServers": {
    "NoteSaverServer": {
      "command": "C:/[ระบุ Path ไปที่โฟลเดอร์โปรเจกต์]/venv/Scripts/python.exe",
      "args": [
        "C:/[ระบุ Path ไปที่โฟลเดอร์โปรเจกต์]/server.py"
      ]
    }
  }
}
ทำการ Hard Quit โปรแกรม Claude Desktop (คลิกขวาที่ไอคอนมุมขวาล่างแล้วเลือก Quit) จากนั้นเปิดโปรแกรมขึ้นมาใหม่
