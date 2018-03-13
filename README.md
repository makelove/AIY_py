This repository contains the APIs and demo apps for the AIY Projects. See
https://aiyprojects.withgoogle.com.

我的经验总结,必看!!!
- https://github.com/makelove/True_Artificial_Intelligence/tree/master/%E7%A1%AC%E4%BB%B6/Google_AIY_voice_kit

- 怎样连接上Google语音助手平台
    - 方法1：
        - 在树莓派上安装，Arm版蓝灯https://github.com/EasyPi/docker-lantern-arm/releases/
            -  下载 lantern_4.4.0-1_armhf.deb
            - sudo dpkg -i lantern_4.4.0-1_armhf.deb
            - sudo systemctl start lantern
            - sudo systemctl enable lantern
            - export http_proxy='http://127.0.0.1:50493';export https_proxy='http://127.0.0.1:50493'
            - 测试 curl https://www.google.com/
            - 运行你的AIY python代码
    - 方法2：
        - 下载蓝灯[蓝灯最新版下载地址](https://github.com/getlantern/forum/issues/833) 
            - Windows 版本(要求XP SP3以上)
        - 在你的Windows电脑上安装
            - 防火墙，开通网络端口50493，50497
            - 找到settings.yaml，修改
                - 把addr: 127.0.0.1:50493改为 addr: 192.168.1.xxx:50493
                - 把socksAddr: 127.0.0.1:50497改为socksAddr: 192.168.1.xxx:50497
            - 启动蓝灯
        - 在树莓派的terminal上输入
            - export http_proxy='http://192.168.1.xxx:50493';export https_proxy='http://192.168.1.xxx:50493'
            - 测试 curl https://www.google.com/
            - 运行你的AIY python代码
    