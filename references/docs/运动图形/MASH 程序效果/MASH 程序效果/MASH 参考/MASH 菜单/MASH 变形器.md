# MASH 变形器

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-BAB94F44-886A-421D-B338-126011EFD794.gif) <!-- baize:img-hook downloaded=false reason="正文 577 字 ≥300，非承重" -->

允许您使用 MASH 网络将网格上的顶点或面变形。

## 变形器节点

#### 变形器类型(Deformer Type)

确定要变换的输入网格上的组件类型。

#### 面位置(Face Position)、面旋转(Face Rotation)、面缩放(Face Scale)

确定将受到影响的变换属性。请注意，即使“变形器类型”(Deformer Type)未设置为“面”(Face)，这些设置仍然有效。

#### 封套网格(Envelope Mesh)

启用后，当“强度”(Strength) 降低时，会导致整个网格收缩至无。

## 强度

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
