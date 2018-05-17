class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        x,y = 0,0
        flag = 0
        head = ListNode(0)
        cur = head
        while (l1 is not None or l2 is not None):
            if (l1 is not None):
                x = l1.val
            else:
                x = 0
            if (l2 is not None):
                y = l2.val    
            else:
                y = 0
            sum = x + y + carry
            carry = sum // 10
            cur.next = ListNode(sum%10)
            cur = cur.next

            if (l1 is not None): l1 = l1.next
            if (l2 is not None): l2 = l2.next
        if (carry > 0):
            cur.next = ListNode(carry)
            
        return head.next