class Solution {
    public String solution(String myString, String pat) {
        int lastIndex = myString.lastIndexOf(pat);
        if (lastIndex == -1) return ""; // pat이 없는 경우
        return myString.substring(0, lastIndex + pat.length());
    }
}
