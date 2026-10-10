# 在 Linux 上设置音频

您可以在 Linux 上使用默认音频设置，而高级用户可以使用某些其他配置设置。

为了帮助您在 Linux 上配置音频设置，Maya 包括一个模板配置文件和一个测试应用程序。您可以在模板文件中调整音频设置，然后使用测试应用程序播放声音来确定音频设置在 Maya 中能否正常工作。

## 编辑模板配置文件

alsoftrc.sample 模板配置文件仅适用于高级用户。（在安装 Maya 的 /bin 子目录中查找此文件。默认情况下，位于 /usr/autodesk/maya*<版本>*/bin/ 中。）该文件介绍各个 OpenAL 参数并允许您设定这些参数来调整音频配置。如果计划使用模板文件，请将其复制到 ~/.alsoftrc。

## 使用测试应用程序播放声音

如果选择修改模板配置文件，则您可以运行 runTime/bin/testMayaAudio 测试应用程序来播放声音文件的序列。使用与 Maya 使用的库完全相同的库设置测试应用程序。如果使用测试应用程序能成功播放声音，音频配置也会在 Maya 中工作。

运行该应用程序时，您将看到类似于以下内容的输出：

```text
testMayaAudio: audio library (MAYA_AUDIO_LIBRARY) 2 OpenAL
testMayaAudio: media_path /Volumes/Emerald/aw/main/build/optim/runTime/Maya.app/Contents/bin/media/
testMayaAudio: OpenAL audio device (MAYA_AUDIO_OPENAL_DEVICE) Not defined
testMayaAudio: Starting sound playback
```

## 相关主题

- [音频变量](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-6C2912FA-7B1B-4CA4-BFDD-1681ABC7DB24)
