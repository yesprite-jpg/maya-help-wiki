# 四元值切换(Quad Switch)

您可以使用“切换属性”(Switch Attribute)中的三个按钮对对象进行添加、删除和映射纹理操作。[inShape](三元值切换%28Triple%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-587A) 列中包含工具要映射到的对象。[inQuad](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-75768B55-D9B5-4474-A70D-D0C5A0B2A1E9.htm#WS73099CC142F48755-3D114B7511812357EFE-5859) 列中包含要映射到对象的纹理、文件或放置节点。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用四元值切换工具](../../../渲染节点工具/使用“四元值切换”%28Quad%20Switch%29工具.md)。

#### 添加曲面(Add Surfaces)

单击以确定“四元值切换”(Quad Switch)工具与哪些着色组连接，并将这些着色组中的所有曲面连接到“四元值切换”(Quad Switch)工具。

#### 移除项目(Remove Item)

移除“切换”(Switch)表中的当前选定行。

#### 映射项目(Map Item)

选择“InShape”列，然后单击“映射项目”(Map Item)，以便选择纹理、文件或放置节点以映射到对象。

#### inShape

包含要连接到“四元值切换”(Quad Switch)工具的形状（对象）名称。您可以将任意数量的对象添加到该列中。

在渲染该列中对象之一时，Maya 将“输出”(Output)设定为其相应值。未渲染任何对象时，Maya 会将“输出”(Output)设定为等于[默认](单值切换%28Single%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-589E)设置。

#### inQuad

包含要映射到对象的纹理、文件或放置节点。另请参见[映射项目](三元值切换%28Triple%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-5870)。

#### 默认(Default)

对于“四元值切换”(Quad Switch)，“默认”(Default)属性表示颜色的 RGB 通道。
