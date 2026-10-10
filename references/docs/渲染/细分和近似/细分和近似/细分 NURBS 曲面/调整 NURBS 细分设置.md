# 调整 NURBS 细分设置

**注**

某些高级细分参数会显著增加渲染时间。

因为 NURBS 曲面的细分与指定给曲面的材质无关（除非曲面为置换贴图），所以可以在处理过程早期、对象建模后的任何时候开始调整细分。

调整 NURBS 对象上的细分

1. 确定场景中必须调整细分设置的对象。

  请参见[确定要细分哪些对象](确定要细分哪些对象.md)。

2. 显示细分三角形，以便可视化调整。

  请参见[显示 NURBS 细分三角形](显示%20NURBS%20细分三角形.md)。

3. 选择要对其调整细分的对象。

  如果要将设置应用于“所有曲面”(All surfaces)，请跳过该步骤。

4. 选择[渲染 > 设置 NURBS 细分(Render > Set NURBS Tessellation)](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md) > ![图：选择渲染 设置 NURBS 细分(Render Set NURBS Tessellation) 以打开“设置 NURBS…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 687 字 ≥300，非承重" --> 以打开“设置 NURBS 细分选项”(Set NURBS Tessellation Options)窗口。

5. 选择“选定曲面”(Selected Surfaces)或“所有曲面”(All surfaces)（请参见选定曲面(Selected Surfaces)、所有曲面(All surfaces)）。

6. 将“细分模式”(Tessellation Mode)从[自动(默认)](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md#WS73099CC142F487553B93539F117EA10CE8F5D7E)切换到[手动](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md#WS73099CC142F487553B93539F117EA10CE8F5D84)。

  （也可以调整某些自动细分设置以优化默认设置。请参见[自动模式设置](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md#WS17956D7ADBC6E73642AE5CD3117AE33B5CB-7FCF)。）

7. 选择[基本](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md#WS73099CC142F487553B93539F117EA10CE8F5DBE)或[高级](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md#WS73099CC142F487553B93539F117EA10CE8F5DC2)细分。

  始终以“基本”(Basic)设置开始。“基本”可用于调整少量设置，这些设置会自动确定某些更高级的设置。

  **注**

  某些高级细分参数会显著增加渲染时间，所以要巧妙地选择它们。

8. 测试渲染以查看结果。

  微调刚刚已设定的调整，直到达到足够级别的平滑度。

  **注**

  提示：

  若要防止对象的过度细分，请使用[渲染 > 设置 NURBS 细分(Render > Set NURBS Tessellation)](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md)窗口中的[使用平滑边(Use Smooth Edge)](../../../渲染参考/渲染参考/“渲染”%28Rendering%29菜单集/“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md#WS73099CC142F487553B93539F117EA10CE8F5DB0)属性以便仅沿对象的边增加细分。
