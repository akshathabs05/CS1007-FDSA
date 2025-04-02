arr=['10','89','9','56','4','80','8']
mini=10
maxi=10
maxi2=10
mini2=10
for num in arr:
    num=int(num)
    if num<mini:
       mini=num
    if num>maxi:
       maxi2=maxi
       maxi=num
    elif num> maxi2 and num!=maxi:
           maxi2=num
    elif num<mini2 and num!=mini:
           mini2=num
           

    print("smallest element",mini)
    print("largest element",maxi)
    print("second largest element",maxi2)
    print("second largest element",mini2)



