# 创建动画扫描选项(Create Animated Sweep Options)

- 在“动画”(Animation) [菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129) (**F4**) 中：“可视化 > 创建动画扫描”(Visualize > Create Animated Sweep) > ![图：在“动画”(Animation) 菜单集 (F4) 中：“可视化 创建动画扫描”(Visualize Create An…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 576 字 ≥300，非承重" -->

### 时间范围(Time Range)

设置下列选项之一：

#### 时间滑块(Time Slider)

创建由时间滑块长度定义的时间长度动画扫描。

#### 开始/结束(Start/End)

用于为动画扫描设置一个特定的“开始时间”(Start time)和“结束时间”(End Time)。

#### 按时间(By Time)

对动画求值，并为每个“按时间”(By Time)位置创建几何体。

### 参数化(Parameterization)

设置下列选项之一：

#### 一致(Uniform)

使剖面曲线平行于 V 方向。在 U 方向生成的曲面的参数值间距相等。第一条剖面曲线对应于 U[0] 处曲面的等参线，第二条对应于 U[1] 处等参线，依此类推。

#### 弦长(Chord Length)

导致 U 方向上生成曲面的参数值基于剖面曲线的开始点之间的距离。

### 曲面次数(Surface Degree)

将 U 方向的放样曲面设置为线性或立方。

#### 线性(Linear)

创建显示为面的曲面。

#### 立方(Cubic)

创建平滑曲面。

#### 表面(Surface)

指定是否创建开放或闭合曲面。详细信息请参见[使曲线或曲面开放或闭合](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-17B86448-0237-4369-AB7A-8F381FEAACA7)。

#### 输出几何体(Output Geometry)

指定所创建几何体的类型。可以在“NURBS”或“多边形”(Polygons)中做出选择。
