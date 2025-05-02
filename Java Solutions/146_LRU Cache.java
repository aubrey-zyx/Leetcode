class ListNode {
    int key;
    int val;
    ListNode prev;
    ListNode next;

    public ListNode(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    Map<Integer, ListNode> cache;
    int capacity;
    ListNode left;
    ListNode right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();
        left = new ListNode(-1, -1);
        right = new ListNode(-1, -1);
        left.next = right;
        right.prev = left;
    }

    public void insert(ListNode node) {
        ListNode pre = right.prev, nxt = right;
        pre.next = node;
        nxt.prev = node;
        node.prev = pre;
        node.next = nxt;
    }

    public void remove(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        ListNode node = cache.get(key);
        remove(node);
        insert(node);
        return node.val;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            remove(cache.get(key));
        }
        ListNode node = new ListNode(key, value);
        cache.put(key, node);
        insert(node);
        if (cache.size() > capacity) {
            ListNode lru = left.next;
            remove(lru);
            cache.remove(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */