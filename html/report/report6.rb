#!/usr/bin/ruby
# -*- coding:utf-8 -*-

def showtab(tab)   #table を受け取って、整形して表示する。
  holizon = "--+"
  printf("+%s\n", holizon * tab[0].length)
  tab.each do |line|
    line.each do |cel|
      printf("|%2d",cel)
    end
    printf("|\n+%s\n", holizon * line.length)
  end
  print("\n")
end

def resettab(lamd)   #lambdaに基いたやんぐ図形を作成
  shape = []
  lamd.length.times do |i|
    shape[i] = Array.new(lamd[i],0)
  end
  return shape
end

def makelist(lamd)
  #らむだから標準盤をつくる。入力する行の順番を取得。ex:(2,1)=>[[001],[010]], not [100]
  numbers = []
  n = 0
  lamd.each do |i|
    i.times do #lamd=[3,2,1]ならば、0が3個,1が2個,2が1個で[000112]になる
      numbers << n
    end
    n += 1
  end
  numbers.shift #0を一つ取り除いておいて後で足す。計算量が減るのではないだろうか。 #(A)
  list = numbers.permutation.to_a.uniq #numbersの要素からなる順列を網羅的に作成してlistへ # .uniqで重複を削除

  list.each do |per|
    # list から標準盤でないものを取り除く

    if per.first <= 1 then #(A')二文字目は0か1だけにしたいので、それ以外は無視。
      per.unshift(0) #(A'') 0を最初にもどす
      counter = Array.new(lamd.length, 0) #lambdaの要素が何こある(図形は何行)か数えるのに使う
      per.each do |num|
        counter[num] += 1
        if num > 0 then
          if counter[num] > counter[num-1] then
            list -= [per]
          end
        end
      end
    else
      # (A'')
      list -= [per]
    end
  end
  return list
end

###############################
############ main #############
###############################

if ARGV[0].to_i > 0 then 
  lambda = ARGV.collect { |x| x.to_i} #すべての引数を数字として変換
else
  print "If you tell me lambda numbers, I'll show all StandardTableau.\nPlease enter some numbers. (default= 3 2 1):"
  numbers = gets.chomp!
  
  
  if numbers == "" then
    lambda = [3,2,1]  #default shape
  else
    lambda = []
    numbers.split(/\s+/).each do |i|
      lambda << i.to_i
    end
  end
end
lambda.delete(0)
lambda.sort!.reverse!

stn_tab_list = makelist(lambda)

stn_tab_list.each do |per|
  tableau = resettab(lambda) #標準盤を毎回やんぐ図形に戻す
  per.flatten.length.times do |n|
    x = 0
    y = per.shift
    tableau[y].each do |i|
      if i == 0
        tableau[y][x] = n+1
      else
        x += 1
      end
    end
  end
  showtab(tableau)
end

printf("There are %d Standard Tableau in lambda=%s \n", stn_tab_list.length,lambda)
