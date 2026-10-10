# “渲染”(Rendering)首选项

可以在“首选项”(Preferences)窗口的“渲染”(Rendering)[类别中设置以下首选项。](../“首选项”%28Preferences%29窗口.md)

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 渲染(Rendering)

#### 首选渲染器(Preferred renderer)

可以选择首选渲染器。首选渲染器是指创建新场景（“文件 > 新建场景”(File > New Scene)）或启动 Maya 时 Maya 将重置到的渲染器。

#### 首选渲染设置系统(Preferred Render Setup system)

早期版本的“层编辑器”(Layer Editor)中提供的传统渲染层系统已替换为该渲染设置系统。请参见 [Maya 渲染设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-646154F9-E4D2-4A3E-A0D9-B2F062960A4E)。 此渲染设置系统和传统渲染层系统是分离而独立的系统，只能使用其中一个。

选择您要使用的系统，然后重新启动 Maya。

## 渲染设置首选项(Render Setup Preferences)

您可以采用 .json 文件格式将渲染设置导出为模板。例如，您既可以导出整个渲染设置的配置，也可以仅导出集合的子集，或者渲染层及其集合。可以导出此模板，然后将其导入到另一个场景中，这样就不必重新创建渲染设置。

同样，您可以采用 .json 文件格式导出“渲染设置”(Render Settings)的预设，确保使用一致的设置渲染序列中的每个快照。

模板和预设可以保存到网络位置，并在多个用户之间共享。分别将“全局模板位置”(Global Templates Location)和“全局预设位置”(Global Presets Location)属性设置为此网络位置。

模板和预设也可以保存在本地，供各用户重复使用。分别将“用户模板位置”(User Templates Location)和“用户预设位置”(User Presets Location)属性设置为此本地目录。
