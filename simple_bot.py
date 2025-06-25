from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound
import threading

IP = "5.9.41.143"
PORT = 30728
NUM_BOTS = 3  # bạn có thể tăng số bot

def start_bot(bot_id):
    username = f"TestBot{bot_id}"
    conn = Connection(IP, PORT, username=username)

    def on_join(join_packet):
        print(f"[{username}] ✅ Đã vào server.")

    def on_disconnect(pkt):
        print(f"[{username}] ❌ Mất kết nối hoặc bị từ chối")

    conn.register_packet_listener(on_join, clientbound.play.JoinGamePacket)
    conn.register_packet_listener(on_disconnect, clientbound.play.DisconnectPacket)
    conn.register_packet_listener(on_disconnect, clientbound.login.DisconnectPacket)

    try:
        conn.connect()
    except Exception as ex:
        print(f"[{username}] ❌ Kết nối lỗi: {ex}")

threads = []
for i in range(NUM_BOTS):
    t = threading.Thread(target=start_bot, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print("✅ Hoàn tất các bot!")
