# 绘制集成员身份工具(Paint Set Membership Tool)

- 在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 > (绘制权重)集成员身份”(Deform > (Paint Weights) Set Membership) > ![图：在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 (绘制权重)集成员身份”(Deform (…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1050 字 ≥300，非承重" -->

- 在“动画”(Animation)菜单集中：“动画变形 > 打开完整的变形菜单 > (绘制权重)集成员身份”(Anim Deform > Open Full Deform Menu > (Paint Weights) Set Membership) > ![图：在“动画”(Animation)菜单集中：“动画变形 打开完整的变形菜单 (绘制权重)集成员身份”(Anim Defor…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1050 字 ≥300，非承重" -->

使您能够使用“绘制集成员身份工具”(Paint Set Membership Tool)，通过绘制希望添加到集、传递到集或从集中移除的点，修改可变形对象的哪些点（例如，CV 或顶点）属于多个变形器集。请参见[绘制变形器集成员身份](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-440424C1-C207-496F-8945-851ACCD04779.htm)。请参见手册的 Maya®Artisan™ 部分中的[编辑变形器集成员身份](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E4211EA1-D15E-4603-BCDA-CADE1CEE74C5.htm)和 [Artisan 笔刷工具的工作方式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D0A5ACD2-8D10-4B51-ADD3-E261F9337B07)。

在“绘制操作”(Paint Operations)区域中，有一些“绘制集成员身份工具”(Paint Set Membership Tool)所特有的属性。在下面介绍这些特有属性。有关所有其他区域中所有其他属性的描述，请参见手册的“Artisan”部分中的 [Artisan 工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67B8F095-4A0E-4BAE-938C-CB41B3EBD533)。

## “绘制集成员身份工具”(Paint Set Membership tool)设置

### 绘制操作(Paint Operations)

以下是“绘制操作”(Paint Operations)区域中属性的描述。

#### 添加(Add)

如果对象包含多个变形器集，“添加”(Add)操作会将绘制的 CV 或顶点保留在当前集中，并将其添加到选定集。

如果对象是刚性蒙皮对象，那么“添加”(Add)操作与“传递”操作执行相同的操作：将绘制的 CV 或顶点从当前集中移除，并将其添加到选定集。

#### 传递(Transfer)

如果对象包含多个变形器集，“传递”(Transfer)操作会将绘制的 CV 或顶点从当前集中移除，并将其添加到选定集。

如果对象是刚性蒙皮对象，那么“传递”(Transfer)操作与“添加”(Add)操作执行相同的操作：将绘制的 CV 或顶点从当前集中移除，并将其添加到选定集。

#### 删除(Remove)

“移除”(Remove)操作会将绘制的 CV 或顶点从它们所属的集中移除，从而使这些 CV 或顶点不受任何变形器或关节的影响。

#### 选择要修改的集(Select Set To Modify)

单击要添加到、传递到或从中移除的集的名称。这只是选择集的一种方式。另外还有两种方式。有关详细信息，请参见[删减变形器集成员身份](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-BF580532-BE5D-4401-A812-46873B145C73.htm)。

#### 要修改的集(Set To Modify)

所选择的集的名称会显示在该框中。
