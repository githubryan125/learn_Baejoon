class Solution {
    public int solution(int[] number) {
        int answer = 0;
        int l = number.length;
        
        for(int i=0;i<l;i++){
            for(int j=i+1;j<l;j++){
                for(int k=j+1;k<l;k++){
                    if (number[i]+number[j]+number[k] == 0){
                        answer+=1;
                    }
                }
            }   
        }
        return answer;
    }
}