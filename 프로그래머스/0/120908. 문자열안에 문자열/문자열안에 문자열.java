class Solution {
    public int solution(String str1, String str2) {
        int answer = 2;
        for(int i=0;i<str1.length()-str2.length()+1;i++){
            for(int j=0;j<str2.length();j++){
                System.out.print(str1.charAt(i));
                if(str1.charAt(i+j) == str2.charAt(j)){
                    if(j == str2.length()-1){
                        answer=1;
                        break;
                    }
                }
                else{ break; } 
            }
        }
        return answer;
    }
}