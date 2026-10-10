# “变换工具”(Transformation Tools)选项

- 若要打开“变换工具”(Transformation Tools)卷展栏，请从主菜单中选择“修改 > 变换工具”(Modify > Transformation Tools)。

设置这些选项可控制变换工具的行为。另请参见[变换对象](../../../../变换对象/变换对象.md)。

## 移动工具、旋转工具、缩放工具

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-88EA6F20-93DA-4B64-9349-B3C8915C98D2.gif) <!-- baize:img-hook downloaded=false reason="正文 3066 字 ≥300，非承重" -->![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-241B356A-FDA7-490E-9E75-D3E1C5C32A99.gif) <!-- baize:img-hook downloaded=false reason="正文 3066 字 ≥300，非承重" -->![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-3E714D59-2B75-4AD5-9451-C8B96BB7DE0A.gif) <!-- baize:img-hook downloaded=false reason="正文 3066 字 ≥300，非承重" -->

使用移动、旋转和缩放工具来变换立方体。

这些菜单项的作用等同于在[工具箱(Tool Box)](../../../../界面概述/界面概述/工具箱%28Tool%20Box%29.md)中单击“移动工具”(Move Tool)（热键 **W**）、“旋转工具”(Rotate Tool)（热键 E）或“缩放工具”(Scale Tool)（热键 **R**）。

