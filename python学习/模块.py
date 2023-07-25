##Python 模块
##Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
#模块让你能够有逻辑地组织你的 Python 代码段。
#把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
#模块能定义函数，类和变量，模块里也能包含可执行的代码。
def print_func( par ):
   print("Hello : ", par)
   return
##模块的引入
#列举：import module1[, module2[,... moduleN]]
##比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时，必须这样引用：
##模块名.函数名
# 导入模块
import support
 # 现在可以调用模块里包含的函数了
support.print_func("Runoob")
##>>>Hello : Runoob