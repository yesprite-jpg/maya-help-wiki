# “重新指定路径”(Repath)和“操作预览”(Actions Preview)窗口

## “重新指定路径”(Repath)窗口

可以更改现有文件路径以指向其他位置。

#### 新路径(New path)

Maya 查找正在重新指定路径的文件的目录。可以手动输入路径，将路径粘贴到场中，或单击“浏览”(Browse)以导航到新位置。默认情况下，“新路径”(New path)最初设置为 Maya 的当前工作目录。如果准备场景以供具有不同目录结构或平台的其他人使用，则可以为不存在的文件指定路径。

**注**

要重新指定引用节点的路径，则目标文件必须存在。与

“文件路径编辑器”(File Path Editor)

中的其他节点类型不同，无法重新指定不存在文件的引用节点的路径。

#### 在子目录中搜索文件(Search Subdirectories for Files)

如果启用，Maya 将从子目录到指定的“新路径”(New Path)中进行搜索，直到查找到文件的第一个实例。

#### 重新指定当前已解析文件的路径(Repath Currently Resolved Files)

如果启用，Maya 还会尝试重新指定选择中包括的任何已解析文件的路径。

#### 重新指定路径(Repath)

执行重新指定路径操作，并关闭“重新指定路径”(Repath)窗口。

#### 预览(Preview)

打开“操作预览”(Actions Preview)窗口。请参见[“操作预览”(Actions Preview)窗口](“重新指定路径”%28Repath%29和“操作预览”%28Actions%20Preview%29窗口.md#GUID-283EDDAB-F763-41E4-B5E4-CE7C9E0761CB__SECTION_E50ED99D475E4541A62CCEA1EBE8E1CE)。

#### 取消(Cancel)

取消重新指定路径操作，并关闭“重新指定路径”(Repath)窗口。

## “操作预览”(Actions Preview)窗口

可以在执行重新指定路径操作之前预览其结果。

#### 摘要(Summary)

列出重新指定路径操作导致的将新解析的路径数量和仍保持未解析的路径数量。

#### 细节(Details)

列出关于重新指定路径操作的详细信息，包括将解析的文件的名称、保持未解析的文件的名称和新解析文件的位置。

#### 继续(Continue)

执行重新指定路径操作，并关闭“操作预览”(Actions Preview)窗口。

#### 取消(Cancel)

取消重新指定路径操作，并关闭“操作预览”(Actions Preview)窗口。

## 相关主题

- [管理文件路径](管理文件路径.md)
