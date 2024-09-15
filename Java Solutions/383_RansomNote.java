class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> count = new HashMap<>();
        for (char ch : magazine.toCharArray()) {
            count.put(ch, count.getOrDefault(ch, 0) + 1);
        }
        for (char ch : ransomNote.toCharArray()) {
            if (count.getOrDefault(ch, 0) <= 0) {
                return false;
            }
            count.put(ch, count.get(ch) - 1);
        }
        return true;
    }
}