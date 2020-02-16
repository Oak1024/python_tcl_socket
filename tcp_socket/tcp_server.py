
# https://www.cnblogs.com/yifengs/p/11375900.html 不错的教程，还讲了tcp传送文件
import socket


def main():
    # 创建套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 绑定端口
    tcp_server_socket.bind(("192.168.199.88",7788))

    # 把套接字变成被动
    tcp_server_socket.listen(128)

    # 循环目的：等待新客户端 为多个客户端服务
    while True:
        print("等待一个新的客户端访问：")
        # 分发新的套接字服务客户端
        new_client_socket,client_addr = tcp_server_socket.accept()

        print("一个新的客户端到来：%s" % str(client_addr))  # 因为client_addr是一个元祖 所以要转换成字符串

        # 此时堵塞
        # 循环目的：为同一个客户端服务多次
        while True:
            # 接收客户端发来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发来请求：%s" % recv_data.decode("gbk"))

            # 如果recv堵塞，那么有2种方式：
            # 1.客户端发来数据
            # 2.客户端调用close导致了recv街堵塞
            if recv_data:
                # 向客户端发送信息
                new_client_socket.send("你是谁".encode("gbk"))
            else:
                break

        # 关闭套接字
        new_client_socket.close()
        print("这次服务完毕。。。。")

    # 如果将监听套接字关闭了，那么会导致 不能再次等待新客户的到来，即xxxx.accept就会失败
    tcp_server_socket.close()


if __name__ == '__main__':
    main()