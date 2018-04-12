This repository contains the APIs and demo apps for the AIY Projects. See
https://aiyprojects.withgoogle.com.

- 官方代码https://github.com/google/aiyprojects-raspbian

- 我的经验总结,必看!!!
    - https://github.com/makelove/True_Artificial_Intelligence/tree/master/%E7%A1%AC%E4%BB%B6/Google_AIY_voice_kit

- 怎样连接上Google语音助手平台
    - 方法1：
        - 在树莓派上安装，Arm版蓝灯https://github.com/EasyPi/docker-lantern-arm/releases/
            -  下载 lantern_4.4.0-1_armhf.deb
            - sudo dpkg -i lantern_4.4.0-1_armhf.deb
            - sudo systemctl start lantern
            - sudo systemctl enable lantern
            - ps aux|grep lantern #是否成功启动
            - export http_proxy='http://127.0.0.1:50493';export https_proxy='http://127.0.0.1:50493'
            - 测试 curl https://www.google.com/  #有可能lantern被封
            - 运行你的AIY python代码
    - 方法2：
        - 下载蓝灯[蓝灯最新版下载地址](https://github.com/getlantern/forum/issues/833) 
            - Windows 版本(要求XP SP3以上)
        - 在你的Windows电脑上安装
            - 找到你的局域网IP：192.168.1.xxx
            - 防火墙，开通网络端口50493，50497
            - 找到settings.yaml，修改
                - Windows XP 
                    - C:\Documents and Settings<用户名>\Application Data\Lantern\settings.yaml
                - Windows 7 - Windows 10 
                    -C:\Users<用户名>\AppData\Roaming\Lantern\settings.yaml
                - 把addr: 127.0.0.1:50493改为 addr: 192.168.1.xxx:50493
                - 把socksAddr: 127.0.0.1:50497改为socksAddr: 192.168.1.xxx:50497
            - 启动蓝灯
        - 在树莓派的terminal上输入
            - export http_proxy='http://192.168.1.xxx:50493';export https_proxy='http://192.168.1.xxx:50493'
            - 测试 curl https://www.google.com/
            - 运行你的AIY python代码
```bash
#nano .bashrc

#proxy
export http_proxy='http://192.168.0.159:50493'
export https_proxy='https://192.168.0.159:50493'
export no_proxy=localhost,127.0.0.0/8
```            
-  方法3：
    - 自建shadowsocks服务器
         - https://github.com/VincentChanX/shadowsocks-over-websocket
    - 安装
        - sudo apt install nodejs-legacy
        - sudo apt install npm
        - git clone https://github.com/VincentChanX/shadowsocks-over-websocket.git
        - cd shadowsocks-over-websocket/
        - npm install 
        - 建立你的appxxxx.herokuapp.com
        - 配置密钥 keyyyy
        - node local.js -s  xxxx.herokuapp.com -l 1080 -m aes-256-cfb -k keyyyy -p 80
        - sudo polipo socksParentProxy=localhost:1080 proxyAddress=0.0.0.0 proxyPort=50493
        