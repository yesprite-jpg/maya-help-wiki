# Merge

## MASH 合并

#### 合并类型(Merge Type)

确定用于合并 MASH 网络的方法。选项包括：

- Crossfade：从一个网络褪色至另一个网络。

- 相加(Add)：将子网络的属性添加到父网络。

- 相减(Subtract)：从子网络中减去父网络的属性。

#### 合并位置(Merge Position)、合并旋转(Merge Rotation)、合并缩放(Merge Scale)、合并 ID (Merge Id)、合并可见性(Merge Visibility)

指定两个网络之间要合并的通道。

#### 父节点(Parent Node)

显示合并操作的主节点。

#### 子节点(Child Node)

显示合并操作的次节点。

#### 旋转类型(Rotation Type)

- 矩阵 Lerp(Matrix Lerp)：线性插值。

- 四元数球面线性插值(Quaternion Slerp)：球形线性插值。

## 强度

#### 强度(Strength)

控制网络之间的融合量。值越小，表示子网络的影响越大。

#### 随机强度(Random Strength)

控制添加到合并的随机度量。

#### 阶跃强度(Step Strength)

每次禁用一个对象的节点效果。

#### 强度贴图(Strength Map)

确定输入文件（2D 纹理、动画纹理等）来控制该节点的效果的形状。

#### 贴图投影轴(Map Projection Axis)

确定投影“强度贴图”(Strength Map)时所沿的轴。

#### 贴图辅助对象(Map Helper)

显示用于在场景中交互放置“强度贴图”(Strength Map)的对象。可以在该字段上单击鼠标右键来创建新的辅助对象（平面）（如果不存在）。还可以使用鼠标中键将网格拖入此字段，或者单击鼠标右键连接选定网格。如果网格已连接，还可以单击鼠标右键来断开其连接或者将其显示在大纲视图中。

**注**

为获得最佳结果，请将相同的纹理指定给

“强度贴图”(Strength Map)

和

“贴图辅助对象”(Map Helper)

（在创建新的辅助对象时将自动执行此操作）。