单击每个工具旁边的选项框 (![图：单击每个工具旁边的选项框 () 以打开其设置，您可以在其中执行诸多操作，例如，定义要变换的特定轴（X、Y 或 Z）、指定…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3066 字 ≥300，非承重" -->) 以打开其设置，您可以在其中执行诸多操作，例如，定义要变换的特定轴（X、Y 或 Z）、指定枢轴点位置、设置关节方向默认值或保持 UV，以便相应的 UV 随选择一起移动：

- [移动设置](../../../../界面概述/界面概述/工具箱%28Tool%20Box%29/移动工具%28Move%20Tool%29.md)（在“移动”(Move)工具主题中）

- [旋转设置](../../../../界面概述/界面概述/工具箱%28Tool%20Box%29/旋转工具%28Rotate%20Tool%29.md)（在“旋转”(Rotate)工具主题中）

- [缩放设置](../../../../界面概述/界面概述/工具箱%28Tool%20Box%29/缩放工具%28Scale%20Tool%29.md)（在“缩放”(Scale)工具主题中）

## 类型操纵器

使用此操纵器可精确地变换类型对象。有关详细信息，请参见[类型操纵器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-70E9B80D-486E-4F2E-AC57-61FB9EBB4E3D)。

## 通用操纵器

使用此操纵器可精确地移动、旋转或缩放对象。

## 移动法线工具

使用“移动法线工具”(Move Normal Tool)，可以在 NURBS 曲面中沿曲面的 U 或 V 方向移动选定的 CV。这类似于在“移动工具”(Move Tool)中选择“法线”(Normal)选项。

默认情况下，“更新 [UVN] 三轴架”(Update [UVN] Triad)复选框处于选中状态。

其他所有设置与“移动工具”(Move Tool)相同。

## 移动/旋转/缩放工具

在一个操纵器中同时显示移动、旋转和缩放控制柄。

## 显示操纵器工具

显示为选定节点或属性定制的操纵器。请参阅[显示操纵器工具](../../基本工具/显示操纵器工具%28Show%20Manipulator%20Tool%29.md)。

## 默认对象操纵器

这些项允许您对“显示操纵器工具”(Show Manipulator Tool)使用“移动”(Move)、“旋转”(Rotate)或“缩放”(Scale)操纵器，而不是节点的自定义操纵器。

选择“无”(None)可以显示节点的自定义操纵器，而不会显示变换操纵器。这是默认设置。

该信息与场景一同保存。该信息还将显示在变换节点“属性编辑器”(Attribute Editor)中的“显示”(Display)区域。

## 成比例修改工具

可以基于距离操纵器的距离移动组件。

### 修改类型(Modification type)

#### 世界(World)

成比例修改发生在 XYZ 空间。

#### 参数化(NURBS) (Parametric (NURBS))

成比例修改发生在 UV 空间。

### 修改衰减(Modification Falloff)：线性(Linear)

这是默认的修改衰减。Maya 以线性方式进行修改，并显示“距离中止”(Distance Cutoff)选项。

#### 距离中止(Distance Cutoff)

将忽略距离超出此值的对象。该距离是在 3D 中从操纵器控制柄测量的。对于参数化 (NURBS) 修改类型，可以设置“U 向距离中止”(Distance Cutoff U)和“V 向距离中止”(Distance Cutoff V)。

#### 距离基于(Distance Based On)

从操纵器控制柄到对象之间的距离会直接影响修改因子。距离仅沿选定轴进行计算。如果关闭其中任一项，则计算控制柄与点之间的 PropMod 效果时使用的距离会忽略该组件。

### 修改衰减(Modification Falloff)：幂(Power)

使用“成比例修改工具”(Proportional Modification Tool)，可以将次数设置为 +5 至 -5 之间的任意值，并将衰减设置为非线性（形成增长曲线）。但是，如果将次数设置为 1，衰减将回到线性。

#### 距离中止(Distance Cutoff)

将忽略距离超出此值的对象。该距离是在 3D 中从操纵器控制柄测量的。对于参数化 (NURBS) 修改类型，可以设置“U 向距离中止”(Distance Cutoff U)和“V 向距离中止”(Distance Cutoff V)。

#### 次数(Degree)

指定 U 方向和 V 方向上的效果次数。值为 0 时，会将变换应用至整个区域。

正值会减轻远离操纵器控制柄的对象的变换效果；次数越高，衰减效果越强。

如果“次数”(Degree)为负值，则会增强远离操纵器控制柄的对象的变换效果。

#### 距离基于(Distance Based On)

从操纵器控制柄到对象之间的距离会直接影响修改因子。距离仅沿选定轴进行计算。

### 修改衰减(Modification Falloff)：脚本(Script)

此方法使用 MEL 脚本来确定衰减。

使用适当的参数集，选择“脚本”选项并在“用户定义脚本”(User Defined Script)框中键入设置命令，就可以保存当前参数设置，无需实际调用该函数。如果希望以后再次使用这些设置，可以从“引用编辑器”(Reference Editor)获取该工具脚本。

#### 用户定义脚本(User Defined Script)

脚本应返回修改因子。输入脚本的是“浮点”编号。前三项表示操纵器控制柄的位置。接下来的三项表示操纵点的位置。例如，此脚本返回 1 的点与操纵器控制柄一起移动。此脚本返回 0.5 的点以操纵器控制柄速度的一半进行移动。

### 修改衰减(Modification Falloff)：曲线(Curve)

此选项使用动画曲线创建衰减。动画曲线轮廓可用于生成修改因子。

#### 动画曲线 (Anim. Curve)

输入现有动画曲线的名称。其垂直方向映射至修改因子。距离映射至动画曲线时间轴（以秒为单位）。

可以使用框右侧的下拉列表列出名称以 propModAnimCurve 开头的全部动画曲线，并从中进行选择。也可以从同一下拉列表中选择“新建”(Create New)，新建动画曲线。

#### U 向比例(Scale U)，V 向比例(Scale V)

仅适用于“参数化(NURBS)修改”(Parametric (NURBS)Modification)类型。

#### 距离基于(Distance Based On)

从操纵器控制柄到对象之间的距离会直接影响修改因子。距离仅沿选定轴进行计算。

### 修改衰减(Modification Falloff)：NURBS 曲线(NURBS Curve)

仅适用于“世界修改”(World Modification)类型。此选项使用“NURBS 曲线”(NURBS curve)创建衰减。“NURBS 曲线”(NURBS curve)轮廓可用于生成修改因子。

输入现有“NURBS 曲线”(NURBS curve)的名称。其垂直方向映射至修改因子。距离映射至“NURBS 曲线”(NURBS curve)。

可以使用框右侧的下拉列表列出全部 NURBS 曲线，并从中进行选择。

### 使用 PropMod 脚本

PropMod 脚本类似于“移动”脚本，不同之处在于前者对于移动距离具有附加设置。使用“脚本”选项，可以分别计算每个对象的因子。

用户定义的脚本命令将使用操纵器和对象二者的位置。脚本返回的值将用作具体对象的倍增因子。

#### 示例

创建 myPropMove.mel 文件，如：

```text
global proc float myPropMove
 (float $mx, float $my, float $mz,
 float $px, float $py, float $pz)
{
float $value = rand (1.0);
return $value;
}
```

...可以产生介于 0 到 1 之间的随机值。

如果选择 myPropMove 作为脚本名称，将获得一个所有选定点都使用的随机修改因子。

## 软修改工具

可以通过平滑推拉顶点组修改曲面。您可以设置选项来控制曲面绕移动的顶点变形的清晰度或平滑度。有关详细信息，请参见[软修改(Soft Modification)选项](../../基本工具/软修改工具%28Soft%20Modification%20Tool%29/软修改%28Soft%20Modification%29选项.md)。
