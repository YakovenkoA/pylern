class Singleton:
    instance = None
    
    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
        return Singleton.instance  # Возвращаем существующий экземпляр

if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)