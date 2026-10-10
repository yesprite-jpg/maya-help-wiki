# 重建曲面选项(Rebuild Surface Options)

使用以下选项可设置在选择“曲面 > 重建”(Surfaces > Rebuild)时发生的情况。

#### 重建类型(Rebuild Type)

“重建曲面”(Rebuild Surface)选项窗口根据您选择的“重建类型”(Rebuild Type)选项显示不同的选项：

#### 一致(Uniform)

使用“一致”(Uniform)选项重建具有一致参数化的曲面。您可以使用该选项更改曲面的“跨度数(Number of Spans)和“次数”(Degree)。

#### 减少(Reduce)

如果选择“减少”(Reduce)选项，Maya 会在其移除操作不会导致任何剩余结移动大于“容差”(Tolerance)设置的距离时移除结。“容差”(Tolerance)设置的值越大，将移除的结就越多。

#### 匹配结(Match Knots)

通过匹配另一个曲面的曲线次数、结值以及跨度数和分段数来重建曲面。在重建曲面之前，首先选择要重建的曲面，然后按住 Shift 键并选择要匹配的曲面。“保持”(Keep)选项在您选择“匹配结”(Match Knots)时变为可用。

将[重建方法](重建曲面选项%28Rebuild%20Surface%20Options%29.md#WS73099CC142F48755-3D114B751181C40F14B1DAF)设定为“匹配”可生成质量更好的曲面。

#### 无多个结(No Multiple Knots)

移除在重建操作期间创建的任何附加结。结果曲面与原始曲面的曲线次数相同。在您选择该选项时，“保持”(Keep)选项不可用。

#### 非有理(Non-Rational)

选择“非有理”(Non-Rational)以将有理曲面重建为非有理曲面。有理曲面的 CV 的权重不全都等于 1。非有理曲面的 CV 的权重全都等于 1。结果曲面与原始曲面的次数相同。在您选择该选项时，“保持”(Keep)选项不可用。

默认情况下，Maya 创建其所有 CV 的权重都等于 1 的曲面。其他软件包，特别是设计包，可能会创建其 CV 的权重不等于 1 的曲面。“非有理”(Non-Rational)选项在您从这种包导入曲面时非常有用。

某些设计包使用不等于 1 的权重是因为它们允许更精细的曲面精度。因为 Maya 主要用于娱乐活动，所以通常不需要使用极端精度。如果将已导入的曲面重建为具有相同权重，Maya 会更快速地处理有关曲面的后续工作，同时仍提供精确的精度。

#### 结束条件(End Conditions)

重建曲面的末端 CV 和结的位置。如果选择“结束条件”(End Conditions)，将针对“结束条件”(End Conditions)显示两个附加选项：“无多个结”(No Multiple knots)和“多点结”(Multiple knots)。

当“无多个结”(No Multiple Knots)处于启用状态时，重建的曲面不会通过末端 CV。在某些情况下这会使曲面更难控制，但会使其他操作更加简单。例如，将更易于在相邻曲面之间创建平滑接合。（如果重建两个类型为“无多个结”(No Multiple Knots)的曲面，您可以将 CV 捕捉到一起以获得跨边界的精确切线。）

如果启用“多点结”(Multiple Knots)，曲面将触动末端 CV，使其更易于控制曲面边界和相关切线。

使用“结束条件”(End Conditions)重建的曲面的次数与原始曲面相同。

#### 修剪转化(Trim Convert)

将单区修剪曲面（包含 4 条边界曲面）重建为非修剪曲面。

#### Bezier

将曲面重建为“Bezier”曲面。如果希望使用“Bezier”曲面而不是 NURBS 曲面，请考虑使用该选项来转化曲面。

#### 参数范围(Parameter Range)

三个“参数范围”(Parameter Range)选项用于指定 U 和 V 参数在重建期间如何受到影响。

如果希望结果曲面的 U 和 V 参数在 0 到 1 之间运行，请选择“0 到 1”(0 to 1)。

如果希望重建的曲面的 U 和 V 参数范围与原始曲面的 U 和 V 参数范围匹配，请选择“保持”(Keep)。

如果希望结果曲面的跨度数为您提供整型结值，请选择“0 到跨度数”(0 to #Spans)。这些值将更便于数值输入。如果使用“一致”(Uniform)重建类型，该选项将始终为您提供整型结值。例如，如果要使用“分离”(Detach)并希望键入一个值，则输入数字 2 比输入类似 0.362 的值更容易。

#### 方向(Direction)

“方向”(Direction)选项（U、V、U 和 V）用于确定将为其移除结的曲面的参数化方向。例如，如果选择 U 且重建类型为“无多个结”(No Multiple Knots)，则重建曲面时将仅移除 U 方向中的多点结。“U 和 V”是默认值。

**注**

对周期曲面执行一致曲面重建会始终将曲面重建为在这两个方向上保持一致，而不考虑曲面方向的设置。

#### 保持(Keep)

重建曲面可能会更改 3D 中的曲面。使用“保持”(Keep)选项以确保重建的曲面与输入（或原始）曲面一致。

启用“角点”(Corners)以确保新曲面的角点与原始角点位于同一 3D 点处。启用“CV”以指定是否要保留原始曲面的“CV”。

“跨度数”(NumSpans)为重建的曲面提供的跨度数与原始曲面的跨度数相同。

#### 重建方法(Rebuild Method)

将“重建方法”(Rebuild Method)设定为“匹配”(Match)可生成质量更好的曲面，特别是当重建或引用曲面是周期曲面或这两个曲面的末端都没有多点结时。

将“重建方法”(Rebuild Method)设定为“经典”(Classic)生成的结果与在 Maya 5.0 和早期版本中相同。

#### U 向跨度数(Number of Spans U)/V 向跨度数(Number of Spans V)

如果重建类型是“一致”(Uniform)，则结果曲面中的跨度数可由在“U 向跨度数”/“V 向跨度数”(Number of Spans U/V)框中输入的值设定。

#### U 向次数(Degree U)/V 向次数(Degree V)

结果曲面的次数由您选择的“U 向次数”(Degree U)或“V 向次数”(Degree V)确定。

如果启用“原始”(Original)，则重建的曲面与原始曲面的 U 向/V 向次数相同。

请注意，您可以将“U 向次数”(Degree U)或“V 向次数”(Degree V)设定为“原始”(Original)并将“保持”(Keep)设定为“跨度数”(NumSpans)，以便为具有不同跨度数的多个曲面创建一致重建。

![图：结果曲面的次数由您选择的“U 向次数”(Degree U)或“V 向次数”(Degree V)确定。 如果启用“原始”(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-F4784383-F0A9-4B3F-90E5-FF8F7430346B.png) <!-- baize:img-hook downloaded=false reason="正文 3121 字 ≥300，非承重" -->

#### 保持原始(Keep Original)

保留重建的曲面的原始曲面。如果“保持原始”(Keep Original)处于启用状态，则您可以看到结果曲面与原始曲面的偏差。

#### 使用容差(Use Tolerance)

该选项仅在启用“非有理”(Non-Rational)或“减少”(Reduce)时可用。它设定原始曲面和重建的曲面上的任何点之间的最长距离。容差越小，重建的曲面与原始曲面就越相似。较小的容差可创建许多面片，这将缩短您使用曲面时的处理时间。

“全局”(Global)使用“首选项”(Preferences)窗口中的“位置”(Positional)值。“局部”(Local)允许您在该窗口中直接输入容差。

#### 输出几何体(Output Geometry)

指定创建的几何体类型。（“Subdiv”表示“细分曲面”(Subdiv)。）

#### 输入曲面(Input Surface)

“输入曲面”(Input Surface)信息为只读信息。它允许您访问重建的曲面的历史。单击箭头按钮以选择曲面，然后打开“属性编辑器”(Attribute Editor)的相应区域。

#### 匹配曲面(Match Surface)

如果存在多个曲面且“匹配结”(Match Knots)在重建曲面时已启用，则您也可以访问“匹配曲面”(Match Surface)重建的曲面。

## 相关主题

- [减少曲线或曲面的复杂性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-24DF5B14-6A5A-434E-9693-2318400BC32B.htm)

- [控制多点结和 CV 硬度](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-3CDB7E68-05B8-4546-965A-93D6F16B723D.htm)

- [将曲线或曲面转化为一致参数化](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-5EE99036-5A55-48F3-88AB-DE2A4D729623.htm)

- [将曲面转化为非有理几何体](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-16E7FEFA-8D13-4B1C-96C1-4B6B1485EB05.htm)

- [更改曲线或曲面的次数或跨距数/面片数](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-9D171E9B-AE5F-4C26-8B96-D8F3DEB85724.htm)
