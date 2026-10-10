# 显示 Bifröst 液体中的诊断颜色：工作流示例

您可以将特定通道显示为视口中的颜色渐变，用于诊断或其他用途。此示例说明了如何使用粒子速度值设置“颜色通道重映射”(Color Channel Remap)渐变。

1. 通过增加曲面上的粒子密度，确保液体中有足够的细节。若要执行此操作，请选择 bifrostLiquid，并在 bifrostLiquidPropertiesContainer 节点的属性中滚动到“发射”(Emission)部分，将其展开，然后展开“粒子分布”(Particle Distribution)。

2. 将“曲面粒子密度”(Surface Particle Density)设定为 3。

  通过增加此值，可以在需要细节的液体表面增加粒子的数量，而不是增加贯穿整个体积的粒子数量。

3. 在属性编辑器中，单击 liquidShape 选项卡。

4. 在“显示”(Display)部分中，确保“颜色通道”(Color Channel)设置为“速度”(Velocity)。

5. 播放或拖动模拟。

  大多数粒子为蓝色，表示其速度低于当前“颜色通道最大值”(Color Channel Max) 20。若要显示粒子速度的范围，可重置此值使速度较高的粒子显示为白色。

6. 将值渐变的右侧控件拖动到左侧接近于 0 的位置。

  “选定位置”(Selected Position)值 0.2 可产生良好结果。

  您可以将此值用作 1.0 的一部分，以设置“颜色最大值通道”(Color Max Channel)（例如 0.2 × 20.0 = 4.0）。

7. 将“颜色最大值通道”(Color Max Channel)设置为 4.0。

8. 将值渐变的右侧控件重置为其原始设置：“选定位置”(Selected Position) 1 和 “选定值”(Selected Value) 1.0。

9. 预览模拟。

**注**

提示：

您可以使用

“Bifrost 控件”(Bifrost Controls)

下的

“剪裁”(Clipping)

属性预览形状的切片。
