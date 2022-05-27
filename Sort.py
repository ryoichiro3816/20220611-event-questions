import sys
sys.setrecursionlimit(10 ** 9)

def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) <= 1:
      return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    #　左と右のポインター設定
    l, r = 0, len(array) - 1
    l_, r_ = 0, len(array) - 1

    while l < r:
        if pivot <= array[l] and array[r] < pivot:
          array[l], array[r] = array[r], array[l]
          l_ = l
          r_ = r
          l += 1
          r -= 1
        else:
          if array[l] < pivot:
            l += 1
          if pivot <= array[r]:
            r -= 1
    mid = (l_ + r_) // 2
    return sort(array[:mid + 1]) + sort(array[mid+ 1:])
        
    # ここまで記述

if __name__ == '__main__':
    main()