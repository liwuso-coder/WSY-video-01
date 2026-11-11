# -*- coding: utf-8 -*-
"""复核四平台标题字数是否精确达标。

用法：python check_titles.py < titles.json
titles.json：[{"platform": "douyin", "title": "..."}]，platform 支持中英文平台名。
全部达标退出码 0，否则 1。
"""
import json
import sys

LIMITS = {
    "douyin": 29, "抖音": 29,
    "xiaohongshu": 20, "xhs": 20, "小红书": 20,
    "shipinhao": 16, "wechat": 16, "视频号": 16, "微信视频号": 16, "微信短视频": 16,
    "bilibili": 46, "b站": 46, "B站": 46,
}


def main():
    items = json.load(sys.stdin)
    failed = 0
    for i, it in enumerate(items, 1):
        platform = it.get("platform", "")
        title = it.get("title", "")
        limit = LIMITS.get(platform)
        if limit is None:
            print(f"[{i}] 未知平台 {platform!r}，跳过")
            failed += 1
            continue
        n = len(title)
        ok = n == limit
        if not ok:
            failed += 1
        print(f"[{i}] {platform} {n}字 / 要求{limit}字 {'OK' if ok else 'FAIL'} {title}")
    print(f"共 {len(items)} 条，不达标 {failed} 条")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
