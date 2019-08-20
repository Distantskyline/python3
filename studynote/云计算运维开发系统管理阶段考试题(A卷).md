## 云计算运维开发系统管理阶段考试题(A卷)

- 不得参阅任何与考试有关的笔记或内容
- 不得交头接耳、相互传递纸条等违规行为
- 不得询问讲师一切与考试有关的内容

---

1. 在Linux系统中寻找以`.json`结尾的文件, 并且全部拷贝到`/JSON`目录中; 请统计共有多少个文件？

   ```shell
   mkdir /JSON
   find / -type f -iname *.json -exec cp -rf {} /JSON/ \;
   ls -l /JSON | wc -l
   ```

   

2. 请统计`access_log`日志中访问量前十的IP地址, 要求显示的信息为`IP地址  -  访问次数`

   ```shell
   awk '{ ips[$1]++ }END{ for(ip in ips){ print ip, ips[ip] } }' access_log | sort -k2 -rn | head -10
   ```

   

3. 请写出这些符号的意义: `$?` `$#` `$0` `$$`

   ```shell
   $?: 上调命令执行后返回的状态码
   $#: 所加位置变量的个数
   $0: 其脚本本身
   $$: 脚本执行时的pid
   ```

   

4. 如何让Linux系统的历史记录显示具体时间(精确到秒); 怎么样同步系统的时间为互联网时间

   ```shell
   echo "export HISTTIMEFORMAT=\"%Y-%m-%d %H:%M:%S - \"" >>/etc/profile
   source /etc/profile
   
   ntpdate -b ntp1.aliyun.com
   ```

   

5. 在三月份每7天执行一次系统健康检查, 健康检查时运行脚本checkHealth.sh, 请写出具体步骤及命令

   ```shell
   0 0 */7 3 *	bash checkHealth.sh
   ```

   

6. sql语句中, 查询框架有哪些？(至少写两种); 删除数据的框架是？插入数据的框架是？修改数据的框架是？

   ```shell
   select * from database.table;
   select 
   
   delete from table where fieldname=?;
   
   insert into tables values();
   
   update tablename set fieldname01=? where fieldname02=?
   ```

   

7. 请简述MySQL主从复制的原理, 并画出其原理图

8. 将数据`{bavduer: {sex: Man, like: basketball, company: qfcloud}}`插入到redis中的语句是？

   ```shell
   hash key-value
   
   redis> hmset bavduer sex Man .. .. .. ..
   ```

   

9. push代码时, 分别要执行那几个步骤？命令是什么？

   ```shell
   添加文件至仓库: git add --all
   提交文件至仓库: git commit -m "描述"
   推送至远程仓库: git push -u origin master
   ```

   

10. 在命令行中删除file.txt文件中所有带`qfcloud`的行(正则); 

   截取本机的IP地址; 

   查找ipaddr.txt中所有符合规范的IP地址(正则)

   ```shell
   sed -i(.bak) "/.*qfcloud.*/d" file.txt 
   
   ifconfig | grep inet | awk 'NR==2{ print $2 }'//
   
   1-255: [1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]
   0-255: [0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]
   
   ^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){2}.)([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$
   ```

   
