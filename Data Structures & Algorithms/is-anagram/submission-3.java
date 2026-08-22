
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> map_s = new HashMap<>();
        HashMap<Character, Integer> map_t = new HashMap<>();

        for (char c :s.toCharArray()) {
            if (map_s.containsKey(c)){
                map_s.put(c, map_s.get(c)+1);
            } else {
                map_s.put(c, 1);
            }
        }

        for (char c :t.toCharArray()) {
            if (map_t.containsKey(c)){
                map_t.put(c, map_t.get(c)+1);
            } else {
                map_t.put(c, 1);
            }
        }

        return map_s.equals(map_t);


    }
}