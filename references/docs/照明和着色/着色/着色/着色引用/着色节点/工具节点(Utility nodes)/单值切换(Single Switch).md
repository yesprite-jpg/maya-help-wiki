# 单值切换(Single Switch)

可以使用“切换属性”(Switch Attributes)区域中的单个按钮向对象添加、移除并映射纹理。

[inShape](三元值切换%28Triple%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-587A) 列中包含工具将要映射的对象。

[inSingle](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-193F9C60-FFAD-4BE6-A11F-B11FBB47B4EA.htm#WS73099CC142F48755-3D114B7511812357EFE-58A8) 列中包含将要映射到对象的纹理、文件或放置节点。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用单值切换工具](../../../渲染节点工具/使用“单值切换”%28Single%20Switch%29工具.md)。

#### 添加曲面(Add Surfaces)

单击以确定“单值切换”(Single Switch)工具所连接的着色组，并将这些着色组中的所有曲面连接到“单值切换”(Single Switch)工具。

#### inShape

包含要连接到“单值切换”(Single Switch)工具的形状（对象）的名称。可以在该列中添加任意数量的对象。

在渲染该列中对象之一时，Maya 将“输出”(Output)设定为其相应值。在不渲染任何对象时，Maya 将“输出”(Output)设定为等于[默认](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-193F9C60-FFAD-4BE6-A11F-B11FBB47B4EA.htm#WS73099CC142F48755-3D114B7511812357EFE-589E)设置。

#### inSingle

包含要映射到对象的纹理、文件或放置节点。另请参见[映射项目](三元值切换%28Triple%20Switch%29.md#WS73099CC142F48755-3D114B7511812357EFE-5870)。

#### 移除项目(Remove Item)

移除“切换”(Switch)表中的当前选定行。

## 映射项目(Map Item)

亮显“inShape”列，然后单击“映射项目”(Map Item)按钮来选择纹理、文件或放置节点以将其映射到对象。

**注**

提示：

也可以将光标放在列上，然后在弹出菜单的“贴图”(Map)上单击鼠标右键。

#### 默认(Default)

对于“单值切换”(Single Switch)而言，“默认”(Default)属性代表单个浮点值（例如，材质凹凸贴图属性的“凹凸深度”(Bump Depth)）。在对表面进行着色时，如果其不在“inShape” 列中，则使用该值。着色节点也可以映射到“默认”(Default)。
