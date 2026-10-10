# “替换字符串”(Replace String)工具

针对在“文件路径编辑器”(File Path Editor)浏览器中选定的元素执行搜索和替换操作。该功能仅更改 Maya 中的属性和路径。磁盘上的文件不受“替换字符串”(Replace String)工具所做的更改影响。

#### 受影响的字符串(Affected String)

确定受“替换字符串”(Replace String)工具影响的字符串。从下列选项中进行选择：

##### 节点名称(Node Name)

搜索与在浏览器列表中选定的元素相关的节点名称。

##### 目录路径(Directory Path)

搜索与在浏览器列表中选定的元素相关的目录路径。实际文件名不受影响。

##### 文件名(Filename)

搜索与在浏览器列表中选定的元素相关的文件名。

##### 完整的文件路径(Full FilePath)

搜索与在浏览器列表中选定的元素相关的目录路径和文件名。

##### 全部(All)

搜索与在浏览器列表中选定的元素相关的节点名称、文件名和文件路径。

#### 搜索字符串(Search String)

搜索并替换的字符串。

**注**

“搜索字符串”(Search String)

是区分大小写的。

#### 替换字符串(Replace String)

替换“搜索字符串”(Search String)文本的字符串。

#### 替换第一个实例(Replace First Instance)

当运行“替换字符串”(Replace String)时，仅搜索字符串的第一个实例将被替换。

例如，如果要将字符串 Beast 替换为 Spaceman，且已选中“替换第一个实例”(Replace First Instance)，则字符串 C:/Assets/Beast/Beast_Files/model.ma 将变为 C:/Assets/Spaceman/Beast_Files/model.ma。

#### 替换所有实例(Replace Every Instance)

当运行“替换字符串”(Replace String)时，搜索字符串的所有实例将被替换。

例如，如果要将字符串 Beast 替换为 Spaceman，且已选中“替换所有实例”(Replace Every Instance)，则字符串 C:/Assets/Beast/Beast_Files/model.ma 将变为 C:/Assets/Spaceman/Spaceman_Files/model.ma。

#### 替换(Replace)

使用“替换字符串”(Replace String)窗口的参数执行搜索和替换操作。

#### 预览(Preview)

打开[操作预览窗口](“重新指定路径”%28Repath%29和“操作预览”%28Actions%20Preview%29窗口.md#GUID-283EDDAB-F763-41E4-B5E4-CE7C9E0761CB__SECTION_E50ED99D475E4541A62CCEA1EBE8E1CE)，可以在执行操作之前预览搜索和替换操作的结果。

#### 取消(Cancel)

取消搜索和替换操作，并关闭“替换字符串”(Replace String)工具。
