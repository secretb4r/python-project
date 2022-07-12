class List(list):
    def __new__(cls, LIST:set) -> set:
        if isinstance([], list) == isinstance(LIST, list):
            return super().__new__(cls,LIST)
        else:
            raise Exception("invalid type")

    # initializer for list object
    def __init__(self, LIST:list) -> list:
        self.list = LIST
    
    def __repr__(self):
        return f"{self.list}"
    
    def _append(self, val1:any) -> list:
        self.list[len(self.list): ] = [val1]

first_list = [x for x in range(12)]
first = List(first_list)
first._append(23)
print(first)

