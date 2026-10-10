# 与 Adobe After Effects 的实时链接

通过在 Maya 与 Adobe® After Effects® 之间创建实时链接，可以同时在这两个软件中查看场景，以及在 Maya 中执行更改，然后使更改在 After Effects 中实时更新。

兼容元素包括：

- 摄影机（包括“变换”(Transforms)、“焦距”(Focal Length)/“光圈”(Aperture)、“缩放”(Zoom)）

- 聚光灯、点光源和环境光（包括“变换”(Transforms)、“强度”(Intensity)、“颜色”(Color)、“圆锥体”(Cone)）

- 组（转化为 Null 元素）

- 定位器（包括“变换”(Transforms)）

- 平面（若要调整大小，请缩放 1x1 平面。请勿使用“宽度”(Width)/“高度”(Height)）。

- 网格（转化为实体）

导出的数据包括：

- 位置

- 旋转

- 缩放

- 强度、圆锥体角度和颜色（对于灯光）

安装实时链接插件

1. 请确保您对要安装到的系统拥有管理员权限。

2. 从 [Adobe Exchange](https://exchange.adobe.com/creativecloud.details.17593.html#.WLROZ28rJaQ) 下载 **Maya 实时链接**插件。

  Adobe Exchange 将自动提取文件，然后将这些文件复制到位于以下位置的目录中：

  - Windows：..\Program Files (x86)\Common Files\Adobe\CEP\extensions

  - Mac：/Library/Application Support/Adobe/CEP/extensions

设置链接

1. 同时打开 Maya 和 Adobe® After Effects®。

2. 在 After Effects 中，转到“窗口 > 扩展 > Maya 实时链接”(Window > Extensions > Maya Live Link).

3. 在 Maya 中，转到“文件 > Adobe® After Effects® 实时链接”(File > Adobe® After Effects® Live Link)。

4. 单击“链接全部”(Link All)以将所有兼容的场景元素链接到 After Effects，或者使用鼠标中键将特定元素从“大纲视图”(Outliner)拖动到“特定对象”(Specific objects)字段中，然后单击“链接指定对象”(Link Specified)。

  After Effects 会将 Maya 场景加载到其当前合成中。除非链接断开，否则进一步更改 Maya 场景将自动在 After Effects 中更新。

## 相关主题

- [“AE 实时链接”(AE Live Link)窗口](“AE%20实时链接”%28AE%20Live%20Link%29窗口.md)
