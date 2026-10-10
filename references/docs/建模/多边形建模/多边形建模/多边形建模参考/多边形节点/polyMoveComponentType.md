# polyMoveComponentType

“变换组件”(Transform Components)（“编辑网格 > 变换”(Edit Mesh > Transform)）可用于相对于法线变换（移动、旋转或缩放）多边形组件（边、顶点、面和 UV）。通过“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)编辑“polyMoveComponentType”节点（其中 ComponentType 为边、顶点、面或 UV）上的以下属性，可以对变换的组件进行其他修改。

## 变换属性

#### 平移(Translate)

该值会沿 X、Y 或 Z 轴移动组件。

#### 缩放(Scale)

输入值以沿 X、Y 或 Z 轴缩放组件。

#### 旋转(Rotate)

该值设定要围绕 X、Y 或 Z 轴旋转组件的角度。

## 多边形移动组件历史

#### 偏移(Offset)

“偏移”(Offset)选项仅对选定面可用。输入值以偏移变换的面的边。该选项可以用于产生倒角效果。实际上，使用该选项会按统一比例缩放面。

**注**

选定 UV 的选项窗口不包含局部值。

#### 局部平移(Local Translate)

该值会沿 X、Y 或 Z 轴局部移动组件。正值或负值指示会将组件局部移动多远。

**注**

提示：

变换所沿的路径可以垂直于变换的面，或者与变换的面呈任何其他角度。若要沿面法线变换，请将局部值“平移”(Translate)的 Z 值设定为 1，然后单击“移动面”(Move Face)按钮。

#### 局部旋转(Local Rotate)

该值设定要围绕 X、Y 或 Z 轴局部旋转组件的角度。

#### 局部比例(Local Scale)

该值沿 X、Y 或 Z 轴局部缩放组件。

#### 局部方向(Local Direction)

输入值以设定局部轴中 X、Y 或 Z 点的位置。请注意，将 Y 方向值更改为 4.0 时，操纵器控制柄会相应地改变。

![图：输入值以设定局部轴中 X、Y 或 Z 点的位置。请注意，将 Y 方向值更改为 4.0 时，操纵器控制柄会相应地改变。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-A39F775A-C4DD-4D19-837C-94924B15CB43.png) <!-- baize:img-hook downloaded=false reason="正文 785 字 ≥300，非承重" -->

#### 世界空间(World Space)

启用“世界空间”(World Space)设置可在随机更改值时使用世界空间坐标系。有关世界空间坐标的信息，请参见[世界空间、对象空间和局部空间](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A63AC5C8-8822-42AC-827E-164B5266DA03)。
