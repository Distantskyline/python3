## 云计算开发: 周六自习练习题

-Author: bavdu

-Email: bavduer@gmail.com

-Github: https://github.com/bavdu

---



##### 基础概念题

---

1. 按要求创建如下文件并添加内容:

   - 在/opt目录下创建目录admins、目录userfile、文件README.txt

   - 在/opt/admins中创建文件userlist.json

   - 在/opt/userfile中创建文件jack.json、tom.json

   - 把如下内容添加至README.txt文件中, 无格式要求

     ```markdown
     ##JSON Format
     
     	The json format is often used by us to transfer data over the Internet, and json's biggest feature is the ability to transfer data between any language without the need for a specific interpretation process.
     	For example, the files stored in the two directories under the current folder are the json forms used.
     ```

   - 把如下内容添加至userlist.json中,要求所有信息均在同一行中

     ```json
     {'User': {
         'tom':
             {
                 'uid': 10248,
                 'gid': 1024,
                 'homedir': "/home/tom",
                 'shell': 'nologin'
             },
         'jack':
             {
                 'uid': 20489,
                 'gid': 2048,
                 'homedir': "/home/jack",
                 'shell': 'nologin'
             }
     }}
     ```

   - 把如下内容添加至jack.json中, 要求所有信息均在同一行中

     ```json
     jack = {
         'owner': 'self',
         'group': 'wheel',
         'sudo': 'no Password'
     }
     ```

   - 把如下内容添加至tom.json中, 要求所有信息均在同一行中

     ```json
     tom = {
         'owner': 'root',
         'group': 'admins',
         'sudo': 'yes Password'
     }
     ```

   

2. 按照要求创建用户并设置权限

   - 创建组adminx, 创建组userlistx

   - 创建用户jack, 创建用户tom, 他们的密码都是`qfPyCloud..`

   - 把admins目录的所属组修改为adminx, 把userlist目录的所属组修改为userlistx

   - 把jack.json文件的拥有者修改为jack, 把tom.json文件的拥有者修改为tom

   - jack用户的第二个组为wheel, 并设置jack用户能够免密使用sudo提权

   - 第1题中所有的文件及目录, 对于除属主属组意外的用户没有任何权限

     

3. 按要求安装软件在Linux系统中:

   - 在系统中安装`tree`命令、`ifconfig`命令、`lftp`命令

   - 如果系统出现如下错误应该怎么解决？

     ```tex
     -bash: wget: command not found
     ```

   - 请问`ifconfig`命令, 来源于哪一个软件包？

   - 请把系统的base源, epel源设置成清华yum源, 其他源可备份或删除, 试验安装yum-utils软件包检查可用性

   

4. 请简述进程和线程的概念, 及其两者之间的关系

   - 请问如何查看进程的静态信息？怎样停止该进程的运行？
   - 请问如何查看某个进程的网络信息？

   

5. 请把第1题中以`.json`结尾的文件打包为`jsonball.tar.xz`(结合find命令)

6. 请写出查看IP地址的所有命令, Linux中网络的重新连接该使用什么指令？(具体命令)





##### 错误处理题

---

1. 系统中报出如下错误应当如何处理？要求: 写出错误原因及处理方案

   ```shell
   [root@linux_basis ~]# yum -y install vim
   已加载插件：fastestmirror
   
   
   File contains parsing errors: file:///etc/yum.repos.d/CentOS-Base.repo
   	[line 21]: updates]
   	
   ********第21行 开头少个 [  ******
   ```

