class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) return 0;
        HashSet<Character> set = new HashSet<>();

        int l = 0;
        int r = 0;
        int maxl = 0;

        while (r < s.length()) {
            if (!set.contains(s.charAt(r))) {
                set.add(s.charAt(r));
                maxl = Math.max(maxl, r - l + 1);
                r++;
            } else {
                set.remove(s.charAt(l));
                l++;
            }

        }
        return maxl;
    }
}

