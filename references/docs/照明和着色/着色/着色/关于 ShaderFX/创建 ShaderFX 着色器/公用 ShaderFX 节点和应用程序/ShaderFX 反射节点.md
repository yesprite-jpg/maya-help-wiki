# ShaderFX 反射节点

## 反射立方体贴图

通过以下方法创建该节点：在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > 反射立方体贴图”(Hw Shader Nodes > Textures > Reflection Cube Map)。

若要将反射立方体贴图连接到“ShaderFX”网络，您必须使用 .dds 立方体贴图。在一并连接到“反射强度”(Reflection Intensity)（如下方网络中所示）之前，反射立方体贴图不影响反射。调整“属性编辑器”(Attribute Editor)中的“浮点型”(Float)值来调整反射量。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-4D80CECA-4C3B-4FA0-806D-3005D8C90817.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E86722D7-2CAE-4AA3-8E92-BB043986AFAD.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

### 模糊反射

如果立方体贴图包含 Mipmap，还可以模糊反射。将“浮点型”(Float)节点连接到“反射立方体贴图”(Reflection Cube Map)的“Mip Map 级别”(Mip Map Level)属性，如下方网络中所示。调整“浮点”(Float)值，跳转到下一下 Mipmap 级别来控制模糊量。在此示例中，使用值 5 来选择下一个 Mipmap。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-32CD23FA-BC9A-4472-9BA4-EDA3A11E0160.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-79744537-14CD-489A-AE27-75E34C66337A.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

## 球形反射 UV

通过以下方法创建该节点：在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > 球形反射 UV”(Hw Shader Nodes > Textures > Spherical Reflection UVs)。

类似于“反射立方体贴图”(Reflection Cube Map)节点，可使用该节点来创建反射。但是，可以不使用立方体贴图，而改用具有已在纹理上渲染球体的球体纹理。由于这种纹理只需要一个图像，而不像立方体那样需要六个图像，因此成本比立方体贴图低。但缺点是，它所生成输出的质量要比立方体贴图生成的反射或 latlong 反射低。

将“球形反射 UV”(Spherical Reflection UVs)节点的“UV”属性连接到“纹理贴图”(Texture Map)节点的“UV”属性。然后，将“纹理贴图”(Texture Map)的“颜色”(Color)属性连接到“TraditionalGameSurfaceShader”的“反射”(Reflection)属性。将“浮点型”(Float)节点连接到“TraditionalGameSurfaceShader”的“反射强度”(Reflection Intensity)属性，如下方网络中所示。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FB8772BE-736D-47F6-9EC8-EA04F59D9060.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-29456975-462B-49D9-A1F4-02F886CDFE6C.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

有时，您可能会看到收缩效果，其中某些区域未无缝融合在一起。将“浮点型”(Float)连接到“球形反射 UV”(Spherical Reflection UVs)节点的“收缩”(Pinching)属性并调整“浮点型”(Float)的值，直到接缝消失。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9D7D3050-B81E-4287-925F-E8D0B4DD3183.png) <!-- baize:img-hook downloaded=false reason="正文 1127 字 ≥300，非承重" -->

## Latlong 反射

除了反射立方体贴图和球形反射之外，您还可以将 Latlong 反射添加到场景中。有关示例网络，请参见[添加 Latlong HDR 反射和各向异性高光](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-15525851-1125-484E-8466-5740B3884212.htm#GUID-15525851-1125-484E-8466-5740B3884212__SECTION_F371687BDF5A434BA5D4C73555D778FF)。
