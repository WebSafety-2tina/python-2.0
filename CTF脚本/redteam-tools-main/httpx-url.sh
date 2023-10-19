#!/bin/bash
#forum.ywhack.com
VERSION="PoC_Info v1.0"

TARGET="$1"
WORKSPACE=$TARGET
WORKING_DIR="$(cd "$(dirname "$0")" ; pwd -P)"
RESULTS_PATH="$WORKING_DIR"

RED="\033[1;31m"
GREEN="\033[1;32m"
BLUE="\033[1;36m"
YELLOW="\033[1;33m"
RESET="\033[0m"

# filename=$TARGET_$(date +%s)'.txt'
time=$(date "+%Y年%m月%d日%H时%M分%S秒")

# logo
Logo(){
echo  "${GREEN}    
 ${RED}v$VERSION${RESET}  ${GREEN} 
 by ${YELLOW}@Blackhold${RESET}\n "
}
# 提示

# 信息开始
infostart(){
     echo "${GREEN}[+] Running InfoExp.${RESET}"
     echo "$TARGET" | /Users/blackhold/Tools/scan/httpx_0.0.8/httpx -silent | /Users/blackhold/Tools/scan/nuclei_2.1.0/nuclei -t /Users/blackhold/Tools/scan/nuclei_2.1.0/nuclei-templates/ -o results_$time.txt
     echo "\n"
     echo "${RED}已经在当前目录生成${RESET}${GREEN}results_$time.txt${RESET}${RED}，请注意查看！${RESET}"
     echo "${RED}运行结束！bye.${RESET}  by ${YELLOW}@Blackhold${RESET}"
}

Logo
#checkArgs $TARGET
infostart
exit 1