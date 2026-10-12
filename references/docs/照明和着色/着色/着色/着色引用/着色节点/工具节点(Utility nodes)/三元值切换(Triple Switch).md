# 三元值切换(Triple Switch)

可以使用“切换属性”(Switch Attributes)中的三个按钮向对象中添加、映射纹理或从中移除纹理。[inShape](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-734708F6-0A57-4CF1-ACAB-664AD4A6FB62.htm#WS73099CC142F48755-3D114B7511812357EFE-587A) 列中包含要将工具映射到的对象。[inTriple](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-734708F6-0A57-4CF1-ACAB-664AD4A6FB62.htm#WS73099CC142F48755-3D114B7511812357EFE-5876) 列中包含要映射到对象的纹理、文件或放置节点。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用三元值切换工具](../../../渲染节点工具/使用“三元值切换”%28Triple%20Switch%29工具.md)。

#### 添加曲面(Add Surfaces)

单击以确定“三元值切换”(Triple Switch)工具所连接的着色组并将这些着色组中的所有曲面连接到“三元值切换”(Triple Switch)工具。

#### inShape

包含要连接到“三元值切换”(Triple Switch)工具的形状（对象）的名称。可以在该列中添加任意数量的对象。

在渲染该列中对象之一时，Maya 将“输出”(Output)设定为其相应值。当不渲染任何对象时，Maya 将“输出”(Output)设定为等于[默认](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-193F9C60-FFAD-4BE6-A11F-B11FBB47B4EA.htm#WS73099CC142F48755-3D114B7511812357EFE-589E)设置。

#### inTriple

包含要映射到对象的纹理、文件或放置节点。另请参见[映射项目](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-734708F6-0A57-4CF1-ACAB-664AD4A6FB62.htm#WS73099CC142F48755-3D114B7511812357EFE-5870)。

#### 移除项目(Remove Item)

移除“切换”(Switch)表中的当前选定行。

#### 映射项目(Map Item)

高亮显示“InShape”列，然后单击“映射项目”(Map Item)按钮来选择一个纹理、文件或放置节点以将其映射到对象。

#### 默认(Default)

对于“三元值切换”(Triple Switch)，“默认”(Default)属性表示某种颜色的 RGB 通道。
