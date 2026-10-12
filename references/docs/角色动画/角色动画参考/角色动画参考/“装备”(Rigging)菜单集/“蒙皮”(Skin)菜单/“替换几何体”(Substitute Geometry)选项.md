# “替换几何体”(Substitute Geometry)选项

- 在“装备”(Rigging)菜单集中，选择“蒙皮 > 替换几何体”(Skin > Substitute Geometry) > ![图：在“装备”(Rigging)菜单集中，选择“蒙皮 替换几何体”(Skin Substitute Geometry) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 841 字 ≥300，非承重" -->。

## 旧几何体选项(Old Geometry Options)

当同时禁用下面两个选项时，将在替换时删除绑定的几何体的原始片。

#### 保留旧几何体(Retain old geometry)

启用时，不会在替换对象上删除绑定的几何体的原始片、其骨架及其影响。

#### 将旧几何体移至某一层(Move Old Geometry To A Layer)

启用时，不会在替换对象上删除绑定的几何体的原始片、骨架及影响，并将它们置于新的显示层。放置绑定的几何体的旧片、骨架及影响的显示层名为 [旧几何体的名称] Shape_oldSkin。

## 新几何体设置(New Geometry Settings)

选择下列选项之一。

#### 禁用非蒙皮变形器(Disable Non-Skin Deformers)

启用后，将在原始绑定几何体传递到新几何体时禁用对原始几何体的任何*非蒙皮*变形。若要对新几何体重新启用该变形，请为每个变形器重置该节点状态。

禁用时，仅将*蒙皮*变形从绑定几何体的原始片传递到几何体的新片。

#### 将新几何体移至某一层(Move New Geometry To A Layer)

启用时，在替换对象上将几何体的新片置于与绑定的几何体的原始片分离的显示层。放置几何体的新片的层名为 [旧几何体的名称] Shape_newSkin。

#### 重置权重时使用的距离容差(Re-weighting Distance Tolerance)

指定关节对新的几何体部分的影响随与每个关节之间的距离降低的速度。“重置权重时使用的距离容差”(Re-weighting Distance Tolerance)越大，通过距离产生减慢影响的速度越快。“重置权重时使用的距离容差”(Re-weighting Distance Tolerance)越小，每个关节的影响越远。如果几何体的新片具有几何体的原始片没有的附加顶点，并且您希望在重新计算蒙皮时包含它们，则该选项非常有用。

## 相关主题

- [将绑定几何体替换为未绑定的几何体](../../../../对角色进行蒙皮/对角色进行蒙皮/平滑蒙皮/编辑平滑蒙皮/将绑定几何体替换为未绑定的几何体.md)
