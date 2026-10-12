# 高度场(Height Field)

该工具绘制一个平面，该平面以交互方式显示 2D 纹理或“海洋着色器”(Ocean Shader)的置换。该平面当前仅用于预览或交互式显示，不会显示在渲染器中。使用该平面预览置换效果，然后通过将相同纹理置换映射到目标着色器来重新创建置换效果。

**注**

“高度场”(Height Field)

节点不支持 3D 纹理。

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用高度场工具](../../../渲染节点工具/使用“高度场”%28Height%20Field%29工具.md)。

#### 分辨率(Resolution)

相对于平面的最大边的采样数。该值越大，表面就越详细，但绘制时间也就越长。

#### 颜色(Color)

预览表面的基本颜色。这可以使用 2D 纹理或“海洋着色器”(Ocean Shader)进行映射；但只能使用 outColor 值。

#### 位移(Displacement)

平面的置换。这可以使用 2D 纹理或“海洋着色器”(Ocean Shader)进行映射；但始终使用 outAlpha 值。这将对忽略添加的着色引擎输入的纹理进行优化求值。

#### 高度比例(Height Scale)

输入置换的比例因子。该值越大，置换就越明显。

![图：输入置换的比例因子。该值越大，置换就越明显。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FC62747B-01E2-4F5D-B7E0-B8D70C1EF82B.png) <!-- baize:img-hook downloaded=false reason="正文 464 字 ≥300，非承重" -->
