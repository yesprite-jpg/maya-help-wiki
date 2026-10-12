# “线衰减定位器”(Wire Dropoff Locator)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (编辑)线 > 线衰减定位器”(Deform > (Edit) Wire > Wire Dropoff Locator) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (编辑)线 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 495 字 ≥300，非承重" -->

将当前线变形器曲线点设定为线衰减定位器。请参见[将线衰减定位器用于局部变形效果](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-F75CADC0-499C-4C8D-A4B6-4ED2087EDFDF.htm#WS17956D7ADBC6E7369774A83117AE3109E1-7FF2)和[添加线衰减定位器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7EB9325E-DD1A-43E2-8584-2E27D65E4091.htm#WS1A9193826455F5FF6026605B1181C8F4F2E-39D9)。

#### 线节点(Wire Node)

指定线变形器的名称。此外，如果从“现有节点”(Existing Node)下拉菜单中选择线变形器的名称，那么所选择的变形器的名称会显示在该字段中。

#### 现有线节点(Existing Wire Nodes)

列出场景中的当前线变形器。在“线节点”(Wire Node)字段中将显示从该列表中选择的线变形器的名称。

#### 封套(Envelope)

为线衰减定位器指定变形比例因子。该属性与“定位器封套”(Locator Envelope)通道相对应。

#### 百分比(Percent)

指定线衰减定位器对影响线的衰减所具有的局部效果。默认情况下，影响线在每一端有两个隐式定位器，其默认“百分比”(Percent)为 1.000，而其他定位器具有一个相对于隐式定位器的“百分比”(Percent)的效果。
