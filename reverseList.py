class reverseList(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        ListforString = list(s)
        reverseList = []
        for i in range(len(ListforString)-1, -1, -1):
            reverseList.append(ListforString[i])

        
        
        print(reverseList)
        
obj = reverseList()
obj.reverseString("hello")