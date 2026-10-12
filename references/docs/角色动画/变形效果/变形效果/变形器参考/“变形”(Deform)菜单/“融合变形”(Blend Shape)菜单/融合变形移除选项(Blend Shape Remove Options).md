# 融合变形移除选项(Blend Shape Remove Options)

- 在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 > (编辑)融合变形 > 移除”(Deform > (Edit) Blend Shape > Remove) > ![图：在“动画”(Animation)、“绑定”(Rigging)和“建模”(Modeling)菜单集中：“变形 (编辑)融合…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 609 字 ≥300，非承重" -->

通过此命令，可以移除从目标对象（与具有融合形变变形器的基础对象关联）中创建的目标形状。还可以使用[形变编辑器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3C92402C-B24E-4874-AC8D-EADF976A19DC.htm)轻松删除目标形状。请参见[移除目标形状](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-319410C4-C127-4EB0-9104-5D693F38288F.htm)。

#### 指定节点(Specify Node)

如果选定的基础对象形状只受一个融合形变变形器的影响，则不需要将“指定节点”(Specify Node)设定为启用。如果启用，则可以指定“融合变形节点”(BlendShape Node)和“现有节点”(Existing Nodes)。默认设置为禁用。

#### 融合变形节点(BlendShape Node)

指定要移除其目标形状的融合形变变形器名称。（在“指定节点”(Specify Node)处于启用状态时可用。）

#### 现有节点(Existing Nodes)

列出场景中所有的融合形变变形器节点，并指示要移除其目标形状的融合形变变形器。仅在“指定节点”(Specify Node)处于启用状态时可用。

#### 指定目标(Specify Target)

启用后，从当前融合形变变形器中移除指定的目标形状。请参见[基础形状、目标形状和融合变形](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-01EFEC6D-41EA-46AA-81B1-C171DA4316F4.htm)。

#### 目标名称(Target Name)

列出要从当前融合形变变形器中移除的目标对象形状名称。仅在“指定目标”(Specify Target)处于启用状态时可用。
