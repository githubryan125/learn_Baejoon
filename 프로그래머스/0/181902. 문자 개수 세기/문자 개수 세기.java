class Solution {
    public int[] solution(String my_string) {
        int[] num = new int [52];
        for(int i=0;i<my_string.length();i++){
            char C = my_string.charAt(i); 
            if(Character.isUpperCase(C)){
                num[ my_string.charAt(i)-'A' ]++;
            }else{
                num[my_string.charAt(i)-'a'+26]++;
            }
        }
        return num;
    }
}