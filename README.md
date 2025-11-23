# 資料結構與演算法課程 實習練習

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

這是一個完整的資料結構與演算法學習專案，包含從基礎搜尋演算法到進階樹結構的實作練習。本專案按照課程單元循序漸進，涵蓋資料結構核心概念與經典演算法的 Python 實現。

## 📚 目錄

- [專案概述](#專案概述)
- [單元結構](#單元結構)
  - [1_1 搜尋演算法](#1_1-搜尋演算法)
  - [1_2 Two Pointers 技巧](#1_2-two-pointers-技巧)
  - [1_3 線性資料結構與樹](#1_3-線性資料結構與樹)
  - [1_4 排序演算法與遞迴](#1_4-排序演算法與遞迴)
  - [1_5 樹的進階應用](#1_5-樹的進階應用)
  - [1_6 鏈表與矩陣應用](#1_6-鏈表與矩陣應用)
- [環境需求](#環境需求)
- [安裝與使用](#安裝與使用)
- [資料結構實現](#資料結構實現)
- [演算法實現](#演算法實現)
- [學習路徑](#學習路徑)
- [貢獻指南](#貢獻指南)
- [授權](#授權)

## 🎯 專案概述

**專案目標**: 透過實作學習經典資料結構與演算法
**開發語言**: Python 3.12
**程式碼規模**: 22 個 Python 檔案，約 1100 行程式碼
**課程單元**: 6 個主題單元
**版本控制**: Git + GitHub

### 專案特色

- ✅ **完整實作**: 涵蓋 Linked List, Stack, Queue, Tree 等核心資料結構
- ✅ **經典演算法**: 包含 Binary Search, Quick Sort, Merge Sort 等常見演算法
- ✅ **測試驗證**: 每個模組都包含完整的測試案例
- ✅ **中文註解**: 詳細的中文說明，幫助理解關鍵概念
- ✅ **漸進式學習**: 從基礎到進階，循序漸進的學習路徑

## 📖 單元結構

### 1_1 搜尋演算法

**檔案**: `1_1/main.py`

實現二元搜尋 (Binary Search) 演算法，在已排序的陣列中快速查找目標值。

```python
def search(data, target):
    # 二元搜尋實現
    # 時間複雜度: O(log n)
```

**關鍵概念**:
- 二元搜尋的基本原理
- 已排序資料的高效查找
- 時間複雜度分析

---

### 1_2 Two Pointers 技巧

**檔案**: `Test1.py`, `Test2.py`, `Test3.py`, `Test4.py`

#### Test1.py - 整數平方根
```python
def decode(x):
    # 求整數平方根
    # 時間複雜度: O(√n)
```

#### Test2.py - 容器盛水問題 (LeetCode 11)
```python
def tub(height):
    # 使用雙指針技巧
    # 時間複雜度: O(n)
```

#### Test3.py - 括號匹配驗證
```python
def checkClose(s):
    # 驗證括號是否正確配對
    # 時間複雜度: O(n)
```

**關鍵概念**:
- Two Pointers 雙指針技巧
- 時間複雜度優化
- Stack 在括號匹配中的應用

---

### 1_3 線性資料結構與樹

#### 📌 Linked List 實現 (`Linked_list.py`)

完整的單向鏈表實現，包含所有基本操作：

```python
class LinkedList:
    def print()        # 顯示鏈表內容
    def append(value)  # 尾部添加節點
    def insertAt(index, value)  # 指定位置插入
    def removeAt(index)         # 指定位置刪除
    def remove(value)           # 根據值刪除
    def indexOf(value)          # 查找值的索引
    def isEmpty()               # 檢查是否為空
    def size()                  # 獲取鏈表大小
```

**使用範例**:
```python
# 建立鏈表: 1 -> 2 -> 3 -> 4 -> 5
list = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
list.print()  # 輸出: 1 -> 2 -> 3 -> 4 -> 5 -> Null

# 添加節點
list.append(6)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> Null

# 插入節點
list.insertAt(0, 13)  # 13 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> Null

# 刪除節點
list.remove(3)  # 13 -> 1 -> 2 -> 4 -> 5 -> 6 -> Null
```

#### 📌 Queue 實現 (`Queue.py`)

環形佇列 (Circular Queue) 實現：

```python
class Queue:
    def enqueue(item)    # 入隊
    def dequeue()        # 出隊
    def get_front()      # 獲取隊首
    def is_empty()       # 檢查是否為空
    def is_full()        # 檢查是否已滿
    def display()        # 顯示隊列內容
```

#### 📌 雙向佇列 (`Queue_1.py`)

使用雙向鏈表實現的進階佇列：

```python
class MyQueue:
    def insertFront(value)  # 前端插入
    def insertRear(value)   # 後端插入
    def deleteFront()       # 前端刪除
    def deleteRear()        # 後端刪除
    def getFront()          # 獲取前端值
    def getRear()           # 獲取後端值
```

#### 📌 二元搜尋樹 (`Tree.py`)

```python
class Tree:
    def insert(data)         # 插入節點
    def inOrder(node)        # 中序遍歷 (左-根-右)
    def preOrder(node)       # 前序遍歷 (根-左-右)
    def postOrder(node)      # 後序遍歷 (左-右-根)
    def isSymmetric()        # 檢查樹是否對稱
```

**樹的遍歷範例**:
```python
tree = Tree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    tree.insert(value)

# 樹的結構:
#       5
#      / \
#     3   7
#    / \ / \
#   2  4 6  8

tree.preOrder(tree.root)   # 輸出: 5 3 2 4 7 6 8
tree.inOrder(tree.root)    # 輸出: 2 3 4 5 6 7 8 (已排序)
tree.postOrder(tree.root)  # 輸出: 2 4 3 6 8 7 5
```

#### 📌 作業實現

**D1345490_1.py** - MinStack (追蹤最小值的堆疊)
```python
class MinStack:
    def push(x)      # 壓入元素
    def pop()        # 彈出元素
    def peek()       # 查看頂部
    def getMin()     # O(1) 時間獲取最小值
```

**D1345490_2.py** - String 操作

**D1345490_3.py** - 環形佇列完整實現
```python
class MyCircleQueue:
    # 循環佇列的完整實現
    # 包含詳細中文註解說明常見錯誤
```

---

### 1_4 排序演算法與遞迴

#### 📌 排序演算法 (`Algorithm.py`)

實現三種經典排序演算法：

```python
# 1. 冒泡排序 (Bubble Sort)
def bubble_sort(data):
    # 時間複雜度: O(n²)
    # 空間複雜度: O(1)
    # 穩定排序

# 2. 歸併排序 (Merge Sort)
def merge_sort(data):
    # 時間複雜度: O(n log n)
    # 空間複雜度: O(n)
    # 穩定排序 (Divide and Conquer)

# 3. 快速排序 (Quick Sort)
def quick_sort(data):
    # 時間複雜度: 平均 O(n log n), 最差 O(n²)
    # 空間複雜度: O(log n)
    # 不穩定排序
```

**排序演算法比較**:

| 演算法 | 最佳 | 平均 | 最差 | 空間 | 穩定性 |
|--------|------|------|------|------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |

#### 📌 河內塔遞迴 (`main.py`)

經典的遞迴問題實現：

```python
class Hanoi:
    def solve(self, n, source, auxiliary, destination):
        # 遞迴求解河內塔問題
        # 最少移動次數: 2^n - 1
```

**河內塔問題**:
- n = 1: 1 步
- n = 2: 3 步
- n = 3: 7 步
- n = 4: 15 步

#### 📌 作業實現

**D1345490_1.py** - 河內塔改進版本

**D1345490_2.py** - 鏈表轉二元搜尋樹
```python
class Solution:
    def sortedListToBST(head):
        # 將排序鏈表轉為平衡 BST
        # 使用快慢指針找中點
        # 遞迴構建平衡樹

    def levelOrder(root):
        # 層序遍歷 (BFS)
        # 使用 deque 實現
```

---

### 1_5 樹的進階應用

**主題**: 樹的對稱性檢驗 (LeetCode 101)

#### 檔案列表

- `D1345490_1.py` - 對稱性檢驗初始版本
- `D1345490_2.py` - 改進版本 (邊界處理)
- `Test1.py` - isSameTree 測試
- `Test2.py` - 完整的 isSymmetric 實現

#### 核心實現 (`Test2.py`)

```python
class Solution:
    def isSymmetric(self, root):
        """檢查二元樹是否左右對稱"""
        if root is None:
            return True
        return self.sym(root.left, root.right)

    def sym(self, left, right):
        """遞迴比較左右子樹"""
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        # 比較 left.left ↔ right.right 和 left.right ↔ right.left
        return (self.sym(left.left, right.right) and
                self.sym(left.right, right.left))
```

**測試案例**:

```python
# Test 1: 完全對稱樹
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
# 結果: True

# Test 2: 單節點樹
#   1
# 結果: True

# Test 3: None 根節點
# 結果: True

# Test 4: 不對稱樹
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 結果: False
```

---

### 1_6 鏈表與矩陣應用

**主題**: 鏈表數學運算與矩陣遍歷

#### 檔案列表

- `D1345490_1.py` - 兩數相加 (LeetCode 2)
- `D1345490_2.py` - 螺旋矩陣 (LeetCode 54)

#### D1345490_1.py - 兩數相加

使用鏈表表示數字，實現大數相加：

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        兩個鏈表代表的數字相加
        數字以反向儲存（個位在前）
        時間複雜度: O(max(m, n))
        空間複雜度: O(max(m, n))
        """
        head = ListNode()
        current = head
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return head.next
```

**測試案例**:
```python
# 輸入: l1 = [2,4,6], l2 = [5,6,4]
# 代表: 642 + 465 = 1107
# 輸出: [7,0,1,1] -> 7 -> 0 -> 1 -> 1
```

#### D1345490_2.py - 螺旋矩陣

以螺旋順序遍歷矩陣：

```python
class Solution:
    def spiral_Matrix(self, matrix, result=None):
        """
        螺旋順序遍歷矩陣
        順序: 右 -> 下 -> 左 -> 上 (遞迴)
        時間複雜度: O(m * n)
        空間複雜度: O(m * n)
        """
        if result is None:
            result = []
        if matrix:
            result.extend(matrix.pop(0))      # 右
            for row in matrix:
                if row:
                    result.append(row.pop())  # 下
            if matrix:
                result.extend(reversed(matrix.pop()))  # 左
            for i in range(len(matrix) - 1, -1, -1):
                if matrix[i]:
                    result.append(matrix[i].pop(0))    # 上
            return self.spiral_Matrix(matrix, result)
        return result
```

**測試案例**:
```python
# 輸入:
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12]]

# 輸出: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

**關鍵概念**:
- 鏈表的數學運算與進位處理
- 矩陣的螺旋遍歷
- 遞迴解法

---

## 💻 環境需求

- **Python**: 3.12 或以上
- **作業系統**: macOS, Linux, Windows
- **依賴套件**: 無 (僅使用 Python 標準庫)

## 🚀 安裝與使用

### 1. Clone 專案

```bash
git clone git@github.com:Yacolate0519-cmd/DataStructure.git
cd DataStructure
```

### 2. 執行範例

每個單元的程式碼都可以直接執行：

```bash
# 執行 Linked List 範例
python 1_3/Linked_list.py

# 執行排序演算法
python 1_4/Algorithm.py

# 執行樹的遍歷
python 1_3/Tree.py

# 執行對稱樹檢驗
python 1_5/Test2.py
```

### 3. 測試各單元

```bash
# 單元 1: 二元搜尋
cd 1_1 && python main.py

# 單元 2: Two Pointers
cd 1_2 && python Test2.py

# 單元 3: 資料結構
cd 1_3 && python Linked_list.py
cd 1_3 && python Queue.py
cd 1_3 && python Tree.py

# 單元 4: 排序與遞迴
cd 1_4 && python Algorithm.py
cd 1_4 && python main.py

# 單元 5: 樹的對稱性
cd 1_5 && python Test2.py

# 單元 6: 鏈表與矩陣應用
cd 1_6 && python D1345490_1.py
cd 1_6 && python D1345490_2.py
```

## 📊 資料結構實現

本專案實現了以下資料結構：

### 線性結構

| 資料結構 | 檔案 | 特點 |
|---------|------|------|
| 單向鏈表 | `1_3/Linked_list.py` | 完整的插入、刪除、查找操作 |
| 雙向鏈表 | `1_3/Queue_1.py` | 支援前後端雙向操作 |
| 堆疊 (Stack) | `1_3/D1345490_1.py` | MinStack 變種，O(1) 查詢最小值 |
| 佇列 (Queue) | `1_3/Queue.py` | 環形佇列實現 |
| 環形佇列 | `1_3/D1345490_3.py` | 詳細中文註解版本 |

### 樹結構

| 資料結構 | 檔案 | 特點 |
|---------|------|------|
| 二元搜尋樹 (BST) | `1_3/Tree.py` | 插入、三種遍歷方式 |
| 平衡 BST | `1_4/D1345490_2.py` | 從排序鏈表構建 |
| 對稱樹檢驗 | `1_5/Test2.py` | 遞迴比較左右子樹 |

## 🔧 演算法實現

### 搜尋演算法

- **Binary Search** (`1_1/main.py`) - O(log n)

### 排序演算法

- **Bubble Sort** (`1_4/Algorithm.py`) - O(n²)
- **Merge Sort** (`1_4/Algorithm.py`) - O(n log n)
- **Quick Sort** (`1_4/Algorithm.py`) - O(n log n)

### 遞迴演算法

- **Tower of Hanoi** (`1_4/main.py`) - 經典遞迴問題
- **樹的遍歷** (`1_3/Tree.py`) - 前序、中序、後序
- **鏈表轉樹** (`1_4/D1345490_2.py`) - 快慢指針 + 遞迴

### 其他技巧

- **Two Pointers** (`1_2/Test2.py`) - 容器盛水問題
- **Stack 應用** (`1_2/Test3.py`) - 括號匹配
- **BFS** (`1_4/D1345490_2.py`) - 層序遍歷
- **鏈表數學** (`1_6/D1345490_1.py`) - 兩數相加
- **矩陣遍歷** (`1_6/D1345490_2.py`) - 螺旋矩陣

## 📈 學習路徑

建議按照以下順序學習：

```
1. 1_1 搜尋演算法
   ↓
2. 1_2 Two Pointers 技巧
   ↓
3. 1_3 線性資料結構
   ├─ Linked List (基礎)
   ├─ Stack & Queue
   └─ Tree (入門)
   ↓
4. 1_4 排序與遞迴
   ├─ 排序演算法比較
   ├─ Hanoi 遞迴思維
   └─ 鏈表轉樹 (綜合應用)
   ↓
5. 1_5 樹的進階問題
   └─ 對稱性檢驗 (遞迴應用)
   ↓
6. 1_6 鏈表與矩陣應用
   ├─ 兩數相加 (進位處理)
   └─ 螺旋矩陣 (遞迴遍歷)
```

### 核心概念進階

```
基礎 → 技巧 → 結構 → 演算法 → 應用
 ↓      ↓      ↓       ↓       ↓
搜尋   雙指針  鏈表    排序    樹的
             堆疊    遞迴    對稱性
             佇列
             樹
```

## 📚 教學資源

專案包含以下 PDF 教學文檔：

- `1_3/Stack and Queue.pdf` - Stack 與 Queue 教學
- `1_4/Recursion.pdf` - 遞迴概念教學
- `1_5/題目.pdf` - 第 5 單元習題說明

## 🎓 程式碼特色

### 完整的測試案例

每個實作都包含 `if __name__ == '__main__':` 測試區塊：

```python
if __name__ == '__main__':
    # 測試案例 1
    # 測試案例 2
    # 預期輸出
```

### 詳細的中文註解

特別是在複雜實作中，如 `D1345490_3.py`：

```python
# 常見錯誤說明
# 正確的實現方式
# 邊界條件處理
```

### 時間複雜度分析

程式碼中標註了關鍵演算法的時間複雜度：

- O(1) - 常數時間
- O(log n) - 對數時間
- O(n) - 線性時間
- O(n log n) - 線性對數時間
- O(n²) - 平方時間

## 📝 專案統計

- **總程式碼行數**: ~1100 行
- **Python 檔案**: 22 個
- **平均每檔**: 50 行
- **課程單元**: 6 個
- **實現的資料結構**: 8 種
- **實現的演算法**: 12+ 種

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

### 提交流程

1. Fork 本專案
2. 建立您的 Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit 您的變更 (`git commit -m 'Add some AmazingFeature'`)
4. Push 到 Branch (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

### 程式碼規範

- 遵循 PEP 8 風格指南
- 添加適當的中文註解
- 包含測試案例
- 標註時間複雜度

## 📄 授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案

## 👤 作者

**Yacolate0519-cmd**

- GitHub: [@Yacolate0519-cmd](https://github.com/Yacolate0519-cmd)
- Repository: [DataStructure](https://github.com/Yacolate0519-cmd/DataStructure)

## 🙏 致謝

- 感謝所有資料結構與演算法課程的教材
- 感謝 LeetCode 提供的經典題目
- 感謝開源社群的貢獻

## 📮 聯絡方式

如有任何問題或建議，歡迎：

- 開啟 [GitHub Issue](https://github.com/Yacolate0519-cmd/DataStructure/issues)
- 提交 [Pull Request](https://github.com/Yacolate0519-cmd/DataStructure/pulls)

---

**最後更新**: 2025-11-23
**專案狀態**: 持續更新中 🚧

**Happy Coding! 🎉**
