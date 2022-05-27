# binary search
   
def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    #　左、右ポインターを設定
    l, r = 0, len(sorted_array)

    while l <= r:
      #真ん中の値を更新(整数)
      mid = (l + r) // 2 
      # 真ん中の値とターゲットが一致したらインデックスを返す
      if target_number == sorted_array[mid]:
        return mid
      #　一致しなかったら、ポインターを更新
      elif target_number < sorted_array[mid]:
        r = mid - 1
      else:
        l = mid + 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()