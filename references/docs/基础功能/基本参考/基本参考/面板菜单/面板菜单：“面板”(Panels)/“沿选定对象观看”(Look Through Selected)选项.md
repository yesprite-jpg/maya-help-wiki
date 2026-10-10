# “沿选定对象观看”(Look Through Selected)选项

用于沿选定摄影机、对象或灯光观看。

选择“面板 > 沿选定对象观看”(Panels > Look Through Selected) > ![图：选择“面板 沿选定对象观看”(Panels Look Through Selected) 可打开“沿选定对象观看选项”(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 719 字 ≥300，非承重" --> 可打开“沿选定对象观看选项”(Look Through Selected Options)窗口。可以为观看时所用的摄影机设置“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)值。

#### 近剪裁平面(Near Clip Plane)、远剪裁平面(Far Clip Plane)

这表示透视或正交摄影机近剪裁平面和远剪裁平面的距离。“近剪裁平面”(Near Clip Plane)的默认设置是 0.1，“远剪裁平面”(Far Clip Plane)的默认设置是 10000。

（仅适用于 Maya 软件渲染）默认情况下启用“自动渲染剪裁平面”(Auto Render Clip Plane) （请参见[自动渲染剪裁平面](../面板菜单：“视图”%28View%29/摄影机属性编辑器%28Camera%20Attribute%20Editor%29.md#WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FAB)），“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)值并不确定剪裁平面的位置。

如果近剪裁平面与远剪裁平面之间的距离远大于包含场景中所有对象所需的距离，则某些对象的图像质量可能会较差。将“近剪裁平面”(Near Clip Plane)和“远剪裁平面”(Far Clip Plane)属性分别设定为最小和最大值，从而产生所需结果。

**注**

提示：

通常在摄影机的特定范围内渲染对象。将近剪裁平面和远剪裁平面设定为略微超出场景中对象的界限，这有助于提高图像质量。

**注**

远比率：近剪裁平面确定深度精度。尝试保持尽可能小的比率，以获得更好的结果。

由于大多数深度精度集中在近剪裁平面，因此在远处对象上尽量避免过多细节。

对于硬件渲染来说，此概念非常重要，因为它仅拥有 24 位深度精度，而软件渲染却拥有 32 位深度精度。
