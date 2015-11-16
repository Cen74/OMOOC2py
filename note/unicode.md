
Python 中文处理经常会遇到encode, decode 函数，但两者的概念容易混淆。

##简介
- encode( code ) -encode from unicode to bytes.
将一个uni object 转化为指定code编码方式的字节流, 默认为assii
- decode(code ) - decode from bytes to unicode
将字节流（编码方式code)转化为uni object 

##例子
```
>>> y = u'中文'  # y 是'中文' uni object
'>>> y
u'\u4e2d\u6587'

>>> y_utf_str = y.encode('utf-8')  # 将‘中文’ (uni object) 变化为按utf-8编码方式的字符串
>>> y_utf_str
'\xe4\xb8\xad\xe6\x96\x87'

>>> x = '中文'
>>> x
'\xd6\xd0\xce\xc4'      #win10 下'中文‘的编码方式与上面明显不符，是gb2312编码方式

# 如何让中文按utf-8编码方式传输
>>> x_utf = x.decode('gb2312').encode('utf-8')  # 将gb2312编码方式的bytes转化为utf-8编码方式的byte
>>> x_utf
'\xe4\xb8\xad\xe6\x96\x87'

```
- 另外一种解决中文编码方式的方式是将系统默认编码方式设置为'utf-8'
```
# sys.setdefaultencoding() does not exist, here!import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
```

## Refernce 
['assii code cannot decode byte'](http://stackoverflow.com/questions/9644099/python-ascii-codec-cant-decode-byte)
