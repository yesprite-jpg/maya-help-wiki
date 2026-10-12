# Blinn

该材质（着色器）尤其适用于模拟通常具有柔和镜面反射高光的金属曲面（如铜或铝）。

**注**

“Blinn”是以下三种常见材质中计算量最大的：“Lambert”、“Phong”和“Blinn”。

通过设定“Blinn”材质的属性，可以控制发亮高光区的大小和曲面反射其周围事物的能力。

可以在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

**注**

提示：

与“Phong”曲面上的较强高光相比，“Blinn”曲面上的柔和高光出现瑕疵或薄高光闪烁的可能性较小。对带有凹凸或置换贴图的曲面使用“Blinn”表面材质以减少高光瑕疵或闪烁。

## “镜面反射着色”(Specular Shading)属性 (Blinn)

#### 偏心率(Eccentricity)

控制曲面上发亮高光区的大小。有效范围为 0（无高光）到 0.999（宽高光，不是很有光泽的曲面）。值为 0.1 会产生较小的高光（很有光泽的曲面）。默认值为 0.3。

#### 镜面反射衰减(Specular Roll Off)

使曲面可以反射其周围事物（环境、其他曲面）或“反射的颜色”(Reflected Color)（以倾斜角度观看曲面时）。滑块范围为 0 到 1。默认值为 0.7。

若要帮助可视化“Blinn”材质样例中“镜面反射衰减”(Specular Roll Off)的效果，请将纹理指定给“反射的颜色”(Reflected Color)。

![图：使曲面可以反射其周围事物（环境、其他曲面）或“反射的颜色”(Reflected Color)（以倾斜角度观看曲面时）。滑…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FD01B5FA-5503-4BAC-A57F-EF4F8A20A6A8.png) <!-- baize:img-hook downloaded=false reason="正文 719 字 ≥300，非承重" -->

**注**

提示：

使用“镜面反射衰减”(Specular Roll Off)值 0.3 模拟湿曲面（例如，未干的涂料）。

#### 镜面反射颜色(Specular Color)

请参见[常见表面材质镜面反射着色属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D9193CD6-EF2C-4EA3-A31E-C3BDB3E17F87.htm)。

#### 反射率(Reflectivity)

请参见[常见表面材质镜面反射着色属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D9193CD6-EF2C-4EA3-A31E-C3BDB3E17F87.htm)。

#### 反射的颜色(Reflected Color)

请参见[常见表面材质镜面反射着色属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D9193CD6-EF2C-4EA3-A31E-C3BDB3E17F87.htm)。
