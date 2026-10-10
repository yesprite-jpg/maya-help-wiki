# 重建曲线选项(Rebuild Curve Options)

使用以下选项可设置在选择“曲线 > 重建”(Curves > Rebuild)时发生的情况。

#### 重建类型(Rebuild Type)

“一致”(Uniform)可通过一致参数化重建曲线。使用该选项，可以更改曲线的“跨度数”(Number of Spans)和“次数”(Degree)。

“减少”(Reduce)可移除结，条件是移除结不会导致任何剩余的结移动的距离大于容差设置。容差设置越高，移除的结就越多。

“匹配结”(Match Knots)可通过匹配曲线次数、结值及另一曲线的跨度数来重建曲线。首先选择要重建的曲线，并按住 Shift 键的同时选择要匹配的曲线，然后再重建曲线。选择“匹配结”(Match Knots)后，“保持”(Keep)选项将变为可用状态。

“无多个结”(No Multiple Knots)可移除重建操作过程中创建的任何额外的结。该曲线的曲线次数与原始曲线相同。选择该选项后，“保持”(Keep)选项将不可用。

![图：“一致”(Uniform)可通过一致参数化重建曲线。使用该选项，可以更改曲线的“跨度数”(Number of Spans…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B1C89444-EB25-4E03-8889-B8B43B9A2A69.png) <!-- baize:img-hook downloaded=false reason="正文 1857 字 ≥300，非承重" -->

曲率越高的区域，“曲率”(Curvature)可插入的节点就越多。该曲线的次数与原始曲线相同。选择该选项后，“保持”(Keep)选项将不可用，但会显示“使用容差”(Use Tolerance)选项。

![图：“一致”(Uniform)可通过一致参数化重建曲线。使用该选项，可以更改曲线的“跨度数”(Number of Spans…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-6DA1235E-0C43-430E-A53E-D82A217A8ADD.png) <!-- baize:img-hook downloaded=false reason="正文 1857 字 ≥300，非承重" -->

“结束条件”(End Conditions)可重建曲线末端 CV 和末端结的位置。如果选择“结束条件”(End Conditions)，则会为“结束条件”(End Conditions)显示两个附加选项：“无多个结”(No Multiple knots)和“多点结”(Multiple knots)。

启用“无多个结”(No Multiple Knots)后，重建曲线将不会通过末端 CV。这样会使曲线在某些情况下更难控制，但会使其他操作更简单。例如，更容易在相邻曲线之间创建平滑接合。（如果通过“无多个结”(No Multiple Knots)重建两个曲线，则可以将 CV 捕捉到一起以获取沿边界的精确切线。）

如果启用“多点结”(Multiple Knots)，则曲线会到达末端 CV，使其更易于控制曲线边界和相关切线。

通过“结束条件”(End Conditions)重建的曲线的次数与原始曲线相同。

#### 参数范围(Parameter Range)

“0 到 1”(0 to 1)可将结果曲线的参数范围设定为 0 到 1。

“保持”(Keep)可将重建曲线的参数范围与原始曲线匹配。

“0 到跨度数”可创建整型结值，使数值输入更加容易。如果使用“一致重建类型”(Uniform Rebuild Type)，则“0 到跨度数”(0 to # spans)将始终创建整型结值。这在通过曲线选项输入结参数值时很有用。例如，如果输入结值以进行“分离曲面”(Detach Surfaces)操作，则输入数字 2 比输入类似 0.362 这样的数字更简单。

#### 保持(Keep)

如果要重建曲线使其具有原始的结束点、切线、CV 或跨度数，则启用“末端”(Ends)、“切线”(Tangents)、“CV”(CVs)或“跨度数”(NumSpans)。“跨度数”(NumSpans)仅可与“一致”(Uniform)选项结合使用。

#### 跨度数(Number of Spans)

指定结果曲线中的跨度数。

![图：指定结果曲线中的跨度数。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-CAFAD37B-C81B-4DC3-B1D5-F522F41B655B.png) <!-- baize:img-hook downloaded=false reason="正文 1857 字 ≥300，非承重" -->

#### 次数(Degree)

“次数”(Degree)越高，曲线就越平滑。默认设置（“3 立方”）可适用于大多数曲线。

![图：“次数”(Degree)越高，曲线就越平滑。默认设置（“3 立方”）可适用于大多数曲线。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-39C27AB2-1428-4287-9907-4A107C58E0C6.png) <!-- baize:img-hook downloaded=false reason="正文 1857 字 ≥300，非承重" -->

#### 保持原始(Keep Original)

保持原始曲线并创建新曲线作为重建曲线。这对于比较具有不同选项的各个曲线很有用。

#### 使用容差(Use Tolerance)

如果“重建类型”(Rebuild Type)为“减少”(Reduce)或“曲率”(Curvature)，则选项窗口中会显示“使用容差”(Use Tolerance)选项。这些选项可用于在原始曲线的指定容差内重建曲线。“全局”(Global)从 Maya 的“首选项”(Preferences)窗口中使用容差设置。“局部”(Local)可用于在选项窗口中直接输入容差。

#### 输入曲线(Input Curve)

“输入曲线”(Input Curve)信息是只读的。通过它可以访问重建的原始曲线的历史。单击箭头按钮以选择该曲线，并打开其编辑器的截面。

#### 匹配曲线(Match Curve)

仅当存在多条曲线并且在选项窗口中选择了“匹配结”(Match Knots)时，“匹配曲线”(Match Curve)只读信息才可用。

## 相关主题

- [减少曲线或曲面的复杂性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-24DF5B14-6A5A-434E-9693-2318400BC32B.htm)

- [控制多点结和 CV 硬度](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-3CDB7E68-05B8-4546-965A-93D6F16B723D.htm)

- [自动将跨度数添加到曲线的高曲率区域](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-0EDF1A94-9B4F-4408-8739-7CC42701BB8A.htm)

- [将曲线或曲面转化为一致参数化](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-5EE99036-5A55-48F3-88AB-DE2A4D729623.htm)

- [将曲面转化为非有理几何体](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-16E7FEFA-8D13-4B1C-96C1-4B6B1485EB05.htm)

- [更改曲线或曲面的次数或跨距数/面片数](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-9D171E9B-AE5F-4C26-8B96-D8F3DEB85724.htm)

- [将一条曲线的拓扑与另一条曲线匹配](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-71E4B341-B523-4CC0-8E24-BFAABB1B5F99.htm)
