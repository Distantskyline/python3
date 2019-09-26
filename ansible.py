ansible all -m ping -o
               shell a ' '
#过滤某个模块
ansible-doc -l | grep
#计划任务
ansible all  -m cron -a ' minute="*/5",hour="*",day="*",month="*",weekday="*",job="*",name="*"'
#删除
ansbile all -m cron 'name=" " satate=absent'
#copy模块
ansible all -m copy -a 'src=   dest=     owner=    group=   mode=   '
#file模块
ansible all -m file -a 'owner="root"  group="root" mode=   dest=" "  '

ansible all -m file -a 'path=   stat=touch/absent'
#url下载
ansible all -m get-url -a 'url=    dest=    '
#yum 模块
ansible all -m yum -a'name=    state=latest/absent'
#service服务
ansible all -m service -a 'name=  state=started/restarted/stopped   enabled=true'
#script脚本
ansible all -m script -a ' '


ansible-play  路径  --syntax-check
