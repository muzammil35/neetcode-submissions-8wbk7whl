class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        List<List<Integer>> list = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {

            // Skip duplicate first numbers
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            for (int j = i + 1; j < nums.length; j++) {

                // Skip duplicate second numbers
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                int target = -1 * (nums[i] + nums[j]);

                if (map.containsKey(target)
                        && map.get(target) != i
                        && map.get(target) != j && map.get(target) > i && map.get(target) > j) {

                    List<Integer> inner = new ArrayList<>();

                    inner.add(nums[i]);
                    inner.add(nums[j]);
                    inner.add(target);

                    list.add(inner);
                }
            }
        }

        return list;
    }
}
