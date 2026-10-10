# 关键帧动画和“曲线图编辑器”(Graph Editor)

通过[“曲线图编辑器”(Graph Editor)](../../曲线图编辑器%28Graph%20Editor%29/曲线图编辑器%28Graph%20Editor%29.md)，可以使用关键帧和动画曲线的可视表示形式编辑动画。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-98B5004E-3275-471B-8CFA-461D7298C694.gif) <!-- baize:img-hook downloaded=false reason="正文 1889 字 ≥300，非承重" -->

## 动画曲线

使用“曲线图编辑器”(Graph Editor)可以操纵动画曲线。动画曲线可用于显示关键帧（表示为点）在时间和空间中的移动方式。每个关键帧均具有切线，使您可以控制动画曲线分段如何进入和退出关键帧。

“曲线图编辑器”(Graph Editor)可用作场景视图中的一个面板或一个独立窗口。若要将“曲线图编辑器”(Graph Editor)放置在场景视图中，请选择要在其中显示“曲线图编辑器”(Graph Editor)的场景视图，然后选择“面板 > 面板 > 曲线图编辑器”(Panels > Panel > Graph Editor)。若要将“曲线图编辑器”(Graph Editor)作为独立窗口打开，请选择“窗口 > 动画编辑器 > 曲线图编辑器”(Windows > Animation Editors > Graph Editor)。

“曲线图编辑器”(Graph Editor)仅适用于关键帧和动画曲线，因此某些类型的动画在此处将不可查看。在“曲线图编辑器”(Graph Editor)中，“表达式”(Expressions)和反向运动学不可编辑。

**注**

使用

“显示结果”(Show Results)

可生成无法作为动画曲线进行正常查看的动画的可表示动画曲线。但是，通过

“显示结果”(Show Results)

无法编辑这些曲线。

### Euler 角度过滤

将运动捕捉数据作为动画曲线导入到 Maya 中时，如果将旋转值限制为特定范围，可能会损坏这些曲线。可以通过过滤这些曲线来纠正该损坏问题。

Euler 角度使用三个单独的向量（X、Y 和 Z 轴）计算旋转插值。

在“曲线图编辑器”(Graph Editor)中，选择损坏的动画曲线（例如，“旋转 X”(Rotate X)、“旋转 Y”(Rotate Y)和“旋转 Z”(Rotate Z)），然后选择“曲线 > Euler 过滤器”(Curves > Euler Filter)。过滤始终应用到整个曲线，而不是某段时间内选定的曲线分段。

### 四元数旋转

Maya 提供动画旋转的四元数平滑插值。四元数使用四个向量（X、Y、Z 轴以及一个旋转角度 (W)）计算旋转插值。这样可以防止使用 Euler 角度插值时偶尔遇到的万向锁定和翻转问题。对于想要使用 Euler 插值的情况，Maya 还支持 Euler 角度插值。

四元数曲线是同步的，这意味着 XYZ 曲线上用于确定旋转的关键帧会在时间方向上同时保持锁定状态。在一条曲线上添加、删除或移动关键帧时，也会在相关曲线上更新相应的关键帧。这样可以避免在仅从其中一个轴删除关键帧时，或在时间方向上单独移动顶点时可能发生的意外插值问题。

Maya 还有一个用于创建“同步 Euler”(Synchronized Euler)角度曲线”的选项。在该模式下，关键帧会同时锁定在四元数模式下，但关键帧之间的插值会处于 Euler 角度模式下。

可以使用“曲线图编辑器”(Graph Editor)和“摄影表”(Dope Sheet)中的“曲线 > 更改旋转插值”(Curves > Change Rotation Interp)菜单更改现有曲线的旋转插值类型。请参见[设定曲线的旋转插值](编辑曲线/设定曲线的旋转插值.md)。

不管旋转是四元数还是 Euler 角度，“通道盒”(Channel Box)都会显示 Euler 角度值。

## 在“曲线图编辑器”(Graph Editor)中设置 IK/FK 关键帧曲线

使用“设置 IK/FK 关键帧”在 IK 和 FK 之间（反之亦然）设置动画时，“曲线图编辑器”(Graph Editor)会将 IK 控制柄及其关节的动画曲线显示为一部分实线和一部分虚线。

例如，当显示 IK 控制柄的“平移 X”(Translate X)、“平移 Y”(Translate Y)或“平移 Z”(Translate Z)通道的动画曲线时，该曲线在“IK 融合”(Ik Blend)为 1.000 时显示为实线，在“IK 融合”(Ik Blend)为 0.000 时显示为虚线。换句话说，实线显示的是 IK 控制柄控制关节链动画的位置，虚线显示的是 FK（设定关键帧的关节旋转）控制动画的位置。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-BE64F60E-B471-4241-B24D-8F3207E2AA24.png) <!-- baize:img-hook downloaded=false reason="正文 1889 字 ≥300，非承重" -->

**注**

直接设置

“IK 融合”(Ik Blend)

属性动画不会导致 IK/FK 融合曲线显示为实线/虚线。仅当使用

“设置 IK/FK 关键帧”(Set IK/FK Key)

设置动画通道关键帧时，IK/FK 融合曲线才在曲线视图中显示为实线和虚线。

有关“IK 融合”(Ik Blend)属性或“设置 IK/FK 关键帧”(Set IK/FK Key)的详细信息，请参见 [IK/FK 融合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-05052A96-DBF4-4E91-925F-17244DDA4B9E)以及[“IK/FK 关键帧”(IK/FK Keys)菜单](../../动画引用/动画引用/“动画”%28Animation%29菜单集/“关键帧”%28Key%29菜单/“IKFK%20关键帧”%28IKFK%20Keys%29菜单.md)中的“设置 IK/FK 关键帧”(Set IK/FK Key)。
