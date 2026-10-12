# 常见表面材质的“镜面反射着色”(Specular Shading)属性

某些曲面的反光度强于其他曲面（例如湿鱼的曲面反光度强于干树叶）。根据曲面的反光度，曲面以不同方式反射灯光。

反光对象直接反射灯光；蒙版对象漫反射灯光。镜面反射高光显示了对象上光源从一致角度得到反射的位置；此外，对象上的反射还显示从周围对象上反弹的灯光。

镜面反射高光直接取决于视图（摄影机），而不是灯光位置，类似漫反射着色。

曲面上镜面反射高光的大小会使曲面看起来平坦或反光。

**注**

仅拥有镜面反射属性（

“各向异性”(Anisotropic)、“Blinn”、

“Phong”

和“PhongE”

）的材质才具有表面高光。镜面反射高光是材质上的白色反光辉光。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-51BA93E3-B67B-49AE-A0EF-1273B9541E46.png) <!-- baize:img-hook downloaded=false reason="正文 1165 字 ≥300，非承重" -->

**注**

提示：

建议将“Blinn”材质用于动画中的反光曲面。其他镜面反射材质上的高光（如“Phong” 和“PhongE”）可能会在设定动画后闪烁。

对于特定于材质的镜面反射着色属性，请参见特定材质。例如，有关“各向异性”(Anisotropic)材质的镜面反射着色属性的信息，请参见[各向异性。](各向异性%28Anisotropic%29.md)

#### 镜面反射颜色(Specular Color)

表面上闪耀的高光的颜色。黑色“镜面反射颜色”(Specular Color)不产生表面高光。默认颜色值为 0.5。

![图：表面上闪耀的高光的颜色。黑色“镜面反射颜色”(Specular Color)不产生表面高光。默认颜色值为 0.5。 提示…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-471C551F-0075-4803-9757-C2100054FE30.png) <!-- baize:img-hook downloaded=false reason="正文 1165 字 ≥300，非承重" -->

**注**

提示：

对于有光泽的塑料表面，请使用发白的

“镜面反射颜色”(Specular Color)

。对于金属表面，请使用类似于表面颜色的

“镜面反射颜色”(Specular Color)

。

#### 反射率(Reflectivity)

使表面能够反射周围的物体或者“反射的颜色”(Reflected Color)（类似于“镜面反射衰减”(Specular Roll Off)）。有效范围是 0 到无限。滑块范围为 0（无反射）到 1（清晰的反射）。默认值为 0.5。

![图：使表面能够反射周围的物体或者“反射的颜色”(Reflected Color)（类似于“镜面反射衰减”(Specular …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-60F31851-4274-400F-955A-70D5BF495A2D.png) <!-- baize:img-hook downloaded=false reason="正文 1165 字 ≥300，非承重" -->

常见表面材质的“反射率”(Reflectivity)值为汽车喷漆 (0.4)、玻璃 (0.7)、镜子 (1)、铬 (1)。

**注**

- 对于[各向异性](各向异性%28Anisotropic%29.md)材质，必须禁用“各向异性反射率”(Anisotropic Reflectivity)才能更改该值。

- 实际的反射仅在光线跟踪过程中计算。

- 如果您正在执行光线跟踪并且希望在反射中显示场景中的其他对象，则对于这些对象，必须确保在“属性编辑器”(Attribute Editor)的“渲染统计信息”(Render Stats)区域启用了“在反射中可见”(Visible In Reflections)属性。（默认情况下该选项处于启用状态。）

#### 反射的颜色(Reflected Color)

表示从材质反射的光的颜色。进行光线跟踪时，Maya 会使用从表面反射的光（像镜子那样）的颜色使颜色倍增。这可用于对反射进行染色。

如果未进行光线跟踪，则可以将图像、纹理或环境贴图映射到“反射的颜色”(Reflected Color)属性以创建虚设反射，这与光线跟踪相比，速度更快并且使用的内存更少。这称为反射映射。有关反射的详细信息，请参见[真实反射](../../../../反射和环境/真实反射.md)。
