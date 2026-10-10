# 移动 UV 壳工具(Move UV Shell Tool)

可用于通过在壳上选择单个 UV 在 UV 编辑器的 2D 视图中选择并重新定位 UV 壳。可以自动防止已重新定位的 UV 壳与其他 UV 壳重叠。

若要打开“移动 UV 壳工具”(Move UV Shell Tool)，请从“UV 编辑器”(UV Editor)菜单中选择“工具 > 移动 UV 壳”(Tools > Move UV Shell)。

选择“工具 > 移动 UV 壳”(Tools > Move UV Shell) > ![图：选择“工具 移动 UV 壳”(Tools Move UV Shell) 时，在“工具设置”(Tool Settings)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 661 字 ≥300，非承重" -->时，在“工具设置”(Tool Settings)窗口中将显示以下选项。

## 移动 UV 壳设置

#### 禁止重叠(Prevent overlap)

“禁止重叠”(Prevent overlap)设置可禁止 UV 壳意外移动到会导致它与 UV 编辑器视图中的现有 UV 壳重叠的位置。默认情况下会启用该选项。例如，如果选择并移动 UV 壳，然后将其重新定位到已被某个现有 UV 壳占据的区域，那么选定壳将执行下列操作之一：

- 捕捉回到其先前位置（如果重叠很大）。

- 基于拖动 UV 壳的方向，捕捉到可能的最近位置（如果重叠很小）。

#### 壳间距(Shell spacing)

当“禁止重叠”(Prevent overlap)处于启用状态时，将已重新定位的 UV 壳与其他现有 UV 壳隔开的距离指定为贴图大小的百分比。

#### 放置迭代次数(Placement iterations)

指定当平移一个或多个 UV 时，为了以最佳方式获得“壳间距”(Shell spacing)距离而不捕捉回到原始位置，该工具在开始位置和结束位置之间检查的次数。值越大，就越有可能产生最接近的结果，但完成移动所花费的时间也越长。选定 UV 壳的数量也会影响用于完成移动的时间。默认设置为 16。
