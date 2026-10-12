# ShaderFX 的“时间”(Time)节点

通过在“ShaderFX”编辑器中选择“硬件着色器节点 > 输入应用 > 时间”(Hw Shader Nodes > Inputs Application > Time)创建该节点。

下面的示例演示了如何将“时间”(Time)节点与“Sin”节点结合使用。若要创建“Sin”节点，请从 ShaderFX 菜单栏中选择“设置 > 切换高级模式”(Settings > Toggle Advanced Mode)以启用高级模式，然后选择“硬件着色器节点 > 数学 > Sin”(Hw Shader Nodes > Math > Sin)。

在“ShaderFX”菜单栏中选择“设置 > 播放动画着色器”(Settings > Play Animated Shaders)，对图表网络的动画进行可视化。

默认情况下，“sin”节点从 -1 到 1 进行制图。在 -1 到 0 的范围内，将绘制黑色，而从 0 到 1 的范围内，将从黑色到白色进行绘制。

“添加”(Add)节点会将 1 添加到“Sin”图表。“Sin”节点现在从 0 到 2 进行制图。它永远不会小于零，从黑色到白色进行绘制。

“相除”(Divide)节点会将“Sin”图表除以 2。“Sin”节点现在从 0 到 1 进行绘制。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8CAC90BF-4398-4667-B7B6-E26621E1DAD3.png) <!-- baize:img-hook downloaded=false reason="正文 498 字 ≥300，非承重" -->

此样例有助于创建动画效果或淡出效果。
