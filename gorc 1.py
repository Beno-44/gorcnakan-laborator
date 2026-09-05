def sortt(a):
    for i in range(1, len(a)):
        banali=a[i]
        j=i-1
        while j>= 0 and a[j]> banali:
            a[j+1]=a[j]
            j-=1
            a[j+1] = banali
    return a
tver=[78, 5, 66, -8, 132]
dasavorvac_tver=sortt(tver)
print(dasavorvac_tver)        