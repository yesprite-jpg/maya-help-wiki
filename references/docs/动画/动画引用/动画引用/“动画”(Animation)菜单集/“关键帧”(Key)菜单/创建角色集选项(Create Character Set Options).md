# 创建角色集选项(Create Character Set Options)

- 在“动画”(Animation) [菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129) (**F4**) 中：“关键帧 > 创建角色集”(Key > Create Character Set) > ![图：在“动画”(Animation) 菜单集 (F4) 中：“关键帧 创建角色集”(Key Create Character…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1144 字 ≥300，非承重" -->

另请参见[创建角色集](../../../../Maya%20中的非线性动画/Maya%20中的非线性动画/Trax%20编辑器/创建、加载和亮显角色集/创建角色集%28Create%20character%20sets%29.md)。

#### 名称(Name)

指定角色集的名称。默认名称为 character*n*。

#### 选定节点以下的层级(Hierarchy below selected node)

指定角色集中包含选定对象以下的层级中的所有对象。如果禁用此选项，那么角色集中只包含选定对象。

#### 属性(Attributes)

指定哪些属性将包括在角色集内，作为可设置关键帧的属性。可以选择“所有可设置关键帧”(All Keyable)、“来自通道盒”(From Channel Box)或“除以下项外全部可设置关键帧的属性”(All Keyable Except)。

#### 所有可设置关键帧(All Keyable)

指定所有选定对象的所有可设置关键帧属性都将包括在内，以作为角色集的属性。

#### 来自通道盒(From Channel Box)

指定只将“通道盒”(Channel Box)中当前选定的通道包括在角色集内。

### 除以下项外其他所有可设置关键帧的属性(All Keyable except)

指定某些属性是否包含在角色集中。通过此选项可以在创建角色集时控制角色集中包含的属性数量。这样可以节省时间，减少“通道盒”(Channel Box)中列出的属性数量，并有助于提高动画工作的效率。

#### 平移(Translate)

指定包含平移属性作为可设置关键帧属性，选中启用除外（默认设置为禁用）。

#### 旋转(Rotate)

指定包含旋转属性作为可设置关键帧属性，选中启用除外（默认设置为禁用）。

#### 缩放(Scale)

指定排除缩放属性作为可设置关键帧属性，选中禁用除外（默认设置为启用）。

#### 可见性(Visibility)

指定排除可见性属性作为可设置关键帧属性，选中禁用除外（默认设置为启用）。

#### 动态(Dynamic)

指定排除动态属性作为可设置关键帧属性，选中禁用除外（默认设置为启用）。

### 重定向角色(Redirect Character)

使当前角色集可重定向。如果角色集可重定向，这就意味着现在可以更改已建立（例如，运动捕捉）动画的平移和方向。

#### 旋转和平移(Rotation and Translation)

为当前角色集创建旋转和平移控制。

#### 仅旋转(Rotation Only)

为当前角色集创建旋转重定向控制。旋转重定向控制出现在当前角色的原点。

如果要更改角色集枢轴的方向，旋转重定向控制非常有用。例如，可以操纵旋转重定向控制，使角色在行进途中旋转 90 度（可能是围绕一个角）。

#### 仅平移(Translation Only)

为当前角色集创建平移重定向控制。旋转重定向控制出现在当前角色的原点。

如果要更改对象轴周围的点的平移，平移重定向控制非常有用。例如，可以操纵平移重定向控制，以更改角色跳起后落地的地点。
