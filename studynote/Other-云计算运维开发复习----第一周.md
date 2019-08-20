## 云计算运维开发复习指导

-Author: bavdu

-Email: bavduer@gmail.com

-Github: https://github.com/bavdu

---



各位: 知识较为灵活别钻牛角尖、不会的问题可以静下来琢磨琢磨、再不会就去查查百度、实在不会了Q我



1. 文件都有哪些处理方式(创建、rm删除、vim修改、find查找(查找过程中的打包))
2. Linux系统中怎么安装软件？如何配置清华yum源？如何根据特定的信息查找该信息的来源包？
3. Linux系统中查找到指定的进程, 并停止它
4. Linux系统中如何修改文件的权限？如何修改文件的拥有者和所属组？
5. 用户在创建的过程中有哪些常见的选项？并解释他们的作用？(-u -g -M -s -d)
6. Linux系统中怎么设置网络为静态网络？桥接和NAT的区别？
7. 桥接中的静态地址怎么设置请写出详细信息(网段: 10.36.145.0/24)
8. NAT中的静态地址怎么设置请写出详细信息(网段: 192.168.161.0/24)



补充知识点:

```shell
$ systemctl stop firewalld		# 设置关闭防火墙
$ systemctl disable firewalld # 设置开机禁止启动防火墙

$ setenforce 0								# 关闭Linux系统的SElinux防护机制,生产环境必须关闭
```



新服务器系统初始化流程:

```shell
1. systemctl stop firewalld && systemctl disable firewalld
2. yum -y install vim net-tools wget
3. yum -y install groupinstall "Development Tools"
4. 修改网卡为静态获取IP地址
```



