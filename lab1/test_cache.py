from cache import LRUCache

def test_basic():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    
    assert cache.get('Jesse') == 'James'
    
    cache.rem('Walter')
    assert cache.get('Walter') == ''
    
    print("Базовый тест пройден!")
    

def test_lru():
    cache = LRUCache(2)
    cache.set('a', '1')
    cache.set('b', '2')
    cache.get('a')
    cache.set('c', '3')
    
    assert cache.get('a') == '1'
    assert cache.get('b') == ''
    assert cache.get('c') == '3'
    
    print("LRU тест пройден!")

def test_edge_cases():
    cache = LRUCache(1)
    cache.set('a', '1')
    cache.set('b', '2')
    
    assert cache.get('a') == ''
    assert cache.get('b') == '2'
    
    print("Тест граничных случаев пройден!")

if __name__ == "__main__":
    test_basic()
    test_lru()
    test_edge_cases()
    print("\nВсе тесты пройдены!")