# 使用 MEL 命令保存和加载流水线缓存

## Alembic 缓存

可以使用 AbcImport 和 AbcExport MEL 命令导入和导出 Alembic 文件。例如，使用以下命令导出多边形圆环：

AbcExport -j "-frameRange 1 120 -root pTorus1 -file c:/temp/test.abc";

可以使用 AbcExport -h; 和 AbcImport -h;，在“脚本编辑器”(Script Editor)中查看有关这些命令的帮助信息。

## GPU 缓存

您可以使用以下命令导出 GPU 缓存。

- 若要缓存一个对象，请使用以下命令：

  gpuCache -f filename dagObject

- 若要将所选对象缓存到单个文件，请使用以下命令：

  gpuCache -directory "/dest/path" -fileName "filename" -saveMultipleFiles false [object1 object2 ....]

  result: /dest/path/filename.abc

- 若要将所选对象缓存到多个文件，请使用以下命令：

  gpuCache -directory "/dest/path" -filePrefix "ddd_" -clashOption nodeName [object1 object2 ...]

  result: /dest/path/ddd_object1.abc, /dest/path/ddd_object2.abc, ...

缓存多个对象或文件时，您可以使用 -prompt 标志在覆盖现有文件时显示警告消息。

对于 GPU 缓存，没有输入命令。但是，您可以创建 gpuCache 节点，并设定缓存文件名称和路径的属性。例如：

createNode -n "mine" gpuCache;

setAttr -e -type "string" mine.cacheFileName "dd.abc";

setAttr -e -type "string" mine.cacheGeomPath "|"; // eg the root.

在“脚本编辑器”(Script Editor)中使用 help gpuCache; 可获得关于 gpuCache 命令的帮助。

## 相关主题

- [Alembic 缓存](../Alembic%20缓存.md)

- [关于 Alembic 缓存](关于%20Alembic%20缓存.md)

- [关于 GPU 缓存](关于%20GPU%20缓存.md)
