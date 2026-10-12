# 环境雾(Environment Fog)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A9E44E40-43A8-46AC-8481-F19EB93B3125.png) <!-- baize:img-hook downloaded=false reason="正文 5606 字 ≥300，非承重" -->

模拟空气中精细粒子（雾、烟或灰尘）的效果。这些粒子影响大气的外观以及大气中对象的外观。若要模拟特定灯光照明的空气中粒子，请使用“灯光雾”(Light Fog)（请参见[灯光雾](灯光雾%28Light%20Fog%29.md)）。

有两种“环境雾”(Environment Fog)类型：“简单雾”(Simple Fog)（默认）和“物理雾”(Physical Fog)，各自都具有特定属性。

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

**注**

注意：

环境雾无法投射阴影。如果想要投射阴影，请使用“灯光雾”(Light Fog)（请参见[灯光雾](灯光雾%28Light%20Fog%29.md)）。请参见“蒙版不透明度”(Matte Opacity)。

## 简单雾(Simple Fog)

#### 颜色(Color)

更改以模拟不同效果，如烟雾（棕色雾），或创建远距离幻象（蓝雾）。默认设置为白色。

#### 基于颜色的透明度(Color Based Transparency)

如果禁用，由环境雾遮蔽的对象显示为平面着色轮廓。如果启用，由环境雾遮蔽的对象将完全着色，而不仅仅是平面着色轮廓。

如果雾“颜色”(Color)很深（黑色），则禁用“基于颜色的透明度”(Color Based Transparency)，否则雾将不可见。默认情况下，“基于颜色的透明度”(Color Based Transparency)处于启用状态。

#### 饱和度距离(Saturation Distance)

离开环境雾完全饱和的摄影机（其颜色值达到“颜色”(Color)设置）的距离（按场景的线性工作单位测量）。“饱和度距离”(Saturation Distance)对被遮蔽雾内部或后方对象的影响程度。滑块范围为 0.001 到 200。默认值为 100。

若要更改雾内部或后方对象的遮蔽量，请调整“饱和度距离”(Saturation Distance)属性和“颜色”(Color)属性的值。

#### 使用层(Use Layer)

如果启用，则可以将纹理指定给“层”(Layer)属性，从而创建环境雾在摄影机视图上（即两个维度中）的密度和颜色变化。如果禁用，恒定密度环境雾将填充摄影机视图。默认情况下，“使用层”(Use Layer)处于禁用状态。

#### 层(Layer)

可以将纹理映射到雾，使雾的密度具有斑块效果。最常用的应用程序是将“密度”(Density)映射到 3D 纹理，如“匀值分形”(Solid Fractal)和将“渐变”(Ramp)纹理映射到“层”(Layer)属性。将“渐变”(Ramp)设为黑色和白色，以获得透明度和不透明度的对比度。默认情况下，“使用层”(Use Layer)处于禁用状态。

#### 使用高度(Use Height)

如果启用，环境雾介于“最小高度”(Min Height)和“最大高度”(Max Height)之间。如果禁用，环境雾将填充摄影机视图。默认情况下，“使用高度”(Use Height)处于禁用状态。

#### 最小高度(Min Height)、最大高度(Max Height)

（“使用高度”(Use Height)处于启用状态时）距离环境雾所在原点的最小高度和最大高度（按场景的线性工作单位测量）。如果“最大高度”(Max Height)小于最小高度”(Min Height)，则环境雾将从最小高度”(Min Height)延伸到无穷大。滑块范围为 -10 到 10。“最小高度”(Min Height)的默认值为 -1，而“最大高度”(Max Height)的默认值为为 1。

#### 融合范围(Blend Range)

环境雾从完全密度逐渐衰减到零密度的垂直距离（按场景的线性工作单位测量）。（雾的边缘由“最小高度”(Min Height)值和“最大高度”(Max Height)值定义。）滑块范围是 0（雾在“最小高度”(Min Height)和“最大高度”(Max Height)处突然结束）到 1（雾在“最小高度”(Min Height)和“最大高度”(Max Height)处逐渐衰减）。默认值为 0。

## 物理雾(Physical Fog)

若要访问“物理雾”(Physical Fog)属性，必须启用它（单击“属性编辑器”(Attribute Editor)中样例下的复选框）。

#### 雾类型(Fog Type)

控制 Maya 如何模拟场景中的雾。它具有多个不同设置，取决于想要的雾效果类型。该属性仅在“物理雾”(Physical Fog)处于启用状态时可用。

#### 一致雾(Uniform Fog)

雾在所有方向上具有一致的密度。

#### 大气(Atmospheric)

雾在地面附近最厚，在向上移动过程中变薄（衰退）。

#### 天空(Sky)

