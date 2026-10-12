# bend

选择 bend 变形器节点作为[“通道盒”(Channel Box)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4C954FB2-8B6A-4BBD-9695-DF432616D0D2)中弯曲节点的“输入”(INPUTS)时，以下属性将显示在[“属性编辑器”(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)的“非线性变形器属性”(Nonlinear Deformer Attributes)区域中。也可以在使用[创建弯曲变形器选项](../“变形”%28Deform%29菜单/“非线性”%28Nonlinear%29菜单/“弯曲”%28Bend%29选项.md)（“变形 > (创建)非线性 > 弯曲”(Deform > (Create) Nonlinear > Bend) > ![图：选择 bend 变形器节点作为“通道盒”(Channel Box)中弯曲节点的“输入”(INPUTS)时，以下属性将显示…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 488 字 ≥300，非承重" -->）创建弯曲节点时设置这些属性。

#### 曲率(Curvature)

指定弯曲量（以度为单位）。负值指定朝着弯曲变形器的负 X 轴弯曲。正值指定朝着变形器的正 X 轴弯曲。使用滑块选择介于 -230 到 230 之间的值。默认值为 0，表示不指定任何弯曲。

#### 下限(Low Bound)

指定沿弯曲变形器的负 Y 轴弯曲的下限。值可以是负数或零。值可以是负数或零。使用滑块在 -10.0000 到 0.0000 的范围内选择值。默认值为 -1.0000。

#### 上限(High Bound)

指定沿弯曲变形器的正 Y 轴弯曲的上限。值只能是正数（最小值为 0.0000）。使用滑块在 0.0000 到 10.0000 的范围内选择值。默认值为 1.0000。

## 相关主题

- [创建弯曲变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-71522A4F-F800-46CC-AF53-FD246E89EC8B.htm)
