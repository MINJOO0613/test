class Queue:
    def __init__(self):
        self.front = None
    
    def push(self, value):
        if not self.front:                      # 기존에 입력된 값이 없으면 
            self.front = Node(value, None)      # 값을 입력함
                                                
        node = self.front                       # 값이 있다면
        while node.next:
            node = node.next                    # 그 다음 순서로 값을 넣어준다
        node.next = Node(value, None)           # 마지막 순서에 다음으로 새로 만들어 넣는다

    def pop(self):
        if not self.front:                      # 앞의 순서가 비었다면 종료
            return None                         # 첫 번째 순서를 먼저 반환하고 그 다음 순서를 반환

        node = self.front
        self.front = self.front.next
        return node.item
    
    def is_empty(self):
        return self.front is None