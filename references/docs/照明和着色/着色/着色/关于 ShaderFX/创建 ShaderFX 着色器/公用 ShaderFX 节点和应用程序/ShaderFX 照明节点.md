# ShaderFX 照明节点

## 降低颜色饱和度(Desaturate Color)

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 照明 > 降低颜色饱和度”(Hw Shader Nodes > Lighting > Desaturate Color)，创建此节点。

“降低颜色饱和度”(Desaturate Color)节点可将颜色转换为灰度。此节点最适用于混合两个纹理或颜色，或创建曲面遮罩。

在本示例中，“纹理贴图”(Texture Map)将转换为灰度，但其渐变图案用于混合蓝色和黄色。结果生成蓝色和黄色的渐变图案。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D39171C9-6470-4539-9FD5-48344D0E3255.png) <!-- baize:img-hook downloaded=false reason="正文 865 字 ≥300，非承重" -->

## 环境地面天空(Ambient Ground Sky)

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 照明 > 环境地面天空”(Hw Shader Nodes > Lighting > Ambient Ground Sky)创建此节点。

“环境地面天空”(Ambient Ground Sky)节点可在对象的顶部和底部着不同的颜色。它模拟来自天空和地面的灯光。

连接“地面颜色”(Ground Color)和“天空颜色”(Sky Color)，如本示例所示，并将“环境地面天空”(Ambient Ground Sky)的“颜色”(Color)属性连接到“TraditionalGameSurfaceShader”的“发射”(Emissive)属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-947075B1-6182-485C-8F5D-96BED1CE3B17.png) <!-- baize:img-hook downloaded=false reason="正文 865 字 ≥300，非承重" -->

天空颜色和地面颜色将随着世界空间而非对象旋转。旋转对象时，其顶部保留天空颜色，底部保留地面颜色。

将漫反射颜色“纹理贴图”(Texture Map)连接到“TraditionalGameSurfaceShader”的“漫反射颜色”(Diffuse Color)属性和“环境地面天空”(Ambient Ground Sky)的“漫反射系数颜色”(Albedo Color)，使材料以逼真的物理方式反射灯光。

在现实世界中，太阳和地面不能将对象的颜色更改为太阳和地面的颜色。例如，蓝色天空不会将木椅染为蓝色，因为木材永远不会完全反射蓝色。连接“漫反射系数颜色”(Albedo Color)属性可确保实现逼真的物理渲染。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-60A08B41-0AA0-4F5E-A1D7-C8747532D7C0.png) <!-- baize:img-hook downloaded=false reason="正文 865 字 ≥300，非承重" -->

图像由 www.cgtextures.com 提供。
