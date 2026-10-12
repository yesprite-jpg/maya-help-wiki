# 示例 ShaderFX 图

## 添加 latlong HDR 反射和各向异性高光

以下示例演示了如何将 latlong HDR 反射和各向异性高光添加到场景中。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-C2583A02-C688-463C-8826-3525A0A817DC.png) <!-- baize:img-hook downloaded=false reason="正文 546 字 ≥300，非承重" -->

着色器图如下所示：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A36BEC9A-F0C3-4334-982C-37BED0C642BB.png) <!-- baize:img-hook downloaded=false reason="正文 546 字 ≥300，非承重" -->

“LatLong UV”和“纹理贴图”(Texture Map)节点将为场景提供 latlong HDR 反射。“反射强度”(Reflection Intensity)可控制反射量。

为了添加各向异性高光，请在“ShaderFX” “属性编辑器”(Attribute Editor)中将“镜面反射”(Specular)切换为“各向异性”(Anisotropic)。

“各向异性扩散”(Anisotropic Spread)可控制镜面反射高光的形状。

## 应用曲面遮罩

以下示例将演示如何应用曲面遮罩以遮罩和分解纹理部分。请注意，阴影也会遵循遮罩。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-EF66AF0E-5696-485A-A49A-88F958D9B358.png) <!-- baize:img-hook downloaded=false reason="正文 546 字 ≥300，非承重" -->

着色器图如下所示：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-285A8B53-AB26-498F-B4A7-9C8728941ACA.png) <!-- baize:img-hook downloaded=false reason="正文 546 字 ≥300，非承重" -->

按照图中所示，将曲面遮罩纹理连接到“材质”(Material)节点的“曲面遮罩”(Surface Mask)属性，然后将树叶纹理连接到“TraditionalGameSurfaceShader”节点的“漫反射颜色”(Diffuse Color)属性。然后，您可以选择“材质”(Material)节点并调整“SurfaceMaskCutoff”属性以控制要遮罩的数量。将切断比“SurfaceMaskCutoff”阈值更暗的所有值。
