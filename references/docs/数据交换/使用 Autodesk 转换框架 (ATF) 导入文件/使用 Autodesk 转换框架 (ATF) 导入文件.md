# 使用 Autodesk 转换框架 (ATF) 导入文件

Maya 使用欧特克转换框架 (ATF) 文件转换系统，简化欧特克和第三方文件格式的数据交换。

**注**

仅 Windows 支持 ATF。

若要导入 ATF 文件，请执行以下操作：

1. 选择“文件 > 导入”(File > Import)。

  将显示 Maya“导入”(Import)窗口。

2. 找到 ATF 文件并选择下列受支持的 ATF 文件类型之一：

  - IGES_ATF

  - JT_ATF

  - PARASOLID_ATF

  - SAT_ATF

  - STEP_ATF

  - STL_ATF

  - WIRE_ATF

  - CATIAV4_ATF

  - CATIAV5_ATF

  - DWG_ATF/DXF_ATF

  - NX_ATF

  - PROE_ATF

3. 展开“文件类型特定选项”(File Type Specific Options)并激活“Aruba 细分”(Aruba Tessellation)或“ATF 细分”(ATF Tessellation)，以激活特定 ATF 类型的选项。

4. 根据需要调整设置。有关这些设置的描述，请参见“导入选项”主题中的 [Autodesk 转换框架 (ATF)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-37B31221-7BBC-40DA-AB33-47C333EF4E14#GUID-37B31221-7BBC-40DA-AB33-47C333EF4E14__SECTION_658450AD4CB14104A6697AC639C880F6)。

**注**

如果您导入 .iges 文件，后跟 .step 文件，ATF 会变得不稳定，反之亦然。请尝试在单独的会话中导入这些文件。

5. 如果要使用缝合，请激活“ATF 缝合服务”(ATF Stitching Services)，使用“容差”(Tolerance)滑块设置不缝合间隙的限制，并在“分隔方式”(Separation by)列表中选择相应选项以对曲面进行分组。
