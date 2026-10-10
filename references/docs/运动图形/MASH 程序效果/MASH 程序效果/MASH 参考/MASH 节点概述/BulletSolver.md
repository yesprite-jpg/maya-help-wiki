# BulletSolver

确定 [MASH 动力学](动力学.md)模拟的动力学特性并定义其碰撞对象和场。将“动力学”(Dynamics)节点指定给 MASH 网络时，系统会自动创建其中一个属性。

**注**

此节点显示在

“大纲视图”(Outliner)

中，而非

“MASH 编辑器”(MASH Editor)

中。

## 解算器设置

#### 开始帧(Start Frame)

确定动力学模拟的开始帧。

#### 碰撞迭代(Collision Iterations)

确定每帧的碰撞计算次数。值越大，碰撞越精确，但性能会因此而降低。

#### 内部帧速率(Internal Frame Rate)

确定模拟的帧速率。值越大，模拟越精确，但性能会因此而降低。

#### 碰撞边界(Collision Margin)

指定 MASH 对象将围绕边界框发生碰撞的区域。

#### 重力(Gravity)

指定模拟的重力方向。

### 地面(Ground)

#### 地面(Ground)

启用 MASH 对象将在其中发生碰撞的不可见地平面。

#### 位置(Position)

确定“地平面”(Ground Plane)在 3D 空间中的位置。

#### 摩擦力(Friction)

确定 MASH 对象在“地平面”(Ground Plane)上滑动的难易程度。

#### 反弹(Bounce)

确定 MASH 对象在撞击“地平面”(Ground Plane)之后反弹的高度。

#### 阻尼(Damping)

减弱地平面的效果。增加该值可减弱地平面属性的效果。

#### 地平面上方向向量(Ground Plane Up Vector)（位于“附加属性”(Extra Attributes)部分）

确定地平面的方向。

#### 交互遮罩

这可用于自定义特定点或点范围（通过其 ID）的碰撞行为。

#### 接触遮罩层(Contact Mask Layers)

指定启用“从碰撞发射”(Emit From Collisions)时不会生成点的层。

#### 碰撞组层(Collision Group Layers)

指定地面所属的层。

#### 碰撞遮罩层(Collision Mask Layers)

指定可以与地面碰撞的层。

### 碰撞对象(Collider Objects)

列出场景中可与 MASH 网络碰撞的网格。您可以使用鼠标中键将现有场拖动到“场”(Fields)列表中，或者选择这些场，然后单击鼠标右键并选择“连接”(Connect)。还可以选择现有条目，然后单击鼠标右键将其显示在“大纲视图”(Outliner)中，或者断开它们与模拟的连接。

向此列表添加网格时，还会将 MASH 分段添加到其各自的形状节点。

**注**

若要将对象与更复杂的动画碰撞，建议先将对象放入单独的 MASH 网络中，然后再在其中为对象设置动画。这将确保碰撞对象按照与其发生碰撞的 MASH 网络相同的子步间隔进行更新。（无需将碰撞的 MASH 网络添加到

“碰撞对象”(Collider Objects)

列表中。只要它们使用相同的 Bullet 解算器，便会自动发生碰撞。）

### 场(Fields)

确定当前影响模拟的[场](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-85AEE528-4477-46DF-8B9E-2E8AEC3C8784)。您可以使用鼠标中键将现有场拖动到“场”(Fields)列表中，或者选择这些场，然后单击鼠标右键并选择“连接”(Connect)。还可以选择现有条目，然后单击鼠标右键将其显示在“大纲视图”(Outliner)中，或者断开它们与模拟的连接。

### 从碰撞发射(Emit From Collisions)

将“动力学”(Dynamic)节点的[从碰撞发射(Emit From Collisions)](动力学.md)属性创建的稳定点提供给指定的 MASH Waiter。借助此选项，您可以使用一个 MASH 网络的碰撞在另一个 MASH 网络中创建新点。

### 调试(Debugging)

#### 绘制样式(Draw Style)

确定如何在“视口”(Viewport)中显示调试信息。

#### 碰撞形状(Collision Shapes)

显示每个对象的边界框，用于确定“调试绘制样式”(Debug Draw Style)中的碰撞。

#### 刚体颜色(Rigid Body Color)、睡眠刚体颜色(Sleeping Rigid Body Color)

将调试颜色指定给活动对象和非活动对象。

#### 地面(Ground)

显示“地平面”(Ground Plane)的位置。

#### 约束(Constraints)

将对象之间的约束显示为彩色线。

#### 碰撞位置(Collision Positions)

启用“动力学”(Dynamic)节点的[从碰撞发射(Emit From Collisions)](动力学.md)属性时，在碰撞点处以“线颜色”(Line Color)显示点。

#### MASH 力方向(MASH Force Direction)

将作用于每个对象的净力方向显示为从每个对象中心发出的彩色线。

#### 线宽(Line Thickness)

确定线宽，用于显示调试信息。

#### 线颜色(Line Color)

确定线颜色，用于显示约束和力向量调试信息。
