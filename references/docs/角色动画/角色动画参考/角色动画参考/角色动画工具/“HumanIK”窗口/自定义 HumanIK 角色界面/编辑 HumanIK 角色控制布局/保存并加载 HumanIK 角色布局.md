# 保存并加载 HumanIK 角色布局

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-95717444-1F6D-47B8-9126-FE19FF06A427.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" -->

可以自定义默认角色背景

保存布局的步骤

1. 在执行更改所使用的 XML 编辑器或文本编辑器中，使用唯一的名称保存自定义文件。

2. （可选）将您的文件保存到新位置。

  **注**

  如果将文件保存在

  CharacterControls

  目录之外的位置，请确保将所有图像资源（即

  DefaultImages

  文件夹）复制到该新位置。

加载新布局的步骤

默认情况下，Maya 会在 CharacterControls 目录中查找 CharacterControlsConfig.xml 和 CustomRigControlsConfig.xml，以打开“控制”(Controls)或“自定义绑定”(Custom Rig)选项卡。加载新布局时，自定义文件的名称和路径将存储为新的默认值，每次启动新的 Maya 会话时都会加载该默认值。

1. 通过从以下选项中进行选择将您的文件的名称和位置告知 Maya：

  - ![图：编辑控制绑定 加载 UI 配置(Edit Control Rig Load UI Configuration)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" --> > 编辑控制绑定 > 加载 UI 配置(Edit Control Rig > Load UI Configuration)

  - ![图：编辑自定义绑定映射 加载 UI 配置(Edit Custom Rig Mapping Load UI Configura…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" --> > 编辑自定义绑定映射 > 加载 UI 配置(Edit Custom Rig Mapping > Load UI Configuration)

2. 在显示的“导入 UI 配置文件”(Import UI Configuration File)对话框中浏览到自定义配置文件的位置。

3. 选择文件，然后单击“打开”(Open)。

  默认值将更新，并且您的自定义布局会显示在“HumanIK”窗口中。该布局会继续显示在 窗口中，即使在结束 Maya 会话或打开新文件后也如此。

4. 如果在加载布局后对布局进行更改，则可以通过选择下列选项之一对其进行更新：

  - ![图：编辑控制绑定 更新 UI 配置(Edit Control Rig Update UI Configuration)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" --> > 编辑控制绑定 > 更新 UI 配置(Edit Control Rig > Update UI Configuration)

  - ![图：编辑自定义绑定映射 更新 UI 配置(Edit Custom Rig Mapping Update UI Configu…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 1108 字 ≥300，非承重" --> > 编辑自定义绑定映射 > 更新 UI 配置(Edit Custom Rig Mapping > Update UI Configuration)

**注**

如果您的自定义配置文件被删除或缺失，Maya 将使用

CharacterControlsConfig.xml

和

CustomRigControlsConfig.xml

文件还原默认布局。

使用 MEL 加载新布局的步骤

1. 在命令行或“脚本编辑器”(Script Editor)中键入以下 MEL 命令之一：

  - 对于“控制绑定”(Control Rig)选项卡，使用 MEL 命令：updateHIKCharacterToolConfig( "path/to/my/config.xml" );

  - 对于“自定义绑定映射”(Custom Rig Mapping)选项卡，使用 MEL 命令：hikUpdateHIKCustomRigConfig( "path/to/my/config.xml" );

## 相关主题

- [自定义 HumanIK 角色界面](../../自定义%20HumanIK%20角色界面.md)
