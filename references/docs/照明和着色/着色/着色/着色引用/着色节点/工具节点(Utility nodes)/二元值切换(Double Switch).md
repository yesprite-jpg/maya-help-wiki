# 二元值切换(Double Switch)

可以使用“切换属性”(Switch Attribute)中的三个按钮来添加纹理、移除纹理以及将纹理映射到对象。

[inShape](三元值切换%28Triple%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-587A) 列包含工具要映射到的对象。

[inDouble](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-44394C98-7A39-45F1-9053-2277FEBC50AC.htm#WS73099CC142F48755-3D114B7511812357EFE-588E) 列包含要映射到对象的纹理、文件或放置节点。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用二元值切换工具](../../../渲染节点工具/使用“二元值切换”%28Double%20Switch%29工具.md)。

## 添加曲面(Add Surfaces)

单击以确定“二元值切换”(Double Switch)工具要连接到的着色组，并将这些着色组中的所有曲面连接到“二元值切换”(Double Switch)工具。

#### inShape

包含要连接到“二元值切换”(Double Switch)工具的形状（对象）的名称。可以向该列中添加任意数量的对象。

在渲染该列中对象之一时，Maya 将“输出”(Output)设定为其相应值。如果不渲染任何对象，Maya 会将“输出”(Output)设定为等于[默认](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-193F9C60-FFAD-4BE6-A11F-B11FBB47B4EA.htm#WS73099CC142F48755-3D114B7511812357EFE-589E)设置。

#### inDouble

包含要映射到对象的纹理、文件或放置节点。另请参见[映射项目](三元值切换%28Triple%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-5870)。

#### 移除项目(Remove Item)

移除“切换”(Switch)表中的当前选定行。

#### 映射项目(Map Item)

亮显“InShape”列，然后单击“映射项目”(Map Item)按钮以选择要映射到对象的纹理、文件或放置节点。

**注**

提示：

可以在该列单击鼠标右键，然后从弹出菜单中选择“贴图”(Map)。

#### 默认(Default)

对于二元值切换，“默认”(Default)值表示两个浮点值（例如，place2dTexture 工具的“平移帧”(Translate Frame)或“UV 向重复”(Repeat UV)值）。
