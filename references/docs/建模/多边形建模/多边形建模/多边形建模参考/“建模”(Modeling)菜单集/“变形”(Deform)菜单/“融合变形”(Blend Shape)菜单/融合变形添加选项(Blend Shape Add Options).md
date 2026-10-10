# 融合变形添加选项(Blend Shape Add Options)

- 在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 > (编辑)融合变形 > 添加”(Deform > (Edit) Blend Shape > Add) > ![图：在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 (编辑)融合…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1347 字 ≥300，非承重" -->

此命令可将目标对象添加到基础对象上的融合形变变形（请参见[基础形状、目标形状和融合变形](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-01EFEC6D-41EA-46AA-81B1-C171DA4316F4)）。这将为目标对象创建目标形状。有关详细信息，请参见[添加目标形状](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E980D990-53FC-47C9-B9B8-C8451E933665)。

#### 指定节点(Specify Node)

如果所选择的基础对象形状仅受一个融合形变变形器影响，则不需要启用“指定节点”(Specify Node)。如果启用，则可以指定“融合变形节点”(BlendShape Node)和“现有节点”(Existing Nodes)。默认情况下会禁用“指定节点”。

#### 融合变形节点(BlendShape Node)

指定希望将目标对象形状添加到的融合形变变形器的名称。仅当启用“指定节点”(Specify Node)时，“融合变形节点”(BlendShape Node)才可用。

#### 现有节点(Existing Nodes)

列出场景中的所有融合形变变形器节点，并指示要将目标对象形状添加到的融合形变变形器。仅当启用“指定节点”(Specify Node)时，“现有节点”(Existing Nodes)才可用。

#### 添加中间目标(Add In-Between Target)

指定是否要指定“目标索引”(Target Index)和“中间权重”(In-between weight)。通常需要指定“目标索引”(Target Index)和“中间”(InBetween)权重来控制要添加的目标对象形状的效果。

#### 目标索引(Target Index)

如果融合形变变形器以并行方式融合目标对象形状（创建融合形变变形器时，禁用了“中间”(In-Between)创建选项），则可以添加新的目标对象形状，使它们可以与其中一个现有目标对象形状串行工作。为“目标索引”(Target Index)确定适当值的一种快速方法是：在形变编辑器（“窗口 > 动画编辑器 > 形变编辑器”(Windows > Animation Editors > Shape Editor)）中查看目标滑块的顺序。在该编辑器中，每个目标对象的形状都有自己的权重滑块。在编辑器中，从左往右看，最左侧的目标滑块的“目标索引”(Target Index)值是 1，下一个是 2，依此类推。

如果融合形变变形器串行融合目标对象形状（创建融合形变变形器时，启用了“中间”(In-Between)创建选项），“目标索引”(Target Index)只能是 1，因为仅有一个目标滑块。这种情况下，不必指定“目标索引”(Target Index)，但是需要指定“中间权重”(In-Between Weight)。

#### 中间权重(In-Between Weight)

指定权重，在该权重下，添加的目标对象形状将具有最大的影响。使用滑块选择从 0 到小于 1 的任何值之间的值。不要选择 1，因为 1 是现有目标对象形状具有其最大影响的权重。

#### 目标形状选项(Target Shape Options)

指定是否检查添加的目标对象形状与基础对象和现有目标对象具有相同的拓扑。例如，如果使用 NURBS 对象，可以检查是否所有形状具有相同的 CV 数量。单击“检查拓扑”(Check Topology)可启用（默认）或禁用它。
