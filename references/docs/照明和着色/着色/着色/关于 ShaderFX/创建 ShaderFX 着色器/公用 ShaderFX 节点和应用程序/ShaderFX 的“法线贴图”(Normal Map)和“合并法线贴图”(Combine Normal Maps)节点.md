# ShaderFX 的“法线贴图”(Normal Map)和“合并法线贴图”(Combine Normal Maps)节点

## ShaderFX 的“法线贴图”(Normal Map)节点

通过以下方法创建该节点：在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > 法线贴图”(Hw Shader Nodes > Textures > Normal Map)。

当将法线贴图直接连接到“TraditionalGameSurfaceShader”的“法线”(Normal)属性时，请使用“法线贴图”(Normal Map)节点，而不是“纹理贴图”(Texture Map)节点。“法线贴图”(Normal Map)节点将法线贴图转化为世界空间，而“纹理贴图”(Texture Map)节点将其保持在切线空间。

或者，可以从 ShaderFX 菜单栏中选择“设置 > 切换高级模式”(Settings > Toggle Advanced Mode)以启用高级模式，然后选择“硬件着色器节点 > 各种 > 法线空间转化器”(Hw Shader Nodes > Various > Normal Space Converter)以创建“法线空间转化器”(Normal Space Converter)节点。将“纹理贴图”(Texture Map)节点连接到该节点时，贴图将转化为世界空间。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-EDCB4237-9630-439B-B62E-C022A7F2E186.png) <!-- baize:img-hook downloaded=false reason="正文 978 字 ≥300，非承重" -->

## ShaderFX 的“合并法线贴图”(Combine Normal Maps)节点

通过以下方法创建该节点：在“ShaderFX”编辑器中选择“硬件着色器节点 > 纹理 > 合并法线贴图”(Hw Shader Nodes > Textures > Combine Normal Maps)。

您可以为着色器图表提供两个法线贴图：低分辨率的基准法线贴图；更详细、分辨率更高贴图（可提供模型的更精细凹凸细节）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-1EDE878E-17D2-42EC-825B-2BC1D9B9CAD0.png) <!-- baize:img-hook downloaded=false reason="正文 978 字 ≥300，非承重" -->

将基准法线作为“纹理贴图”(Texture Map)连接到“合并法线贴图”(Combine Normal Maps)的“基础”(Base)属性，将详细的法线贴图作为“纹理贴图”(Texture Map)连接到“详细信息”(Detail)属性，然后将“合并法线贴图”(Combine Normal Maps)的“法线”(Normal)属性连接到“TraditionalGameSurfaceShader”的“法线”(Normal)属性。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-4291B0C5-49D0-4489-990A-AC9DB6014975.png) <!-- baize:img-hook downloaded=false reason="正文 978 字 ≥300，非承重" -->

**注**

将“合并法线贴图”(Combine Normal Maps)

转化为世界空间；因此，通过

“纹理贴图”(Texture Map)

节点而非

“法线贴图”(Normal Map)

节点连接法线贴图。
