# polyChipOff

从网格中提取面（“编辑网格 > 提取”(Edit Mesh > Extract)）时，将创建 polyChipOff 节点。

## 变换属性(Transform Attributes)

#### 平移(Translate)

该值将使挤出的或复制的面沿 X、Y 或 Z 轴移动。

#### 旋转(Rotate)

该值设定角度，需要按该角度绕枢轴的 X、Y 或 Z 轴旋转挤出的或复制的面。

#### 缩放(Scale)

输入一个值，以便沿枢轴的 X、Y 或 Z 轴缩放挤出或复制的面。

#### 枢轴(Pivot)

该值定义平移、旋转和缩放操作居中所围绕的点。

## 多边形碎片禁用历史(Poly Chip Off History)

#### 偏移(Offset)

该值为局部值指定通用偏移。

#### 局部平移(Local Translate)

该值将使挤出或复制的面沿 X、Y 或 Z 轴局部移动。正值或负值表示挤出的或复制的面局部移动的距离。

#### 局部旋转(Local Rotate)

该值设定角度，需要按该角度绕选择的中心的 X、Y 或 Z 轴局部旋转挤出的或复制的面。

#### 局部比例(Local Scale)

该值沿选择的中心的 X、Y 或 Z 轴局部缩放挤出或复制的面。

#### 局部方向(Local Direction)

输入一个值，以便设定局部轴上 X、Y 或 Z 点的位置。请注意，将 Y 方向值更改为 4.0 时，操纵器控制柄如何根据它更改。

![图：输入一个值，以便设定局部轴上 X、Y 或 Z 点的位置。请注意，将 Y 方向值更改为 4.0 时，操纵器控制柄如何根据它…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-096B5B1A-5CF6-432B-A204-50D1936DE4FF.png) <!-- baize:img-hook downloaded=false reason="正文 787 字 ≥300，非承重" -->

#### 随机(Random)

输入一个值，以便向随机方向复制面，值为 0 到 1。下限值更接近指定的方向。较高的值更加随机化。

在以下的示例中，挤出面的随机值为 0、0.5 和 1。

![图：输入一个值，以便向随机方向复制面，值为 0 到 1。下限值更接近指定的方向。较高的值更加随机化。 在以下的示例中，挤出面…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-27889E7F-D100-4466-BD1A-3854135C5D66.png) <!-- baize:img-hook downloaded=false reason="正文 787 字 ≥300，非承重" -->

#### 复制(Duplicate)

启用该属性以复制面而不是提取它们。

#### 保持面的连接性(Keep faces together)

启用该属性时，Maya 单独提取每个面。禁用该选项时，Maya 作为一个整体提取所有面。

#### 世界空间(World space)

启用“世界空间坐标”(World Space Coords)以便在随机更改值时使用世界坐标系。

## 相关主题

- [提取选项(Extract Options)](../“建模”%28Modeling%29菜单集/“编辑网格”%28Edit%20Mesh%29菜单/提取选项%28Extract%20Options%29.md)

- [从网格提取面](../../编辑多边形/合并、分割和拆分/合并和分离多边形网格/从网格提取面.md)