2. 系统中报出如下错误应当如何处理？要求: 写出错误原因及处理方案

   ```shell
   [root@linux_basis ~]# yum -y install vim
   已加载插件：fastestmirror
   Loading mirror speeds from cached hostfile
   epel/x86_64/metalink                                                         | 5.5 kB  00:00:00
    * epel: mirrors.tuna.tsinghua.edu.cn
   https://mxxirrors.tuna.tsinghua.edu.cn/centos/7/os/x86_64/repodata/repomd.xml: [Errno 14] curl#6 - "Could not resolve host: mxxirrors.tuna.tsinghua.edu.cn; 未知的错误"
   正在尝试其它镜像。
   
   ********源有问题********
   
    One of the configured repositories failed (CentOS-7 - Base),
    and yum doesn't have enough cached data to continue. At this point the only
    safe thing yum can do is fail. There are a few ways to work "fix" this:
   
        1. Contact the upstream for the repository and get them to fix the problem.
   
        2. Reconfigure the baseurl/etc. for the repository, to point to a working
           upstream. This is most often useful if you are using a newer
           distribution release than is supported by the repository (and the
           packages for the previous distribution release still work).
   
        3. Run the command with the repository temporarily disabled
               yum --disablerepo=base ...
   
        4. Disable the repository permanently, so yum won't use it by default. Yum
           will then just ignore the repository until you permanently enable it
           again or use --enablerepo for temporary usage:
   
               yum-config-manager --disable base
           or
               subscription-manager repos --disable=base
   
        5. Configure the failing repository to be skipped, if it is unavailable.
           Note that yum will try to contact the repo. when it runs most commands,
           so will have to try and fail each time (and thus. yum will be be much
           slower). If it is a very temporary problem though, this is often a nice
           compromise:
   
               yum-config-manager --save --setopt=base.skip_if_unavailable=true
   
   failure: repodata/repomd.xml from base: [Errno 256] No more mirrors to try.
   https://mxxirrors.tuna.tsinghua.edu.cn/centos/7/os/x86_64/repodata/repomd.xml: 
   [Errno 14] curl#6 - "Could not resolve host: mxxirrors.tuna.tsinghua.edu.cn; 未知的错误"
   ```

3. 系统中报出如下错误应当如何处理？要求: 写出错误原因及处理方案

   ```shell
   
   [root@linux_basis ~]# mkdir /opt/operator
   [root@linux_basis ~]# touch /mnt/operator
   [root@linux_basis ~]# cp -r /opt/operator /mnt/
   cp: 无法以目录"/opt/operator" 来覆盖非目录"/mnt/operator"
   [root@linux_basis ~]# ls -l /mnt/
   总用量 4
   -rw-r--r-- 1 root root    0 7月  19 17:44 operator
   
   *********文件名重复*********
   ```

4. 系统中报出如下错误应当如何处理？要求: 写出错误原因及处理方案

   ``` 
   E325: 注意
   发现交换文件 ".passwd.swp"
               所有者: root    日期: Fri Jul 19 17:51:14 2019
               文件名: ~root/passwd
               修改过: 是
               用户名: root      主机名: linux_basis
              进程 ID: 17680
   正在打开文件 "passwd"
                 日期: Wed Jul 17 14:49:23 2019
   
   (1) Another program may be editing the same file.  If this is the case,
       be careful not to end up with two different instances of the same
       file when making changes.  Quit, or continue with caution.
   (2) An edit session for this file crashed.
       如果是这样，请用 ":recover" 或 "vim -r passwd"
       恢复修改的内容 (请见 ":help recovery")。
       如果你已经进行了恢复，请删除交换文件 ".passwd.swp"
       以避免再看到此消息。
   
   交换文件 ".passwd.swp" 已存在！
   以只读方式打开([O]), 直接编辑((E)), 恢复((R)), 删除交换文件((D)), 退出((Q)), 中止((A)):
   
   ********直接编辑(E) 保存后退出删除隐藏的交换文件********
   ```

5. 系统中报出如下错误应当如何处理？要求: 写出错误原因及处理方案

   ```shell
   [root@linux_basis ~]# mkdir filelist
   [root@linux_basis ~]# touch filelist/operator{01..10}.txt
   [root@linux_basis ~]# find filelist/ -type f file*
   find: 路径必须在表达式之前: filelist
   用法: find [-H] [-L] [-P] [-Olevel] [-D help|tree|search|stat|rates|opt|exec] [path...] [expression]
   
   *************find filelist/ -type f -iname operator*.txt*********
   ```

6. 系统中报出如下错误应当如何处理？要求: 写出错误原因及处理方案

   ```shell
   [root@linux_basis ~]# echo 'hello pycloud classmate' >hello.py
   [root@linux_basis ~]# cat holle.py
   cat: holle.py: 没有那个文件或目录
   
   ```

*******cat hello.py********
   ```
   
   



##### 流程梳理题

---

1. 部署nginx源码包时, 都需要哪几个步骤？分别是什么作用？
2. 备份文件时, 应当遵循什么流程？为什么？
3. 删除文件时, 应当遵循什么流程？为什么？
   ```