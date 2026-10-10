# MASH 抖动变形器

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-AE2ADBA0-145F-4AFA-9E6F-360851DF4609.gif) <!-- baize:img-hook downloaded=false reason="正文 629 字 ≥300，非承重" -->

使网格上的点在移动时振动。但与常规“抖动变形器”(Jiggle Deformer)不同，此抖动可与 MASH 衰减对象、贴图等进行交互。它不需要使用 MASH 网络。

## 抖动变形器

#### 阻尼(Damping)

禁用抖动的弹性。较高的值会减小弹性（振动频率）。

#### 刚度(Stiffness)

设置抖动的刚性。较高的值会减小弹力（振动距离）。

#### 平行抖动(Directional Jiggle)

进一步沿移动方向拉伸抖动。

#### 法线强度(Normal Strength)

确定抖动点朝其曲面法线方向偏移的精确程度。较高的值会使点保持沿其法线移动。

#### 最大速度(Max Velocity)

确定点在抖动期间可移动的最大速度。

### 强度

#### 强度(Strength)

同时减弱对所有顶点的节点效果。

#### 随机强度(Random Strength)

按随机顺序平滑地减弱顶点的节点效果。

#### 阶跃强度(Step Strength)

每次禁用一个顶点的节点效果。

#### 强度贴图(Strength Map)

确定输入文件（2D 纹理、动画纹理等）来控制该节点的效果。

#### 贴图投影轴(Map Projection Axis)

确定投影“强度贴图”(Strength Map)时所沿的轴。

#### 贴图辅助对象(Map Helper)

显示用于在场景中交互确定随机影响的对象。

#### 创建贴图辅助对象(Create Map Helper)

创建新的定位器，并将其连接到“贴图辅助对象”(Map Helper)。

#### 连接贴图辅助对象(Connect Map Helper)

将选定对象连接到“贴图辅助对象”(Map Helper)。
