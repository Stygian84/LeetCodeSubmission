class Foo:
    def __init__(self):

        
        self.event_first = threading.Event()
        self.event_second = threading.Event()

        
        thread1 = threading.Thread(target=self.first)
        thread2 = threading.Thread(target=self.second)
        thread3 = threading.Thread(target=self.third)
        
        
        thread1.start()
        thread2.start()
        thread3.start()
        
        
        thread1.join()
        thread2.join()
        thread3.join()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.event_first.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.event_first.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.event_second.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.event_second.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()