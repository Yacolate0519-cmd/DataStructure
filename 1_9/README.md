# 1_9 - Trie 和 Hash 資料結構實作

本資料夾包含 Trie 資料結構和 Hash Table 應用的實作練習。

## 檔案說明

### D1345490_1.py
實作完整的 Trie (字典樹) 資料結構，包含以下功能：
- `add_Word(word)`: 新增單字到 Trie，並記錄出現頻率
- `search_Word(word)`: 搜尋單字是否存在
- `query(prefix, k)`: 根據前綴查詢，返回前 k 個最常出現的單字（按頻率降序，頻率相同則按字母順序）
- `remove_Word(word)`: 移除單字（頻率 > 1 時減少計數，頻率為 1 時標記為非結束節點）

**特點**：
- 支援單字頻率統計
- 前綴查詢功能
- 結果排序（頻率優先，字母次之）

### D1345490_2.py
實作 Two Sum 問題的 Hash Table 解法。

**問題描述**：給定一個整數陣列 `nums` 和目標值 `target`，找出陣列中兩個數字的索引，使其和等於 `target`。

**解法**：
- 使用 Hash Table (字典) 儲存已見過的數字及其索引
- 時間複雜度：O(n)
- 空間複雜度：O(n)

### test.py
基礎的 Trie 實作練習，包含：
- `insert(word)`: 插入單字
- `search(word)`: 搜尋單字（區分大小寫）
- `display()`: 顯示所有儲存的單字

**範例**：插入 "Apple" 和 "Banana"，並測試大小寫敏感的搜尋功能。

## 相關資料
- `Trie and Hash.pdf`: Trie 和 Hash 資料結構的理論說明文件

## 執行方式

```bash
# 執行 Trie 完整實作
python D1345490_1.py

# 執行 Two Sum 問題
python D1345490_2.py

# 執行基礎 Trie 測試
python test.py
```

## 學習重點

1. **Trie 資料結構**
   - 適合用於字串搜尋和前綴匹配
   - 時間複雜度：插入/搜尋均為 O(m)，m 為字串長度
   - 空間複雜度：O(ALPHABET_SIZE * N * M)

2. **Hash Table 應用**
   - Two Sum 問題的高效解法
   - 以空間換取時間的經典案例
   - Python 字典的底層實作即為 Hash Table

## 作者
學號：D1345490
