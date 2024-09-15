class Solution {
    public String reverseVowels(String s) {
        char[] arr = s.toCharArray();
        int i = 0, j = s.length() - 1;
        while (i <= j) {
            while (i < j && !isVowel(arr[i])) {
                i++;
            }
            while (i < j && !isVowel(arr[j])) {
                j--;
            }
            char tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
        return new String(arr);
    }

    public boolean isVowel(char ch) {
        return "aeiouAEIOU".indexOf(ch) != -1;
    }
}