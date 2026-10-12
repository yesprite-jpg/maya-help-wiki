# ShaderFX 动画书节点

通过在“ShaderFX”编辑器中选择“硬件着色器 > 纹理 > 动画书”(Hw Shader Nodes > Textures > Flip Book)，创建此节点。

将若干帧组合为一个纹理，然后使用“动画书”(Flip Book)节点循环浏览每个帧。每个帧也称为一个精灵。

您可以选择“ShaderFX”菜单栏中的“设置 > 播放已设置动画的着色器”(Settings > Play Animated Shaders)，在“ShaderFX”编辑器中播放动画，或在“Viewport 2.0”中使用“Maya 播放控制”(Maya Playback Controls)播放动画。

默认情况下，“动画书”(Flip Book)节点会假定纹理的配置为 2 个水平图像 x 2 个垂直图像。

选择“动画书”(Flip Book)节点，然后修改“HorizontalImages”和“VerticalImages”属性，以使其适应纹理的配置。

您还可以在“ShaderFX”编辑器中调整“FramesPerSec”属性，更改播放速度。

由于将大量图像加载到显卡上需要消耗大量资源，而使用该节点可将各帧组合为一个纹理并循环浏览各帧，从而降低资源消耗。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-68A6A290-70FE-43E9-A2AC-209F5AB7179F.png) <!-- baize:img-hook downloaded=false reason="正文 487 字 ≥300，非承重" -->
