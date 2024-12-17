import asyncio
import websockets
import os

# تحديد المنفذ (Railway يرسل المنفذ في المتغير PORT)
PORT = int(os.getenv("PORT", 8000))

# قائمة لتخزين اتصالات المستخدمين
connected_users = set()

async def handler(websocket, path):
    # إضافة الاتصال الجديد
    connected_users.add(websocket)
    try:
        async for message in websocket:
            # إرسال الرسالة لجميع المستخدمين المتصلين
            for user in connected_users:
                if user != websocket:
                    await user.send(message)
    except:
        pass
    finally:
        connected_users.remove(websocket)

# تشغيل الخادم
start_server = websockets.serve(handler, "0.0.0.0", PORT)

print(f"Server is running on port {PORT}...")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
