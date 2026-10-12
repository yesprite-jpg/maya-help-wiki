# 支持 GPU 的变形器

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 564 字 ≥300，非承重" -->

为了提高播放性能，Maya 将某些变形器的处理分载到图形处理单元 (GPU)。

**注**

虽然 GPU 支持仅适用于 VP 2.0，但在许多情况下，通过 GPU 支持更新变形器使旧版 CPU 变形器的性能略有提升。

默认情况下，“GPU 覆盖”(GPU Override)在 Maya 中处于活动状态，但如果将其禁用，可以在[“动画”(Animation)首选项（在“设置”(Settings)下）](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F)中启用它。

以下变形器提供 GPU 支持：

- [blendShape](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9D06EE32-416C-47D8-93D4-0EFA13F9C836.htm)

- [cluster](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B7C96FEA-C415-4927-8E02-396F0E837DE2.htm)

- [deltaMush](../Delta%20Mush%20变形器/Delta%20Mush%20选项%28Delta%20Mush%20Options%29.md)

- groupParts

- ![图：jiggle](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-F739B7B8-5D9E-4941-87D9-083D6D195CA7.png) <!-- baize:img-hook downloaded=false reason="正文 564 字 ≥300，非承重" -->[jiggle](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EE9CA51E-F618-4EE4-8D9F-6D6470EBF89E.htm)

- [晶格](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-334813CE-30E5-43CB-B032-CF8FE1ED96F7.htm)

- ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 564 字 ≥300，非承重" -->[变形](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EFDD514A-10FF-44A2-BC93-0F53DB5ABA19.htm)

- [非线性变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8DF6AA06-2848-4CA8-AB57-313057EA14B1.htm)

- [接近度包裹(Proximity Wrap)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0D7E6B72-6021-4C66-9262-089D10246C3F.htm)

- [雕刻](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8A7188B9-34C1-48B8-B690-5CB0EA36932D.htm)（请参见下面的注释）

- [solidify](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-DFCD71CC-DA9E-4011-B6F6-EABE68217578.htm)

- [skinCluster](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-87526111-3EE7-4759-8DB3-433B907FB759.htm)

- [softMod](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B93EE24C-9E77-41C6-AC26-341A41FADAD0.htm)

- [tension](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-A8FB24DA-14C3-4230-A6B3-D4FACCB3A3B5.htm)

- [tweak](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-62896A44-870A-415E-8C06-5ADAC503D72B.htm)

- [wire](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-F45EC3DD-F268-4790-B069-DD1E6DF4484D.htm)

**注**

GPU 支持仅适用于隐式球体，即，当雕刻对象几何体是球体时，Maya 将雕刻变形器加入使用 GPU 运行的变形链中。如果雕刻几何体不是球体，则变形将发送到 CPU。

## GPU 支持和选择集

使用子集时**张力**、**Delta Mush** 和**固化**变形器的行为已更改，以支持 GPU。

在 2021 版之前的 Maya 版本中，如果在使用几何体的子集时使用这些变形器，将按一个多边形连接级别在内部展开选择集，并且相应顶点会被指定为锚点。

在新行为中，变形器仅使用子集内的顶点。如果要恢复原始变形器行为，请使用组件标记展开选择集。
