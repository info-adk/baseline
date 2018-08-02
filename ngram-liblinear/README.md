 
 Liblinear使用过程中出现了很多问题，花了很长时间才解决
 
 1.pycharm中通过第三方库安装的liblinear后导入包失败
	<br>原因：未知
 
 2.手动下载安装的包在pycharm无法导入，但是从终端进入python却可以import liblinear并使用
   <br>原因：安装的位置是自定义的而非dist-packages中
   解决方法：打开pycharm，点击 File -> Settings -> Project Interpreter -> 右上角设置 -> more -> 选择解释器版本 
   -> 点击右边最后一个图标 -> 点“+”添加安装包的自定义路径 (到python目录下，eg: liblinear-2.20/python)
	
 3.此时import liblinear成功了，但是很多函数无法使用
     <br>原因：发现liblinear.py 文件确实没定义这些函数
     <br>解决方法: 同一个文件夹下还有liblinearutil.py，内部函数定义齐全，所以改用 import liblinearutil
