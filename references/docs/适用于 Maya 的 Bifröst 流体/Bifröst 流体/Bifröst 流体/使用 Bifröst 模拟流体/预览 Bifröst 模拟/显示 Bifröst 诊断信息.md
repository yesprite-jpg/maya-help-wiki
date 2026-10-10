# 显示 Bifröst 诊断信息

可以在视口中将属性通道的值显示为颜色渐变、数值或向量。这样，您就可以分析或诊断自己的模拟。

可显示的属性取决于模拟类型。例如，可以对液体中的“漩涡”(Vorticity)或“翻腾”(Churn)和 Aero 模拟中的“烟”(Smoke)进行可视化。有些属性（如“位置”(Position)和“速度”(Velocity)）通过模拟更新，而其他属性则在 emitterProps 属性中设置并与粒子一起传输。

### 显示诊断颜色

1. 在“bifrostShape”节点的“显示”(Display)属性组中，根据需要选择“粒子”(Particles)或“体素”(Voxels)。

2. 根据需要激活“粒子显示”(Particle Display)或“体素显示”(Voxel Display)组中的“颜色”(Color)。

3. 选择要显示的“通道”(Channel)。对于“位置”(position)和“速度”(velocity)等向量属性，幅值用于驱动颜色渐变。

4. 展开“颜色通道重映射”(Color Channel Remap)，然后将“颜色通道最小值”(Color Channel Min)和“颜色通道最大值”(Color Channel Max)设置为需要的范围。超出此范围的值将钳制为颜色渐变的限制。

5. 使用该颜色渐变定义要显示的渐变。

6. 如果需要，在应用颜色渐变之前，使用值渐变来重映射通道值。例如，可以钳制和偏移值以侧重于值的子范围。

**注**

提示：

您可以使用

“Bifrost 控件”(Bifrost Controls)

下的

“剪裁”(Clipping)

属性预览形状的切片。

### 显示数值或向量

1. 在 bifrostShape 节点的“显示”(Display)属性组中，确保选择“粒子”(Particles)。

2. 在“粒子显示”(Particle Display)组中，选择“数值”(Numeric)或“向量”(Vector)。

3. 选择要显示的通道。

**注**

提示：

降低

“最大粒子显示数”(Max Particle Display Count)

，以便更轻松地读取值。
