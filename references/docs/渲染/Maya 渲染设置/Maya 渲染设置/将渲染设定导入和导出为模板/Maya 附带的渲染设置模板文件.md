# Maya 附带的渲染设置模板文件

以下模板文件适用于 Windows 平台上的 Maya 安装，可在默认用户模板文件夹 (<Documents>\maya\RSTemplates) 中找到。

以下模板文件可用于蒙版输出指定了 aiStandardSurface 着色器的对象：

  RenderLayerExample-Arnold.json：导入此模板可创建一个包含两个集合的层。第一个集合用于将对象添加到该层；第二个集合用于指定要蒙版输出的对象，并具有对应的着色器子集合与蒙版覆盖。

  MatteOverride-Arnold.json：导入此模板可为要蒙版输出的对象创建着色器子集合与对应的蒙版覆盖。

以下模板文件可用于创建覆盖，以便将特定摄影机设置为可渲染或不可渲染。

  RemoveRenderableCameras.json：如果在场景中将摄影机设置为可渲染，但您想在层中将这些摄影机的子集设置为不可渲染，则导入此模板。例如，如果在场景中将 camera1、camera2、camera3、camera4 均设置为可渲染，则可以在 Layer1 中创建覆盖以将 camera1 和 camera2 设置为不可渲染。

  导入该模板后，将要设置为不可渲染的摄影机添加到 Remove_Renderable_Cameras 集合。

  SetRenderableCameras.json：如果在场景中将摄影机设置为不可渲染，但您想在层中将这些摄影机的子集设置为可渲染，则导入此模板。例如，如果在场景中将 camera1、camera2、camera3、camera4 均设置为不可渲染，则可以在 Layer1 中创建覆盖以将 camera1 和 camera2 设置为可渲染。

  导入该模板后，将要设置为可渲染的摄影机添加到 Add_Renderable_Cameras 集合。
