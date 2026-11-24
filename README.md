# pairwise-midi-sample-clock

## 领域

游戏、图形与多媒体

## 主题

MIDI 采样精确调度

## 说明

tempo map 换算、循环点 note-off 与端口串行。

初始状态下 `media/midi_sample_clock.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
