class Solution {
    public int solution(String s) {
        int result = 0;
        String[] answer = new String[4];
        answer = s.split(" ");
        for(int i=0;i<answer.length;i++){
            if(answer[i].equals("Z")){
                result -= Integer.parseInt(answer[i-1]);
            }
            else{
                result += Integer.parseInt(answer[i]);
            }
        }
        return result;
    }
}