# jiggle

## 抖动属性(Jiggle Attributes)

#### 启用(Enable)

选择下列选项之一：

#### 启用(Enable)

此抖动变形器已启用。启用是默认设置。

#### 禁用(Disable)

此抖动变形器已禁用。

#### 仅在对象停止后启用(Enable Only After Object Stops)

设定仅在移动对象停止后抖动，而不是在对象移动时抖动。

#### 刚度(Stiffness)

请参见[刚度](../“变形”%28Deform%29菜单/“抖动变形器”%28Jiggle%20Deformer%29菜单/“抖动变形器”%28Jiggle%20Deformer%29选项.md)。

#### 阻尼(Damping)

请参见[阻尼](../“变形”%28Deform%29菜单/“抖动变形器”%28Jiggle%20Deformer%29菜单/“抖动变形器”%28Jiggle%20Deformer%29选项.md)。

#### 抖动权重(Jiggle Weight)

请参见[权重](../“变形”%28Deform%29菜单/“抖动变形器”%28Jiggle%20Deformer%29菜单/“抖动变形器”%28Jiggle%20Deformer%29选项.md)。

#### 沿法线的力(Force Along Normal)

设定曲面法线方向的抖动幅度。

#### 切线上的力(Force On Tangent)

设定曲面切线方向的抖动幅度。

#### 运动倍增(Motion Multiplier)

如果选择“仅在对象停止后启用”(Enable Only After Object Stops)（请参见[启用](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-39732E56-1759-4F21-B45C-4BE9F9E6896A.htm#WS1A9193826455F5FF-2ADE9D91187AB69A93-4021)），“运动倍增”(Motion Multiplier)会根据对象在停止移动后的抖动幅度缩放。

#### 方向偏移(Direction Bias)

设定曲面相对于其法线方向的抖动方向。“方向偏移”(Direction Bias)为 1.000 将导致抖动变形的曲面仅沿其法线方向移动，“方向偏移”(Direction Bias)为 -1.000 将导致抖动变形的曲面仅沿其法线反方向移动。“方向偏移”(Direction Bias)为 0.000 将导致抖动变形的曲面沿两个方向移动。默认“方向偏移”(Direction Bias)值为 0.000。

![图：设定曲面相对于其法线方向的抖动方向。“方向偏移”(Direction Bias)为 1.000 将导致抖动变形的曲面仅沿…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-CF929BA3-A5E3-4915-9C8C-12232D015603.png) <!-- baize:img-hook downloaded=false reason="正文 913 字 ≥300，非承重" -->

您可以使用“方向偏移”(Direction Bias)属性来防止任何不想要的抖动变形曲面收拢。例如，如果正在为相扑抖动的胃制作动画，可以将“方向偏移”(Direction Bias)属性的值设定为 1.000，以便该角色的胃的曲面只向外抖动。

#### 忽略变换(Ignore Transform)

请参见[忽略变换](../“变形”%28Deform%29菜单/“抖动变形器”%28Jiggle%20Deformer%29菜单/“抖动变形器”%28Jiggle%20Deformer%29选项.md)。

## 磁盘缓存属性(Disk Cache Attributes)

#### 磁盘缓存(Disk Cache)

如果已为该抖动节点控制的抖动动画创建抖动缓存，该字段将显示抖动缓存节点的名称。可以单击名称右侧的箭头按钮来查看抖动缓存设置。请参见[为抖动变形器创建磁盘缓存](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-76E1987D-CF05-4E84-9D50-CD651A1E1F8B.htm#WS1A9193826455F5FF6026605B1181C8F4F2E-3DD3)。

**注**

重要：

若要避免意外的变形，创建抖动变形器后请勿更改可变形对象的点的数量。
