from test_module import A

a = A()
a.showme()


class A:
    def showme(self):
        self.showB() 

a = A()
a.showme()
