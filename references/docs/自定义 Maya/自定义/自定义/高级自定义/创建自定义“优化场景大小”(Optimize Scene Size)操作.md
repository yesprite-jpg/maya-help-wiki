# 创建自定义“优化场景大小”(Optimize Scene Size)操作

您可以编辑 MEL 脚本，该脚本是由“文件 > 优化场景大小”(File > Optimize Scene Size)命令为将清理操作添加到“优化场景大小选项”(Optimize Scene Size Options)（“文件 > 优化场景大小”(File > Optimize Scene Size) > ![图：您可以编辑 MEL 脚本，该脚本是由“文件 优化场景大小”(File Optimize Scene Size)命令为将清…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1684 字 ≥300，非承重" -->）而调用的。该脚本称为 cleanUpScene.mel，可以在 /scripts/startup 目录中找到该脚本。

打开脚本时，您会看到在脚本的末尾附近定义了一组函数，这些函数可帮助您添加和管理场景清理操作。

## 注册新的清理操作

#### cleanUp_AddUserCleanUp()

此函数将注册一个新的您定义的清理操作。该例程实际上可以在 userCleanUp_AddUserCleanUp.mel 脚本中找到，而该脚本可以在 /scripts/startup 目录中找到。

## 配置清理操作

#### userCleanUp_CreateUI()

调用此函数可以为您定义的清理操作创建 UI 。每个操作的 UI 都由一个可以启用和禁用此操作的复选框以及一个仅可用于执行该操作的“立即优化”(Optimize Now)按钮 组成。

#### userCleanUp_SetOptionVars( int $forceFactorySettings )

当清理操作的选项变量初始化到起始位置（启动时）或重置为出厂设置时，调用此函数。可以获取适当的默认值，并设置相应的选项变量。

#### userCleanUp_CleanUpSceneSetup( string $parent, string $forceFactorySettings )

创建完“优化场景大小选项”(Optimize Scene Size Options)对话框后，调用此函数以使用相应的 optionVar 中的值来同步对话框中的复选框。

#### userCleanUp_CleanUpSceneCallback( string $parent, string $doIt )

当需要将“优化场景大小选项”(Optimize Scene Size Options)对话框中复选框的当前状态作为选项变量进行保存时，调用此函数。

## 查看清理操作的属性

#### userCleanUp_GetNumCleanUps()

返回已注册的您定义清理操作的数量。其为 0 到 n-1 之间的数字。

#### userCleanUp_GetOptionVarName( int $cleanUpNum )

返回与指定的您清理操作相关联的选项变量。此变量值指示下次调用“优化场景大小”(Optimize Scene Size)操作时是否会执行特定操作。

#### userCleanUp_GetDefaultValue( int $cleanUpNum )

返回指定的您定义清理操作的默认值（启用或关闭）。

#### string userCleanUp_GetControlName( int $cleanUpNum )

返回“优化场景大小选项”(Optimize Scene Size Options)对话框中复选框控制组的名称，该对话框与指定的您清理操作相关联。当已创建或已破坏对话框，则系统会同步复选框状态以及相应的选项变量（请参见userCleanUp_GetOptionVarName()）。

#### userCleanUp_GetLabel( int $cleanUpNum )

返回应用于标记“优化场景大小选项”(Optimize Scene Size Options)对话框中指定的您定义清理操作的文本。

#### userCleanUp_GetCommand( int $cleanUpNum )

返回应用于执行指定的您定义清理操作的命令字符串。

#### userCleanUp_ListCleanUps()

打印包括所有已注册的您定义清理操作的列表。

#### userCleanUp_GetOptionVars()

返回所有与您定义清理操作相关联的选项变量。

## 运行您的自定义清理操作

#### userCleanUp_PerformCleanUpScene()

执行目前已通过 optionVar 启用的自定义优化场景操作。返回调用该操作时发生的错误数（如果有）。

## 相关主题

- [优化场景大小选项(Optimize Scene Size Options)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6798B37D-0FF0-4ED3-A151-5CC648BB8CED)
