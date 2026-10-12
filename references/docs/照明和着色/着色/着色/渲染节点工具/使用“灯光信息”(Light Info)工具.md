# 使用“灯光信息”(Light Info)工具

有关“灯光信息”(Light Info)工具的描述，请参见[灯光信息](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B28C5B86-685B-471B-8C03-D8AF27462DD6.htm)。

查看“灯光数据”(Light Data)属性并将其连接到“灯光信息”(Light Info)属性

1. 在场景中创建了灯光之后，从“Hypershade”菜单栏中选择“灯光”(Lights)，以在“Hypershade”中查看 LightShape 样例。

2. 从“创建 > 工具”(Create > Utilities)菜单选择“灯光信息”(Light Info)。

3. 按住 Ctrl 和鼠标中键的同时在“灯光信息”(Light Info)样例上拖动 LightShape 样例。将出现“连接编辑器”(Connection Editor)。

4. 在“左侧显示”(Left Display)菜单中，确保启用“显示可读项”(Show Readable)。在“右侧显示”(Right Display)菜单中，确保启用“仅显示输入”(Show Inputs Only)。

5. 单击以将 LightShape 的“世界矩阵”(World Matrix)[0] 属性连接到“灯光信息”(Light Info)节点的“世界矩阵”(World Matrix)属性。

  请注意添加到“灯光信息”(Light Info)的“属性编辑器”(Attribute Editor)顶部的灯光选项卡。单击该选项卡可访问灯光的信息，并可调整这些值以在 X、Y 和 Z 方向上平移和更改灯光。

  也可以从“连接编辑器”(Connection Editor)选择任一“灯光数据”(Light Data)属性。“灯光数据”(Light Data)属性包括灯光方向、灯光强度、灯光环境光、灯光漫反射、灯光镜面反射和灯光阴影分数。

6. 从列表中选择要连接的属性。

使用该信息作为其他着色节点的输入以产生有趣的效果。例如，如果将“采样距离”(Sample Distance)属性连接到材质的其中一种颜色属性，则根据它距离灯光的远近，颜色会发生改变。

**注**

可以将任何对象（不仅仅是灯光）的“世界矩阵”(World Matrix)附加到该节点，以获取有关对象相对于正进行着色的点的位置的信息。
