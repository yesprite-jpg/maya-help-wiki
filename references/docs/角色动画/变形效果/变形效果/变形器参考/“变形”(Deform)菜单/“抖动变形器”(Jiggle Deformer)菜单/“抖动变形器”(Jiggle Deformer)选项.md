# “抖动变形器”(Jiggle Deformer)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)抖动 > 抖动变形器”(Deform > (Create) Jiggle > Jiggle Deformer) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)抖动…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 625 字 ≥300，非承重" -->

**注**

有关创建

抖动

变形器的信息，请参见

创建抖动变形器

。

## “基本”(Basic)选项卡

#### 刚度(Stiffness)

设定抖动的刚性，值范围是从 0 到 1。较高的值会减小弹性、加速抖动，导致点行为类似于受紧密弹簧控制。较低的值会减慢抖动速度，产生类似于海绵弹簧的效果。

#### 阻尼(Damping)

禁用抖动的弹性。较高的值将最大程度减小抖动。较低的值将增加弹性。

#### 权重(Weight)

按比例增大或减小所有点上的抖动，无论各个权重如何。各个抖动权重不会更改值，仅更改抖动的总量。

#### 仅在对象停止时抖动(Jiggle Only When Object Stops)

仅在移动的对象停止时（不是在其移动时）发生抖动。

#### 忽略变换(Ignore Transform)

抖动仅适用于已设置动画的点，不适用于对象的已设置动画的变换节点。例如，假定您已经设置袋鼠说话的同时跳跃的动画。通过为变换节点的平移属性设置关键帧，您设置了跳跃运动的动画，并通过为嘴部的点设置关键帧设置了移动嘴部的动画。如果启用“忽略变换”(Ignore Transform)，则只有正在讲话的嘴部抖动。

## “高级”(Advanced)选项卡

“高级”选项卡中的各个选项为所有变形器所共有。请参见[“高级”(Advanced)变形器选项](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3D228DBA-C968-4870-9B1D-8C2C60DE6970.htm)。
