# macOS 版 Maya 疑难解答

以下部分介绍了 macOS 版 Maya 独有的一些问题，并提供了建议解决方法。

## 在项目文件夹中以项目符号字符开头的文件夹导致 Maya 无法启动

如果 /Users/username/Documents/maya/projects 中存在名称中包含项目符号字符（选项 8）的文件夹，则 Maya 不会保留项目的设置。下次 Maya 运行时它将返回到默认。

### 解决方法

移除有问题的文件夹或对其进行重命名，然后重新启动 Maya。
