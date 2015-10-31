# Net 101 极简交互式笔记的网络版本

需求如下：
	- 每次运行时合理的打印出过往的所有笔记
	- 一次接收输入一行笔记
	- 在服务端保存为文件:
	   - 在所有访问的客户端可以获得历史笔记
	- 支持多个客户端同时进行笔记记录
   
## 分析
总结上次经验，掌握好节奏，分为以下几步

    - 原型。掌握UDP原理，写出实验模型。
    - 完成日记最小功能逐步实现
        + 消息接收
        + 多端
        + 历史获取

## 进展

!(http://learnyousomeerlang.com/static/img/udp.png)
!(http://docs.linuxtone.org/ebooks/C&CPP/c/images/socket.udpflowchart.png)