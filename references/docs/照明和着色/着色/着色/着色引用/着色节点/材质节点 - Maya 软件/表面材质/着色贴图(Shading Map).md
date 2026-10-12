# 着色贴图(Shading Map)

它是一种材质（着色器），可用于创建各种非真实照片级着色效果（如卡通风格的材质），或亮显渲染图像中的阈值。

可以将“着色贴图”(Shading map)着色器与基本着色器（如“Phong”着色器或“Blinn”着色器）和纹理（如“渐变”(Ramp)纹理或“文件”(File)纹理）配合使用。

例如，您可以创建这样一种材质，它将对象的明亮区域（向光区域）渲染为红色，将对象的暗区域（背光区域）渲染为蓝色。对于该示例，您将使用“着色贴图”(Shading Map)着色器、“Phong”着色器和“渐变”(Ramp)纹理。“渐变”(Ramp)纹理顶部是红色，底部是蓝色。将“Phong”着色器的“输出颜色”(Out Color)属性连接到“着色贴图”(Shading Map)着色器的“颜色”(Color)属性。将“渐变”(Ramp)纹理的“输出颜色”(Out Color)属性连接到“着色贴图”(Shading Map)着色器的“着色贴图颜色”(Shading Map Color)属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D8FEB3B1-5E34-4F2F-9014-22BEDFE11324.png) <!-- baize:img-hook downloaded=false reason="正文 919 字 ≥300，非承重" -->

着色贴图的工作方式与后期处理相似：常规着色器为曲面上每个点计算一个颜色，然后着色贴图着色器用另一种颜色替换该颜色。该贴图基于两项：原始颜色的亮度和原始颜色的色调。

可以在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

## 着色贴图属性(Shading Map Attributes)

#### 颜色(Color)

选择一种颜色，或将一个着色器映射到该属性。这提供了要对其应用着色贴图的基础颜色。

#### 着色贴图颜色(Shading Map Color)

定义材质的颜色。默认是灰色。

## 映射选项(Map Options)

#### 映射函数 U (Map Function U)，映射函数 V (Map Function V)

默认值分别是“色调”(Hue)和“明度”，但是其他选项包括“饱和度”(Saturation)、“红”(Red)、“绿”(Green)、“蓝”(Blue)以及“RGB 平均值”(RGB Average)。“映射函数 U”(Map Function U)指定在“shadingMapColor”的 U 方向查找时如何使用输入颜色。“映射函数 V”(Map Function V)指定在“shadingMapColor”的 V 方向查找时如何使用输入颜色。
