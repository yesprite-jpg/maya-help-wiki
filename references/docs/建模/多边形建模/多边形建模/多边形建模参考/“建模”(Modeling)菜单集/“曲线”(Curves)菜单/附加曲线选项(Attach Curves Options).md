# 附加曲线选项(Attach Curves Options)

使用以下选项可设置在选择“曲线 > 附加”(Curves > Attach)时发生的情况。

### 附加方法(Attach Method)

选择两条曲线的接合点的外观。

#### 连接(Connect)

接合曲线，并在接合点处进行最小曲率平滑处理。

#### 融合(Blend)

基于“融合偏移”(Blend Bias)值对接合点处的曲率进行平滑处理。

#### 多点结(Multiple Knots)

“保持”(Keep)可在接合点处创建多点结。这可用于打破接合点处的曲率连续性。

“移除”(Remove)可丢弃接合点处的多点结。这将在接合点处创建平滑曲率。

#### 融合偏移(Blend Bias)

调整接合点处的连续性。

#### 插入结(Insert Knot)

该选项仅在使用“融合”(Blend)选项时可用。将“插入结”(Insert Knot)与“插入参数”(Insert Parameter)值一起使用，可以使融合区域与原始曲线更匹配。

只有在原始曲线没有精确对齐（它们以一个角度相互靠近）且每个原始曲面上接近接合点的最后两个结之间具有较长距离的情况下，该选项才具有明显效果。

“插入结”(Insert Knot)可在接合点附近创建两个附加结。每个结位于从原始曲线接合的点的一个跨度内。可以使用“插入参数”(Insert Parameter)值调整附加结的位置。

#### 插入参数(Insert Parameter)

启用“插入结”(Insert Knot)时调整已添加结的位置。值越接近 0（没有达到 0），接合点处的融合变形与原始曲线的曲率越相似。发生这种情况的原因是已添加结的插入位置离距离融合点最近的末端结较近。有效值从 0 到 1。

下列插图显示由两个相同输入曲线生成的同一融合曲线。顶部融合曲线禁用了“插入结”(Insert Knot)。底部融合曲线启用了“插入结”(Insert Knot)，且“插入参数”(Insert Parameter)值为 0.3。“插入参数”(Insert Parameter)越接近 0，融合曲线与原始曲线的末端形状越相似。

![图：启用“插入结”(Insert Knot)时调整已添加结的位置。值越接近 0（没有达到 0），接合点处的融合变形与原始曲线…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-B9D2F43E-A14A-4652-829E-EB99125323EC.png) <!-- baize:img-hook downloaded=false reason="正文 1335 字 ≥300，非承重" -->

若要以交互方式调整该选项，请在启用“插入结”(Insert Knot)的情况下创建融合曲线。然后选择曲线，显示“通道盒”(Channel Box)，并在“输入”(INPUTS)区域中选择 attachCurve，然后编辑“参数”(Parameter)选项。

#### 保持原始(Keep Originals)

创建附加曲线后保持原始曲线。如果“构建历史”(construction history)处于启用状态，请不要启用该选项；如果缩放或修改附加曲线，其将进行奇怪的变形。

如果要缩放附加曲线，而不更改其基础形状，请确保“构建历史”(construction history)和“保持原始”(Keep Original)同时处于禁用或启用状态。

## 编辑生成的曲线属性

若要查看和编辑附加曲线的选项，请选择曲线，显示“通道盒”(Channel Box)，然后在“输入”(INPUTS)区域中选择 attachCurve。下列选项是唯一一个不可在选项窗口中使用的选项：

#### 反转 1 和反转 2 (Reverse 1 & 2)

“附加曲线”(Attach Curves)附加曲线最近的两端。可以使用这些选项更改要附加的末端。按不同的组合方式启用和禁用选项，直到获得所需的结果。

## 相关主题

- [将曲线或曲面接合在一起](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-B7E89364-3FA9-4D6B-96FD-1934E4F6C47C.htm)
