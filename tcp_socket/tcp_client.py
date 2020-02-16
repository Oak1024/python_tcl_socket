import socket


def main():
    # 1.常见套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 连接服务器
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入端口号："))
    server_addr = (server_ip,server_port)
    tcp_server_socket.connect(server_addr)

    # 发送信息
    send_msg = input("请输入发送内容：")
    tcp_server_socket.send(send_msg.encode("gbk"))

    # 关闭套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()