# 在 Hypershade 中单放节点

在单放节点时，材料查看器和视口将更新以反映单放结果。

## 使用单放图标单放节点

单击节点右上角的 ![图：单击节点右上角的 单放图标（热键 @）。单放节点时，此图标将变为青绿色 。节点的边界变为红色，默认情况下已单放的属性显示…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AA68BC33-AB1D-4D7F-88F7-2E899919F478.png) <!-- baize:img-hook downloaded=false reason="正文 819 字 ≥300，非承重" --> 单放图标（热键 @）。单放节点时，此图标将变为青绿色 ![图：单击节点右上角的 单放图标（热键 @）。单放节点时，此图标将变为青绿色 。节点的边界变为红色，默认情况下已单放的属性显示…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-3121CC66-4D88-4BB0-B7E0-D2DFD81082ED.png) <!-- baize:img-hook downloaded=false reason="正文 819 字 ≥300，非承重" -->。节点的边界变为红色，默认情况下已单放的属性显示为三角形端口 ![图：单击节点右上角的 单放图标（热键 @）。单放节点时，此图标将变为青绿色 。节点的边界变为红色，默认情况下已单放的属性显示…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AD351FDE-4618-458D-AEBE-C8DA2B997CB9.png) <!-- baize:img-hook downloaded=false reason="正文 819 字 ≥300，非承重" -->。

通过双击其端口，可以选择单放该节点上的其他属性。

若要禁用单放，请再次单击 ![图：若要禁用单放，请再次单击 图标（热键 ）。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-3121CC66-4D88-4BB0-B7E0-D2DFD81082ED.png) <!-- baize:img-hook downloaded=false reason="正文 819 字 ≥300，非承重" --> 图标（热键 #）。

## 使用标记菜单单放节点

若要单放节点，请在该节点上单击鼠标右键，然后从标记菜单中选择 “单放”(Solo)。单放节点时，此图标将变为青绿色 ![图：若要单放节点，请在该节点上单击鼠标右键，然后从标记菜单中选择 “单放”(Solo)。单放节点时，此图标将变为青绿色 。节…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-3121CC66-4D88-4BB0-B7E0-D2DFD81082ED.png) <!-- baize:img-hook downloaded=false reason="正文 819 字 ≥300，非承重" -->。节点的边界变为红色，默认情况下已单放的属性显示为三角形端口 ![图：若要单放节点，请在该节点上单击鼠标右键，然后从标记菜单中选择 “单放”(Solo)。单放节点时，此图标将变为青绿色 。节…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AD351FDE-4618-458D-AEBE-C8DA2B997CB9.png) <!-- baize:img-hook downloaded=false reason="正文 819 字 ≥300，非承重" -->。

通过双击其端口，可以选择单放该节点上的其他属性。

若要单放上次已单放的属性，请在节点编辑器工作区中的任意位置单击鼠标右键，然后从标记菜单中选择“单放最后一个连接”(Solo Last Connection)（热键 !）。

若要删除单放，请在节点编辑器工作区中的任意位置单击鼠标右键，然后从标记菜单中选择“移除材质单放”(Remove Material Soloing)。

## 使用热键单放节点

若要单放节点，请使用热键 @。

若要移除单放，请使用热键 #。

若要单放上次已单放的节点/属性，请使用热键 ！。

## 使用 MEL/Python 单放节点

若要单放节点，请使用 soloMaterial 命令并指定节点和（可选）属性，如下所示：

```text
soloMaterial -node "checker1" -attr "outColor"
```

若要单放上次已单放的属性，请使用 -last 标志：

```text
soloMaterial -last
```

若要删除单放，请输入以下 MEL 命令：

```text
soloMaterial -unsolo
```

也可以执行 Python 中的等效命令。详细信息请参见 soloMaterial 命令文档。

## 查询已单放的节点

使用 MEL 或 Python 可以查询已单放的节点和属性：

```text
// To query the soloed node
soloMaterial -q -node

//To query the soloed attribute
soloMaterial -q -attr
```
