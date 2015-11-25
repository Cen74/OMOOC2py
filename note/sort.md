## 积累

### Lambda

Lambda 是匿名函数，用在只用需要一个函数但又不想费力命名的时候

```
map( lambda x: x*x, [y for y in range(10)] )
```

好过：
```
def sq(x):
    return x * x
map(sq, [y for y in range(10)])
```

>「遍历列表，给遇到的每个元素都做某种运算」的过程从一个循环里抽象出来成为一个函数 map，然后用 lambda 表达式将这种运算作为参数传给 map 的话，考虑事情的思维层级会高出一些来