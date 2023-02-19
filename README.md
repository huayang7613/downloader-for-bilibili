# downloader for bilibili/B站视频下载器
 a sample downloader for bilibili

下载B站视频的简单实现

### 使用说明

1. 下载需要的库
   > conda install bs4 requests
   或者
   > pip install bs4 requests
   
1. 按照download_BV.py里的说明获取cookie中需要的部分

2. 修改下载路径(line 54, 关键词path)

3. 填写需要下载的视频的BV号(line 64, 关键词downloadr.bvid)

4. 运行download_BV.py，等待下载完成

### 注意

1. 暂时还未加入try-error机制，可能存在一些问题，自己测试了十个左右视频，情况良好，请在网络良好时使用
2. 下载时调用wget命令，mac需要自行下载，win不知道有没有，可以换成curl命令，暂时只能靠读者自行修改
3. 本脚本仅供大家交流学习之用，请勿滥用
4. 有其他使用建议或问题欢迎反馈