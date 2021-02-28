# Tuning_Helper

一些对调校可能有帮助的脚本。

Some (maybe) uesful scripts for Tuning.

# Why this project

["万象霜天在设计阶段祖娅纳惜帮忙唱过demo"](https://t.bilibili.com/490851866432778633)，这证明了目前虚拟歌手的创作还离不开人类的"先行示范"，因此写了这些脚本来帮助大家创作。算是抛砖引玉吧…

# 项目说明

1. 请将Src文件夹添加到Path中(用.pth文件)
2. 只能用于分析没有背景音乐的声音。对于混有其它音乐的人声，pyin函数无法给出人声的基频
3. 我在librosa的绘图模块里发现了一个Bug，开了个[Issue](https://github.com/librosa/librosa/issues/1283)，这是开发组的[PR](https://github.com/librosa/librosa/pull/1290)。本人学业较为繁忙，麻烦大家帮忙看一下进度

# 更新日志

2021.02.28删除无用文件; 精简用户使用时需输入的内容;  提供更好的模块化绘图方法

2020.08.30上传代码及音乐语音文件(来自标贝中文标准女声音库https://www.data-baker.com/open_source.html中的003796.wav)。See:[hfucyan/autoVtalker](https://github.com/fucyan/autoVtalker)

# 不情之请

如果您在制作作品的过程中使用了我的代码，我在此恳请您在作品中注明(当然，这只是“君子协议”，我无从核查:smile:)