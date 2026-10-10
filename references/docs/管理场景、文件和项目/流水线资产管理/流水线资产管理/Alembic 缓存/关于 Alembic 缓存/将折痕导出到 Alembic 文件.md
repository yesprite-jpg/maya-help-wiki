# 将折痕导出到 Alembic 文件

如果使用的是 Maya 2015、Maya 2014 或 Maya 2013，请按照下列步骤将网格的折痕信息保存到 Alembic 文件。

**注**

在 Maya 2015 Extension 和更高版本中，在

“Alembic 导出”(Alembic Export)

窗口中启用

“写入折痕”(Write Creases)

以导出折痕。若要打开该窗口，请选择

“缓存 > Alembic 缓存 > 将所有内容/选定内容导出到 Alembic”(Cache > Alembic Cache > Export All/Selection to Alembic) > ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 941 字 ≥300，非承重" -->

。有关详细信息，请参见

Alembic 导出选项

。

将网格折痕导出到 Alembic 文件

1. 选择要导出 Alembic 文件的网格的变换节点。

2. 通过执行以下操作，将“细分网格”(Sub Division Mesh)属性添加到网格的形状节点：

  - 在“属性编辑器”(Attribute Editor)中，选择“属性 > 添加属性”(Attributes > Add Attributes)。

  - 在“添加属性”(Add Attribute)窗口的“新建”(New)下，在“长名称”(Long name)旁键入 SubDivisionMesh。

  - 在“数据类型”(Data Type)下，选择“布尔”(Boolean)。

  - 单击“确定”(OK)。

  Maya 会将“细分网格”(Sub Division Mesh)属性添加到节点的“附加属性”(Extra Attributes)部分中。

3. 在“附加属性”(Extra Attributes)部分中，启用“细分网格”(Sub Division Mesh)。

4. 在“动画”(Animation)菜单集中，选择“缓存 > Alembic 缓存 > 将所有内容/选定内容导出到 Alembic”(Cache > Alembic Cache > Export All/Selection to Alembic) > ![图：在“动画”(Animation)菜单集中，选择“缓存 Alembic 缓存 将所有内容/选定内容导出到 Alembic”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 941 字 ≥300，非承重" -->。

5. 在“Alembic 导出”(Alembic Export)窗口中，展开“属性”(Attributes)部分。

  在“属性”(Attribute)下，选择 SubDivisionMesh，然后单击“添加”(Add)。

6. 单击“导出当前选择”(Export Selection)或“应用”(Apply)。

将几何体导出到 Alembic 缓存时，对象的折痕信息将包含在 Alembic 文件中。
