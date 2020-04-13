def modes(arr):
    cnt = []
    for i in arr:
      cnt.append(arr.count(i))
    uniq_cnt = []
    for i in cnt:
      if i not in uniq_cnt:
        uniq_cnt.append(i)
    if len(uniq_cnt) > 1:
        m = []
        for i in list(range(len(cnt))):
            if cnt[i] == max(uniq_cnt):
                m.append(arr[i])
        mode = []
        for i in m:
            if i not in mode:
                mode.append(i)
        return mode
    else:
        print("There is NO mode in the data set")
#mode Function Definition
def mode(data):
  lst=[]
  m=0
  for i in range(len(data)):
    lst.append(data.count(data[i]))
    m=max(lst)
  print(m)
  m1= [x for x in data if data.count(x)==m]
  mode=[] 
  for x in m1:
    if x not in mode:
      mode.append(x)
  return mode
print(mode([1,2,3,3,4,5,5,6,6,6,5,6]))
arr=[1,2,3,3,4,5,5,6,6,6,5,6]
print(modes(arr))