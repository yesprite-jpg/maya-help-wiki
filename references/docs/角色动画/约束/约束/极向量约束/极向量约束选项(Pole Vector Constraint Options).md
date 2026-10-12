# 极向量约束选项(Pole Vector Constraint Options)

- 在“动画”(Animation)菜单集中：“约束 > 极向量”(Constrain > Pole Vector) > ![图：在“动画”(Animation)菜单集中：“约束 极向量”(Constrain Pole Vector)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 447 字 ≥300，非承重" -->

- 在“装备”(Rigging)菜单集中：“约束 > 极向量”(Constrain > Pole Vector) > ![图：在“装备”(Rigging)菜单集中：“约束 极向量”(Constrain Pole Vector)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 447 字 ≥300，非承重" -->

#### 权值

指定受约束极向量的结束位置受目标对象影响的程度。使用滑块选择 0.0000 到 10.0000 之间的值。默认值为 1.0000。

目标对象的权重指定受约束极向量的位置在多大程度上会受到目标对象的影响。权重是极向量约束的属性。对于每个目标对象，名为 *targetObject Wn* 的属性指定每个目标对象的权重。

默认情况下，权重设置为 1，这会使每个目标对象在受约束极向量的端点位置产生相同的影响。通过在“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)中编辑 *targetObject Wn* 属性，您可以更改权重，使某些目标对象的影响大于或小于其他对象的影响。有关更改 *targetObject Wn* 属性的信息，请参见[编辑极向量约束](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7BF41014-37D1-4AA3-92AB-EFBA863ED138.htm)。

### 相关主题

- [极向量约束](../极向量约束.md)

- [创建极向量约束](创建极向量约束.md)

- [编辑极向量约束](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7BF41014-37D1-4AA3-92AB-EFBA863ED138.htm)
