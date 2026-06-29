class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // given a string, we go through each word in the array of Strings
        Map<String, List<String>> map = new HashMap<>(); 

        for(String word : strs){
            char[] letters = word.toCharArray(); // turn word into a array of chars
            Arrays.sort(letters); // sort it
            String sortedWord = new String(letters); // take the sorted char array and turn it back into a word
            map.putIfAbsent(sortedWord, new ArrayList<>()); // method within hashmaps
            map.get(sortedWord).add(word); 
        }

        return new ArrayList<>(map.values()); // im guessing this puts all the values in the map into a arraylist
    }
}
