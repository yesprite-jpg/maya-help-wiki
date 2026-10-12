# 公用 ShaderFX 节点和应用程序

## If Else Basic

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 流控制 > If Else Basic”(Hw Shader Nodes > Flow Control > If Else Basic)，创建此节点。

若要使用此节点，请提供“条件”(Condition)。如果条件为 true，则使用连接到“True”属性的值。如果条件为 false，则使用连接到“False”属性的值。

除了提供“False”属性的值，您还可以提供“默认输出值”(Default Output Value)。除非条件为 true，否则使用“默认输出值”(Default Output Value)。它提供了更清晰的代码并实现了优化。

在本示例中，如果“Bool”设置为 true，则“漫反射颜色”(Diffuse Color)为红色。

如果“Bool”设置为 false，则“漫反射颜色”(Diffuse Color)为绿色。

不管您将绿的“颜色”(Color)连接到“默认输出值”(Default Output Value)还是“False”，都会出现相同的结果。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9A2B1FE4-6B9F-4595-B661-4DD922417242.png) <!-- baize:img-hook downloaded=false reason="正文 783 字 ≥300，非承重" -->

## 比较(Comparison)

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 流控制 > 比较”(Hw Shader Nodes > Flow Control > Comparison)，创建此节点。

“比较”(Comparison)节点将比较两个值。例如，它会比较两个值，查看它们是相等还是一个大于另一个。在“属性编辑器”(Attribute Editor)中选择条件运算符，如 >、<、!=。

为“If Else Basic”节点提供条件非常有用。

在本示例中，“比较”(Comparison)节点会将“纹理贴图”(Texture Map)中的“红色”(Red)通道与指定的浮点值相比较。如果“红色”(Red)通道中的值大于 0.5，则应用“True”值（蓝色）。否则，应用默认值（黄色）。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E6A7F15D-2438-4226-B241-443A20F804A0.png) <!-- baize:img-hook downloaded=false reason="正文 783 字 ≥300，非承重" -->