模拟整个天空的效果，雾在地平线上正确融合，依此类推。使用该选项，为雾场景提供完整背景。该选项对于可看见远距离的场景尤其有用。

#### 水(Water)

模拟水的效果，散射灯光从上方照射进来。对于水下快照非常有用，或者从上方可以看到池水中对象的快照。

#### 水/雾(Water/Fog)

“一致雾”(Uniform Fog)出现在场景中水的上方。

#### 水/大气(Water/Atmos)

大气雾(Atmospheric Fog)出现在场景中水的上方。

#### 水/天空(Water/Sky)

完全“天空雾”(Sky Fog)模拟出现在场景中水的上方。

#### 雾轴(Fog Axis)

将雾模拟使用的方向控制为向上方向。可以任意选择正方向或负方向上的 X、Y 或 Z 轴。

该属性仅在启用“物理雾”(Physical Fog)，并且“雾类型”(Fog Type)不“一致”(Uniform)时可用。

#### 环境半径(Planet Radius)

可用于大气(Atmospheric)、天空(Sky)、“水/大气”(Water/Atmos)和水/天空雾类型(Sky Fog Types)。

### 雾(Fog)

根据选择的[雾类型](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-A88206BD-28F0-404A-92EB-DD7F929986C8.htm#WS73099CC142F48755-3D114B7511841AEFA9F207F)、“雾”(Fog)属性既可启用，也可禁用。

#### 雾颜色(Fog Color)

控制雾散射的灯光颜色。当灯光穿过空气或雾时，某些频率（颜色）直接穿过，而其他频率发生散射。散射的频率使得雾具有其独特的颜色。

#### 雾不透明度(Fog Opacity)

控制哪些灯光频率（颜色）在通过雾时被吸收。这将影响背景中对象被雾染色的方式。

#### 雾密度(Fog Density)

控制雾层中水汽的光学密度。增加该值以加厚雾。

#### 雾最小高度(Fog Min Height)

控制雾层底部的高度。*该属性仅在启用*“物理雾”(Physical Fog)*，并且*“雾类型”(Fog Type)*不*“一致”(Uniform)时可用。

#### 雾最大高度(Fog Max Height)

控制雾层的高度。如果“雾类型”(Fog Type)为“大气”(Atmospheric)（或“水/大气”(Water/Atmos)），则雾的密度从“雾最小高度”(Fog Min Height)向上指数递减。如果“雾类型”(Fog Type)为“天空”(Sky)（或“水/天空”(Water/Sky)），则“雾最大高度”(Fog Max Height)为雾层顶部的高度。*该属性仅在启用*“物理雾”(Physical Fog)*，并且*“雾类型”(Fog Type)*不*“一致”(Uniform)时可用。

#### 雾衰退(Fog Decay)

“雾衰退”(Fog Decay)控制雾在较高海拔高度变薄的速率。值为 0.5 时，会使雾线性衰退。值介于 0.5 到 1 之间时，会使雾在地面附近相当均匀，然后在顶部突然衰减。值介于 0 到 0.5 之间时，会使雾在其基底附近非常快地变薄。*该属性仅在启用*“物理雾”(Physical Fog)*，并且*“雾类型”(Fog Type)*不*“一致”(Uniform)时可用。

#### 雾灯光散射(Fog Light Scatter)

控制灯光在雾中散射的均匀程度。值为 1 时，会使在整个雾中扩散的灯光均匀散射。值越低，靠近太阳位置的雾越明亮。

### 空气(Air)

根据选择的[雾类型](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-A88206BD-28F0-404A-92EB-DD7F929986C8.htm#WS73099CC142F48755-3D114B7511841AEFA9F207F)，“空气”属性既可启用，又可禁用。下表列出了可用于“雾类型”(Fog Type)的“空气”(Air)属性。

#### 空气颜色(Air Color)

控制空气散射的灯光颜色。当灯光穿过空气或雾时，某些频率（颜色）直接穿过，而其他频率发生散射。散射的频率使得天空具有独特的颜色等特征。

#### 空气不透明度(Air Opacity)

控制穿过空气时被吸收的灯光频率（颜色）。这将影响背景中对象被空气染色的方式。例如，地平线上的对象在肉眼看来通常是带蓝色的。

#### 空气密度(Air Density)

控制雾模拟中空气的光学密度。增加该值，使空气看起来更稠密。

#### 空气最小高度(Air Min Height)

控制空气层底部的高度。*该属性仅在启用*“物理雾”(Physical Fog)*，并且*“雾类型”(Fog Type)*不*“一致”(Uniform)时可用。

#### 空气最大高度(Air Max Height)

控制空气层的高度。如果“雾类型”(Fog Type)是“大气”(Atmospheric)（或“水/大气”(Water/Atmos)），则空气密度从“空气最小高度”(Air Min Height)向上指数递减。如果雾类型为“天空”（或“水/天空”），则空气最大高度为空气层顶部的高度。*该属性仅在启用*“物理雾”(Physical Fog)*，并且*“雾类型”(Fog Type)*不*“一致”(Uniform)*时可用。*

#### 空气衰退(Air Decay)

控制空气在较高海拔高度变薄的速率。值为 0.5 时，会使空气线性衰退。值介于 0.5 到 1 之间时，会使空气在地面附近相当均匀，然后在顶部突然衰减。值介于 0 到 0.5 之间时，会导致空气在靠近地面处快速变薄。*该属性仅在启用*“物理雾”(Physical Fog)*，并且*“雾类型”(Fog Type)*不*“一致”(Uniform)*时可用。*

#### 空气灯光散射(Air Light Scatter)

控制灯光在空气中散射的均匀程度。值为 1 表示灯光均匀散射，且看似扩散在整个空气中。较低的值会导致大气在太阳位置周围显得更明亮。*该属性仅在*“物理雾”(Physical Fog)*启用时可用。*

### 水(Water)

如果[雾类型](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-A88206BD-28F0-404A-92EB-DD7F929986C8.htm#WS73099CC142F48755-3D114B7511841AEFA9F207F)为“水”(Water)、“水/雾”(Water/Fog)、“水/大气”(Water/Atmos)或“水/天空”(Water/Sky)，则这些属性将可用。

#### 水颜色(Water Color)

控制由水散射的灯光颜色。当灯光穿过空气或水时，某些频率（颜色）会直接穿过，而其他频率会发生散射。散射的频率使水具有独特的颜色。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型之一时可用。*

#### 水不透明度(Water Opacity)

控制在穿过水时被吸收的灯光频率（颜色）。这将影响背景中对象被水染色的方式。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型之一时可用。*

#### 水密度(Water Density)

控制雾模拟中水的光学密度。增加该值可使水下雾显得更稠密。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型时之一可用。*

#### 水位(Water Level)

值表示水位。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型之一时可用。*

#### 水深(Water Depth)

值表示水深。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型之一时可用。*

#### 水灯光衰退(Water Light Decay)

控制照明随深度衰减的速率。如果不希望灯光发生衰退（即，不希望越深处灯光越暗），则将该值设定为 0。该值为 1.0 会导致线性衰退，且值越高，变暗的速率就越快。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型之一时可用。*

#### 水灯光散射(Water Light Scatter)

控制灯光在水中散射的均匀程度。值为 1 会使灯光均匀散射，并看似扩散在整个水中。较低的值会导致水在光源表面附近显得更明亮。*该属性仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*设定为*“水”(Water)*类型之一时可用。*

## 太阳(Sun)

“太阳强度”(Sun Intensity)控制照明雾的阳光总体亮度。*仅在*“物理雾”(Physical Fog)*启用且*“雾类型”(Fog Type)*不为*“一致”(Uniform)*时可用。*

#### 太阳颜色(Sun Color)

控制照明雾的阳光颜色。

#### 太阳方位角(Sun Azimuth)

控制太阳在围绕“雾轴”(Fog Axis)的虚构圆上所处的位置（角度）。

#### 太阳仰角(Sun Elevation)

控制太阳在从地平线直接到正上方的直线上所处的位置（角度）。值为 90 表示太阳位于正上方（实际上，直接位于“雾轴”(Fog Axis)所指的位置上），值为 0 表示太阳位于地平线。

## 剪裁平面(Clipping Planes)

#### 距离剪裁平面(Distance Clip Planes)

如果将“环境雾”设定为“雾近/远”(Fog Near/Far)，则其存在于“雾近距”(Fog Near Distance)和“雾远距”(Fog Far Distance)之间。如果将“环境雾”设定为“摄影机近/远”(Camera Near/Far)，则其存在于摄影机的近剪裁平面和远剪裁平面之间。默认设置为“雾近/远”(Fog Near/Far)。

#### 雾近距(Fog Near Distance)、雾远距(Fog Far Distance)

将“距离剪裁平面”(Distance Clip Planes)设定为“雾近/远”(Fog Near/Far)时，距环境雾存在的摄影机的最小和最大距离（以场景的线性工作单位衡量）。

如果“雾远距”(Fog Far Distance)小于“雾近距”(Fog Near Distance)，则环境雾从“雾近距”(Fog Near Distance)延伸到无穷大。滑块范围为 0 到 200。“雾近距”(Fog Near Distance)的默认值为 0，“雾远距”(Fog Far Distance)的默认值为 200。
