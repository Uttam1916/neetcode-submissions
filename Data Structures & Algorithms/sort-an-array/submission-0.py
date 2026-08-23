class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(a):
            if len(a)==1:
                return a

            a1=mergesort(a[:len(a)//2])
            a2=mergesort(a[len(a)//2:])
    
            m1,m2=len(a1),len(a2)

            i=0
            j=0
            k=0
            while i<m1 and j<m2:
                if a1[i]<=a2[j]:
                    a[k]=a1[i]
                    i+=1
                else:
                    a[k]=a2[j]
                    j+=1
                k+=1 
            while i<m1:
                a[k]=a1[i]
                i+=1
                k+=1
            while j<m2:  
                a[k]=a2[j]
                j+=1
                k+=1  
            return a
        return mergesort(nums)

        