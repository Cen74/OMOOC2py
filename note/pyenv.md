Pyenv 和 Virtualenv都是用来配置Python多版本环境的，解决多个项目对应不同版本的问题。但初次接触时容易分不清两者之间的区别和运作原理，俺昨天折腾了几个小时，现在把经验总结下希望对其他人有帮助。俺用的是Mac book, 版本为10.11.1，Shell：Bash_it, 以下皆在此环境下操作。
 
一般推荐安装pyenv, 再安装其插件 pyenv-virtualenv 这样可以
 
## 安装
 
Mac下安装Pyenv和其插件pyenv-virtualenv很简单，直接参考官方文档，链接见文章末尾。建议使用brew, 省略了一些配置细节。

需要注意的有：
 
1. 在.bash_profile 下加入以下内容,使命令能在shell里自动完成等自动配置功能。
 
```
$ echo eval "$(pyenv init -)"; >> ~/.bash_profile
$ echo eval "$(pyenv virtualenv-init -)"; >> ~/.bash_profile
```
2. 安装完成后重启shell 使配置生效
 
``` $ exec "$SHELL" ```
 
3. 每次安装新的python 版本或包含binary的package执行如下命令：
```$ pyenv rehash```
 
## Pyenv&Virtualenv 简介
 
### Pyenv 作用原理
- shims
Pyenv 安装后会在PATH上插入shims 路径
这样每次执行python相关的可执行文件时会优先在shims里寻找
```~/.pyenv/shims:/usr/local/bin:/usr/bin:/bin```
 
- 选择python版本
当执行shims,pyenv根据如下顺序选择python 的版本:
    - shell 变量设置( 对应命令 pyenv shell)
    - 当前可执行文件目录下的.python_version文件里的版本号 ( 对应命令 pyenv shell)
    - 向上层母目录查询找到的第一个.pyenv-version 文件
    - 全局的版本号在```~/.pyenv/version``` 文件内（对应命令 pyenv global)
 
- 确定版本文件的位置
确定python 版本后确定，pyenv 会根据版本号在```~/.pyenv/versions/ ``` 文件夹查找对应python的版本。pyenv versions 可以看到系统目前安装的python 版本。
 
###pyenv-virtualenv
pyenv-virtualenv的可以为同一版本的python建立不同的虚拟环境。应用场景：同一python版本下需要用到一个package的不同版本, 维持一个相对干净的运行环境。
 
相关操作可参见官方文档
 
 ## 遗留问题
- ```$ echo eval "$(pyenv virtualenv-init -)"; >> ~/.bash_profile``` 
俺按照说明配置如上命令后pyenv-virtualenv后发现它还是不支持auto-active
 
 