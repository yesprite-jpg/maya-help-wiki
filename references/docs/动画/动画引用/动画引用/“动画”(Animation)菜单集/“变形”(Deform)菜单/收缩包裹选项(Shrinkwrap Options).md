# 收缩包裹选项(Shrinkwrap Options)

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)收缩包裹”(Deform > (Create) ShrinkWrap) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)收缩…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1432 字 ≥300，非承重" -->

#### 投影(Projection)

下列投影方法确定如何将包裹器对象的每个点投影到目标对象：

#### 朝向内部对象(Toward Inner Object)

朝向内部对象进行收缩包裹。朝向内部对象投影包裹器对象的每个点，直到其碰到目标的曲面。

#### 朝向中心(Toward Center)

朝向目标的中心进行收缩包裹。朝向目标的中心投影包裹器对象的每个点，直到其碰到目标的曲面。

#### 平行于轴(Parallel To Axes)

沿轴收缩包裹。沿平行于轴的方向投影包裹器对象的每个点，直到其碰到目标的曲面。

#### 顶点法线(Vertex Normals)

沿法线收缩包裹。沿法线方向的反向投影包裹器对象的每个点，直到其碰到目标的曲面。例如，该方法可用于将皮带收缩包裹到角色，而无需担心对象中心的位置。

#### 最近(Closest)

收缩包裹到目标曲面上的最近点。

#### 如果没有交点，则用最近点(Closest If No Intersection)

启用此选项时，Maya 将为未使用当前选定的投影方法碰到目标对象的点使用“最近”(Closest)投影方法。此选项可确保包裹器对象的所有点都变为目标形状。

#### 双向(Bidirectional)

启用此选项后，会向后和向前投影包裹器对象的点，以查看它们是否碰到目标对象。如果某个点在两个方向上都碰到目标，则会使用最短距离。

#### 反转(Reverse)

启用此选项后，会在相反的方向上投影包裹器对象上的点。例如，该选项可用于沿某个轴的负方向投影包裹器。

#### 偏移(Offset)

指定发生变形后包裹器对象与其目标之间的距离。如果增大“偏移”(Offset)值，Maya 会沿目标的曲面法线移动包裹器的点。

**注**

提示：

可以使用

“偏移”(Offset)

修复包裹器和目标之间的穿透。

#### 目标膨胀(Target Inflation)

指定沿其曲面法线应用到目标对象的膨胀量。

虽然“目标膨胀”(Target Inflation)和[“偏移”(Offset)](收缩包裹选项%28Shrinkwrap%20Options%29.md#GUID-832864E7-A266-4EA8-92A1-7D570759D74E__GUID-22EBF644-C9A7-4D87-86C5-F54EBE6AE417)会产生类似的效果，但“目标膨胀”(Target Inflation)通常会生成更好的变形，尽管会耗费一些额外的计算成本。

#### 边界框中心(Bounding Box Center)

如果禁用此选项（默认设置），会朝向目标的局部坐标系的中心投影包裹器对象的点。启用此选项时，会朝向目标的边界框的中心投影包裹器对象的点。

**注**

该选项仅在

“投影”(Projection)

设置为

“朝向中心”(Toward Center)

时可用。

#### 轴参照(Axis Reference)

设置参考坐标系。您可以从“目标局部”(Target Local)、“变形局部”(Deformed Local)和“全局”(Global)中选择。

**注**

该选项仅在

“投影”(Projection)

设置为

“平行于轴”(Parallel To Axes)

时可用。

#### 沿 X、Y、Z (Along X, Y, Z)

指定沿哪个轴投影包裹器的点。如果选定多个轴，投影会沿相应的单位向量发生。

**注**

该选项仅在

“投影”(Projection)

设置为

“平行于轴”(Parallel To Axes)

时可用。

#### 单个收缩包裹节点(Single Shrinkwrap Node)

启用此选项后，可将所有收缩包裹对象视为单个收缩包裹节点。执行此操作可在整个组内应用同一设置。

## 相关主题

- [收缩包裹变形器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C2D83E32-2D69-478A-B159-6E1005480378)

- 变形 > [收缩包裹](../“变形”%28Deform%29菜单.md#GUID-C1B5085D-3229-4BE8-989E-95C460ADB79C__GUID-920BDC7C-D1BA-485B-8A76-4A1822F8D303)(Deform > ShrinkWrap)
