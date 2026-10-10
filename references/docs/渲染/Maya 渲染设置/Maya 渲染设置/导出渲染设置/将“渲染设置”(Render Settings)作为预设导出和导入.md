# 将“渲染设置”(Render Settings)作为预设导出和导入

将“渲染设置”(Render Settings)作为预设以 .json 文件形式导出，然后导入此文件以便下次渲染时重用相同设置。通过“渲染设置”(Render Settings)窗口或“渲染设置”(Render Setup)编辑器访问这些选项。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" -->

**注**

“渲染设置”(Render Settings)

窗口的

“预设”(Presets)

菜单中的菜单项已在 Maya 2018.4 Update 中重命名。有关详细信息，请参见下面的“预设菜单已重命名”。

## 导出预设

可以通过以下四种方式之一导出“渲染设置”(Render Settings)：

  从“渲染设置”(Render Settings)窗口中选择“预设 > 导出渲染设置”(Presets > Export Render Settings)。

  在“渲染设置”(Render Setup)编辑器的“场景 > 渲染设置”(Scene > Render Settings)部分中单击 ![图：在“渲染设置”(Render Setup)编辑器的“场景 渲染设置”(Scene Render Settings)部分中…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" -->，然后选择“导出当前”(Export Current)。

- 从“渲染设置”(Render Setup)编辑器菜单中选择“文件 > 导出场景渲染设置”(File > Export Scene Render Settings)。

  ![图：从“渲染设置”(Render Setup)编辑器菜单中选择“文件 导出可见层渲染设置”(File Export Visi…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" --> 从“渲染设置”(Render Setup)编辑器菜单中选择“文件 > 导出可见层渲染设置”(File > Export Visible Layer Render Settings)。

默认情况下，预设 .json 文件保存到用户预设位置；即 <Documents>\maya\Presets。有关详细信息，请参见下面的“全局预设和用户预设”。

## 导入预设

可以通过以下三种方式之一执行此操作：

- 从“渲染设置”(Render Setup)编辑器菜单中选择“文件 > 导入场景渲染设置”(File > Import Scene Render Settings)。

  导入窗口默认为用户预设位置；即 <Documents>\maya\Presets。

  在“渲染设置”(Render Settings)窗口中选择“预设 > 导入渲染设置”(Presets > Import Render Settings)。

  在“渲染设置”(Render Setup)编辑器的“场景 > 渲染设置”(Scene > Render Settings)部分中，单击 ![图：在“渲染设置”(Render Setup)编辑器的“场景 渲染设置”(Scene Render Settings)部分中…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" -->。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-6230123E-A418-445C-B35F-439B346F2AD7.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" -->

预设特定于渲染器；因此，只有为当前渲染器设置的预设才会显示在这些菜单中。

## 设置默认预设

在“渲染设置”(Render Settings)窗口中选择“预设 > 设置首选渲染设置”(Presets > Set Preferred Render Settings)，可选择下次创建新场景时要自动加载的预设。

预设特定于渲染器；因此，创建新场景时，仅会加载为当前渲染器设置的首选预设。

## 删除预设

通过在“渲染设置”(Render Settings)窗口中选择“预设 > 删除用户渲染设置”(Presets > Delete User Render Settings)，可以删除用户预设。无法从此编辑器中删除全局预设。

## 预设菜单已重命名

“渲染设置”(Render Settings)窗口的“预设”(Presets)菜单中的菜单项已在 Maya 2018.4 Update 中重命名。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" -->

| 以前 | 现在 |
|---|---|
| 将设置保存为预设 | 导出渲染设置 |
| 加载预设 | 导入渲染设置 |
| 删除用户预设 | 删除用户渲染设置 |
| 设置首选预设 | 设置首选渲染设置 |

## 全局预设和用户预设

可以将预设保存到可全局访问的网络位置以供用户共享，或者保存到仅供您访问的本地文件夹。

从“渲染设置 > 预设”(Render Settings > Presets)菜单或者从“渲染设置”(Render Setup)编辑器 ![图：从“渲染设置 预设”(Render Settings Presets)菜单或者从“渲染设置”(Render Setup)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 2186 字 ≥300，非承重" --> 菜单导入预设时，全局预设和用户预设通过单独的快捷菜单列出。

## 预设文件的位置

通过设置环境变量 MAYA_RENDER_SETUP_GLOBAL_PRESETS_PATH，可以设置全局预设的位置。启动后，Maya 会自动在此文件夹中搜索全局预设。可以通过“首选项”(Preferences)窗口修改此路径。这样，您不必重新启动 Maya 来修改此路径。

在“首选项”(Preferences)窗口（“窗口 > 设置/首选项 > 首选项 > 渲染”(Windows > Settings/Preferences > Preferences > Rendering)）中为全局和用户预设设置位置。

**注**

提示：

从

“渲染设置”(Render Setup)

编辑器中选择

“首选项 > 渲染首选项”(Preferences > Rendering Preferences)

，可以更改预设的位置。

也可使用以下选项变量设置预设位置：

  全局预设：renderSetup_globalPresetsDirectory

  用户预设：renderSetup_userPresetsDirectory

  默认情况下，此变量设置为 <Documents>\maya\Presets。

若要查询其中任一目录，请执行下列操作：

```text
optionVar -q "renderSetup_userPresetsDirectory";
```

若要更改目录，请按如下所示替换选项变量的值：

```text
optionVar -sv "renderSetup_userPresetsDirectory" "C:\myUserPresets";
```

Maya 会自动在这些目录中搜索可用的预设。

## 相关主题

- [导出场景“渲染设置”(Render Settings)和 AOV 并将其应用于新场景](导出场景“渲染设置”%28Render%20Settings%29和%20AOV%20并将其应用于新场景.md)

- [从可见渲染层导出“渲染设置”(Render Settings)和 AOV 并将其应用于新场景](从可见渲染层导出“渲染设置”%28Render%20Settings%29和%20AOV%20并将其应用于新场景.md)
