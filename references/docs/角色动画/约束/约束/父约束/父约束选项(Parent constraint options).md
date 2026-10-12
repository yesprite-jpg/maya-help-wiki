# 父约束选项(Parent constraint options)

- 在“动画”(Animation)或“装备”(Rigging)菜单集中：“约束 > 父对象”(Constrain > Parent) > ![图：在“动画”(Animation)或“装备”(Rigging)菜单集中：“约束 父对象”(Constrain Parent…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 583 字 ≥300，非承重" -->

#### 保持偏移(Maintain Offset)

保持受约束对象的原始状态（约束之前的状态）、相对平移和旋转。使用该选项可以保持受约束对象之间的空间和旋转关系。请参见[偏移父约束](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E6658A95-7702-4BB1-BE19-15DFDE2A335E.htm)。

#### 分解附近对象(Decompose near object)

如果受约束对象与目标对象之间存在旋转偏移，则激活此选项可找到接近受约束对象（而不是目标对象（默认））的旋转分解。

#### 动画层(Animation Layer)

使用该选项可以选择要添加父约束的动画层。有关详细信息，请参见[创建父约束](创建父约束.md)。

#### 将层设置为覆盖(Set Layer To Override)

启用时，在“动画层”(Animation Layer)下拉列表中选择的层会在将约束添加到动画层时自动设定为“覆盖”(Override)模式。这是默认模式，也是建议使用的模式。禁用时，在添加约束时层模式会设定为“相加”(Additive)模式。详细信息请参见[为动画层添加约束](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B865F8D9-AE8E-47F7-AFB4-DFF9D6A17DB4)。

请参见[动画层模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BBCA0BC3-7608-4E86-8E9F-B4099C316156)。

#### 约束轴(Constraint Axes)

决定父约束是受特定轴（“X”、“Y”、“Z”）限制还是受“全部”(All)轴限制。如果选中“全部”(All)，“X”、“Y”和“Z”框将变暗。

#### 权重(Weight)

仅当存在多个目标对象时，权重才有用。

## 相关主题

- [创建父约束](创建父约束.md)
