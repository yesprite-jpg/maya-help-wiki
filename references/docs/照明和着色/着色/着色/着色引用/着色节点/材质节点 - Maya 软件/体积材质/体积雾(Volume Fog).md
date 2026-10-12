# 体积雾(Volume Fog)

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

将该材质应用于体积基本体，以创建诸如球形、圆锥形或小隔间烟、雾或灰尘等效果。有关详细信息，请参见[体积基本体选项(Volume Primitives Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-673FC369-2D8A-47B4-9C1B-99DD55B642AA)。

#### 颜色(Color)

将颜色指定给体积，或将纹理映射到体积。若要使用颜色渐变，请参见[渐变](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-F2C97013-5E4C-41AC-9684-E23AC52C51B8.htm)。

#### 透明度(Transparency)

表示体积的“透明度”(Transparency)的量。

#### 白炽度(Incandescence)

使材质看起来就像是它在发光（如熔岩或发出磷光的苔藓）。例如，在植物素材上稍微点缀白炽度就可以使植被看起来有生机。默认情况下，该颜色为黑色，它不会对曲面有任何影响。

**注**

尽管在应用白炽度时表面看起来会发出辉光，但它并不充当场景中的光源。请参见“辉光强度”(Glow Intensity)。

#### 辉光强度(Glow Intensity)

随着增大该值，材质看起来会发出辉光，并会被灯光的微弱光晕所包围。“辉光强度”(Glow Intensity)与“白炽度”(Incandescence)的差异表现在两个方面：

- 辉光向曲面添加光晕。

- 作为后期处理，Maya 会在渲染结束时添加辉光效果；而白炽度只是使曲面看起来更亮。

  #### 密度(Density)

  表示雾的密度或透明度。

  #### 密度模式(Density Mode)

  确定密度是在世界空间中还是在对象空间中定义的。缩放对象时，对象空间密度会保持外观不变。

  #### 照明(Illuminated)

  如果启用该选项，则为雾计算灯光。每个体积跨度的照明取决于几何体上的体积采样的属性。

  #### 灯光散射(Light Scatter)

  雾在所有方向上散射灯光的量。随着它接近 0，雾将倾向于定向散射灯光，这会在光源周围产生光晕。

## 衰减(Dropoff)

#### 衰减形状(Dropoff Shape)

选择“圆锥体”(Cone)、“球体”(Sphere)、“立方体”(Cube)或“浅色圆锥体”(Light Cone)作为用于定义外部边界的形状，从而创建柔和边缘的体积。例如，如果渲染一个长方体体积，“立方体”(Cube)应该与体积的边匹配。

**注**

“浅色圆锥体”(Light Cone)与“圆锥体”(Cone)不同，在前者的点附近会发生衰减（或褪色）。

#### 边衰减(Edge Dropoff)

定义密度在“衰减形状”(Dropoff Shape)所定义的边附近衰减的突然程度。值为 0.0 会产生没有衰减的硬边。值为 1.0 会产生从体积边缘到体积中心的平滑密度褪色。

#### 轴向衰减(Axial Dropoff)

限定密度沿圆锥体的中心轴向下衰减。值越大，会使雾越不密集，离圆锥体的尖端越远（仅适用于“圆锥体”(Cone)形状）。

#### 衰减方法(Dropoff Method)

选择下列选项之一：

#### 比例不透明度(Scale Opacity)

将总体密度乘以褪色值，会在透明度上产生一致的更改。

#### 减少密度(Subtract Density)

从密度中减去褪色值乘以“衰减减少”(Dropoff Subtract)值之积。密度或透明度带纹理时很有用。低密度区域会变得完全透明，而高密度区域影响不大。例如，这可能会有助于保持蓬松的云的角色。

#### 衰减减少(Dropoff Subtract)

“衰减方法”(Dropoff Method)为“减少密度”(Subtract Density)时，从体积中减去的最大密度量。如果体积密度为 1.0 且“衰减减少”(Dropoff Subtract)为 1.0，那么体积的边是完全透明的。
