# 在“大纲视图”(Outliner)或其他编辑器中显示“渲染设置”(Render Setup)节点

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 621 字 ≥300，非承重" -->

默认情况下，节点（如 renderSetup、renderSetupLayer1、collection1 等）在编辑器（如“大纲视图”(Outliner)和“节点编辑器”(Node Editor)）中是隐藏的。**可在“渲染设置”(Render Setup)编辑器中启用“选项 > 在编辑器中显示渲染设置节点”(Options > Display Render Setup nodes in editors)**显示它们。此外，还必须在“大纲视图”(Outliner)菜单中禁用“显示 > 仅 DAG 对象”(Display > DAG Objects Only)才能在编辑器中看到它们。

**注**

启用此选项时应谨慎操作，因为删除其中任何节点都可能产生异常结果。

本主题介绍的工作流不同于[在大纲视图中过滤并仅显示渲染设置成员](../在大纲视图中过滤并仅显示渲染设置成员.md)中概述的工作流，其中介绍了如何简化大纲视图以显示您的集合（如模型）的成员或着色器。

您可以在场景打开时随时禁用此选项。

此设置与首选项一起保存在选项变量 renderSetup_displayRSNodes 中，并在重新启动 Maya 时保留。

还可以通过设置环境变量 MAYA_RENDER_SETUP_DISPLAY_RS_NODES 控制此选项。值为 0 时禁用该选项，值为 1 时启用该选项。该环境变量优先于首选项。设置该环境变量后，“选项 > 在编辑器中显示渲染设置节点”(Options > Display Render Setup nodes in editors)菜单选项将灰显，系统将应用该环境变量值。
