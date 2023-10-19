#!/bin/bash
# by forum.ywhack.com

#输出文件
filename=$(date +%s)'.log'

echo "信息收集"
echo -e "\n" | tee -a $filename
echo "账户信息收集" | tee -a $filename
cat /etc/passwd | tee -a $filename
echo -e "\n" | tee -a $filename
echo "shadow" | tee -a $filename
cat /etc/shadow | tee -a $filename
echo -e "\n" | tee -a $filename
echo "进程信息收集" | tee -a $filename
ps aux | tee -a $filename
echo -e "\n" | tee -a $filename
echo "网络连接" | tee -a $filename
netstat -antlp | tee -a $filename
echo -e "\n" | tee -a $filename
echo "当前用户:" $(whoami) 2>/dev/null | tee -a $filename
echo -e "\n" | tee -a $filename
echo "端口监听" | tee -a $filename
netstat -lnpt | tee -a $filename
echo -e "\n" | tee -a $filename
echo "可登陆用户" | tee -a $filename
cat /etc/passwd | grep -E -v 'nologin$|false' | tee -a $filename
echo -e "\n" | tee -a $filename
echo "增加用户的日志" | tee -a $filename
grep "useradd" /var/log/secure  | tee -a $filename
echo -e "\n" | tee -a $filename
echo "History操作提取" | tee -a $filename
cat ~/.*history | tee -a $filename
echo -e "\n" | tee -a $filename
echo "登录成功的IP" | tee -a $filename
grep "Accepted " /var/log/secure* | awk '{print $11}' | sort | uniq -c | sort -nr | more | tee -a $filename   
echo -e "\n" | tee -a $filename
echo "查看路由表" | tee -a $filename
route -n | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查看 SSH key" | tee -a $filename
sshkey=${HOME}/.ssh/authorized_keys
if [ -e "${sshkey}" ]; then
    cat ${sshkey} | tee -a $filename
else
    echo -e "SSH key文件不存在\n" | tee -a $filename
fi
echo -e "\n" | tee -a $filename
echo "查看 known_hosts" | tee -a $filename
cat ~/.ssh/known_hosts | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查找WEB-INF" | tee -a $filename
find / -name *.properties 2>/dev/null | grep WEB-INF | tee -a $filename
echo -e "\n" | tee -a $filename
echo "user|pass|pwd|uname|login|db_" | tee -a $filename
find / -name "*.properties" | xargs egrep -i "user|pass|pwd|uname|login|db_" | tee -a $filename
echo -e "\n" | tee -a $filename
echo "jdbc:|pass=|passwd=" | tee -a $filename
find / -regex ".*\.properties\|.*\.conf\|.*\.config\|.*\.sh" | xargs grep -E "=jdbc:|pass=|passwd=" | tee -a $filename
echo -e "\n" | tee -a $filename
# Author cances
echo "ip和网卡信息" | tee -a $filename
ip a | awk '{print $2,$4}' | tee -a $filename
echo -e "\n" | tee -a $filename
echo "可登陆用户" | tee -a $filename
cat /etc/passwd | grep -E -v 'sync$|halt$|nologin$|false|shutdown' | tee -a $filename
echo -e "\n" | tee -a $filename
echo "用户登陆日志" | tee -a $filename
lastlog | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查看 hosts" | tee -a $filename
cat /etc/hosts | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查看 系统版本" | tee -a $filename
cat /etc/*-release | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查看 内核版本" | tee -a $filename
uname -mrs | tee -a $filename