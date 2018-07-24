def median(1st):
    m=len(1st)
    if m<1:
       return None
    if m % 2==1:
       return sorted(1st)[m/2]
    else:
       return sum(sorted(1st)[m//2-1:m//2+1]))/2.0
